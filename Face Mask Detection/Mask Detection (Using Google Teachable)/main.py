import cvzone
import cv2 as cv
from cvzone.ClassificationModule import Classifier

cap=cv.VideoCapture(1)
myClassifier=Classifier("keras_model.h5","labels.txt")

while True:
    success,img=cap.read()
    predictions=myClassifier.getPrediction(img,scale=1)

    cv.imshow("Image",img)
    k=cv.waitKey(1)
    if k==ord("q"):
        break