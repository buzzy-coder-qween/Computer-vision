import cv2
import numpy as np

img = cv2.imread("../Resources/cardes.jpeg")

width,height = 250,350

#problem is i am not able to track the correct coordinates
pts1 = np.float32([[152,166],[278,143],[183,353],[324,323]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput  = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)