#This program can be used to resize all images in a folder in to a particular dimension

import glob

import cv2

for image in glob.glob("*.jpg"):
	img=cv2.imread(image)
	resized=cv2.resize(img,(32,64))
	cv2.imwrite(str(image),resized)

