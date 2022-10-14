import cv2 as vision
from rescale import rescaleFrame

# Change VideoCapture to 1 {That is the index of your USB Port}, if U using external Webcam with USB Connecting
cam = vision.VideoCapture(0)

while True:
    check, frame = cam.read()
    resize = rescaleFrame(frame, 0.5)
    load1 = vision.imshow('Camera 1', frame)
    load2 = vision.imshow('Camera 2', resize)
    key = vision.waitKey(1)
    if key == 27:
        break

cam.release()
vision.destroyAllWindows()
