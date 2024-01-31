from time import sleep
from machine import Pin,PWM
from PPMDecoder import callback

servo_pin = 28
pwm = PWM(Pin(servo_pin))
pwm.freq(50)

def servo_str():
    pwm.duty_u16(valServo)

while True:
    servo_str()
    sleep(1)
