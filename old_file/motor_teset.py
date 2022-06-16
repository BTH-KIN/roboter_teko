import RPi.GPIO as gpio

import time

ENA = 13
ENB = 12
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

def init():    
    gpio.setmode(gpio.BCM)
    gpio.setup(ENA, gpio.OUT)
    gpio.setup(ENB, gpio.OUT)
    gpio.setup(IN1, gpio.OUT)
    gpio.setup(IN2, gpio.OUT)
    gpio.setup(IN3, gpio.OUT)
    gpio.setup(IN4, gpio.OUT)

    gpio.output(ENA, True)
    gpio.output(ENB, True)
    
def forward(sec):
    init()
    gpio.output(IN1, False)
    gpio.output(IN2, True)
    gpio.output(IN3, True)
    gpio.output(IN4, False)
    time.sleep(sec)
    gpio.cleanup() 
    
def reverse(sec):
    init()
    gpio.output(IN1, True)
    gpio.output(IN2, False)
    gpio.output(IN3, False)
    gpio.output(IN4, True)
    time.sleep(sec)
    gpio.cleanup()
    
def left_turn(sec):
    init()
    gpio.output(IN1, True)
    gpio.output(IN2, False)
    gpio.output(IN3, True)
    gpio.output(IN4, False)
    time.sleep(sec)
    gpio.cleanup()

def right_turn(sec):
    init()
    gpio.output(IN1, False)
    gpio.output(IN2, True)
    gpio.output(IN3, False)
    gpio.output(IN4, True)
    time.sleep(sec)
    gpio.cleanup()
    

if __name__ == "__main__":

    seconds = 3 
    time.sleep(seconds)

    print("forward")
    forward(seconds)
    time.sleep(seconds-2)
    
    print("right")
    right_turn(seconds)
    time.sleep(seconds-2)
    
    time.sleep(seconds)
    print("forward")
    forward(seconds)
    time.sleep(seconds-2)
    
    print("right")
    right_turn(seconds)
    time.sleep(seconds-2)