# Bibliotheken laden
from machine import Pin

# Initialisierung von GPIO16 als Eingang
sensor_d = Pin(21, Pin.IN)

# Zähler
count = 0

# Funktion: Interrupt-Behandlung
def sensor_irq(pin):
    global count
    count += 1
    print(count)

# Interrupt-Steuerung
sensor_d.irq(trigger=Pin.IRQ_RISING, handler=sensor_irq)
