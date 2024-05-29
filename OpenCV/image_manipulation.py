import cv2 as cv
import numpy as np
import random

# def changeSize(frame, scale = 0.5):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dim = (width, height)
#     return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

img = cv.imread("sample.jpg", 1)
# resized_img = changeSize(img, 0.75)
# smol_img = cv.resize(img, (400, 400))
# another_img = cv.resize(img, (0, 0), fx = 1.25, fy = 0.25)
# rot_img = cv.rotate(resized_img, cv.ROTATE_90_CLOCKWISE)
#
# cv.imshow("Rotated-Mine", rot_img)
# cv.imshow("Another-Mine", another_img)
# cv.imshow("Smol-Mine", smol_img)
# cv.imshow("Mine", img)
# cv.imshow("Resized-Mine", resized_img)
#
# # for sc in range(1, 11):
# #     re_img = changeSize(img, sc/10)
# #     cv.imshow(f"Mine-{sc}-size", re_img)


# eye1 = img[300:335, 645:720]
# eye2 = img[300:335, 785:860]

# img[500:535, 445:520] = eye1
# img[500:535, 585: 660] = eye2

# for i in range(300, 335):
#     for j in range(645, 720):
#         img[i][j] = [0, 0, random.randrange(255)]
#     for j in range(785, 860):
#         img[i][j] = [0, 0, random.randrange(255)]

# cv.imshow("what-mine? Red-eyes-Mine", img)

# def translate(img, x, y):
#     trans_matrix = np.float32([[1, 0, x], [0, 1, y]])
#     dim = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, trans_matrix, dim)

# trans = translate(img, -100, -100)
# cv.imshow("Mine-moved", trans)

# def rotate(img, angle, center_point = None):
#     h, w = img.shape[0], img.shape[1]
#     if center_point == None:
#         center_point = (w//2, h//2)
#     rot_mat = cv.getRotationMatrix2D(center_point, angle, 1.0)
#     return cv.warpAffine(img, rot_mat, (w, h))

# rot = rotate(img, -45)
# cv.imshow("Rotated-Mine", rot)

# flp = cv.flip(img, -1)
# cv.imshow("Flipped-Mine", flp)

img = cv.resize(img, (0,0), fx = 0.6, fy =0.6)
cv.imshow("Mine", img)

canny = cv.Canny(img, 50, 100)
cv.imshow("Canned-Mine", canny)

cv.waitKey(0)

# cv.imwrite("CVsample.jpg", img)
cv.destroyAllWindows()