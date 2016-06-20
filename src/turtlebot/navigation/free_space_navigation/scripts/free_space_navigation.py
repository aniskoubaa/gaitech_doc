import rospy
from geometry_msgs.msg import Twist
from math import radians

class free_space_navigation():
    def __init__(self):
        # initiliaze
        rospy.init_node('free_space_navigation', anonymous=False)

	# tell user how to stop TurtleBot
	   rospy.loginfo("To stop TurtleBot CTRL + C")

        # What function to call when you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        
	# Create a publisher which can "talk" to TurtleBot and tell it to move
        self.velocityPublisher = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
     
	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 5 HZ
        r = rospy.Rate(5);

        # Twist is a datatype for velocity
        velocityMessage = Twist()
	# let's go forward at 0.2 m/s
        velocityMessage.linear.x = 0.2
	
    # let's turn at 45 deg/s
	    turnMessage = Twist()
        turnMessage.linear.x = 0
        turnMessage.angular.z = radians(45); #45 deg/s in radians/s

    # The Turtlebot will keep moving till you press ctrl + c
    count = 0
        while not rospy.is_shutdown():
            
            rospy.loginfo("Turtlebot is moving Forward")
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
                count = 0
            if(count == 0): 
                rospy.loginfo("TurtleBot will not return to the exact original position but it will be close")

        
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
	    # a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
        self.velocityPublisher.publish(Twist())
	    # sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        free_space_navigation()
    except:
        rospy.loginfo("free_space_navigation node terminated.")

