#/usr/bin/python

from time import sleep
import gpiozero as g0

class driver:
    def __init__(self):
        self.in1 = g0.OutputDevice(4)
        self.in2 = g0.OutputDevice(17)
        self.en1 = g0.OutputDevice(10)
        self.in3 = g0.OutputDevice(5)
        self.in4 = g0.OutputDevice(6)
        self.en2 = g0.OutputDevice(11)

    def motorvorwarts(self): 
        self.en1.on()
        self.in1.on()
        self.in2.off()
        sleep(5)

    def linksdrehen(self):
        self.en1.on()
        self.en2.on()
        self.in1.on()
        self.in2.off()
        self.in3.on()
        self.in4.off()
        sleep(5)



if __name__ == '__main__':
    motor1 = driver()
    motor1.motorvorwarts()
    motor1.linksdrehen()
    



