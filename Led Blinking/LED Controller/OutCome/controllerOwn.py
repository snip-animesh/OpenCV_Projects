import pyfirmata

arduino = pyfirmata.Arduino("COM6")
led1 = arduino.get_pin('d:5:o')
led2 = arduino.get_pin('d:6:o')
led3 = arduino.get_pin('d:7:o')
led4 = arduino.get_pin('d:8:o')
led5 = arduino.get_pin('d:9:o')


def led(fingers):
    led1.write(fingers[0])
    led2.write(fingers[1])
    led3.write(fingers[2])
    led4.write(fingers[3])
    led5.write(fingers[4])
