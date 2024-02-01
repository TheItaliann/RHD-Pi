import RPi.GPIO as GPIO
import time

motor_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin, GPIO.OUT)

pwm_frequency = 1000

pwm = GPIO.PWM(motor_pin, pwm_frequency)
pwm.start(0)

try:
    while True:
        eingabe = input("Eingabe (0-100, 'q' zum Beenden): ")
        if eingabe.lower() == 'q':
            break  # Beenden Sie die Schleife, wenn 'q' eingegeben wird
        duty_cycle = float(eingabe)
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
