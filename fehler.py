from machine import Pin
from utime import ticks_ms, ticks_diff, sleep
#https://github.com/WongKinYiu/yolov7
ir_pin = Pin(28, Pin.IN)
distance_traveled = 0  # in cm
turns = 0
count = 0

last_time = ticks_ms()
hole_dis_cm = 0.22  # distance between the holes in cm
wheel_u_cm = 7.85  # circumference in cm



def detect_object():
    global distance_traveled, turns, count
    if ir_pin.value() == 1:
        distance_traveled += 1.4737 
        count +=1
        if count == 20:
            turns += 1
            count = 0 



def measure_speed():
    if ir_pin.value() == 1:
        now_time = ticks_ms()

        time_ms = ticks_diff(now_time, last_time)

        last_time = now_time

        holes = time_ms / (1000 * hole_dis_cm)
        
        # Distance traveled
        distance_cm = holes * hole_dis_cm
        
        # km/h maker 
        speed_kmh = (distance_cm / 100000) / (time_ms / 3600000)
        
        return speed_kmh
    return 0



while True:
    detect_object()
    print(f"Zurückgelegte Strecke: {distance_traveled} umdrhung {turns}")    
    measure_speed()
    sleep(1)

#>>> %Run -c $EDITOR_CONTENT
Zurückgelegte Strecke: 1.4737 umdrhung 0
Traceback (most recent call last):
  File "<stdin>", line 50, in <module>
  File "<stdin>", line 30, in measure_speed
NameError: local variable referenced before assignment
>>> 
    

