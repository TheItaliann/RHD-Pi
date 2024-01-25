from machine import Pin
import time
ppm_pin_id = 28
ppm_channels = 3

ppm_pin = Pin(ppm_pin_id, Pin.IN, Pin.PULL_UP)
ppm_channels_values = [0] * ppm_channels

def ppm_callback(pin):
    global ppm_channels_values
    ppm_channels_values = [0] * ppm_channels
    ppm_channels_values[0] = time.ticks_us()
    for i in range(1, ppm_channels):
        while ppm_pin.value() == 1:
            pass
        ppm_channels_values[i] = time.ticks_us()

ppm_pin.irq(trigger=Pin.IRQ_RISING, handler=ppm_callback)

while True:
    print(ppm_channels_values)
    time.sleep(1)