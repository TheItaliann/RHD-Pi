from time import sleep
from machine import Pin,PWM
from PPMDecoder import convert 

def map_value(percentage:int) -> int:
    return int((percentage - 0) * (8620 - 1638) / (100 - 0) + 1638)

servo_pin = 28
pwm = PWM(Pin(servo_pin))
pwm.freq(50)

values = convert()
valServo = map_value(values[0])

def servo_str():
    pwm.duty_u16(valServo)

while True:
    servo_str()
    sleep(0.001)
