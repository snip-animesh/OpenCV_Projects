import pyfirmata
arduino = pyfirmata.Arduino("COM8")
rgbR = arduino.get_pin('d:2:o')
rgbG = arduino.get_pin('d:3:o')
rgbB = arduino.get_pin('d:4:o')
arduino.digital[5].mode=pyfirmata.SERVO


def rgb(RGB):
    rgbR.write(RGB[0])
    rgbG.write(RGB[1])
    rgbB.write(RGB[2])

def servo(angle):
    arduino.digital[5].write(angle)

