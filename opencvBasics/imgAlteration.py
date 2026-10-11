import cv2
import numpy as np

img = cv2.imread("../Resources/images.jpeg")
print(img.shape)

imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

imgCropped = img[100:200,200:400]

cv2.imshow("image",img)
cv2.imshow("Resized image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)