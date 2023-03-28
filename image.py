# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 12:29:02 2023

@author: ASUS
"""
## import part

import imageio

#opencv
import cv2 as cv

#scikit image
import skimage

import matplotlib.pyplot as plt

import numpy as np

#pilow
from PIL import Image


#reading image

img_one = cv.imread(r'dataset/images/b.jpg')
print('shape of image one: ' , img_one.shape)

#print(img_one)

plt.imshow(img_one)
plt.title('Image1')
plt.axis('off')

#pillow 

img_one_pil = Image.open(r'dataset/images/b.jpg')
plt.imshow(img_one_pil)
plt.title('Image1 pil')
plt.axis('off')


