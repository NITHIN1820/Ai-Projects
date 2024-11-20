import cv2

vs = cv2.VideoCapture(0)   #Initializing Camera ID 0123456, 1234567

while True:
	_,img = vs.read()
	

	cv2.imshow("VideoStream", img)

	key = cv2.waitKey(1)

	print(key)
	
	if key == ord("q"):
		break
vs.release()
cv2.destroyAllWindows()
