#/usr/bin/python

from email.utils import encode_rfc2231
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

    

    def linksdrehen(self,wait,speed):
        self.en1.value = speed
        self.en2.value = speed
        self.en1.toggle()
        self.en2.toggle()
        self.en1.on()
        self.en2.on()
        self.in1.on()
        self.in2.off()
        self.in3.on()
        self.in4.off()

        sleep(wait)
        
        
    def rechtsdrehen(self,speed,wait):
        self.en1.value = speed
        self.en2.value = speed
        self.en1.toggle()
        self.en2.toggle()
        self.en1.on()
        self.en2.on()
        self.in1.off()
        self.in2.on()
        self.in3.off()
        self.in4.on()
        sleep(wait) 
        self.en1.off()
        self.en2.off() 

    def ruckwarts(self,speed,wait):
        self.en1.value = speed
        self.en2.value = speed
        self.en1.toggle()
        self.en2.toggle()
        self.in1.on()
        self.in2.off()
        self.in3.off()
        self.in4.on()
        sleep(wait)
        self.en1.off()
        self.en2.off() 


    def vorwarts(self,speed,wait):
        self.en1.value = speed
        self.en2.value = speed
        self.en1.toggle()
        self.en2.toggle()
        self.in1.off()
        self.in2.on()
        self.in3.on()
        self.in4.off()
        sleep(wait)
        self.en1.off()
        self.en2.off() 

    def motoraus(self):
        self.en1.off()
        self.en2.off()

    
  
    def drivecontrol(self,richtung,speed,wait):

        if richtung in "vorwarts":
          self.vorwarts(speed,wait) 

        if richtung in "ruckwarts":
            self.ruckwarts(speed,wait) 

        if richtung in "rechts":
          self.rechtsdrehen(speed,wait) 
        
        if richtung in "links":
          self.linksdrehen(speed,wait) 

       

if __name__ == '__main__':
    roboter=driver()

    speed = 0.1
    

    timer = 0.6
    timel = 0.6
    

    roboter.drivecontrol("rechts",speed,timer)
    roboter.motoraus()
    sleep(1)

    roboter.drivecontrol("links",speed,timel)
    roboter.motoraus()
    sleep(1)
    
    roboter.drivecontrol("vorwarts",speed,2)
    roboter.motoraus()

    roboter.drivecontrol("ruckwarts",speed,2)
    roboter.motoraus()
   
    roboter.drivecontrol("vorwarts",speed,3)
    roboter.motoraus()
 


