import cv2
import numpy as np
from quitCV import close
from blank import blankPic

blank = blankPic()
# cv2.imshow('Blank', blank)

# 1. Paint the blank image
# blank[250:350, 350:450] = 0, 0, 255
# cv2.imshow('Green', blank)

# 2. Make a Rectangle in blank picture
cv2.rectangle(blank, (125, 125), (375, 375), (0, 255, 0), thickness=-1)
cv2.imshow('Rectangle', blank)

# # 2. 1 Make an Automatic Half Shape
# halfShape = cv2.rectangle(
#     dummyBlank, (50, 50), (dummyBlank.shape[1] // 2, dummyBlank.shape[1] // 2), (0, 0, 255), thickness=-1)
# cv2.imshow('Automatic Half Shape', halfShape)

# 3. Make a Circle in Blank Picture
circle = blankPic()
cv2.circle(circle, (250, 250), 100, (0, 255, 255), thickness=-1)
cv2.imshow('Circle', circle)

# 4. Make a Line in Blank Picture
line = blankPic()
cv2.line(line, (125, 250), (375, 250), (255, 0, 255), thickness=10)
cv2.imshow('Line', line)

# 5. Put a Text
blankText = blankPic()
cv2.putText(blankText, 'Hello My Name is Bobby', (0, 250),
            cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), thickness=1)
cv2.imshow('Text', blankText)

key = cv2.waitKey(0)
close(key)
