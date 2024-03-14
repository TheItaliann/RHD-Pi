from machine import Pin, PWM
from time import sleep

class Driver():

    def __init__(self, pin1: int, pin2: int, pin3: int, pin4: int): # Initialize the pins for the motor driver
        self.leftForward = PWM(Pin(pin1))
        self.leftBackward = PWM(Pin(pin2))
        self.rightForward = PWM(Pin(pin3))
        self.rightBackward = PWM(Pin(pin4))
        self.leftForward.freq(50)
        self.leftBackward.freq(50)
        self.rightForward.freq(50)
        self.rightBackward.freq(50)
        
    def calcSpeed(self, value: int) -> int:
        '''Calculates the percentage of the value'''
        if value >= 0 and value <= 100:
            perc = ((value * (65535 - 20000)) / 100) + 20000 # Calculate the pwm value for the motor with a percentage
            return int(perc) # Return the percentage of the value
        else:
            print("Value must be between 0 and 100!")

    def stop(self) -> None:
        """Stop the car."""
        self.leftForward.duty_u16(0)  # sets the pwm signal to 0 to stop the motor
        self.leftBackward.duty_u16(0)
        self.rightForward.duty_u16(0)
        self.rightBackward.duty_u16(0)

    def forward(self, speed :int, time: int) -> None:
        """Move the car forward for a given amount of time and the set speed."""
        value = self.calcSpeed(speed) # sets the speed of the car with a pwm value
        self.leftForward.duty_u16(value) # send the signal for the motor controller to move the car forward
        self.rightForward.duty_u16(value)
        print("car is driving")
        sleep(time) #if distance == x:
                        # self.stop
        self.stop()

    def backward(self, speed, time) -> None:
        """Move the car backward for a given amount of time and the set speed."""
        value = self.calcSpeed(speed) 
        self.leftBackward.duty_u16(value) # send the signal for the motor controller to move the car backward
        self.rightBackward.duty_u16(value)
        sleep(time)
        self.stop()

    def turn(self, degrees: int, direction: str) -> None:
        """Turn the car in a given direction for a given amount of degrees."""
        time = (degrees / 110) * 1 # Calculate the time it takes to turn the car(1 second for 90 degrees"have to change the degrees because its not tested yet")
        tireSpeed = self.calcSpeed(50)
        #math direction syntax fehler 
        if direction == "r":
            self.leftForward.duty_u16(tireSpeed)
            self.rightForward.duty_u16(0)
            sleep(time) 
        elif direction == "l":
            self.leftForward.duty_u16(0)
            self.rightForward.duty_u16(tireSpeed)
            sleep(time)
        self.stop()
    
    def Test(self):
        while True:
            direction = input("Enter direction (F/B/R/L)(-1 to exit): ")
            direction = direction.lower()
            if direction == "-1":
                break
            elif direction == "f":
                speed, time = int(input("Enter speed from 1 to 100 (-1 to exit): ")), int(input("Enter time in seconds(-1 to exit): "))
                self.forward(speed, time)
            elif direction == "b":
                speed, time = int(input("Enter speed from 1 to 100 (-1 to exit): ")), int(input("Enter time in seconds(-1 to exit): "))    
                self.backward(speed, time)
            elif direction == "r":
                degrees = int(input("Enter degrees (-1 to exit): "))
                self.turn(degrees, "r")
            elif direction == "l":
                degrees = int(input("Enter degrees (-1 to exit): "))
                self.turn(degrees, "l")
            elif direction == _:
                print("Invalid direction!")
                continue # continue the loop if the input is invalid

    
if __name__ == "__main__":
    test = Driver(0,1,2,3)
    test.Test()
    
