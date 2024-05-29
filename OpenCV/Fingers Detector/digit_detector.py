import cv2 as cv
import numpy as np
import time, os
import keras
from mediapipe.python.solutions import hands, drawing_utils, drawing_styles

mpHands = hands.Hands(static_image_mode=False, max_num_hands=6)
pTime = 0
cTime = 0

def num_fingers(hand_landmarks):
    fingers = 0
    thumb = 0
    direction = 1 # Upright Hand
    if hand_landmarks[9].y > hand_landmarks[0].y: 
        direction = 0 # Inverted Hand

    # Thumb
    if((hand_landmarks[17].x > hand_landmarks[4].x and hand_landmarks[4].x < hand_landmarks[3].x) or 
        (hand_landmarks[17].x < hand_landmarks[4].x and hand_landmarks[4].x > hand_landmarks[3].x)):
                thumb = 1

    # Fingers
    for hl in range(8, 22, 4):
        if(hand_landmarks[hl].y < hand_landmarks[hl-1].y):
            fingers += 1

    if direction:
        return fingers+thumb
    else:
        return (4-fingers)+thumb

cap = cv.VideoCapture(0)
while True:
    isTrue, frame = cap.read()
    frame = cv.flip(frame, 1)
    imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = mpHands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for hls in results.multi_hand_landmarks:
            pad = 20
            x1 = np.min([int(landmark.x*frame.shape[1]) for landmark in hls.landmark])-pad
            y1 = np.min([int(landmark.y*frame.shape[0]) for landmark in hls.landmark])-pad
            x2 = np.max([int(landmark.x*frame.shape[1]) for landmark in hls.landmark])+pad
            y2 = np.max([int(landmark.y*frame.shape[0]) for landmark in hls.landmark])+pad
            cv.putText(frame, str(num_fingers(hls.landmark)), (x1-20, y1-20), cv.FONT_HERSHEY_COMPLEX, 2, (30, 255, 30))
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            drawing_utils.draw_landmarks(frame, hls, hands.HAND_CONNECTIONS, drawing_styles.get_default_hand_landmarks_style(), drawing_styles.get_default_hand_connections_style())

            
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(frame, f"FPS: {fps:.2f}", (frame.shape[1]-200, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv.imshow("LIVE", frame)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()