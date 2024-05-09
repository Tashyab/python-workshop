import cv2 as cv
import numpy as np 

img = cv.imread("chessboard.png")
# cv.imshow("Chessboard", img)
# cv.waitKey(0)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray_img, 100, 0.05, 10)
corners = np.intp(corners)

xlist, ylist = [], []
for corner in corners:
    x, y = np.ravel(corner)
    img = cv.circle(img, (x, y), 5, (255, 0, 255), -1)

for i in range(len(corners)):
    pt1 = np.ravel(corners[i])
    darr = []
    dmin = 1000
    corner1 = tuple(pt1)
    for j in range(i + 1, len(corners)):
        pt2 = np.ravel(corners[j])
        d = np.linalg.norm(pt1 - pt2)
        darr.append(d)
        if d < dmin:
            corner2 = tuple(pt2)
    color = tuple(map(int, np.random.randint(0, 255, size = 3)))
    img = cv.line(img, corner1, corner2, color, 1)

# cv.imshow("Grayscale Chessboard", gray_img)
cv.imshow("Corners in a chessboard", img)
cv.waitKey(0)

cv.destroyAllWindows()