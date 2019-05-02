# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:37:07 2019

@author: courtney
"""

import os
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

images = []
START = 0
STOP = 0
GLACIER_ID = '003'
YEAR = '2018'

chips_path = r'/home/courtney/Desktop/practice/'+GLACIER_ID+'_'+YEAR+'_'+'chips'
os.chdir(chips_path)
chips = sorted(os.listdir(chips_path))

for chip in chips:
    rchip = np.int16(plt.imread(chip))
    images.append(rchip)

(width, height)=np.shape(images[0])
gfiltered0 = np.zeros((width, height), dtype = np.int16)
gfiltered1 = np.zeros((width, height), dtype = np.int16)
gfiltered2 = np.zeros((width, height), dtype = np.int16)
lfiltered3 = np.zeros((width, height), dtype = np.int16)
lfiltered4 = np.zeros((width, height), dtype = np.int16)

#Filter each image with a gaussian filter and then take the difference
for i in range(44, 45, 1):
    scipy.ndimage.gaussian_filter(images[i],5, order=0, output=gfiltered0, mode='constant', cval=0.0, truncate = 3/10)
    scipy.ndimage.gaussian_filter(images[i+1],5, order=0, output=gfiltered1, mode='constant', cval=0.0, truncate = 3/10)
    plt.figure('Difference in Gaussian filtered images '+chips[i]+' and '+chips[i+1])
    plt.imshow(gfiltered0 - gfiltered1, cmap='seismic',vmin=-128, vmax=128, interpolation='none')
    plt.show()

#Take the difference between each image and then filter the resulting image
for i in range(44, 45, 1):
    plt.figure("Gaussian filter of difference between " + chips[i] + ' and ' + chips[i+1])
    scipy.ndimage.gaussian_filter(images[i]-images[i+1],5,order=0, output=gfiltered2, mode='constant', cval=0.0, truncate = 3/10)
    plt.imshow(gfiltered2, cmap='seismic', vmin=-128, vmax=128, interpolation='none')
    plt.show()


#The convolution operator is distributive, so I should get the same output, but I am not
plt.figure('Checking the difference')
plt.imshow((gfiltered0-gfiltered1)-gfiltered2, cmap = 'gray', vmin=-128, vmax=128, interpolation='none')
plt.show()

#Laplace filter
plt.figure('Laplace filter')
scipy.ndimage.laplace(gfiltered2, output=lfiltered3, mode='constant', cval=0.0)
plt.imshow(lfiltered3, cmap='gray', interpolation='none')
plt.show()
