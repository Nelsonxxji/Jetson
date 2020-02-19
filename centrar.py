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
while True:
    # Move servo on channel O between extremes.
    #Piernas
    setServo( 1, 90, 190, 530) 
    setServo( 5, 90, 175, 515)  
    setServo( 9, 90, 185, 525)
    setServo(15, 90, 175, 500)
    #Rodillas
    setServo( 2, 90, 290, 650) 
    setServo( 6, 90, 275, 635) 
    setServo(10, 90, 270, 645)
    setServo(14, 90, 165, 505) 
    #Pies max(140)
    setServo( 3, 90, 125, 640) 
    setServo( 7, 90, 145, 625) 
    setServo(11, 90, 140, 620)
    setServo(13, 90, 135, 630) 
    time.sleep(1)
