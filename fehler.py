from machine import Pin
from main import Driver
import _thread

sensor_d = Pin(28, Pin.IN)
distance_trv = 0

def distance(pin):
    global distance_trv
    distance_trv += 1
    print(distance_trv)
    
def test():
    test = Driver(0,1,2,3)
    test.forward(100, 1)

if __name__ == "__main__":
    _thread.start_new_thread(test, ())
    while True:
        sensor_d.irq(trigger=Pin.IRQ_RISING, handler=distance)

        
