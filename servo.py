from time import sleep
from machine import Pin,PWM

servo_pin = 28

grad000 = 1638
grad180 = 8192



step_size = (grad180 - grad000) // 18 


grad010 = grad000 + step_size * 1
grad020 = grad000 + step_size * 2
grad030 = grad000 + step_size * 3
grad040 = grad000 + step_size * 4
grad050 = grad000 + step_size * 5
grad060 = grad000 + step_size * 6
grad070 = grad000 + step_size * 7
grad080 = grad000 + step_size * 8
grad090 = grad000 + step_size * 9
grad100 = grad000 + step_size * 10
grad110 = grad000 + step_size * 11
grad120 = grad000 + step_size * 12
grad130 = grad000 + step_size * 13
grad140 = grad000 + step_size * 14
grad150 = grad000 + step_size * 15
grad160 = grad000 + step_size * 16
grad170 = grad000 + step_size * 17
grad180 = grad000 + step_size * 18

pwm = PWM(Pin(servo_pin))
pwm.freq(50)

while True:
    print("10")
    pwm.duty_u16(grad010)
    sleep(0.1)


    print("20")
    pwm.duty_u16(grad010)
    sleep(0.1)

    print("30")
    pwm.duty_u16(grad030)
    sleep(0.1)

    print("40")
    pwm.duty_u16(grad040)
    sleep(0.1)

    print("50")
    pwm.duty_u16(grad050)
    sleep(0.1)

    print("60")
    pwm.duty_u16(grad060)
    sleep(0.1)

    print("70")
    pwm.duty_u16(grad070)
    sleep(0.1)

    print("80")
    pwm.duty_u16(grad080)
    sleep(0.1)

    print("90")
    pwm.duty_u16(grad090)
    sleep(0.1)

    print("100")
    pwm.duty_u16(grad100)
    sleep(0.1)

    print("110")
    pwm.duty_u16(grad110)
    sleep(0.1)

    print("120")
    pwm.duty_u16(grad120)
    sleep(0.1)

    print("130")
    pwm.duty_u16(grad130)
    sleep(0.1)

    print("140")
    pwm.duty_u16(grad140)
    sleep(0.1)

    print("150")
    pwm.duty_u16(grad150)
    sleep(0.1)

    print("160")
    pwm.duty_u16(grad160)
    sleep(0.1)

    print("170")
    pwm.duty_u16(grad170)
    sleep(0.1)

    print("180!!!!!")
    pwm.duty_u16(grad180)
    sleep(0.1)

    print("0")
    pwm.duty_u16(grad000)
    sleep(0.1)

    print("180!!!!!")
    pwm.duty_u16(grad180)
    sleep(0.1)

    print("90")
    pwm.duty_u16(grad090)
    sleep(0.1)

    pwm.deinit()
    print('Ende')
