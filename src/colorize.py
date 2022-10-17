import cv2

img = cv2.imread('assets/Photos/park.jpg')
cv2.imshow('Park', img)

# Converting to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Converting to Blur
blur = cv2.GaussianBlur(img, (7, 6), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

cv2.waitKey(0)
