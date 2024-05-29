import cv2 as cv
import numpy as np

img = cv.resize(cv.imread("highway.jpg"), (0, 0), fx = 0.34, fy = 0.34)
# cv.imshow("Highway or Myway", img)
# cv.waitKey(0)
# img_gray = cv.resize(cv.imread("highway.jpg"), (0, 0), fx = 0.34, fy = 0.34)
template = cv.resize(cv.imread("blue_car.png"), (0,0), fx = 0.8, fy = 0.8)
th, tw = template.shape[:2]
                     
methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]
for method in methods:
    img_cpy = img.copy()
    result = cv.matchTemplate(img_cpy, template, method)

    # Single template matching
    # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result) 
    # location = min_loc if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED] else max_loc
    # bottom_right = (location[0]+tw, location[1]+th)
    # print(f"{method} and {location}")
    # cv.rectangle(img, location, bottom_right, (0, 165, 255), 2)

    # Multiple template matching
    threshold = 0.2 if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED] else 0.8
    location = np.where(result >= threshold)

    for loc in zip(*location[::-1]):
        # print(f"{method} and {loc}")
        bottom_right = (loc[0]+tw, loc[1]+th)
        cv.rectangle(img_cpy, loc, bottom_right, (0, 165, 255), 2)
    cv.imshow("Identify", img_cpy)
    cv.waitKey(0)

cv.destroyAllWindows()