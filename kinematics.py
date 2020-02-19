#!/usr/bin/env python3
from __future__ import division
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import time
import Adafruit_PCA9685
import numpy as np


# Set frequency to 60hz, good for servos.
pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
pwm.set_pwm_freq(60)

def valmap(value,istart,istop,ostart,ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def setServo(channel,angle, servo_min, servo_max):
    duty = int(valmap(angle,0,170,servo_min,servo_max))
    pwm.set_pwm(channel,0,duty)

class Angles(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/joint_states', JointState,self.callback)
        self.position = 12*[1.5701,]
        
    def callback(self, msg):
        self.position = msg.position

rospy.init_node('listener', anonymous=True)
valores = Angles()
rate = rospy.Rate(10) #10Hz

while not rospy.is_shutdown():
    # Move servo on channel O between extremes.
    #Piernas
    setServo(1,np.degrees(valores.position[0]), 190, 530)
    setServo(5,np.degrees(valores.position[1]), 175, 515)
    setServo(9,np.degrees(valores.position[2]), 185, 525)
    setServo(15,np.degrees(valores.position[3]), 175, 500)
    #print(valores.position)
    #Rodillas
    setServo(2,np.degrees(valores.position[4]), 290, 650)
    setServo(6,np.degrees(valores.position[5]), 275, 635)
    setServo(10,np.degrees(valores.position[6]), 270, 645)
    setServo(14,np.degrees(valores.position[7]), 165, 505)

   #Pies max(140)
    setServo(3,np.degrees(valores.position[8]), 125, 640)
    setServo(7,np.degrees(valores.position[9]), 145, 625)
    setServo(11,np.degrees(valores.position[10]), 140, 620)
    setServo(13,np.degrees(valores.position[11]), 135, 630)

    rate.sleep()

