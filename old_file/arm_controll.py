#/usr/bin/python

from __future__ import division
import time
import Adafruit_PCA9685
 
class armcontroller:

    def __init__(Self):

        # Alternatively specify a different address and/or bus:
        #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
        Self.pwm = Adafruit_PCA9685.PCA9685()

        # Configure min and max servo pulse lengths
        Self.servo_min = 150  # Min pulse length out of 4096
        Self.servo_max = 600  # Max pulse length out of 4096

        # Set frequency to 60hz, good for servos.
        Self.pwm.set_pwm_freq(50)
        

    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pulse(Self, channel, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096     # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        Self.pwm.set_pwm(channel, 0, pulse)
    
if __name__ == '__main__':
    servo = 0
    pwmsig = 384
    
    robi = armcontroller() 
    robi.pwm.set_pwm(servo, 0, pwmsig)
    robi.pwm.set_pwm(4, 0, 4096)
    time.sleep(10)


# # print('Moving servo on channel 0, press Ctrl-C to quit...')
# while True:
#     # Move servo on channel O between extremes.
#     robi.pwm.set_pwm(servo, 0, 256)
#     time.sleep(1)
#     robi.pwm.set_pwm(servo, 0, 512)
#     time.sleep(1)