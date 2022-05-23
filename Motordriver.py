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

    def motorvorwarts(self,speed,wait):
        self.in1.on()
        self.in2.off()
        self.en1.value = speed
        self.en1.toggle()
        

        sleep(wait)

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
    
  
    def drivecontrol(self,richtung,speed, wait):
       if richtung in "vorwarts":
          self.motorvorwarts(speed,wait) 

if __name__ == '__main__':
    roboter=driver()
    roboter.drivecontrol("vorwarts",0.5,10)
   
 


