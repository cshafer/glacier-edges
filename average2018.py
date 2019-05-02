# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:06:04 2019

@author: courtney
"""

# Getting an average over time for one chip location
# First I created a new directory called 003_2018_chips
# containing all the chips generated using the glaciers.py
# for just the 003 glacier and for the year 2018

import os
import numpy as np
import matplotlib.pyplot as plt

images = []
chips_path = r"/home/courtney/Desktop/practice/047_2018_chips/"
os.chdir(chips_path)

for chips in os.listdir(chips_path):
    chip = np.int16(plt.imread(chips))
    images.append(chip)

asum = np.zeros((176, 201), dtype=np.int16)

for i in range(len(images)):
    asum = asum + images[i]

average = asum/len(images)

figure1, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4)
ax1.imshow(average, cmap='gray', vmin=0, vmax=255, interpolation='none')
ax2.imshow(images[35] - average, cmap='gray', vmin=-128, vmax=128, interpolation = 'none')
ax3.imshow(images[36] - average, cmap='seismic', vmin=-128, vmax=128)
ax4.imshow(images[37] - average, cmap='seismic', vmin=-128, vmax=128)
