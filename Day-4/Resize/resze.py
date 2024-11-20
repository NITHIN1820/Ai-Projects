import cv2 #opencv-python

import imutils #resize

img = cv2.imread('Source.png') # read an image

resizedImg = imutils.resize(img, width=100) #resize process

cv2.imshow('Source.png', img)

cv2.imshow('Resized.jpg',resizedImg)










##cv2.imwrite('resizedImage.jpg', resizedImg)
