from machine import Pin, time_pulse_us as Pulse
import time

class PPMDecoder:
    def __init__(self, pin1, pin2, pin3) -> None:
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.throttle = Pin(self.pin2, Pin.IN, Pin.PULL_UP)
        self.servo = Pin(self.pin1, Pin.IN, Pin.PULL_UP)
        self.button = Pin(self.pin3, Pin.IN, Pin.PULL_UP)
        self.time = 0
        self.channels = [0, 0, 0]

    def callback(self):
        self.time_servo = Pulse(self.pin1, 1, 1_000_000)       
        self.time_throttle = Pulse(self.pin2, 1, 1_000_000)       
        self.time_button = Pulse(self.pin3, 1, 1_000_000)
        self.channels[0] = self.time_servo()
        self.channels[1] = self.time_throttle()
        self.channels[2] = self.time_button()      
        return self.channels
    
if __name__ == "__main__":
    ppm = PPMDecoder(27, 26, 22)
    while True:
        print(ppm.callback())
        time.sleep(1)