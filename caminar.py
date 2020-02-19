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
setServo( 1, 120, 190, 530)
setServo( 5, 60, 175, 515)
setServo( 9, 60, 185, 525)
setServo(15, 120, 175, 500)
#Rodillas
setServo( 2, 120, 290, 650)
setServo( 6, 120, 275, 635)
setServo(10, 120, 270, 645)
setServo(14, 120, 165, 505)
#Pies max(140)
setServo( 3, 120, 125, 640)
setServo( 7, 120, 145, 625)
setServo(11, 120, 140, 620)
setServo(13, 120, 135, 630)
time.sleep(.5)

while True:
    # Move servo on channel O between extremes.
    #Piernas
    setServo( 1, 110, 190, 530) 
    setServo( 5,  90, 175, 515)  
    setServo( 9,  70, 185, 525)
    setServo(15,  90, 175, 500)
    #Rodillas
    setServo( 2, 140, 290, 650) 
    setServo( 6, 120, 260, 625) 
    setServo(10, 120, 270, 645)
    setServo(14, 140, 165, 505) 
    #Pies max(140)
    setServo( 3,  95, 125, 640) 
    setServo( 7, 138, 145, 625) 
    setServo(11,  95, 140, 620)
    setServo(13, 138, 135, 630) 
    time.sleep(.5)

	#Piernas
    setServo( 1, 110, 190, 530) 
    setServo( 5,  90, 175, 515)  
    setServo( 9,  70, 185, 525)
    setServo(15,  90, 175, 500)
    #Rodillas
    setServo( 2, 120, 290, 650) 
    setServo( 6, 120, 260, 625) 
    setServo(10, 120, 270, 645)
    setServo(14, 120, 165, 505) 
    #Pies max(140)
    setServo( 3,  95, 125, 640) 
    setServo( 7, 138, 145, 625) 
    setServo(11,  95, 140, 620)
    setServo(13, 138, 135, 630) 
    time.sleep(.2)

	#Piernas
    setServo( 1,  90, 190, 530) 
    setServo( 5,  70, 175, 515)  
    setServo( 9,  90, 185, 525)
    setServo(15, 110, 175, 500)
    #Rodillas
    setServo( 2, 120, 290, 650) 
    setServo( 6, 140, 260, 625) 
    setServo(10, 140, 270, 645)
    setServo(14, 120, 165, 505) 
    #Pies max(140)
    setServo( 3, 138, 125, 640) 
    setServo( 7,  95, 145, 625) 
    setServo(11, 138, 140, 620)
    setServo(13,  95, 135, 630) 
    time.sleep(.5)

	#Piernas
    setServo( 1,  90, 190, 530) 
    setServo( 5,  70, 175, 515)  
    setServo( 9,  90, 185, 525)
    setServo(15, 110, 175, 500)
    #Rodillas
    setServo( 2, 120, 290, 650) 
    setServo( 6, 120, 260, 625) 
    setServo(10, 120, 270, 645)
    setServo(14, 120, 165, 505) 
    #Pies max(140)
    setServo( 3, 138, 125, 640) 
    setServo( 7,  95, 145, 625) 
    setServo(11, 138, 140, 620)
    setServo(13,  95, 135, 630) 
    time.sleep(.2)
