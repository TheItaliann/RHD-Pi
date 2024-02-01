import RPi.GPIO as GPIO
import time

motor_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin, GPIO.OUT)

pwm_frequency = 1000

pwm = GPIO.PWM(motor_pin, pwm_frequency)
pwm.start(0)

while True:
    eingabe = input("eingabe ")
    pwm.ChangeDutyCycle(eingabe)
    time.sleep(2)
        

pwm.stop()
GPIO.cleanup()
