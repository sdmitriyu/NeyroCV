import cv2
import numpy as np

bgr = np.zeros((450, 450, 3), dtype='uint8')

circle1 = cv2.circle(bgr, (bgr.shape[1] // 2, 220), 190, (233, 232, 232), 6)
circle2 = cv2.circle(bgr, (bgr.shape[1] // 2, 250), 80, (27, 149, 23), 6)

rectangle1 = cv2.rectangle(bgr, (110, 140), (320, 250), (0, 0, 0), cv2.FILLED)

line1 = cv2.line(bgr, (305, 250), (305, 140), (244, 4, 0), 6)
line2 = cv2.line(bgr, (145, 250), (145, 140), (244, 4, 0), 6)

line3 = cv2.line(bgr, (135, 140), (155, 140), (3, 0, 178), 6)
line4 = cv2.line(bgr, (295, 140), (315, 140), (3, 0, 178), 6)


cv2.imshow('Logo', bgr)
cv2.waitKey(0)
