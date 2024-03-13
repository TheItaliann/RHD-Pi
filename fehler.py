from machine import Pin
from utime import ticks_ms, ticks_diff, sleep


ir_pin = Pin(28, Pin.IN)


distance_traveled = 0  
turns = 0  
count = 0


hole_dis_cm = 0.22  
wheel_u_cm = 7.85  

last_time = ticks_ms()

def detect_object():
    global distance_traveled, turns, count
    if ir_pin.value() == 1:
        distance_traveled += hole_dis_cm
        count += 1
        if count == 20:
            turns += 1
            count = 0

def measure_speed():
    global last_time
    if ir_pin.value() == 1:
        now_time = ticks_ms()
        time_ms = ticks_diff(now_time, last_time)
        last_time = now_time
        holes = time_ms / (1000 * hole_dis_cm)
        # Berechne die zurückgelegte Strecke
        distance_cm = holes * hole_dis_cm
        # Berechne die Geschwindigkeit in km/h
        speed_kmh = (distance_cm / 100000) / (time_ms / 3600000)
        return speed_kmh
    return 0

while True:
    detect_object()
    print(f"Zurückgelegte Strecke: {distance_traveled:.2f} cm | Umdrehungen: {turns}")
    velocity = measure_speed()
    print(f"Geschwindigkeit: {velocity:.2f} km/h")
    sleep(1)

