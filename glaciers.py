# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 08:15:21 2018

@author: courtney
"""
import time
import re
import subprocess
import os
import matplotlib.pyplot as plt

start_time = time.time()

init_path = r"/home/courtney/Desktop/practice/"
os.chdir(init_path)

# glaciers_path = r"/home/courtney/Desktop/practice/glaciers.txt"
glaciers_path = r"/home/courtney/Desktop/practice/av_glaciers.txt"
# mosaics_path = r"/home/courtney/Desktop/practice/mosaics50m/"
mosaics_path = r"/Volumes/insar9/ian/Sentinel1/quadrants/mosaics50m"
# chips_path = r"/home/courtney/Desktop/practice/chips/"
chips_path = r"/home/courtney/Desktop/practice/035_2018_chips"


def Get_vrt(date):
    '''
    Returns the .vrt file associated with a particular
    directory labeled with the date in which radar imagery
    was captured
    '''
    for file in os.listdir(date):
        if file.endswith('.vrt'):
            vrt = file
    return vrt


def Create_chips(vrt, date, glacier_info):
    '''
    Cuts multiple glacier "chips" from a .vrt file whose corner
    coordinates are specified from the text file, "glacier_info"
    '''
    lines = [line.rstrip('\n') for line in open(glacier_info)]
    for line in lines:
        glacier_coords = line.split(' ')
        subprocess.call(['gdalwarp', '-t_srs', 'EPSG:3413', '-te', glacier_coords[1], glacier_coords[2], glacier_coords[3], glacier_coords[4], '-tr', '50', '50', vrt, glacier_coords[0]+'.'+date+'.tif'])
'''
dated_directories = []
date_regex = re.compile(r"2018-\d{2}-\d{2}")
for directory in sorted(os.listdir(mosaics_path)):
    if date_regex.search(directory) is not None:
        dated_directories.append(directory)

for date in dated_directories:
    date_path = mosaics_path + '/' + date
    os.chdir(date_path)
    vrt_path = date_path + '/' + Get_vrt(date_path)
    os.chdir(chips_path)
    Create_chips(vrt_path, date, glaciers_path)
'''


directories = sorted(os.listdir(mosaics_path))
date_regex = re.compile(r"2018-\d{2}-\d{2}")  # For example, 2018-04-12

for date in directories:
    if date_regex.search(date) is not None:
        date_path = mosaics_path + '/' + date
        os.chdir(date_path)
        vrt_path = date_path + '/' + Get_vrt(date_path)
        os.chdir(chips_path)
        Create_chips(vrt_path, date, glaciers_path)

print("--- %s seconds ---" % (time.time() - start_time))

'''
subprocess.call("./cutchips", shell=True)

images = []

for tif in os.listdir(cwd):
    if tif.lower().endswith('.tif'):
        images.append(tif)

plt.figure(1)
count=1

for i in images:
    image = plt.imread(i)
    plt.subplot(2, 5, count)
    plt.imshow(image, cmap='gray')
    count=count+1

plt.show()'''
