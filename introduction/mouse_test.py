### This script opens a window and prints the actions of the mouse.

import cv2
import numpy as np

# mouse callback function
def dumpmouse(event,x,y,flags,param):
    print event, x, y, flags, param

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',dumpmouse)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
