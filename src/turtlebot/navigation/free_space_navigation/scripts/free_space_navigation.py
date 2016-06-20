#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import radians

class free_space_navigation():
    def __init__(self):
        # initiliaze
        rospy.init_node('free_space_navigation', anonymous=False)

        # What to do you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        
        self.velocityPublisher = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
     
    # 2 HZ
        r = rospy.Rate(2);

    # create two different Twist() variables.  One for moving forward.  One for turning 45 degrees.

        # let's go forward at 0.2 m/s
        velocityMessage = Twist()
        velocityMessage.linear.x = 0.2
    # by default angular.z is 0 so setting this isn't required

        #let's turn at 45 deg/s
        turnMessage = Twist()
        turnMessage.linear.x = 0
        turnMessage.angular.z = radians(45); #45 deg/s in radians/s

    #two keep drawing squares.  Go forward for 2 seconds (10 x 5 HZ) then turn for 2 second
    count = 0
        while not rospy.is_shutdown():
        # go forward 0.4 m (2 seconds * 0.2 m / seconds)
        rospy.loginfo("Turtlebot moves forwards")
            for x in range(0,10):
                self.velocityPublisher.publish(velocityMessage)
                r.sleep()
        # turn 90 degrees
        rospy.loginfo("Turtlebot is Turning")
            for x in range(0,10):
                self.velocityPublisher.publish(turnMessage)
                r.sleep()            
        count = count + 1
        if(count == 4): 
                shutdown()
        if(count == 0): 
                rospy.loginfo("TurtleBot will not return to the exact original position but it will be close")
        
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop Drawing Squares")
        self.velocityPublisher.publish(Twist())
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        free_space_navigation()
    except:
        rospy.loginfo("node terminated.")