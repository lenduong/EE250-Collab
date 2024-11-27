import cv2

cam = cv2.VideoCapture(0)

#while True:
ret, image = cam.read()
#cv2.imshow('Imagetest',image)
#k = cv2.waitKey(1)
#if k != -1:
#	break

#image_path = r'~/ee250_fp_grish_le/testing/testimage.jpg'
#image = cv2.imread(image_path)

cv2.imwrite('./testing/testimage2.jpg', image)
cam.release()
#cv2.destroyAllWindows()
