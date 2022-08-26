import os
import time
import cv2 as cv


if os.path.exists('dataset'):
    print('Folder already exists!')
else:
    os.mkdir('dataset')
    print('Directory created!')

def capture_face_data(cam, face_detect, id, name):
    print(name + " please stand in front of the camera")
    time.sleep(5)

    count = 0
    while(True):
        ret, frame = cam.read()
        frame = cv.flip(frame, 1)
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = face_detect.detectMultiScale(gray_frame, 1.3, 5)

        for x,y,w,h in faces:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            count += 1
            cv.imwrite("dataset/" + name + "." + str(id) + "." + str(count) + ".jpg", gray_frame[y:y+h, x:x+w])
        if count == 30:
            print(name + " your face has been registered!")
            break

def main():
    print("Testing...")        

if __name__ == "__main__":
    main()
