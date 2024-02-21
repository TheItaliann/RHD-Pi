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
        self.throttle.irq(trigger=Pin.IRQ_RISING, handler=self.startTimer)
        self.button.irq(trigger=Pin.IRQ_RISING, handler=self.startTimer)
        return self.channels
    def startTimer(self, pin):
        self.startTime = time.ticks_us()
        self.throttle.irq(trigger=Pin.IRQ_FALLING, handler=self.endTimer2)
        
        self.servo.irq(trigger=Pin.IRQ_FALLING, handler=self.endTimer1)
        
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.endTimer3)
    def endTimer1(self, pin):
        self.endTime1 = time.ticks_us()
        self.channels[0] = time.ticks_diff(self.endTime1, self.startTime)
    def endTimer2(self, pin):
        self.endTime2 = time.ticks_us()
        self.channels[1] = time.ticks_diff(self.endTime2, self.startTime)
    def endTimer3(self, pin):
        self.endTime3 = time.ticks_us()
        self.channels[2] = time.ticks_diff(self.endTime3, self.startTime)
            
        
    
    def convert(self) -> list: # convert the pulse width to a value between 0 and 100
        min_servo = 0
        max_servo = 99999999
        min_throttle = 0
        max_throttle = 99999999
        if self.channels[0] < min_servo:
            min_servo = self.channels[0]
        elif self.channels[0] > max_servo:
            max_servo = self.channels[0]
        if self.channels[1] < min_throttle:
            min_throttle = self.channels[1]
        elif self.channels[1] > max_throttle:
            max_throttle = self.channels[1]

        
        steering = ((self.channels[0] - 981587) / (982213 - 981587)) * 100 # Calculate steering value
        throttle = ((self.channels[1] - 981442) / (982284 - 981442)) * 100 # Calculate throttle value
        if self.channels[2] < 982000:
            button_state = "Off"
        else:
            button_state = "On"
        print(f"button is {button_state}")
        return [steering, throttle, button_state]

            

if __name__ == "__main__":
    ppm = PPMDecoder(27, 28, 26)
    while True:
        raw = ppm.callback()
        values = ppm.convert()
        servo = int(values[0])
        throttle = int(values[1])
        
        button = values[2]
        print("Servo: ", servo, "Throttle: ", throttle, "Button: ", button,)
        print("")
        time.sleep(1)
    
