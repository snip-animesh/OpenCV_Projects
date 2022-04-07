from cvzone.SerialModule import SerialObject
import cv2 as cv

PORT = "COM5"
# imgLedOn = cv.imread("../Resources/LedOn.jpg")
# imgLedOff = cv.imread("../Resources/LedOff.jpg")
imgLedOn = cv.imread("../Resources/Pin13On.jpg")
imgLedOff = cv.imread("../Resources/Pin13Off.jpg")
arduino = SerialObject(PORT)
while True:
    arduino.sendData([1])
    cv.imshow("Image", imgLedOn)
    cv.waitKey(3000)  # waitKey in milliseconds
    arduino.sendData([0])
    cv.imshow("Image", imgLedOff)
    cv.waitKey(1000)
