import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

from face_recognizer_train import label_map
label_map = label_map

def recognize(imgpath):
    img = cv.imread(imgpath)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f"Label: {str(label_map[label])} with Confidence: {confidence}")
        cv.putText(img, str(label_map[label]), (x-10, y-10), cv.FONT_HERSHEY_COMPLEX, 2.0, (0, 255, 0), 3, cv.LINE_AA)
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)
    
    img = cv.resize(img, (400, 400), interpolation=cv.INTER_AREA)
    cv.imshow('Detected Face', img)
    cv.waitKey(0)

recognize(r'C:\Users\Acer\3D Objects\Projects\python-workshop\OpenCV\Face Recognizer\Test Images\priyanka_sample.jpg')
