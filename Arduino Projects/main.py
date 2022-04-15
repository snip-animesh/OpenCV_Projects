import pyfirmata ,time
comport = "COM8"
arduino = pyfirmata.Arduino(comport)

time.sleep(1)
#define
pinR=arduino.get_pin('d:14:o')
pinG=arduino.get_pin('d:15:o')
pinB=arduino.get_pin('d:16:o')


# pinR.write(1)
while True:
    pinR.write(0)
    pinG.write(1)
    pinB.write(0)
    print("done")

#     rgb=[map(int,input().split())]
#     pinR.write(rgb[0])
#     pinG.write(rgb[1])
#     pinB.write(rgb[2])

