import machine
import utime
#from decoder import perendage_speed

ESC_PIN = 16  

pwm = machine.PWM(machine.Pin(ESC_PIN))
pwm.freq(50)  
speed = 100 #perendage_speed

def set_speed(speed):
    speed = min(max(speed, 0), 100)
    
    duty_cycle = int(speed * 10.24)
    pwm.duty_u16(duty_cycle)

try:
    while True:
        if speed < 0:
            continue
        set_speed()
          

except KeyboardInterrupt:
    print("beendet")
finally:
    pwm.deinit()  
