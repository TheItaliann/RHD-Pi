from time import sleep
from machine import Pin,PWM
from PPMDecoder import callback

def map_value(percentage:int) -> int:
    return int((percentage - 0) * (8620 - 1638) / (100 - 0) + 1638)

servo_pin = 28
pwm = PWM(Pin(servo_pin))
pwm.freq(50)

values = callback()
valServo = map_value(100)

def servo_str():
    pwm.duty_u16(valServo)

while True:
    servo_str()
    sleep(1)
