from pyfirmata import util, STRING_DATA
import pyfirmata

servo_pin=7
arduino = pyfirmata.Arduino("COM6")
rgbR = arduino.get_pin('d:2:o')
rgbG = arduino.get_pin('d:3:o')
rgbB = arduino.get_pin('d:4:o')
arduino.digital[servo_pin].mode = pyfirmata.SERVO


def rgb(RGB):
    rgbR.write(RGB[0])
    rgbG.write(RGB[1])
    rgbB.write(RGB[2])


def servo(angle):
    arduino.digital[servo_pin].write(angle)


def lcd(name, roll):
    arduino.send_sysex(STRING_DATA, util.str_to_two_byte_iter(name))
    arduino.send_sysex(STRING_DATA, util.str_to_two_byte_iter(roll))
