'''
ECBM E4040 Fall 2022 Assignment 2
MLP class and functions
'''

import numpy as np

from ..layer_funcs import *
from ..reg_funcs import *


class MLP:
    '''
    MLP with an arbitrary number of dense hidden layers,
    and a softmax loss function. For a network with L layers,
    the architecture will be

    input >> [Affine + (BN) + ReLU + (dropout)] x (L - 1) >> [Affine] >> softmax_loss >> output

    Here "x (L - 1)" means to repeat L - 1 times. 
    '''

    def __init__(self, input_dim=3072, hidden_dims=[200, 200], num_classes=10, weight_scale=1e-2,
                 l2_reg=0.0, use_bn=None, dropout_config=None, momentum=0.0):
        '''
        Inputs:
        - weight_scale: (float) for layer weight initialization
        - l2_reg: (float) L2 regularization
        - use_bn: (bool) decide whether to use batch normalization or not
        - dropout_config: (dict) configuration for dropout
        - momentum: (float) for Nesterov Momentum parameters update
        '''

        params = {}
        grads = {}
        self.num_layers = len(hidden_dims) + 1

        if dropout_config == None:
            dropout_config = {"enabled": False}

        self.l2_reg = l2_reg
        self.use_bn = use_bn
        bn_params = []
        self.dropout_config = dropout_config

        dims = [input_dim] + hidden_dims

        for i in range(len(hidden_dims)):
            # initialize weights and bias for the first (L-1) layer
            weight_name = "weight_{}".format(i)
            bias_name = "bias_{}".format(i)
            W = weight_scale * np.random.rand(dims[i], dims[i + 1])
            b = np.zeros(dims[i + 1])
            params[weight_name] = W
            params[bias_name] = b
            # initalize batch normalization parameters
            if use_bn:
                # add batch normalization parameters: bn_gamma, bn_beta
                params["bn_gamma_{}".format(i)] = np.ones(dims[i + 1])
                params["bn_beta_{}".format(i)] = np.zeros(dims[i + 1])
                # initialize the empty dictionary to store moving mean and var later
                #bn_params.append(dict())
                bn_params.append({"epsilon": 1e-3, "decay": 0.999})

        # initialize weights and bias for the last layer
        weight_name = "weight_{}".format(len(hidden_dims))
        bias_name = "bias_{}".format(len(hidden_dims))
        W = weight_scale * np.random.rand(dims[-1], num_classes)
        b = np.zeros(num_classes)
        params[weight_name] = W
        params[bias_name] = b

        self.params = params
        self.grads = {k: np.zeros_like(p) for k, p in params.items()}
        self.bn_params = bn_params
        self.mode = "train"

    def forward(self, X):
        '''
        Feed forward

        Inputs:
        - X: input data

        Returns
        - out: the output of the network
        '''

        cache = {}
        num_layers = self.num_layers
        params = self.params
        use_bn = self.use_bn
        bn_params = self.bn_params
        dropout_config = self.dropout_config

        ###################################################
        # Feedforward                                     #
        ###################################################
        x = X
        for i in range(num_layers - 1):
            # Affine
            w = params["weight_{}".format(i)]
            b = params["bias_{}".format(i)]
            cache_name = "affine_{}".format(i)
            x, cache[cache_name] = affine_forward(x, w, b)
            #print(params)
            # Batch Normalization
            ###############################################
            # TODO: Add batch normalization here          #
            ###############################################
            #raise NotImplementedError
            if use_bn:
                #bn_forward(x, gamma, beta, bn_params, mode):

                gamma = params['bn_gamma_{}'.format(i)]
                beta = params['bn_beta_{}'.format(i)]
                cache_name_bn = 'bn_{}'.format(i)
                    
                x,cache[cache_name_bn] = bn_forward(x, gamma, beta, bn_params[i], mode='train')
            ###############################################
            # END OF BATCH NORMALIZATION                  #
            ###############################################

            # ReLU
            cache_name = "relu_{}".format(i)
            x, cache[cache_name] = relu_forward(x)

            # Dropout
            ###############################################
            # TODO: Add dropout here                      #
            ###############################################
            #raise NotImplementedError
            if dropout_config['enabled']:
                cache_name_dropout = 'dropout_{}'.format(i)
                x, cache[cache_name_dropout] = dropout_forward(x, dropout_config, mode='train')
                
                
            ###############################################
            # END OF DROPOUT                              #
            ###############################################

        # The last layer
        w = params["weight_{}".format(num_layers - 1)]
        b = params["bias_{}".format(num_layers - 1)]
        cache_name = "affine_{}".format(num_layers - 1)
        x, cache[cache_name] = affine_forward(x, w, b)

        if self.mode == "train": self.cache = cache

        return x

    def loss(self, preds, y):
        '''
        Calculate the cross-entropy loss and then use backpropogation
        to get gradients wst W,b in each layer.

        Inputs:
        - preds: predictions from feed forward
        - y: ground truth

        Return loss value(float)
        '''

        loss = 0.0
        l2_reg = self.l2_reg
        use_bn = self.use_bn
        dropout_config = self.dropout_config
        num_layers = self.num_layers

        cache = self.cache
        params = self.params
        grads = dict()

        ###################################################
        # Backpropogation                                 #
        ###################################################
        loss, dx = softmax_loss(preds, y)
        dx, dw, db = affine_backward(
            dx, cache["affine_{}".format(num_layers - 1)])
        grads["weight_{}".format(num_layers - 1)] = dw
        grads["bias_{}".format(num_layers - 1)] = db
        for i in range(num_layers - 1):
            # the i-th layer from the front is 
            # the (num_layers - 2 - i)-th layer from the back
            j = num_layers - 2 - i
            # Dropout backward
            ###############################################
            # TODO: Add dropout here                      #
            ###############################################
            #raise NotImplementedError
            if dropout_config["enabled"]:
                dx = dropout_backward(dx, cache['dropout_{}'.format(j)])
                
            ###############################################
            # END OF DROPOUT                              #
            ###############################################

            # ReLU backward
            dx = relu_backward(dx, cache["relu_{}".format(j)])
            # Batch Normalization backward
            ###############################################
            # TODO: Add batch normalization here          #
            ###############################################
            #raise NotImplementedError
            if use_bn:
                dx, dgamma, dbeta = bn_backward(dx, cache['bn_{}'.format(j)])

                
            ###############################################
            # END OF BATCH NORMALIZATION                  #
            ###############################################

            # Affine backward
            dx, dw, db = affine_backward(dx, cache["affine_{}".format(j)])
            grads["weight_{}".format(j)] = dw
            grads["bias_{}".format(j)] = db

        # Add L2 regularization to loss as well as gradients
        square_weights = 0.0
        for i in range(num_layers):
            w = params["weight_{}".format(i)]
            square_weights += np.sum(w ** 2)
            grads["weight_{}".format(i)] += l2_reg * w

        loss += 0.5 * l2_reg * square_weights
        self.grads = grads

        return loss

    def predict(self, X):
        '''
        Return the label prediction of input data

        Inputs:
        - X: (float) a tensor of shape (N, D)

        Returns: 
        - predictions: (int) an array of length N
        '''

        self.mode = "test"
        scores = self.forward(X)
        predictions = np.argmax(scores, axis=1)
        self.mode = "train"

        return predictions

    def check_accuracy(self, X, y):
        '''
        Return the classification accuracy of input data

        Inputs:
        - X: (float) a tensor of shape (N, D)
        - y: (int) an array of length N. ground truth label 
        Returns: 
        - acc: (float) between 0 and 1
        '''
        y_pred = self.predict(X)
        acc = np.mean(np.equal(y, y_pred))

        return acc
