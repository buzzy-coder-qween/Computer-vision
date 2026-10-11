import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)

while True:
    success,img = cap.read()
    if not success:
        break
    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

