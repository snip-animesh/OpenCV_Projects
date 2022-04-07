from cvzone.SerialModule import SerialObject

arduino = SerialObject("COM5")

while True:
    myData = arduino.getData()
    # myData = myData.decode("latin1")
    print(myData[0])