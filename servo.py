# Bibliotheken laden
from machine import Pin, PWM
from time import sleep

# GPIO für Steuersignal
servo_pin = 28

# 0 Grad
grad000 = 1638
# 90 Grad
grad090 = 4915
# 180 Grad
grad180 = 8192

pwm = PWM(Pin(servo_pin))
pwm.freq(50)

print('Position: Mitte (90 Grad)')
pwm.duty_u16(grad090)
sleep(2)

print('Position: Ganz Links (0 Grad)')
pwm.duty_u16(grad000)
sleep(2)

print('Position: Mitte (90 Grad)')
pwm.duty_u16(grad090)
sleep(2)

print('Position: Ganz Rechts (180 Grad)')
pwm.duty_u16(grad180)
sleep(2)

print('Position: Mitte (90 Grad)')
pwm.duty_u16(grad090)
sleep(2)

pwm.deinit()
print('Ende')
