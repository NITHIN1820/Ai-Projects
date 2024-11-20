import cv2

img = cv2.imread('novitech.png')

#dst = cv2.GaussianBlur(src, (kernel),borderType)
gaussianImg = cv2.GaussianBlur(img, (41, 41), 50)
gaussianImg1 = cv2.GaussianBlur(img, (21, 21), 0)
gaussianImg2 = cv2.GaussianBlur(img, (91, 91), 0)

cv2.imshow("Original", img)
cv2.imshow("GaussianBlur", gaussianImg)
cv2.imshow("GaussianBlur1", gaussianImg1)
cv2.imshow("GaussianBlur2", gaussianImg2)












