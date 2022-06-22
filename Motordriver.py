#/usr/bin/python

from time import sleep
import gpiozero as g0

class driver:
    def __init__(self):
        self.in1 = g0.OutputDevice(23)
        self.in2 = g0.OutputDevice(18)
        self.en1 = g0.PWMLED(19)
        self.in3 = g0.OutputDevice(5)
        self.in4 = g0.OutputDevice(6)
        self.en2 = g0.PWMLED(13)

    

       
    def linksdrehen(self,speed):
        # print("Speed",speed)
        self.en1.value = speed
        self.en2.value = speed
        self.en1.toggle()
        self.en2.toggle()
        self.en1.value 
        self.en2.value
        self.in1.off()
        self.in2.on()
        self.in3.on()
        self.in4.off() 
        
        
    def rechtsdrehen(self,speed):
        self.en1.value = speed
        self.en2.value = speed
        self.en1.toggle()
        self.en2.toggle()
        self.en1.value 
        self.en2.value
        self.in1.on()
        self.in2.off()
        self.in3.off()
        self.in4.on()
      

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

    def linkskurvevorwarts(self,speed,wait):
        self.en1.value = speed + 0.4
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

    def rechtskurvorwarts(self,speed,wait):
        self.en1.value = speed 
        self.en2.value = speed + 0.4
        self.en1.toggle()
        self.en2.toggle()
        self.in1.off()
        self.in2.on()
        self.in3.on()
        self.in4.off()
        sleep(wait)
        self.en1.off()
        self.en2.off() 

    def rechtskurveruckwarts(self,speed,wait):
        self.en1.value = speed + 0.4
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



    def linkskurveruckwarts(self,speed,wait):
        self.en1.value = speed 
        self.en2.value = speed + 0.4
        self.en1.toggle()
        self.en2.toggle()
        self.in1.on()
        self.in2.off()
        self.in3.off()
        self.in4.on()
        sleep(wait)
        self.en1.off()
        self.en2.off()        

    def stop(self):
        self.en1.off()
        self.en2.off()

    
  
    def drivecontrol(self,richtung,speed,wait):

        if richtung == "vorwarts":
          self.vorwarts(speed,wait) 

        if richtung == "ruckwarts":
            self.ruckwarts(speed,wait) 

        if richtung == "rechts":
          self.rechtsdrehen(speed) 
        
        if richtung == "links":
          self.linksdrehen(speed) 

        if richtung == "linkskurvevorwarts":
          self.linkskurvevorwarts(speed,wait) 

        if richtung == "rechtskurvevorwarts":
          self.rechtskurvorwarts(speed,wait) 

        if richtung == "rechtskurveruckwarts":
          self.rechtskurveruckwarts(speed,wait)     
        
        if richtung == "linkskurveruckwarts":
          self.linkskurveruckwarts(speed,wait) 

        if richtung == "stop":
          self.stop() 
       

if __name__ == '__main__':
    roboter=driver()

    speed = 0.1
    
    
 
  
    # roboter.drivecontrol("links",speed,0)
    # sleep(0.3)
    # roboter.drivecontrol("stop",speed,0)

    roboter.drivecontrol("rechts", speed,2)
    sleep(2)
    roboter.drivecontrol("stop",speed,0)


    # roboter.drivecontrol("ruckwarts",speed,2)
    
   
    # roboter.drivecontrol("vorwarts",speed,2)
    
 
    # roboter.drivecontrol("linkskurvevorwarts",speed,2)


    # roboter.drivecontrol("rechtskurvevorwarts",speed,4)


    # roboter.drivecontrol("rechtskurveruckwarts",speed,4)

 
    #roboter.drivecontrol("linkskurveruckwarts",speed,4)

    
