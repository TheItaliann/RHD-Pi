from machine import Pin
import time
ppm_pin_id = 27
ppm_channels = 3

ppm_pin = Pin(ppm_pin_id, Pin.IN, Pin.PULL_UP)
ppm_channels_values = [0] * ppm_channels
timer = time.ticks_us()


def ppm_callback(pin):
    now = time.ticks_us()
    delta = time.ticks_diff(now,timer)
    timer = now
    
    global ppm_channels_values
    ppm_channels_values = [0] * ppm_channels
    for i in range(1, ppm_channels):
        while ppm_pin.value() == 1:
            pass
        ppm_channels_values[i] = delta

ppm_pin.irq(trigger=Pin.IRQ_RISING, handler=ppm_callback)

while True:
    print(ppm_channels_values)
    time.sleep(1)


