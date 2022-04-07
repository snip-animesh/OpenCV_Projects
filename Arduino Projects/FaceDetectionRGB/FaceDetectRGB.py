import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

faceDetector = FaceDetector()
arduino=SerialObject("COM5")

cap=cv.VideoCapture(1)
while True:
    success,img=cap.read()
    img,bbox=faceDetector.findFaces(img)
    if bbox:
        arduino.sendData([1,0])
    else:
        arduino.sendData([0,1])

    cv.imshow("Images",img)
    cv.waitKey(1)