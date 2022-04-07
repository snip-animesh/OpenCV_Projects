from cvzone.SerialModule import SerialObject
import time

PORT="COM5"
arduino=SerialObject(PORT)
while True:
    arduino.sendData([1])
    time.sleep(3)
    arduino.sendData([0])
    time.sleep(1)
