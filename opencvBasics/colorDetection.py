import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

cap = cv2.VideoCapture(0)

myColorFinder = ColorFinder(trackBar=True)

hsvVal = [  {'hmin': 37, 'smin': 37, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255},
            {'hmin': 23, 'smin': 215, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255},
            {'hmin': 49, 'smin': 147, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}
          ]

while True:
    success,img = cap.read()
    if not success:
        break

    imgColor, mask = myColorFinder.update(img, hsvVal)

    imgStack = cvzone.stackImages([img, imgColor, mask], 3, 0.5)

    cv2.imshow("Colour Detection",imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
