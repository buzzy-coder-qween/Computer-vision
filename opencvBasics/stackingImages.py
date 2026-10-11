import cv2
import numpy as np
import stackFunction #created a new python file for the function which helps in stacking images and videos


image = cv2.imread("../Resources/images.jpeg")
kernel = np.ones((5,5), np.uint8)


imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(image,150,200)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

StackedImages= stackFunction.stackImages(0.8, ([image, imgGray, imgBlur], [imgCanny, imgDilation, imgEroded]))

#cv2.imshow("Original",image)
#cv2.imshow("Gray image", imgGray)
#cv2.imshow("Blur image", imgBlur)
#cv2.imshow("Canny image", imgCanny)
#cv2.imshow("Dilated image", imgDilation)
#cv2.imshow("Eroded image", imgEroded)
cv2.imshow("StackedImage",StackedImages)

cv2.waitKey(0)