import cv2
import numpy as np

cap = cv2.VideoCapture('http://192.168.75.157:8080/video')

while True:
    ret, frame = cap.read()
    resized = cv2.resize(frame, (600, 400))
    cv2.imshow("Android_cam", resized)

    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
