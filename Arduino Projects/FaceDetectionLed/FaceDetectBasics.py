import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector

faceDetector = FaceDetector()

cap=cv.VideoCapture(1)
while True:
    success,img=cap.read()
    img,bbox=faceDetector.findFaces(img)
    cv.imshow("Images",img)
    cv.waitKey(1)
