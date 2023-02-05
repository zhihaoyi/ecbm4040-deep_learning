"""
Implementation of softmax classifer.
"""

import numpy as np


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops over N samples)

    NOTE:
    In this function, you are NOT supposed to use functions like:
    - np.dot
    - np.matmul (or operator @)
    - np.linalg.norm
    You can (not necessarily) use functions like:
    - np.sum
    - np.log
    - np.exp

    Inputs have dimension D, there are K classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: a numpy array of shape (D + 1, K) containing weights.
    - X: a numpy array of shape (N, D + 1) containing a minibatch of data.
    - y: a numpy array of shape (N,) containing training labels; y[i] = k means 
        that X[i] has label k, where 0 <= k < K.
    - reg: regularization strength. For regularization, we use L2 norm.

    Returns a tuple of:
    - loss: the mean value of loss functions over N examples in minibatch.
    - gradient: gradient wrt W, an array of same shape as W
    """

    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    ############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.    #
    # Store the loss in loss and the gradient in dW. If you are not careful    #
    # here, it is easy to run into numeric instability. Don't forget the       #
    # regularization!                                                          #
    # NOTE: PLEASE pay attention to data types!                                #
    ############################################################################
    ############################################################################
    #                     START OF YOUR CODE                                   #
    ############################################################################
    
    #------- loss -------
    # input:
        # W [D+1,K] [785,10]
        # X [N,D+1] [100,785]
        # y [N,]    [100,] 
        # reg float
    # output:
        # loss float

    K = W.shape[1]
    N = X.shape[0]
    D = W.shape[0]
    loss_temp = 0

    dot_total = []
    
    dot_ = np.zeros((N,K))
    for n in range(N):
        for k in range(K):
            for d in range(D):
                dot_[n][k] += X[n][d]*W[d][k]
  
        sig = np.exp(dot_[n][y[n]])/np.sum(np.exp(dot_[n]))
        loss_temp += -np.log(sig)
    

    #------- dW -------
    # y[N,K], dot_[N,K], X[N,D]
    y1 = np.zeros((N, K)) 
    for n in range(N):  #[N,K] 
        y1[n,y[n].astype(int)] = 1   
    
    dot_exp = np.exp(dot_)
    for n in range(N):
        dot_exp[n] /= np.sum(dot_exp[n])
    
    for n in range(N):
        for k in range(K):
            for d in range(D):
                dW[d][k] -= X.T[d][n]*(y1[n][k]-dot_exp[n][k])
                    
    loss = (loss_temp/N) + (reg/2)*np.sum(W*W)
    dW = (dW/N) + reg*W 

    
    # raise NotImplementedError
    ############################################################################
    #                     END OF YOUR CODE                                     #
    ############################################################################

    return loss, dW


def softmax(x):
    """
    Softmax function, vectorized version

    Inputs
    - x: (float) a numpy array of shape (N, C), containing the data

    Return a numpy array
    - h: (float) a numpy array of shape (N, C), containing the softmax of x
    """

    h = np.zeros_like(x)

    ############################################################################
    # TODO:                                                                    #
    # Implement the softmax function.                                          #
    # NOTE:                                                                    #
    # Carefully deal with different input shapes.                              #
    ############################################################################
    ############################################################################
    #                     START OF YOUR CODE                                   #
    ############################################################################
    
    
    h = np.exp(x)/np.sum(np.exp(x), axis = 1, keepdims = True)
    
    # raise NotImplementedError
    ############################################################################
    #                     END OF YOUR CODE                                     #
    ############################################################################

    return h


def onehot(y, K):
    """
    One-hot encoding function, vectorized version.

    Inputs
    - x: (uint8) a numpy array of shape (N,) containing labels; y[i] = k means 
        that X[i] has label k, where 0 <= k < K.
    - K: total number of classes

    Returns a numpy array
    - y: (float) the encoded labels of shape (N, K)
    """

    N = y.shape[0]
    y1 = np.zeros((N, K))

    ############################################################################
    # TODO:                                                                    #
    # Implement the one-hot encoding function.                                 #
    ############################################################################
    ############################################################################
    #                     START OF YOUR CODE                                   #
    ############################################################################
    
    for n in range(N):
        y1[n,y[n].astype(int)] = 1
    
    # raise NotImplementedError
    ############################################################################
    #                     END OF YOUR CODE                                     #
    ############################################################################

    return y1


def cross_entropy(p, q):
    """
    Cross entropy function, vectorized version.

    Inputs:
    - p: (float) a numpy array of shape (N, K), containing ground truth labels
    - q: (float) a numpy array of shape (N, K), containing predicted labels

    Returns:
    - h: (float) a numpy array of shape (N,), containing the cross entropy of 
        each data point
    """

    h = np.zeros(p.shape[0])

    ############################################################################
    # TODO:                                                                    #
    # Implement cross entropy function.                                        #
    ############################################################################
    ############################################################################
    #                     START OF YOUR CODE                                   #
    ############################################################################

    h = -np.sum(p*np.log(q), axis=1)
    
    # raise NotImplementedError
    ############################################################################
    #                     END OF YOUR CODE                                     #
    ############################################################################

    return h


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    NOTE:
    In this function, you CAN (not necessarily) use functions like:
    - np.dot (unrecommanded)
    - np.matmul (or operator @)
    - np.linalg.norm
    You MUST use the functions you wrote above:
    - onehot
    - softmax
    - crossentropy

    Inputs and outputs are the same as softmax_loss_naive.
    """

    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    ############################################################################
    # TODO: 																   #
	# Compute the softmax loss and its gradient using no explicit loops.       #
    # Store the loss in loss and the gradient in dW. If you are not careful    #
    # here, it is easy to run into numeric instability. Don't forget the       #
    # regularization!                                                          #
    ############################################################################
    ############################################################################
    #                     START OF YOUR CODE                                   #
    ############################################################################
    K = W.shape[1]
    N = X.shape[0]
    # ------- loss -------
    # input:
        # W [D+1,K] [785,10]
        # X [N,D+1] [100,785]
        # y [N,]    [100,] 
        
    sig = softmax(X@W) # [100,10]
    one_hot = onehot(y,K) # [100,10]
    f = X@W
    sig = softmax(f)
    h = cross_entropy(one_hot,sig)
    loss = np.sum(h)/N + (reg/2)*np.sum(W*W)
    
    # ------- dW -------
    dW = -(1/N)*X.T@(one_hot-sig) + reg*W
    
    
    # raise NotImplementedError
    ############################################################################
    #                     END OF YOUR CODE                                     #
    ############################################################################

    return loss, dW
