import cv2 as cv

cap = cv.VideoCapture(0)
while True:
    isTrue, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    img = cv.line(frame, (0, 0), (width, height), (0, 0, 255), 10)
    img = cv.line(frame, (0, height), (width, 0), (0, 0, 255), 10)
    img = cv.rectangle(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv.circle(frame, (width//2, height//2), 60, (0, 255, 0), 10)
    img = cv.circle(frame, (width//2, height//2), 20, (0, 255, 0), -1)
    font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
    img = cv.putText(frame, "Yo bitch! I can draw.", (30, 60), font, 2, (0, 0, 0), 2, cv.LINE_AA)
    cv.imshow("Live with drawing", frame)
    if(cv.waitKey(10) & 0xFF == ord('q')):
        break

cap.release()
cv.destroyAllWindows()