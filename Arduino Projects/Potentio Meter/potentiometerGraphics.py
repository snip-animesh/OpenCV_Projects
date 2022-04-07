import numpy as np
from cvzone.SerialModule import SerialObject
import cv2 as cv
import keyboard

arduino = SerialObject("COM5")

while True:
    myData = arduino.getData()
    print(myData[0])
    img = cv.imread('potentiometer.jpg')
    try:
        val = myData[0]
        cv.putText(img, val.zfill(4), (260, 280), cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
        val = np.interp(int(myData[0]), [0, 1023], [-90, 270])
    except:
        continue
    if int(myData[0]) != 0:
        cv.ellipse(img, (320, 265), (131, 131), 0, -90, val, (255, 100, 0), 10)
    cv.imshow("Image", img)
    cv.waitKey(1)
    if keyboard.is_pressed("esc"):
        break
