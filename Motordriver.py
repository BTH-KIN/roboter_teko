#/usr/bin/python

from time import sleep
import gpiozero as g0

class driver:
    def __init__(self):
        self.in1 = g0.OutputDevice(4)
        self.in2 = g0.OutputDevice(17)
        self.en1 = g0.PWMLED(19)
        self.in3 = g0.OutputDevice(5)
        self.in4 = g0.OutputDevice(6)
        self.en2 = g0.PWMLED(13)

    def motorvorwarts(self):
        self.in1.on()
        self.in2.off()
        self.en1.value = 0.5
        self.en1.toggle()
        
        sleep(5)

    def linksdrehen(self):
        self.en1.on()
        self.en2.on()
        self.in1.on()
        self.in2.off()
        self.in3.on()
        self.in4.off()
        sleep(5)

    def ruckwarts(self):
        self.en1.on()
        self.en2.on()
        self.in1.on()
        self.in2.off()
        self.in3.off()
        self.in4.on()
        sleep(5)

    def vorwarts(self):
        self.en1.on()
        self.en2.on()
        self.in1.off()
        self.in2.on()
        self.in3.on()
        self.in4.off()
        sleep(5)

    def rechsdrehen(self):
        self.en1.on()
        self.en2.on()
        self.in1.off()
        self.in2.on()
        self.in3.off()
        self.in4.on()
        sleep(5)          



if __name__ == '__main__':
    motor1 = driver()
    print("motorvorwarts")
    motor1.motorvorwarts()
   # print("linksdrehen")
   # motor1.linksdrehen()
   # print("ruckwarts")
   # motor1.ruckwarts()
   # motor1.vorwarts()
   # motor1.linksdrehen()


