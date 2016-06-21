#!/usr/bin/env python

import rospy
import tf
import numpy
from geometry_msgs.msg import Twist
from math import radians
from nav_msgs.msg import Odometry


class free_space_navigation():
    LINEAR_VELOCITY_MINIMUM_THRESHOLD  = 0.2
    ANGULAR_VELOCITY_MINIMUM_THRESHOLD = 0.4
    turtlebot_odom_pose = Odometry()

    def __init__(self):
        # initiliaze
        rospy.init_node('free_space_navigation', anonymous=False)

        # What to do you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        
        self.velocityPublisher = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscribe("/odom", 10, self.poseCallback);     
    # 2 HZ
        r = rospy.Rate(2);
        r.sleep()
    # create two different Twist() variables.  One for moving forward.  One for turning 45 degrees.

        
    # by default angular.z is 0 so setting this isn't required

        #let's turn at 45 deg/s
        turnMessage = Twist()
        turnMessage.linear.x = 0
        turnMessage.angular.z = radians(25); #45 deg/s in radians/s

    #two keep drawing squares.  Go forward for 2 seconds (10 x 5 HZ) then turn for 2 second
    count = 0
        while not rospy.is_shutdown():
        # go forward 0.4 m (2 seconds * 0.2 m / seconds)
        (roll,pitch,yaw) = euler_from_quaternion(turtlebot_odom_pose.pose.pose.orientation)
        rospy.loginfo("robot initial pose: (%.2f, %.2f, %.2f)",
                                        turtlebot_odom_pose.pose.pose.position.x,
                                        turtlebot_odom_pose.pose.pose.position.y,
                                        degrees(yaw))
        moveSquare(1.0)

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
    
    def moveSquare(self,sideLength):
        for i in range(0, 4):
            move(self,0.3, sideLength, true)
            rotate (self,0.3, radiansa(85), true)
    
    def rotate(self,angular_velocity,radians, clockwise):

    #delcare a Twist message to send velocity commands
        velocityMessage = Twist()
    #declare tf transform listener: this transform listener will be used to listen and capture the transformation between
    # the odom frame (that represent the reference frame) and the base_footprint frame the represent moving frame
        TFListener = TransformListener()
    #declare tf transform
    #init_transform: is the transformation before starting the motion
        init_transform = geometry_msgs.msg.TransformStamped()
    #current_transformation: is the transformation while the robot is moving
        current_transform = geometry_msgs.msg.TransformStamped()
    #initial coordinates (for method 3)
        initial_turtlebot_odom_pose = Odometry()

        angle_turned =0.0

        angular_velocity = angular_velocity if angular_velocity>ANGULAR_VELOCITY_MINIMUM_THRESHOLD else ANGULAR_VELOCITY_MINIMUM_THRESHOLD
        
        while(radians < 0):
            radians += 2*pi
    
        while(radians > 2*pi):
            radians -= 2*pi
    
    # wait for the listener to get the first message
        TFListener.waitForTransform("base_footprint", "odom", rospy.Time(0),rospy.Duration(1.0))


    # record the starting transform from the odometry to the base frame
        TFListener.lookupTransform("base_footprint", "odom", rospy.Time(0),current_transform)

        velocityMessage.linear.x = 0.0
        velocityMessage.linear.y = 0.0
        velocityMessage.linear.z = angular_velocity if clockwise else -angular_velocity
        #the axis we want to be rotating by
        desired_turn_axis= [0,0,1]
        desired_turn_axis=desired_turn_axis if (!clockwise)  else (-1*desired_turn_axis)
        
        rate=rospy.Rate(10)
        done = False
        
        while (!done):
            #send the drive command
            self.velocityPublisher.publish(velocityMessage);
            rate.sleep();
            # get the current transform
            try:

                # wait for the listener to get the first message
                TFListener.waitForTransform("base_footprint", "odom", rospy.Time(0),rospy.Duration(1.0))
                # record the starting transform from the odometry to the base frame
                TFListener.lookupTransform("base_footprint", "odom", rospy.Time(0),current_transform)
            except TransformException e:
                break

# *************************************** I need Help HERE **************************************************                

            # I cannot find how to initialize these variables      
            relative_transform = Transform.init_transform.inverse() * current_transform;
            actual_turn_axis = relative_transform.getRotation().getAxis();
            angle_turned = relative_transform.getRotation().getAngle();
# ***********************************************************************************************************    

            if (fabs(angle_turned) < 1.0e-2):
                continue
            if (vdot(desired_turn_axis,actual_turn_axis) < 0 ):
                angle_turned = (2 * pi) - angle_turned
            
            if (!clockwise):
                velocityMessage.angular.z = (angular_velocity-ANGULAR_VELOCITY_MINIMUM_THRESHOLD) * (fabs(degrees(radians-angle_turned)/degrees(radians)))+ANGULAR_VELOCITY_MINIMUM_THRESHOLD
            elif (clockwise):
                velocityMessage.angular.z = (-angular_velocity+ANGULAR_VELOCITY_MINIMUM_THRESHOLD) * (fabs(degrees(radians-angle_turned)/degrees(radians)))-ANGULAR_VELOCITY_MINIMUM_THRESHOLD

            if (angle_turned > radians):
                done = True
                velocityMessage.linear.x , velocityMessage.linear.y , velocityMessage.angular.z = 0
                velocityPublisher.publish(velocityMessage)
        

        if (done) return angle_turned
        return angle_turned

    def calculateYaw( x1, y1, x2,y2):
        bearing = atan2((y2 - y1),(x2 - x1));
        #if(bearing < 0) bearing += 2 * PI;
        bearing *= 180.0 / pi
        return bearing

if __name__ == '__main__':
    try:
        free_space_navigation()
    except:
        rospy.loginfo("node terminated.")


