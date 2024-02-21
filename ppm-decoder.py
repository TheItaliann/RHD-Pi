from machine import Pin
import time

class PPMDecoder:
    def __init__(self, pin1, pin2, pin3) -> None:
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.throttle = Pin(self.pin2, Pin.IN, Pin.PULL_UP)
        self.servo = Pin(self.pin1, Pin.IN, Pin.PULL_UP)
        self.button = Pin(self.pin3, Pin.IN, Pin.PULL_UP)
        self.channels = [0, 0, 0]

    def callback(self) -> list: # using the callback function to get the pulse width
        self.servo.irq(trigger=Pin.IRQ_RISING, handler=self.startTimer)
        return self.channels
    def startTimer(self):
        self.startTime = time.ticks_us()
        self.servo.irq(trigger=Pin.IRQ_FALLING, handler=self.endTimer1)
        self.throttle.irq(trigger=Pin.IRQ_FALLING, handler=self.endTimer2)
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.endTimer3)
    def endTimer1(self):
        self.endTime = time.ticks_us()
        self.channels[0] = time.ticks_diff(self.endTime, self.startTime)
    def endTimer2(self):
        self.endTime = time.ticks_us()
        self.channels[1] = time.ticks_diff(self.endTime, self.startTime)
    def endTimer3(self):
        self.endTime = time.ticks_us()
        self.channels[2] = time.ticks_diff(self.endTime, self.startTime)
            
        
    
    def convert(self) -> list:
        steering = ((servo - 1198) / (1785 - 1198)) * 100 # Calculate steering value
        throttle = ((throttle - 1488) / (1924 - 1488)) * 100 # Calculate throttle value
        if button > 900:
            button_state = "Off"
        else:
            button_state = "On"
        print(f"button is {button_state}")
        return [steering, throttle, button_state]

            

if __name__ == "__main__":
    ppm = PPMDecoder(27, 21, 22)
    while True:
        values = ppm.callback()
        servo = values[0]
        throttle = values[1]
        button = values[2]
        print("Servo: ", servo, "Throttle: ", throttle, "Button: ", button,)
        print("")
        time.sleep(1)
    