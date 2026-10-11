import cv2
import cvzone
import numpy as np
from cvzone.Utils import findContours

shape = cv2.imread("../Resources/shapes2.png")
shapeGray = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY)
shapeCanny = cv2.Canny(shapeGray, 50,100)
shapeDilate = cv2.dilate(shapeCanny, np.ones((4,4),np.uint8), iterations=1 )
shapeContour, conFound = findContours(shape, shapeDilate, filter=None, drawCon=True)

print(conFound[0]['bbox'])

shapeStack = cvzone.stackImages([shape,shapeGray,shapeCanny, shapeDilate, shapeContour], 3, 1)
cv2.imshow("Image Stack", shapeStack)

cv2.waitKey(0)