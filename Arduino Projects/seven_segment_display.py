import pyfirmata
comport = "COM8"
arduino = pyfirmata.Arduino(comport)
digits=[
    [1,1,1,1,1,1,1], #0
    [0,1,1,0,0,0,0], #1
    [1,1,0,1,1,0,1], #2
    [1,1,1,1,0,0,1], #3
    [0,1,1,0,0,1,1], #4
    [1,0,1,1,0,1,1], #5
    [1,0,1,1,1,1,1], #6
    [1,1,1,0,0,1,0], #7
    [1,1,1,1,1,1,1], #8
    [1,1,1,1,0,1,1], #9
]

#define
pinA=arduino.get_pin('d:11:o')
pinB=arduino.get_pin('d:12:o')
pinC=arduino.get_pin('d:2:o')
pinD=arduino.get_pin('d:3:o')
pinE=arduino.get_pin('d:4:o')
pinF=arduino.get_pin('d:5:o')
pinG=arduino.get_pin('d:6:o')
pinD1=arduino.get_pin('d:7:o')
pinD2=arduino.get_pin('d:8:o')
pinD3=arduino.get_pin('d:9:o')
pinD4=arduino.get_pin('d:10:o')

pins=[pinA,pinB,pinC,pinD,pinE,pinF,pinG]

number=27
while True:
    for i in range(7):
        pins[i].write(digits[0][i])
    pinD3.write(0)
    pinD1.write(0)
    pinD2.write(0)
    pinD4.write(0)
