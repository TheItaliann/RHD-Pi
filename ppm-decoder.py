from machine import Pin, time_pulse_us as time_pulse_us
import time

class PPMDecoder:
    def __init__(self, pins, channel) -> None:
        self.pins = []
        self.channels = []
        for i in range(pins):
            self.pins.append(Pin(i, Pin.IN, Pin.PULL_UP))
        for j in range(channel):
            self.channels = [0] * self.channels

    def callback(self):
        current_channel = 0
        if len(self.channels) == len(self.pins):
            for Pin in self.pins:
                istime = Pulse(Pin, 0, 1_000_000)
                if istime > 0:
                    self.channels[current_channel] = istime
                    current_channel += 1
        return self.channels