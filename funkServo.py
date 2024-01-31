from time import sleep
from machine import Pin,PWM

servo_pin = 28
pwm = PWM(Pin(servo_pin))
pwm.freq(50)

def servo_str():
    Wert = int(input("eingabe PWM: "))
    pwm.duty_u16(Wert)
servo_str()
