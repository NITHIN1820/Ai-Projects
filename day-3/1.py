import cv2 #import lib

img = cv2.imread("novitech.png") # read the source img

cv2.imshow('display',img) #its show the sorce in our display
#opencv.syntax('name.jpg', source img )

cv2.imwrite('nithin.jpg',img) # save the image

cv2.waitKey(10000) #10 sec
cv2.destroyAllWindows() #close the output window
