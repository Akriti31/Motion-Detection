import cv2
import numpy as np
import time

cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame =cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    cv2.imshow('fg',fgmask)
    
    if cv2.waitKey(1)& 0xFF ==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
