# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:28:12 2019

@author: courtney
"""

# This code will take the difference between 2 images and display the resulting
# image in a separate window. It is assumed that the user used glaciers.py to
# create the chips and stored them in a separate file. That file is formatted
# as "###_YYYY_chips" where ### is the glacier id and YYYY is the year we're
# considering. The specified range can be modified with "START" and "STOP" to
# consider only a specific set of images. The original imagery used is also
# displayed

import os
import numpy as np
import matplotlib.pyplot as plt

START = 0
STOP = 5
GLACIER_ID = '047'
YEAR = '2018'

images = []
chips_path = r'/home/courtney/Desktop/practice/'+GLACIER_ID+'_'+YEAR+'_'+'chips'
os.chdir(chips_path)
chips = sorted(os.listdir(chips_path))

for chip in chips:
    rchip = np.int16(plt.imread(chip))
    images.append(rchip)

for i in range(START, STOP, 1):
    plt.figure("Difference between " + chips[i] + ' and ' + chips[i+1])
    plt.imshow(images[i]-images[i+1], cmap='seismic', vmin=-128, vmax=128)
    plt.show()

for i in range(START, STOP+1, 1):
    plt.figure()
    plt.title(chips[i])
    plt.imshow(images[i], cmap='gray', vmin=0, vmax=255)
    plt.show()
