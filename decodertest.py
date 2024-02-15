from machine import PIN
import utime

PWM_PIN_CH1 = 17
PWM_PIN_CH2 = 19
PWM_PIN_CH3 = 22


PWM_THRESHOLD_CH1 = 1.788 
PWM_THRESHOLD_CH2 = 1.924  
PWM_THRESHOLD_CH3 = 1.992 


CHANNEL_STATES = {
    "on": True,
    "off": False
}


pwm_ch1 = Pin(PWM_PIN_CH1, Pin.IN, Pin.PULL_UP)
pwm_ch2 = Pin(PWM_PIN_CH2, Pin.IN, Pin.PULL_UP)
pwm_ch3 = Pin(PWM_PIN_CH3, Pin.IN, Pin.PULL_UP)

def decode_pwm_pulse(pin):
    pulse_start = utime.ticks_us()
    while pin.value() == 1:
        pass
    pulse_duration = utime.ticks_diff(utime.ticks_us(), pulse_start)
    return pulse_duration

def map_to_percentage(pulse_duration, threshold):
    if pulse_duration < threshold:
        return 0
    elif pulse_duration > 2000:  
        return 100
    else:
        return int((pulse_duration - threshold) / (2000 - threshold) * 100)

def decode_channels():
    ch1_pulse = decode_pwm_pulse(pwm_ch1)
    ch2_pulse = decode_pwm_pulse(pwm_ch2)
    ch3_pulse = decode_pwm_pulse(pwm_ch3)

    ch1_percentage = map_to_percentage(ch1_pulse, PWM_THRESHOLD_CH1)
    ch2_percentage = map_to_percentage(ch2_pulse, PWM_THRESHOLD_CH2)

    if ch3_pulse < PWM_THRESHOLD_CH3:
        ch3_state = "off"
    else:
        ch3_state = "on"

    return ch1_percentage, ch2_percentage, ch3_state

while True:
    ch1, ch2, ch3 = decode_channels()
    print("Channel 1: {}%  Channel 2: {}%  Channel 3: {}".format(ch1, ch2, ch3))
    utime.sleep(0.1)  
