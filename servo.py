from machine import Pin, PWM
import time

servo_pin = 7

servo_pwm = PWM(Pin(servo_pin), freq=50)  # Passen Sie die Frequenz an, falls erforderlich

def servo_position(angle):
    duty_cycle = int(((angle / 180) * 1000) + 500)
    servo_pwm.duty_u16(duty_cycle)

try:
    while True:
        for angle in range(0, 180, 10):  # Ändern Sie den Bereich je nach Ihren Anforderungen
            servo_position(angle)
            time.sleep_ms(500)  # Ändern Sie die Verzögerung je nach Ihren Anforderungen
except Exception as e:
    print("Fehler:", e)
    servo_pwm.deinit()  # Deinitialisieren Sie den PWM-Pin im Fehlerfall
