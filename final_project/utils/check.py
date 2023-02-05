"""
Check function.
"""
import tensorflow as tf

def check(zA, zB, relation):
    """
    Directly check correctness, called by check_fn.
    za, zb: the predicted depth of point a, b
    relation: the ground-truth ordinal relations. closer (+1), further (-1), and equal (0).
    """
    if (relation==1) and (zA < zB): # 1 means A is closer than B
        return 1
    elif (relation==-1) and (zA > zB): # -1 means B is closer than A
        return 1
    elif (relation==0) and (zA == zB): # 0 means equally close
        return 1
    else:
        return 0

def check_fn(labels, output):
    """
    Function, check whether the predicted depth relation is correct.
    Inputs:
    - labels: 3-D tensor, relative depth data, [batch, 1, 5]
    - output: output of  4-D tensor, [batch, height, width, channel]
    For the thrid dimension, 5 numbers are [yA, xA, yB, xB, label] (x: width, y: height, label: relation)
    """
    # counter init
    total_correct = 0
    # remove the last dimension of output (channel) 
    pred = tf.reshape(output, output.shape[0:3])
    
    for i,label in enumerate(labels): # loop every image in the batch

        # Get point A, B and their relation from labels
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
        # Count correctly classified images
        total_correct += check(zA, zB, ground_truth)
        
    return total_correct