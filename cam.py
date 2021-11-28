import cv2
cam=cv2.VideoCapture(0)
while (cam.isOpened()):
	while (True):
		result,image=cam.read()
		cv2.imshow("img",img)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
	cam.release()
	cv2.destroyAllWindows()
else:
	print("Camera has not yet opened")

