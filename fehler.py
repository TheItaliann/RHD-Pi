from machine import Pin

sensor_d = Pin(21, Pin.IN)
count = 0
distance_trv = 0

def distance():
    distance_trv += 1.4137
    
def sensor_irq(pin):
    global count
    count += 1
    
while True:
    sensor_d.irq(trigger=Pin.IRQ_RISING, handler=distance)
