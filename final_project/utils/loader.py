"""
Functions to load images and labels.
"""
import numpy as np
from PIL import Image # use Python Imaging Library to load images

def load_images(filename_list, DIW_PATH, input_width, input_height):
    """
    Load images from path with givn filenames.
    Input
    - filename_list: a list of filenames
    """
    images = list()
    for i in range(len(filename_list)):
        filename = filename_list[i]
        # filename starts with a ".", which we should discard when loading
        # print(DIW_PATH + filename[1:]) # DEBUG USE
        pic = Image.open(DIW_PATH + filename[1:])
        pic = pic.resize((input_width, input_height)) # we have already scaled the label, now scale the image
        # pic.show() # DEBUG USE
        pic = np.array(pic, dtype = float) # conevrt to numpy array

        # check if it is a gray image
        if len(pic.shape) < 3:
            pic = np.expand_dims(pic, 2)
            pic = np.concatenate((pic,)*3, -1)

        images.append(pic)
    return np.stack(images, axis=0)

def load_labels(filename_list, depth_info):
    """
    Load corresponding labels according to given filenames.
    Input
    - filename_list: a list of filenames
    - depth info: a dictionary of {filename:[yA XA，yB，xB,relation]}
    """
    labels = list()
    for i in range(len(filename_list)):
        filename = filename_list[i]
        labels.append(depth_info[filename]) # get corresponded depth information as the label
    return np.asarray(labels)