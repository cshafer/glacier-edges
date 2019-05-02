# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:01:01 2019

@author: courtney
"""

import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/home/courtney/Desktop/practice/chips')

uim01 = plt.imread('glacier003.2018-08-01.tif')
uim07 = plt.imread('glacier003.2018-08-07.tif')
uim13 = plt.imread('glacier003.2018-08-13.tif')
uim19 = plt.imread('glacier003.2018-08-19.tif')
uim25 = plt.imread('glacier003.2018-08-25.tif')

im01 = np.int16(uim01)
im07 = np.int16(uim07)
im13 = np.int16(uim13)
im19 = np.int16(uim19)

figure1, (ax11, ax12, ax13, ax14) = plt.subplots(nrows=1, ncols=4, figsize=(58, 8))
ax11.imshow(im01-im07, cmap='seismic', vmin = -255, vmax= 255)
ax12.imshow(im07-im13, cmap='seismic', vmin = -255, vmax= 255)
ax13.imshow(im13-im19, cmap='seismic', vmin = -255, vmax= 255)
ax14.imshow(im19-im25, cmap='seismic', vmin = -255, vmax= 255)

