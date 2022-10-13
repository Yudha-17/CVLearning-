import cv2 as vision

# Change VideoCapture to 1, if U using external Webcam with USB Connecting
cam = vision.VideoCapture(0)

while True:
    check, frame = cam.read()
    vision.imshow('Gimmick Camera', frame)
    key = vision.waitKey(1)
    if key == 27:
        break

cam.release()
vision.destroyAllWindows()
