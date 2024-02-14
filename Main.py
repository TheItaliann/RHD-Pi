import utime
from PPM_decoder import button_state
from funkServo import servo_st
from machine import Pin, PWM
from PPMDecoder import convert

def map_value(percentage: int) -> int:
    return int((percentage - 0) * (8620 - 1638) / (100 - 0) + 1638)

servo_pin = 28
pwm_servo = PWM(Pin(servo_pin))
pwm_servo.freq(50)

ESC_PIN = 16
pwm_esc = PWM(Pin(ESC_PIN))
pwm_esc.freq(50)
speed = 100

def set_speed(speed):
    speed = min(max(speed, 0), 100)
    duty_cycle = int(speed * 10.24)
    pwm_esc.duty_u16(duty_cycle)

running = False

while True:
    channel_3_state = button_state()  # Assuming button_state() returns the state of channel 3
    if channel_3_state == "on":
        running = True
    elif channel_3_state == "off":
        running = False

    if running:
        values = convert()
        valServo = map_value(values[0])
        servo_st(valServo)
        set_speed(speed)
        
    else:
        while button_state() != "on":
            # Pausing until the button is turned on again
            utime.sleep(0.1)  # Adjust the sleep duration as needed
