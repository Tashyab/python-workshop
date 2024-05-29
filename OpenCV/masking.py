import cv2 as cv
import numpy as np

img = cv.resize(cv.imread('sample.jpg'), (0, 0), fx = 0.5, fy = 0.5)
cv.imshow("Sample", img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 80, 255, -1)
cv.imshow("Mask", mask)
masked_img = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Masked Image", masked_img)

cv.waitKey(0)
cv.destroyAllWindows()