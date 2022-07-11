import main
import cv2
import numpy as np
from cvzone.SerialModule import SerialObject

arduino = SerialObject("COM5")

cap = cv2.VideoCapture(0)
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)

# Observe maximum and minimum length of fingers by running
# main.py file
maximum_length = 120
minimum_length = 20

while True:
    succ, img = cap.read()
    # Getteing the length
    length = main.run(img)

    if length != None and length > maximum_length:
        length = maximum_length
    elif length != None and length < minimum_length:
        length = minimum_length
    if length != None:
        # print(length)
        # led_val = 255 * ((length - minimum_length) / (maximum_length - minimum_length))

        # Do the prev task using numpy
        led_val=np.interp(length, [minimum_length, maximum_length],[0,255])
        print(int(led_val))

        arduino.sendData([int(length)])
    else:
        arduino.sendData([0])
