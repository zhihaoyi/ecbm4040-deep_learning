'''
E4040 2022Fall Assignment3
LSTM
'''

import tensorflow as tf


class LSTMCell(tf.keras.Model):
    '''
    Build your own LSTMCell as a trainable model inherited from tensorflow base model. 

    Methods: 
    - __init__: initialize the model
    - build   : build the parameters
    - call    : implement the forward pass

    Once you have built this model, tensorflow will be able to calculate the gradients 
    and update the parameters like a regular keras.layer object that you're familiar with. 

    This is a useful technique when you need to create something uncommon on your own. 
    See details in https://www.tensorflow.org/api_docs/python/tf/keras/Model
    '''

    def __init__(
        self, units, 
        kernel_initializer=tf.keras.initializers.GlorotUniform, 
        recurrent_initializer=tf.keras.initializers.Orthogonal, 
        bias_initializer=tf.keras.initializers.Zeros
    ):
        ''' Initialize the model '''

        # save the useful arguemnts
        # number of units (dimensions) for LSTM
        self.units = units
        # weight initializers
        self.kernel_initializer = kernel_initializer
        self.recurrent_initializer = recurrent_initializer
        self.bias_initializer = bias_initializer

        # for RNN layer
        self.state_size = (units, units)

        # when deriving your own model on top of tf.keras.model, 
        # firstly you need to initialize this base model
        super().__init__()


    def build(self, input_shape):
        '''
        Build the parameters

        When calling a model, Tensorflow will build it before feeding in input data. 
        This is done when you call "model.build()" or specify an "input_shape". 

        When building the model, each component (layer) will be built by calling this
        "build" method with an argument of "input_shape", which allows for more 
        flexibility because you don't need to specify the data shape until runtime. 

        :param input_shape: shape of "inputs" of "call" method [batch_size, time_steps, dim]
        '''

        kernel_shape, recurrent_shape, bias_shape = None, None, None

        ###################################################
        # TODO: Specify the parameter shapes              #
        ###################################################
        #raise NotImplementedError
        
        
        # input_shape [4,8]
        # batch_size = 4 -------------> N
        # time_steps = 8 -------------> T
        # dimension of each input ----> D
        # units ----------------------> K
        
        # kernel_shape ---------------> D x 4K
        # recurrent_shape ------------> K x 4K
        # bias_shape -----------------> 4K
        
        
        units = self.units
        
        kernel_shape = (input_shape[-1], 4*units)
        recurrent_shape = (units, 4*units)
        bias_shape = (4*units,)
                
        
        ###################################################
        # END TODO                                        #
        ###################################################

        # build the parameters using "add_weights"
        # this is a method inherited from keras.Model
        self.kernel = self.add_weight(
            shape=kernel_shape, 
            name='kernel', 
            initializer=self.kernel_initializer
        )
        self.recurrent_kernel = self.add_weight(
            shape=recurrent_shape, 
            name='recurrent_kernel', 
            initializer=self.recurrent_initializer
        )
        self.bias = self.add_weight(
            shape=bias_shape, 
            name='bias', 
            initializer=self.bias_initializer
        )
        # the weights will then be readily available for use
        # in the "call" method, and they are added automatically
        # to backpropagation and optimization

        # set build flag to true
        self.built = True


    def call(self, inputs, states):
        '''
        Forward pass for LSTM cell. 

        :param inputs: cell inputs of one time step, 
            a tf.Tensor of shape [batch_size, dims]
        :param states: cell states from last time step, 
            a tuple of (hidden_states, carry_states)

        Return
        : a tuple of new hidden states and cell states
        '''

        h, c = None, None

        ###################################################
        # TODO: LSTMCell forward pass                     #
        ###################################################
        #raise NotImplementedError
        
        
        """
        input:
            inputs = [batch_size, dims] [4, 8] x_t
            states = a tuple of (hidden_states, carry_states) (h_t-1, c_t-1)
        
        kernel_shape ---------------> D x 4K
        recurrent_shape ------------> K x 4K
        bias_shape -----------------> 4K
                
        input_dim   D = 8
        units       K = 64
        
        inputs ---------------------> [4, 8]
        """
        
        kernel = self.kernel #[8, 256]
        recurrent_kernel = self.recurrent_kernel #[64, 256]
        bias = self.bias #[256,]
        
        h_prev = states[0] #[4,64]
        c_prev = states[1] #[4,64]
        
        w_i, w_f, w_c, w_o = tf.split(kernel, num_or_size_splits=4, axis=1) #[8,64]
        wr_i, wr_f, wr_c, wr_o = tf.split(recurrent_kernel, num_or_size_splits=4, axis=1) #[64,64]
        b_i, b_f, b_c, b_o = tf.split(bias, num_or_size_splits=4, axis=0) #[64,]
        
        zw_f = inputs@w_f + h_prev@wr_f + b_f # (4,64)
        f = tf.sigmoid(zw_f)

        zw_i = inputs@w_i + h_prev@wr_i + b_i # (4,64)
        i = tf.sigmoid(zw_i)

        zw_c_ = inputs@w_c + h_prev@wr_c + b_c # (4,64)
        c_ = tf.tanh(zw_c_)

        zw_o = inputs@w_o + h_prev@wr_o + b_o # (4,64)
        o = tf.sigmoid(zw_o)
        
        c = f*c_prev + i*c_
        h = o*tf.tanh(c)
        
        
        ###################################################
        # END TODO                                        #
        ###################################################

        return h, [h, c]


class LSTMModel(tf.keras.Model):
    ''' Define your own LSTM Model '''

    def __init__(self, units, output_dim, activation, input_shape):
        '''
        Initialize the model. 

        :params units: number of units for LSTMCell
        :params output_dim: final output dimension 
        :params activation: activation of the final layer
        :params input_shape: shape of model input
        '''

        # initialize the base class first
        super().__init__()

        ###################################################
        # TODO: Add the RNN and other layers              #
        ###################################################
        #raise NotImplementedError

        
        lstm_cell = LSTMCell(units)
        
        self.rnn_layer = tf.keras.layers.RNN(lstm_cell, return_sequences=True)
        
        self.output_layer = tf.keras.layers.Dense(1, activation=activation)
        
        
        
        ###################################################
        # END TODO                                        #
        ###################################################


    def call(self, inputs):
        '''
        LSTM model forward pass. 
        '''

        # don't forget this conversion becuase we have 
        # initialized our weights to be float
        # certain operations must require identical types
        x = tf.cast(inputs, float)

        ###################################################
        # TODO: Feedforward through your model            #
        ###################################################
        #raise NotImplementedError
        

        x = self.rnn_layer(x)
        x = self.output_layer(x)        
        

        ###################################################
        # END TODO                                        #
        ###################################################

        return x

