import RPi.GPIO as GPIO
import time

motor_pin = 4 # Beispiel-GPIO-Pin (ersetzen Sie dies durch Ihren gewünschten Pin)

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin, GPIO.OUT)

try:
    while True:
        eingabe = input("Drücken Sie Enter, um den Motor zu starten (q zum Beenden): ")
        if eingabe.lower() == 'q':
            break  # Beenden Sie die Schleife, wenn 'q' eingegeben wird

        # Motor starten
        GPIO.output(motor_pin, GPIO.HIGH)
        time.sleep(3)  # Motor für 3 Sekunden laufen lassen

        # Motor stoppen
        GPIO.output(motor_pin, GPIO.LOW)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
