import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while True:
    isTrue, frame = cap.read()
    frame = cv.resize(frame, (frame.shape[0], frame.shape[0]))
    img = np.zeros(frame.shape, np.uint8)
    # width = int(cap.get(3))
    # height = int(cap.get(4))
    width, height = frame.shape[0], frame.shape[0]
    smol_frame = cv.resize(frame, (0, 0), fx = 0.5, fy = 0.5)

    img[height//2:, width//2:] = cv.rotate(smol_frame, cv.ROTATE_90_COUNTERCLOCKWISE)
    img[:height//2, :width//2] = cv.rotate(smol_frame, cv.ROTATE_90_CLOCKWISE)
    img[height//2:, :width//2] = smol_frame
    img[:height//2, width//2:] = cv.rotate(smol_frame, cv.ROTATE_180)

    cv.imshow("Live Video", img)

    if(cv.waitKey(10) & 0xFF == ord('q')):
        break


cap.release()
cv.destroyAllWindows()

