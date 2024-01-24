from ppm_reader import PpmReader
import time
ppm_pin_id = 28
ppm_channels = 3
ppmReader=PpmReader(ppm_pin_id,ppm_channels)

def connect() -> bool:
    """Wait for the connection with the Remote"""
    while ppmReader.get_valid_packets() == 0:
        print("Waiting for the Remote to connect...")
        time.sleep(0.5)
    print("Remote connected!")
    return True

def connection() -> bool:
    """Check if the Remote is still connected"""
    last_paccket_time=ppmReader.time_since_last_packet()
    print("Last packet time: "+str(last_paccket_time))
    if last_paccket_time > 25000: # if 25ms without packets
        print("Remote disconnected!")
        return False
    else:
        # if a packet is received within 25ms
        print("connected")
        return True

def reader() -> None:
    # read the PPM signal and check connection
    print(ppmReader.get_values())
