import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(
    'E:\Python\Python_Projects\All Files\OpenCv\data\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('E:\Python\Python_Projects\All Files\OpenCv\data\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    #    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_found = False  # ---Initially set the flag to be False
for (x, y, w, h) in faces:
    if w > 0:  # --- Set the flag True if w>0 (i.e, if face is detected)
        face_found = True

        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)  # --- highlight the face
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, 'name', (0, 130), font, 1, (200, 255, 155))  # ---write the text

    cv2.imshow('Face having name', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
