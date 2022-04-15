from cvzone.SerialModule import SerialObject

arduino=SerialObject("COM5")

while True:
    rgb=list(map(int,input().split()))
    # print(rgb)
    myData=arduino.getData()
    print(myData[0])
    if myData[0] ==1:
        arduino.sendData(rgb)
    elif myData[0] ==0:
        arduino.sendData([135])
