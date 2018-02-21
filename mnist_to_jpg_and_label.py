import keras
from keras.datasets import mnist

import numpy as np
from PIL import Image, ImageOps
import os
import random

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def save_image(filename, data_array):

    #bgcolor = (0xff, 0xff, 0xff)
    bgcolor = (0x00, 0x00, 0xff)
    screen = (500, 375)

    img = Image.new('RGB', screen, bgcolor)

    mnist_img = Image.fromarray(data_array.astype('uint8'))
    mnist_img_invert = ImageOps.invert(mnist_img)

    #w = int(round(mnist_img.width * random.uniform(8.0, 10.0)))
    w = int(mnist_img.width*10)
    mnist_img_invert = mnist_img_invert.resize((w,w))

    #x = random.randint(0, img.width-w)
    #y = random.randint(0, img.height-w)
    x = int((img.width-w)/2)
    y = int((img.height-w)/2)
    img.paste(mnist_img_invert, (x, y))
    img.save(filename)

    return convert((img.width,img.height), (float(x), float(x+w), float(y), float(y+w)))

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

DIR_NAME = "JPEGImages"
if os.path.exists(DIR_NAME) == False:
    os.mkdir(DIR_NAME)

LABEL_DIR_NAME = "labels"
if os.path.exists(LABEL_DIR_NAME) == False:
    os.mkdir(LABEL_DIR_NAME)

j = 0
no = 0

for li in [x_train, x_test]:
    j += 1
    i = 0
    print("[---------------------------------------------------------------]")
    for x in li:
        # Write Image file
        filename = "{0}/{1:05d}.jpg".format(DIR_NAME,no)
        print(filename)
        ret = save_image(filename, x)
        print(ret)

        # Write label file
        label_filename = "{0}/{1:05d}.txt".format(LABEL_DIR_NAME,no)
        print(label_filename)
        f = open(label_filename, 'w')

        y = 0
        if j == 1:
            y = y_train[i]
        else:
            y = y_test[i]
        
        str = "{0:d} {1:f} {2:f} {3:f} {4:f}".format(y, ret[0], ret[1], ret[2], ret[3])
        f.write(str)
        f.close()

        i += 1
        no += 1
