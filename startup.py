import setup
import trainer
import sentry
import os 
import cv2 as cv
from PIL import Image

startup_text = open("startup.txt", "r")
print(startup_text.read())
family_names = {}

face_detect = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_recognize = cv.face.LBPHFaceRecognizer_create()
cam = cv.VideoCapture(0)

while(True):
    option = input("SENTRY-->")
    option = option.lower()

    if option == "setup":
        print("How many members do you want to register?")
        mems = int(input())
        print("\n")
        print("Enter their names:")
        for i in range(mems):
            name = input()
            family_names[i] = name

        
        for id in family_names:
            setup.capture_face_data(cam, face_detect, id, family_names[id])
            cam.release()
            cv.destroyAllWindows()
        
        trainer.train(face_detect, face_recognize)

    elif option == "start":
        sentry.sentry(face_detect, face_recognize, family_names)
    
    elif option == "reset":
        print("Resetting will erase all the data. Are you sure you want to go ahead? Y/N")
        choice = input()
        
        if choice == "Y":
            print("Deleting face data......")
            for file in os.listdir('dataset'):
                os.remove(os.path.join('dataset', file))
            os.remove('classifier/classifier.yml')
            print("Face data cleared!")
            continue
        if choice == "N":
            continue
       
    elif option == "exit":
        break


    
    



