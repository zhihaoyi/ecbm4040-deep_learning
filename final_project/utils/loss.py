"""
Loss function based on keras Loss
"""
import tensorflow as tf

def loss(za, zb, relation):
    """
    Directly calculate loss, called by loss_fn.
    za, zb: the predicted depth of point a, b
    relation: the ground-truth ordinal relations. closer (+1), further (-1), and equal (0).
    """
    if relation == 1:
        return tf.math.log(1 + tf.math.exp(-za + zb))
    elif relation == -1:
        return tf.math.log(1 + tf.math.exp(za - zb))
    else:
        return tf.math.multiply((za-zb), (za-zb))

class loss_fn(tf.keras.losses.Loss):
    def __init__(self, name = "custom_loss"):
        super().__init__(name = name)
    def call(self, y_true, y_pred):
        """
        Function, calculate loss.
        Inputs:
        - y_true: y_true 3-D tensor, relative depth data, [batch, 1, 5]
        - y_pred: forward pass' otuput,  4-D tensor, [batch, height, width, channel]
        For the thrid dimension, 5 numbers are [yA, xA, yB, xB, label] (x: width, y: height, label: relation)
        """
        # counter init
        total_loss = 0
        # remove the last dimension of y_pred (channel) 
        pred = tf.reshape(y_pred, y_pred.shape[0:3])

        for i,label in enumerate(y_true): # loop every image in the batch

            # Get point A, B and their relation from y_true
            yA = label[0][0]
            xA = label[0][1]
            yB = label[0][2]
            xB = label[0][3]
            ground_truth = label[0][4]
            # Get prediction of point A, B
            point_A = tf.stack([yA, xA], -1)
            point_B = tf.stack([yB, xB], -1)
            zA = tf.gather_nd(pred[i], point_A)
            zB = tf.gather_nd(pred[i], point_B)
            # Sum the loss of this training batch
            total_loss += loss(zA, zB, ground_truth)

        return total_loss