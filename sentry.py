import cv2 as cv 
import os
import numpy as np

def sentry(face_detect, face_recognize, names):
    face_recognize.read('classifier/classifier.yml')
    cam = cv.VideoCapture(0)
    name = ""
    font = cv.FONT_HERSHEY_TRIPLEX
    while True:
        ret, frame = cam.read()
        frame = cv.flip(frame, 1)
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = face_detect.detectMultiScale(gray_frame, 1.3, 5)

        for x,y,w,h in faces:
            cv.rectangle(frame, (x,y), (x+w, y+h), (175, 0, 0), 2)
            id, confidence = face_recognize.predict(gray_frame[y:y+h, x:x+w])

            if confidence < 100:
                name = os.listdir('dataset')[id*30 - 2].split()[-1].split('.')[0]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                name = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv.putText(frame, name, (x+5, y-5), font, 1, (255, 255, 255), 2)
            cv.putText(frame, str(confidence), (x+5, y+h-5), font, 1, (255, 255, 255), 1)
            
        cv.imshow('camera', frame)
        k = cv.waitKey(10) & 0xff 
        if k == 27:
            break
    cam.release()
    cv.destroyAllWindows()

