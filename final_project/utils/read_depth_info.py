"""
Define read_depth_info function.
"""
import math

def read_depth_info(path, input_height = 240, input_width = 320):
    '''
    Function to read in annotations from .csv file.
    Input 
    - path: str. the path of DIW_train_val.csv file.
    - input_height = 240
    - input_width = 320
    Output
    - depth_info: dictionary. {filename: [yA, xA, yB, xB, label]}
    ''' 
    depth_info = dict()# create empty dict for labels

    with open(path, 'r') as read: # read designated .csv
        lines = read.readlines()
        info = list() # create an empty list
        for line in lines: # get every line in DIW_train_val.csv
            if len(line.rstrip('\n')) == 0:
                continue
            info.append(line.rstrip('\n'))

    # define a rule for changing label notation
    change_notation = {'<': -1, '=': 0, '>': 1}
    
    i = 0
    while i < len(info):
        filename = info[i] # get file name
        pair_info = info[i+1].split(',') # get point pair information, pair info has 7 elements
        pair_info[4] = change_notation[pair_info[4]] # apply the rule for changing label notation
        pair_info = [int(v) for v in pair_info]

        # scale the point pair (A and B) according to the real shape of the image
        ori_img_width = float(pair_info[5]) # get real shape, which is not always 320x240
        ori_img_height = float(pair_info[6])
        yA_scale = float(pair_info[0]-1)/ori_img_height # calculate normalized A position
        xA_scale = float(pair_info[1]-1)/ori_img_width
        yB_scale = float(pair_info[2]-1)/ori_img_height # calculate normalized B position
        xB_scale = float(pair_info[3]-1)/ori_img_width
        yA = min(input_height-1, max(0, math.floor(yA_scale * input_height))) # project normalized A position to 320x240
        xA = min(input_width -1, max(0, math.floor(xA_scale * input_width)))
        yB = min(input_height-1, max(0, math.floor(yB_scale * input_height))) # project normalized B position to 320x240
        xB = min(input_width -1, max(0, math.floor(xB_scale * input_width)))

        # prevent A and B being scaled to the same point
        if (yA == yB) and (xA == xB): # if this happens
            if yA_scale > yB_scale:
                yA = min(yA + 10, input_height-1) # move yA a little
            else:
                yA = max(yA - 10, 0)
            if xA_scale > xB_scale:
                xA = min(xA + 10, input_width-1) # move xA a little
            else:
                xA = max(xA - 10, 0)
        
        # append new key (filename) and value (point pair and relative depth)
        temp = list()
        temp.append([int(yA), int(xA), int(yB), int(xB), int(pair_info[4])]) # the processed depth_info
        depth_info[filename] = temp 
        i += 2

    print("Successfully processed {} labels from {}.".format(len(depth_info), path))
    return depth_info