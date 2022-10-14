import cv2
from rescale import rescaleFrame
from quitCV import close

# THIS CODE IS TO READING IMAGES #
# img = cv2.imread("assets/Photos/cat_large.jpg")
# cap1 = cv2.imshow('Cat', img)
# cap2 = cv2.imshow('Cat_Resize', rescaleFrame(img, 0.1))
# key = cv2.waitKey(0)
# cv2.destroyAllWindows()

# THIS CODE IS TO READING VIDEOS #
# U can fill that with integer refer to your connected camera
cap = cv2.VideoCapture('assets/Videos/kitten.mp4')
i = 0

# # Using Loop, because the video will be rendered frame by frame
while True:
    i += 1
    check, frame = cap.read()
    video1 = cv2.imshow("Kucing", frame)
    video2 = cv2.imshow("Kucing Kecil", rescaleFrame(frame, 0.5))
    if cv2.waitKey(60) == 27:
        break
close()
