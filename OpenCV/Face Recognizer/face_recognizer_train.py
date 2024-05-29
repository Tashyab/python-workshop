import numpy as np
import cv2 as cv
import os

DIR = r"C:\Users\Acer\3D Objects\Projects\python-workshop\OpenCV\Face Recognizer\ImgRecog Dataset\Faces"

CLASSES = []
for files in os.listdir(DIR):
    CLASSES.append(files)

LABELS = []
FEATURES = []

label_map = dict(zip([i for i in range(len(CLASSES))], CLASSES))
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

def train_recog():
    for person in CLASSES:
        label = CLASSES.index(person)
        filepath = os.path.join(DIR, person)

        for files in os.listdir(filepath):
            imgpath = os.path.join(filepath, files)
            img_arr = cv.imread(imgpath)
            gray = cv.cvtColor(img_arr, cv.COLOR_RGB2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]
                FEATURES.append(face_roi)
                LABELS.append(label)

if __name__=="__main__":
    print("-----------Training started")
    train_recog()
    # print("Number of labels: ", len(LABELS))
    # print("Number of features: ", len(FEATURES))
    print("Training done---------")

    FEATURES = np.array(FEATURES, dtype='object')
    LABELS = np.array(LABELS)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.train(FEATURES, LABELS)

    np.save('features.npy', FEATURES)
    np.save('labels.npy', LABELS)
    face_recognizer.save('face_trained.yml')
