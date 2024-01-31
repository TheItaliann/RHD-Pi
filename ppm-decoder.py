from machine import Pin, time_pulse_us as Pulse
import time

class PPMDecoder:
    def __init__(self, pin) -> None:
        self.pin = pin
        self.pin.irq(trigger=Pin.IRQ_RISING, handler=self.callback)
        self.servo = Pin(self.pin, Pin.IN, Pin.PULL_UP)
        self.time = 0

    def callback(self):
        self.time = Pulse(self.pin, 1, 1_000_000)        
        return self.time
    
if __name__ == "__main__":
    ppm = PPMDecoder(15)
    while True:
        print(ppm.callback())
        time.sleep(1)