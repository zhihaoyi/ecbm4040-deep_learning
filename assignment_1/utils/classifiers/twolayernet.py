"""
Implementation of a two-layer network. 
"""

import numpy as np
from utils.layer_utils import AffineLayer, DenseLayer


class TwoLayerNet(object):
    """
    A two-layer fully-connected neural network. The net has an input dimension of
    N, a hidden layer dimension of H, and performs classification over C classes.
    We train the network with a softmax loss function and L2 regularization on the
    weight matrices. The network uses a Leaky_ReLU nonlinearity after the first fully
    connected layer.

    In other words, the network has the following architecture:
    input -> DenseLayer -> AffineLayer -> softmax loss -> output
    Or more detailed,
    input -> affine transform -> Leaky_ReLU -> affine transform -> softmax -> output

    The outputs of the second fully-connected layer are the scores for each class.
    """

    def __init__(self, input_dim=3072, hidden_dim=200, num_classes=10, reg=0.0, weight_scale=1e-3):
        """
        Inputs:
        - reg: (float) L2 regularization
        - weight_scale: (float) for layer weight initialization
        """

        self.layer1 = DenseLayer(input_dim, hidden_dim, weight_scale=weight_scale)
        self.layer2 = AffineLayer(hidden_dim, num_classes, weight_scale=weight_scale)
        self.reg = reg
        self.velocities = None

    def forward(self, X):
        """
        Feed forward

        Inputs:
        - X: a numpy array of (N, D) containing input data

        Returns a numpy array of (N, K) containing prediction scores
        """

        ############################################################################
        #                        START OF YOUR CODE                                #
        ############################################################################
        ############################################################################
        # TODO: Feedforward                                                        #
        # NOTE: Use the methods defined for the layers in layer_utils.py           #
        ############################################################################
        layer1 = self.layer1
        layer2 = self.layer2
        #print(X.shape) [100,784]
        layer1_out = layer1.feedforward(X)
        #print(layer1_out.shape) [100,100]
        layer2_out = layer2.feedforward(layer1_out)
        #print(layer2_out.shape) [100,20]
        X = layer2_out 
                                 
        #raise NotImplementedError
        ############################################################################
        #                          END OF YOUR CODE                                #
        ############################################################################

        return X

    def loss(self, scores, labels):
        """
        Calculate the cross-entropy loss and then use backpropogation
        to get gradients wst W,b in each layer.
        Do regularization for better model generalization.

        Inputs:
        - scores: a numpy array of (N, K) containing prediction scores 
        - labels: a numpy array of (N,) containing ground truth

        Return loss value (float)
        """

        loss = 0.0

        from ..layer_funcs import softmax_loss

        ############################################################################
        #                        START OF YOUR CODE                                #
        ############################################################################
        ############################################################################
        # TODO:                                                                    #
        # Backpropogation, here is just one dense layer, it should be pretty easy  #
        # NOTE: Use the methods defined for each layer, and you no longer need to  #
        # mannually cache the parameters because it would be taken care of by the  #
        # functions in layer_utils.py                                              #
        ############################################################################
        layer1 = self.layer1
        layer2 = self.layer2
        
        loss,dout = softmax_loss(scores,labels)
        #print(dout.shape)
        layer2_back = layer2.backward(dout)
        #print(layer2_back)
        layer1_back = layer1.backward(layer2_back)
        #print(layer1_back.shape)
        
        #raise NotImplementedError
        ############################################################################
        #                          END OF YOUR CODE                                #
        ############################################################################

        # Add L2 regularization
        squared_weights = np.sum(self.layer1.params['W']**2) \
            + np.sum(self.layer2.params['W']**2) # equivalant to a squared Frobenius norm
        loss += 0.5 * self.reg * squared_weights

        return loss

    def step(self, learning_rate=1e-5, optim='SGD', momentum=0.5):
        """
        Use SGD to implement a single-step update to each weight and bias.
        Set learning rate to 0.00001, momentum to 0.5.
        """

        # fetch the parameters from layer cache
        params = {
            'l1_W': self.layer1.params['W'], 
            'l1_b': self.layer1.params['b'], 
            'l2_W': self.layer2.params['W'], 
            'l2_b': self.layer2.params['b']
        }
        grads = {
            'l1_W': self.layer1.gradients['W'], 
            'l1_b': self.layer1.gradients['b'], 
            'l2_W': self.layer2.gradients['W'], 
            'l2_b': self.layer2.gradients['b']
        }

        # fetch the velocities stored from previous iteration
        # if None (i.e. this is the first iteration), build velocities from scratch
        velocities = self.velocities or \
            {name: np.zeros_like(param) for name, param in params.items()}

        # Add L2 regularization:
        reg = self.reg
        grads = {name: grad+ reg * params[name] for name, grad in grads.items()}

        ############################################################################
        # TODO:                                                                    #
        # Use SGD or SGD with momentum to update variables in layer1 and layer2    #
        # NOTE: iterate through all the parameters and do the update one by one    #
        ############################################################################
        ############################################################################
        #                         START OF YOUR CODE                               #
        ############################################################################

        params['l1_W'] = params['l1_W'] - learning_rate*grads['l1_W']
        params['l1_b'] = params['l1_b'] - learning_rate*grads['l1_b']
        params['l2_W'] = params['l2_W'] - learning_rate*grads['l2_W']
        params['l2_b'] = params['l2_b'] - learning_rate*grads['l2_b']
        
        #raise NotImplementedError
        ############################################################################
        #                          END OF YOUR CODE                                #
        ############################################################################

        # update parameters in layers (2 parameters W & b in each layer)
        # with an additional reg
        self.update_model((params, reg))
        # store the parameters for model saving
        self.params = params
        # store the velocities for the next iteration
        self.velocities = velocities

    def predict(self, X):
        """
        Return the label prediction of input data

        Inputs:
        - X: (float) a tensor of shape (N, D)

        Returns: 
        - preds: (int) an array of length N
        """

        preds = np.zeros(X.shape[0])

        ############################################################################
        # TODO: generate predictions                                               #
        ############################################################################
        ############################################################################
        #                         START OF YOUR CODE                               #
        ############################################################################

        layer1 = self.layer1
        layer2 = self.layer2
        
        layer1_out = layer1.feedforward(X)
        layer2_out = layer2.feedforward(layer1_out)
        preds = np.argmax(layer2_out,axis = 1)
        
        #raise NotImplementedError
        ############################################################################
        #                          END OF YOUR CODE                                #
        ############################################################################

        return preds

    def save_model(self):
        """
        Save model's parameters, including two layers' W and b and reg.
        """
        return self.params, self.reg

    def update_model(self, model):
        """
        Update layers and reg with new parameters.
        """

        params, reg = model

        # filter out the parameters for layer 1
        # update the weights in layer 1 by calling layer1.update()
        self.layer1.update_layer({
            name.split('_')[1]: param for name, param in params.items()
            if name.startswith('l1')
        })
        # likewise
        self.layer2.update_layer({
            name.split('_')[1]: param for name, param in params.items()
            if name.startswith('l2')
        })
        self.reg = reg
