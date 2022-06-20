#!/usr/bin/python3

import sys
import smbus2
import gpiozero as G0
from time import sleep

import subprocess

try:
    from ST_VL6180X import VL6180X
except ImportError:
    print("Error importing ST_VL6180X.VL6180X!")
    exit()

class TOF:

    __on_pins    = [27]
    __alert_pins    = [4]
    __en_pins       = [17]
    __i2c_address   = [0x10]

    def __init__(self, debug=False, tof_bus = smbus2.SMBus(1)):
        self.debug = debug
        self.bus = tof_bus
        self.gpio_init()
        self.tof_init()

    def gpio_init(self):
        self.tof_alert = [G0.DigitalInputDevice(pin) for pin in self.__alert_pins]
        self.tof_en = [G0.DigitalOutputDevice(pin) for pin in self.__en_pins]
        self.tof_on = [G0.DigitalOutputDevice(pin) for pin in self.__on_pins]
        self.tof_on[0].off()
 
    def tof_init(self):
        # Inital sensor
        self.tof = []
        self.tof = VL6180X(address=0x29, debug=self.debug, bus = self.bus)

        # for address, enabel_pin in zip(self.__i2c_address, self.tof_en):
        #     enabel_pin.on()
        #     sleep(0.5)
        #     tof = VL6180X(address=0x29, debug=self.debug, bus = self.bus)
        #     print("Set new adress sensor 1: {:X}".format(tof.change_address(0x29,address)))
        #     self.tof.append(tof)

    def get_distance(self,sensor):
        if sensor >= 0 and sensor < len(self.tof):
            distans = self.tof[sensor].get_distance()
            # print("Measured distance from Sensor 0x{:X} is : {:} mm".format(self.tof[sensor].address,distans))
            return distans 
        else:
            print("Sensor is not There")
        
        


    def test(self):

       
        # apply pre calibrated offset
        self.tof[0].set_range_offset(23)
        print("Range offset set to: {:d}".format(self.tof[1].get_range_offset()))

        # setup ToF ranging/ALS sensor
        self.tof[0].get_identification()
        if self.tof[0].idModel != 0xB4:
            print("Not a valid sensor id: ".format(self.tof[1].idModel))
        else:
            print("Sensor model: {:X}".format(self.tof[1].idModel))
            print("Sensor model rev.: {:d}.{:d}"
                .format(self.tof[1].idModelRevMajor, self.tof[1].idModelRevMinor))
            print("Sensor module rev.: {:d}.{:d}"
                .format(self.tof[1].idModuleRevMajor, self.tof[1].idModuleRevMinor))
            print("Sensor date/time: {:X}/{:X}".format(self.tof[1].idDate, self.tof[1].idTime))
        self.tof[1].default_settings()

        sleep(1)

        """-- MAIN LOOP --"""
        try:
            x = 0
            while True:
                
                # for x in range(4):
                    # self.get_distance(x)
                print("Sensor {:}: {:}".format(x, self.get_distance(x)))
                print("\n")

                # self.get_distance(self.tof[1])
                # self.get_distance(self.tof_2)
                # self.get_distance(self.tof_3)
                # self.get_distance(self.tof_4)
                # sleep(5)
                #print("Measured distance is : ", self.tof[1].get_distance(), " mm" )
                #print("Measured light level is : ", self.tof[1].get_ambient_light(20), " lux")
                sleep(5)
        except KeyboardInterrupt:
            print("\nquit")

    

if __name__ == '__main__':
    debug = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "debug":  # sys.argv[0] is the filename
            debug = True

    sensortest = TOF(debug)
    print(sensortest.get_distance(0))
    # sensortest.test()

     
     