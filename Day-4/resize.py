import cv2
import imutils

img= cv2.imread('Babith.jpg')

resizeImg= imutils.resize(img,width=500)

cv2.imshow('Babith.jpg',img)
cv2.imshow('resized.jpg',resizeImg)
