import pyfirmata

comport = "COM6"
arduino = pyfirmata.Arduino(comport)
led1 = arduino.get_pin('d:5:o')
led2 = arduino.get_pin('d:6:o')
led3 = arduino.get_pin('d:7:o')
led4 = arduino.get_pin('d:8:o')
led5 = arduino.get_pin('d:9:o')


def led(total):
    if total == 0:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
    elif total == 1:
        led1.write(1)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
    elif total == 2:
        led1.write(1)
        led2.write(1)
        led3.write(0)
        led4.write(0)
        led5.write(0)
    elif total == 3:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        led4.write(0)
        led5.write(0)
    elif total == 4:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        led4.write(1)
        led5.write(0)
    elif total == 5:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        led4.write(1)
        led5.write(1)
