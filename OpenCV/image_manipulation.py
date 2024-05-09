import cv2 as cv


# def changeSize(frame, scale = 0.5):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dim = (width, height)
#     return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

# img = cv.imread("sample.jpg", 1)
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
#
#
# cv.waitKey(0)


import random
img = cv.imread("sample.jpg")

eye1 = img[300:335, 645:720]
eye2 = img[300:335, 785:860]

img[500:535, 445:520] = eye1
img[500:535, 585: 660] = eye2

for i in range(300, 335):
    for j in range(645, 720):
        img[i][j] = [0, 0, random.randrange(255)]
    for j in range(785, 860):
        img[i][j] = [0, 0, random.randrange(255)]

cv.imshow("what-mine? Red-eyes-Mine", img)
cv.waitKey(0)
cv.imwrite("CVsample.jpg", img)

cv.destroyAllWindows()