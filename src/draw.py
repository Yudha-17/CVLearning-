import cv2
import numpy as np
from quitCV import close

blank = np.zeros((500, 700, 3), dtype='uint8')
cv2.imshow('Blank', blank)

# 1. Paint the blank image
blank[250:350, 350:450] = 0, 0, 255
cv2.imshow('Green', blank)

# 2. Make a Rectangle in blank picture

key = cv2.waitKey(0)
close(key)
