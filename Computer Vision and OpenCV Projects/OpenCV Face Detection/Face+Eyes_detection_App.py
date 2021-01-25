'''
step1. GoTo Command Prompt and install package opencv using command 'pip install opencv-python'

after running the code
'''

import numpy as np
import cv2, time

# We point OpenCV's CascadeClassifier function to where our
# classifier (XML file format) is stored
#face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Update your image path Here!
img = cv2.imread('C:/Users/gsc-30431/PycharmProjects/test1.py/Python_Projects/FaceDetection_App/img3.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# When no faces detected, face_classifier returns and empty tuple
if faces is ():
    print("No Face Found")

for (x ,y ,w ,h) in faces:
    cv2.rectangle(img ,(x ,y) ,( x +w , y +h) ,(255 ,0 ,0) ,2)
    cv2.imshow('img' ,img)
    cv2.waitKey(100)
    roi_gray = gray[y: y +h, x: x +w]
    roi_color = img[y: y +h, x: x +w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex ,ey ,ew ,eh) in eyes:
        cv2.rectangle(roi_color ,(ex ,ey) ,(ex +ew ,ey +eh) ,(0 ,255 ,0) ,2)
        cv2.imshow('img' ,img)
        cv2.waitKey(500)

    cv2.waitKey(500)


cv2.waitKey(0)
cv2.destroyAllWindows()