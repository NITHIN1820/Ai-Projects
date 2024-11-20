
import cv2


img=cv2.imread("Babith.jpg")

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#dst = cv2.threshold(src, threshold, maxValueForThreshold,binary,type)[1] 

thresholdImg = cv2.threshold(grayImg,100,255,cv2.THRESH_BINARY)[1]


cv2.imshow("original",img)
cv2.imshow("threshold.jpg",thresholdImg)



#0 - White

#180 -

#255 - Black
