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
        self.pin1.irq(trigger=Pin.IRQ_RISING, handler=self.callback)
        self.pin1.irq(trigger=Pin.IRQ_FALLING, handler=self.callback)
        self.pin2.irq(trigger=Pin.IRQ_FALLING, handler=self.callback)
        self.pin3.irq(trigger=Pin.IRQ_FALLING, handler=self.callback)

    def callback(self) -> list: # using the callback function to get the pulse width
        '''This function is used to get the pulse width of the PPM signal. It uses the IRQ to get the pulse width of the PPM signal. It is called when the signal is rising and falling. It returns the pulse width of the PPM signal.'''
        timer = 0
        if self.pin1.irq(trigger=Pin.IRQ_RISING):
            timer = time.ticks_us()
        if self.pin1.irq(trigger=Pin.IRQ_FALLING):
            self.channels[0] = time.ticks_diff(timer, time.ticks_us())
        if self.pin2.irq(trigger=Pin.IRQ_FALLING):
            self.channels[1] = time.ticks_diff(timer, time.ticks_us())
        if self.pin3.irq(trigger=Pin.IRQ_FALLING):
            self.channels[2] = time.ticks_diff(timer, time.ticks_us())


        return self.channels
    
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
        state = ppm.button()
        servo = values[0]
        throttle = values[1]
        button = values[2]
        print("Servo: ", servo, "Throttle: ", throttle, "Button: ", button,)
        print("")
        time.sleep(1)
    