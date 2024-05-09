import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}

for key in color_dict_HSV:
    color_dict_HSV[key] = np.array(color_dict_HSV[key])

while True:
    isTrue, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    # frame[:, :, 0] = 0
    # frame[:, :, 1] = 0
    # cv.imshow("Red-bitch", frame)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # mask = cv.inRange(hsv, color_dict_HSV['red1'][1], color_dict_HSV['red1'][0])
    # mask = 255 - mask
    lower_red = (0, 70, 50)
    upper_red = (10, 255, 255)
    mask1 = cv.inRange(hsv, lower_red, upper_red)
    lower_red = (170, 70, 50)
    upper_red = (180, 255, 255)
    mask2 = cv.inRange(hsv, lower_red, upper_red)
    mask = mask1 + mask2

    img = cv.bitwise_and(frame, frame, mask=mask)
    anti_img = cv.bitwise_and(frame, frame, mask=255-mask)

    cv.imshow("Lets go Live niggas-img", img)
    cv.imshow("Lets go Live niggas-mask", anti_img)

    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()