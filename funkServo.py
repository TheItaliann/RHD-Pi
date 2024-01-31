from time import sleep
from machine import Pin,PWM

servo_pin = 28


def servo_str():
    pwm = PWM(Pin(servo_pin))
    Wert = int(input("eingabe PWM: "))
    pwm.duty_u16(Wert)
