#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys, select, termios, tty


# Initialize PID control parameters, can tweak these values
Kp = 1.0   # Proportional gain
Ki = 0.1   # Integral gain
Kd = 0.01  # Derivative gain

# Initialize error and integral term for PID
error_integral = 0
prev_error = 0

# Callback function to get current turtle pose
def poseCallback(data):
    global current_pose
    current_pose = data

def update_pid(target, current, prev_error, error_integral):
    error = target - current
    error_integral += error
    error_derivative = error - prev_error

    linear_speed = Kp * error + Ki * error_integral + Kd * error_derivative

    return linear_speed, error, error_integral

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

## Desired linear speed of the turtle, can adjust this value
target_speed = 1.0

 
def vels(speed, turn):
    return "currently:\tspeed %s\tturn %s " % (speed, turn)

if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)

    ###TODO: Initialize a ros node named turtle_keyboard_control ###

    ###TODO: Create a publisher that publishes to the /turtle1/cmd_vel topic (it's built into the turtlesim environment) ###
    # pub =  # Create publisher 

    ###TODO: Initialize a subscriber that subscribes to the /turtle1/pose topic ###

    
    try:
        print(msg)
        print(vels(speed, turn))
        while True:
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                theta = moveBindings[key][1]
            else:
                x = 0
                theta = 0
                if (key == '\x03'):
                    break

            target_linear_speed, prev_error, error_integral = update_pid(target_speed, current_pose.y, prev_error, error_integral)
            ###TODO: Create a new Twist message ###
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

