import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=2)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand1 = hands[0]
        #lmlist is the landmark list
        lmList = hand1["lmList"]
        handType = hand1["type"]

    cv2.imshow("Hand Detection", img)

    if cv2.waitKey(1)& 0XFF == ord('q'):
        break