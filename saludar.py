from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

def valmap(value,istart,istop,ostart,ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def setServo(channel,angle, servo_min, servo_max):
    duty = int(valmap(angle,0,170,servo_min,servo_max))
    pwm.set_pwm(channel,0,duty)


print('Press Ctrl-C to quit...')

# Move servo on channel O between extremes.
#Piernas
setServo( 1, 135, 190, 530) 
setServo( 5,  90, 175, 515)  
setServo( 9,  90, 185, 525)
setServo(15,  45, 175, 500)
#Rodillas
setServo( 2, 130, 290, 650) 
setServo( 6, 130, 275, 635) 
setServo(10, 130, 270, 645)
setServo(14, 130, 165, 505) 
#Pies max(140)
setServo( 3, 140, 125, 640) 
setServo( 7,   0, 145, 625) 
setServo(11, 140, 140, 620)
setServo(13, 140, 135, 630) 
time.sleep(.5)

while True:
    #Piernas 
    setServo( 5,  90, 175, 515)  
    #Rodillas
    setServo( 6, 150, 260, 625) 
    #Pies max(140)
    setServo( 7,   0, 145, 625) 
    time.sleep(.5)

	#Piernas 
    setServo( 5, 145, 175, 515)  
    #Rodillas
    setServo( 6, 150, 260, 625) 
    #Pies max(140)
    setServo( 7,  30, 145, 625) 
    time.sleep(.5)

	#Piernas 
    setServo( 5,  90, 175, 515)  
    #Rodillas
    setServo( 6, 150, 260, 625) 
    #Pies max(140)
    setServo( 7,   0, 145, 625) 
    time.sleep(.5)

	#Piernas 
    setServo( 5,  55, 175, 515)  
    #Rodillas
    setServo( 6, 150, 260, 625) 
    #Pies max(140)
    setServo( 7,  30, 145, 625) 
    time.sleep(.5)
