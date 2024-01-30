from time import sleep
from machine import Pin,PWM
servo_pin = 28

while True:
    Wert = int(input("eingabe PWM: "))
    if Wert == "00":
        break

    pwm = PWM(Pin(servo_pin))

    pwm.duty_u16(Wert)
