import cv2 as cv


def close(confirmation=27):
    if confirmation == 27:
        return cv.destroyAllWindows()
