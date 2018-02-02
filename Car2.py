#Class by Fares Al Ghazy, made on the 9th of December,2017
#Class is to control PiCa, a 3 wheel (2-motor 1 contour )raspberry pi car , using L298N
#Class objective is to give high level access to wheels with pwm, constructor will only take pins
#USES BCM NUMBERING
 
 
#Import all libraries
 
import RPi.GPIO as GPIO
import time
 
 
class Car:
   
#Constructor, initializes GPIO and provides highlevel access to pins
    def __init__(self, ForwardWheelleft,BackWheelleft,ForwardWheelright,BackWheelright):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(ForwardWheelleft,GPIO.OUT)
        GPIO.setup(BackWheelleft,GPIO.OUT)
        GPIO.setup(ForwardWheelright,GPIO.OUT)
        GPIO.setup(BackWheelright,GPIO.OUT)
        #Store pin numbers in class
        self.FWL=ForwardWheelleft
        self.BWL=BackWheelleft
        self.FWR=ForwardWheelright
        self.BWR=BackWheelright
        #All wheels should be off first
        self.allzero()
    #Function to reset allGPIOS
    def allzero(self):
        GPIO.output(self.FWL,0)
        GPIO.output(self.BWL,0)
        GPIO.output(self.FWR,0)
        GPIO.output(self.BWR,0)
    def steer(self,angle):

        
        angle=int(angle)
        if(angle==0):
            self.allzero()
        if(0<angle<=10):
            GPIO.output(self.FWL,1)
            GPIO.output(self.BWL,0)
            GPIO.output(self.FWR,0)
            GPIO.output(self.BWR,0)
        if (80<=angle<=100):
            GPIO.output(self.FWL,1)
            GPIO.output(self.FWR,1)
            GPIO.output(self.BWL,0)
            GPIO.output(self.BWR,0)
        if (170<=angle<=190):
            GPIO.output(self.FWL,0)
            GPIO.output(self.BWL,0)
            GPIO.output(self.BWR,0)
            GPIO.output(self.FWR,1)
        if (260<=angle<=280):
            GPIO.output(self.BWR,1)
            GPIO.output(self.BWL,1)
            GPIO.output(self.FWL,0)
            GPIO.output(self.FWR,0)
        if(angle>=355):
            GPIO.output(self.BWL,1)
            GPIO.output(self.FWR,0)
            GPIO.output(self.BWR,0)
            GPIO.output(self.FWL,0) 
       
