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
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Load our image then convert it to grayscale
# Update your image path Here!
image = cv2.imread('C:/Users/gsc-30431/PycharmProjects/test1.py/Python_Projects/FaceDetection_App/img2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Our classifier returns the ROI of the detected face as a tuple
# It stores the top left coordinate and the bottom right coordiantes
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# When no faces detected, face_classifier returns and empty tuple
if faces is ():
    print("No faces found")

# We iterate through our faces array and draw a rectangle
# over each face in faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Face Detection', image)
    cv2.waitKey(1200)
cv2.waitKey(0)
cv2.destroyAllWindows()