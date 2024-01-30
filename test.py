# Bibliotheken laden
from machine import Pin, PWM
from time import sleep

# GPIO für Steuersignal
servo_pin = 28

# 0 Grad
grad000 = 500000
# 45 Grad
grad045 = 1000000
# 90 Grad
grad090 = 1500000
# 135 Grad
grad135 = 2000000
# 180 Grad
grad180 = 2500000

pwm = PWM(Pin(servo_pin))
pwm.freq(50)

print('Position: Mitte (90 Grad)')
pwm.duty_ns(grad090)
sleep(2)

print('Position: Ganz Links (0 Grad)')
pwm.duty_ns(grad000)
sleep(2)

print('Position: Mitte (90 Grad)')
pwm.duty_ns(grad090)
sleep(2)

print('Position: Ganz Rechts (180 Grad)')
pwm.duty_ns(grad180)
sleep(2)

print('Position: Mitte (90 Grad)')
pwm.duty_ns(grad090)
sleep(2)

pwm.deinit()
print('Ende')
