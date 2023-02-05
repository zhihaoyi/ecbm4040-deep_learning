"""
Implementations of logistic regression. 
"""

import numpy as np


def logistic_regression_loss_naive(w, X, y, reg):
    """
    Logistic regression loss function, naive implementation (with loops over N samples)

    NOTE:
    In this function, you are NOT supposed to use functions like:
    - np.dot
    - np.matmul (or operator @)
    - np.linalg.norm
    You can (not necessarily) use functions like:
    - np.sum
    - np.log
    - np.exp

    Use this linear classification method to find optimal decision boundary.

    Inputs have dimension D, there are K classes, and we operate on minibatches
    of N examples.

    Inputs:
    - w: (float) a numpy array of shape (D + 1,) containing weights.
    - X: (float) a numpy array of shape (N, D + 1) containing a minibatch of data.
    - y: (uint8) a numpy array of shape (N,) containing training labels; y[i] = k means 
        that X[i] has label k, where k can be either 0 or 1.
    - reg: (float) regularization strength. For regularization, we use L2 norm.

    Returns a tuple of:
    - loss: (float) the mean value of loss functions over N examples in minibatch.
    - gradient: (float) gradient wrt W, an array of same shape as W
    """

    # Set the loss to a random number
    loss = 0
    # Initialize the gradient to zero
    dw = np.zeros_like(w)

    ############################################################################
    # TODO:                                                                    #
    # Compute the softmax loss and its gradient using explicit loops.          #
    # Store the loss in loss and the gradient in dW. If you are not careful    #
    # here, it is easy to run into numeric instability. Don't forget the       #
    # regularization!                                                          #
    # NOTE: You may want to convert y to float for computations. For numpy     #
    # dtypes, see https://numpy.org/doc/stable/reference/arrays.dtypes.html    #
    ############################################################################
    ############################################################################
    #                              START OF YOUR CODE                          #
    ############################################################################
    
    # ------- loss -------
    # input: 
        # w [785,]
        # X [100,785]
        # y [100,]
        # reg float
    # output:
        # loss float

    N = X.shape[0] #100
    D = w.shape[0] #785
    y = np.array(y, dtype = np.float32) # [100,]
    sig_store = np.zeros_like(y)
    
    temp_loss = 0
    
    for i in range(N): #100
        f = 0
        for j in range(D): #785
            f += X[i][j]*w[j]
                   
        sig = 1/(1+np.exp(-f))
        sig_store[i] = sig
        
        temp_loss += -y[i]*np.log(sig) - (1-y[i])*np.log(1-sig)
               
    loss = temp_loss/N + (reg/2)*np.sum(w*w)
    
    # ------- dw -------
    # input:
        # y [100,]
        # sig_store = [100,]
        # X [100,785]
    # output:
        # dw [785,]
        
    for i in range(D): #785
        for j in range(N): #100
            dw[i] += (sig_store[j]-y[j]) * X[j][i] / N
    
    
    #raise NotImplementedError
    ############################################################################
    #                               END OF YOUR CODE                           #
    ############################################################################

    return loss, dw


def sigmoid(x):
    """
    Sigmoid function.

    Inputs:
    - x: (float) a numpy array of shape (N,)

    Returns:
    - h: (float) a numpy array of shape (N,), containing the element-wise sigmoid of x
    """

    h = np.zeros_like(x)

    ############################################################################
    # TODO:                                                                    #
    # Implement sigmoid function.                                              #         
    ############################################################################
    ############################################################################
    #                          START OF YOUR CODE                              #
    ############################################################################
    
    h = 1/(1+np.exp(-x))
    
    #raise NotImplementedError
    ############################################################################
    #                          END OF YOUR CODE                                #
    ############################################################################

    return h 


def logistic_regression_loss_vectorized(w, X, y, reg):
    """
    Logistic regression loss function, vectorized version.

    NOTE:
    In this function, you CAN (not necessarily) use functions like:
    - np.dot (unrecommanded)
    - np.matmul
    - np.linalg.norm
    You MUST use the functions you wrote above:
    - sigmoid

    Use this linear classification method to find optimal decision boundary.

    Inputs and outputs are the same as softmax_loss_naive.
    """

    # Set the loss to a random number
    loss = 0
    # Initialize the gradient to zero
    dw = np.zeros_like(w)

    ############################################################################
    # TODO:                                                                    #
    # Compute the logistic regression loss and its gradient using no           # 
    # explicit loops.                                                          #
    # Store the loss in loss and the gradient in dW. If you are not careful    #
    # here, it is easy to run into numeric instability. Don't forget the       #
    # regularization!                                                          #
    # NOTE: For multiplication bewteen vectors/matrices, np.matmul(A, B) is    #
    # recommanded (i.e. A @ B) over np.dot see                                 #
    # https://numpy.org/doc/stable/reference/generated/numpy.matmul.html       #
    # Again, pay attention to the data types!                                  #
    ############################################################################
    ############################################################################
    #                          START OF YOUR CODE                              #
    ############################################################################
    
    # ------- loss -------
    # input:
        # w [785,]
        # X [100,785]
        # y [100,]
        # reg float
    # output:
        # loss float
        
    N = X.shape[0]    
    y = np.array(y, dtype = np.float32)
    loss_temp = 0
    
    sig = sigmoid(X@w) #[100,]
    loss_temp = -y.T@np.log(sig) - (1-y.T)@np.log(1-sig)
    loss = loss_temp/N + (reg/2)*(w.T@w)
    
    # ------- dw -------
    # input:
        # y [100,]
        # sig = [100,]
        # X [100,785]
    # output:
        # dw [785,]
        
    dw = X.T@(sig-y)/N

    
    #raise NotImplementedError
    ############################################################################
    #                          END OF YOUR CODE                                #
    ############################################################################

    return loss, dw
