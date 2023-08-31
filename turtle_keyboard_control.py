#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg = """
Control Your Turtle!
---------------------------
Moving around:
   m1
m3  s  m4
   m2

m1/m2 : increase/decrease linear velocity
m3/m4 : increase/decrease angular velocity
space key, s : stop
CTRL-C to quit
"""

###TODO: Fill in the alphabet keys you'd want to control the turtle with. (move up, down, left, right). Be sure to update the message above for the keys you choose###
# moveKeys = {
#     '__': (1, 0),
#     '__': (-1, 0),
#     '__': (0, 1),
#     '__': (0, -1),
# }

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


###TODO: Change the velocity and turning speed (float) ###
# speed = 
# turn = 
 
def vels(speed, turn):
    return "currently:\tspeed %s\tturn %s " % (speed, turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    ###TODO: Initialize a ros node named turtle_keyboard_control ###

    ###TODO: Create a publisher that publishes to the /turtle1/cmd_vel topic (it's built into the turtlesim environment) ###
    # pub =  # Create publisher 

    try:
        print(msg)
        print(vels(speed, turn))
        while True:
            ## gets keyboard press, then controls turtle if it's a key defined in moveKeys
            key = getKey()
            if key in moveKeys.keys():
                x = moveKeys[key][0]
                theta = moveKeys[key][1]
            else:
                x = 0
                theta = 0
                if (key == '\x03'):
                    break
            
            ###TODO: create a new Twist message ###
            # __ =   
            # __.linear.x = x * speed
            # __.angular.z = theta * turn

            # pub.publish(__)

    except Exception as e:
        print(e)

    finally:
        ###TODO: Do the same as before, create a new Twist message. This is to stop the turtle after exiting ###
        # __ =  
        # __.linear.x = 0
        # __.angular.z = 0
        # pub.publish(__)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
