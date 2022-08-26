import cv2 as cv
import numpy as np
import os
from PIL import Image

if(os.path.exists("classifier")):
    print("Directory Exists!")
else:
    os.mkdir("classifier")

def train(face_detect, face_recognize):
    paths = [os.path.join('dataset', fname) for fname in os.listdir('dataset')]
    faces_tr = []
    labels = []

    for path in paths:
        pil_img = Image.open(path).convert("L")
        cv_img = np.array(pil_img, 'uint8')
        id = int(path.split()[-1].split(".")[1])

        faces = face_detect.detectMultiScale(cv_img, 1.3, 5)
        for x,y,w,h in faces:
            faces_tr.append(cv_img[y:y+h, x:x+w])
            labels.append(id)

    print("Training the model......\n")
    face_recognize.train(faces_tr, np.array(labels))
    print("Training complete!\n")
    face_recognize.write('classifier/classifier.yml')

def main():
    print("Testing...")
    
if __name__ == "__main__" :
    main()

