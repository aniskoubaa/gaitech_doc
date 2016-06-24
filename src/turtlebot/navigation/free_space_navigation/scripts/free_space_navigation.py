#!/usr/bin/env python

import rospy
import tf
import numpy
import geometry_msgs.msg
from geometry_msgs.msg import Twist, Point, Quaternion
from math import radians,degrees
from math import *
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from rbx1_nav.transform_utils import quat_to_angle, normalize_angle

LINEAR_VELOCITY_MINIMUM_THRESHOLD  = 0.2
ANGULAR_VELOCITY_MINIMUM_THRESHOLD = 0.4
class free_space_navigation():

    

    def poseCallback(self,pose_message):

        self.turtlebot_odom_pose.pose.pose.position.x=pose_message.pose.pose.position.x
        self.turtlebot_odom_pose.pose.pose.position.y=pose_message.pose.pose.position.y
        self.turtlebot_odom_pose.pose.pose.position.z=pose_message.pose.pose.position.z

        self.turtlebot_odom_pose.pose.pose.orientation.w=pose_message.pose.pose.orientation.w
        self.turtlebot_odom_pose.pose.pose.orientation.x=pose_message.pose.pose.orientation.x
        self.turtlebot_odom_pose.pose.pose.orientation.y=pose_message.pose.pose.orientation.y
        self.turtlebot_odom_pose.pose.pose.orientation.z=pose_message.pose.pose.orientation.z

        def get_odom(self,listener):
        # Get the current transform between the odom and base frames
            try:
                    (trans, rot)  = listener.lookupTransform(self.odom_frame, self.base_frame, rospy.Time(0))
            except (tf.Exception, tf.ConnectivityException, tf.LookupException):
                    rospy.loginfo("TF Exception")
                    return

            return (Point(*trans), quat_to_angle(Quaternion(*rot)))


 # a function that makes the robot move straight
 # @param speed: represents the speed of the robot the robot
 # @param distance: represents the distance to move by the robot
 # @param isForward: if True, the robot moves forward,otherwise, it moves backward
 #
 # Method 1: using tf and Calculate the distance between the two transformations

    def move(self, speed, distance, isForward):
        #declare a Twist message to send velocity commands
            VelocityMessage = Twist()
        # declare tf transform listener: this transform listener will be used to listen and capture the transformation between
        # the odom frame (that represent the reference frame) and the base_footprint frame the represent moving frame
            listener = tf.TransformListener()
        #declare tf transform
        #init_transform: is the transformation before starting the motion
            init_transform = geometry_msgs.msg.TransformStamped()
        #current_transformation: is the transformation while the robot is moving
            current_transform = geometry_msgs.msg.TransformStamped()
            
        position = Point()

        #set the linear velocity to a positive value if isFoward is True
            if (isForward):
                    VelocityMessage.linear.x =abs(speed)
            else: #else set the velocity to negative value to move backward
                    VelocityMessage.linear.x =-abs(speed)

            loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    


     #  First, we capture the initial transformation before starting the motion.
     # we call this transformation "init_transform"
     # It is important to "waitForTransform" otherwise, it might not be captured.
     
            try:
            #wait for the transform to be found

                    listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0),rospy.Duration(10.0))
            #Once the transform is found,get the initial_transform transformation.
                    listener.lookupTransform("/base_footprint", "/odom", rospy.Time(0))
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                    rospy.Duration(1.0)
        
        # Get the starting position values     
                (position, rotation) = self.get_odom(listener)
                        
                x_start = position.x
                y_start = position.y
            
            # Keep track of the distance traveled
                distance_moved = 0
            
            # Enter the loop to move along a side
                while distance_moved < distance and not rospy.is_shutdown():
                # Publish the Twist message and sleep 1 cycle         
                    self.velocityPublisher.publish(VelocityMessage)
               
            try:
            #wait for the transform to be found

                listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0),rospy.Duration(10.0))
            #Once the transform is found,get the initial_transform transformation.
                listener.lookupTransform("/base_footprint", "/odom", rospy.Time(0))
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                rospy.Duration(1.0)
                
                # Get the current position
                    (position, rotation) = self.get_odom(listener)
                # Compute the Euclidean distance from the start
                    distance_moved = sqrt(pow((position.x - x_start), 2) + 
                                    pow((position.y - y_start), 2))
                            
            #finally, stop the robot when the distance is moved
        VelocityMessage = Twist()           
            self.velocityPublisher.publish(VelocityMessage)
        rospy.sleep(1.0)
    
    def move_v2(self, speed, distance, isForward):

        #declare a Twist message to send velocity commands
        VelocityMessage = Twist()
        # declare tf transform listener: this transform listener will be used to listen and capture the transformation between
        # the odom frame (that represent the reference frame) and the base_footprint frame the represent moving frame
        listener = tf.TransformListener()
        #declare tf transform
        #init_transform: is the transformation before starting the motion
        init_transform = geometry_msgs.msg.TransformStamped()
        #current_transformation: is the transformation while the robot is moving
        current_transform = geometry_msgs.msg.TransformStamped()
        #initial coordinates (for method 3)
        initial_turtlebot_odom_pose = Odometry()

        # set the linear velocity to a positive value if isFoward is True
        if (isForward):
            VelocityMessage.linear.x =abs(speed)
        else: #else set the velocity to negative value to move backward
            VelocityMessage.linear.x =-abs(speed)
        #all velocities of other axes must be zero.
        VelocityMessage.linear.y =0.0
        VelocityMessage.linear.z =0.0
        VelocityMessage.angular.x =0.0
        VelocityMessage.angular.y =0.0
        VelocityMessage.angular.z =0.0

        distance_moved = 0.0
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)

     # First, we capture the initial transformation before starting the motion.
     # we call this transformation "init_transform"
     # It is important to "waitForTransform" otherwise, it might not be captured.
     
        try:
            #wait for the transform to be found

            listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0),rospy.Duration(10.0))
            #Once the transform is found,get the initial_transform transformation.
            listener.lookupTransform("/base_footprint", "/odom", rospy.Time(0),init_transform)
        except Exception:
            rospy.Duration(1.0)
    
        while True :
            
        #/***************************************
        # * STEP1. PUBLISH THE VELOCITY MESSAGE
        # ***************************************/
            self.velocityPublisher.publish(VelocityMessage)
            loop_rate.sleep()
        #/**************************************************
        # * STEP2. ESTIMATE THE DISTANCE MOVED BY THE ROBOT
        # *************************************************/

                #wait for the transform to be found
            listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0), rospy.Duration(10.0) )
                #Once the transform is found,get the initial_transform transformation.
            (trans,rot) = listener.lookupTransform("/base_footprint", "/odom",rospy.Time(0))

#*********************************Same Problem as rotate Method***********************************************************
         # Method 2: using transform composition. We calculate the relative transform, then we determine its length
         # Hint:
         #    --> transform.getOrigin().length(): return the displacement of the origin of the transformation
         #
                        transform = tf.transformations.concatenate_matrices(tf.transformations.translation_matrix(trans),      tf.transformations.quaternion_matrix(rot))
                        #rospy.loginfo(type(transform))
                        inverse_transform = tf.transformations.inverse_matrix(transform)
            relative_transform = inverse_transform * current_transform.transform.translation.x
                        rospy.loginfo(type(relative_transform))
            distance_moved= relative_transform
#*************************************************************************************************************************
        
            if not distance_moved<distance:
                break
    #finally, stop the robot when the distance is moved
        VelocityMessage.linear.x =0
        self.velocityPublisher.publish(VelocityMessage)
    
    # a function that makes the robot move straight
    # @param speed: represents the speed of the robot the robot
    # @param distance: represents the distance to move by the robot
    # @param isForward: if True, the robot moves forward,otherwise, it moves backward
    #
    # Method 3: we use coordinates of the robot to estimate the distance

    def move_v3(self, speed, distance, isForward):
        #declare a Twist message to send velocity commands
        VelocityMessage = Twist()
        # declare tf transform listener: this transform listener will be used to listen and capture the transformation between
        # the odom frame (that represent the reference frame) and the base_footprint frame the represent moving frame
        listener = tf.TransformListener()

        #set the linear velocity to a positive value if isFoward is True
        if (isForward):
            VelocityMessage.linear.x =abs(speed)
        else: #else set the velocity to negative value to move backward
            VelocityMessage.linear.x =-abs(speed)

        # all velocities of other axes must be zero.
        VelocityMessage.linear.y =0
        VelocityMessage.linear.z =0
        #The angular velocity of all axes must be zero because we want  a straight motion
        VelocityMessage.angular.x = 0
        VelocityMessage.angular.y = 0
        VelocityMessage.angular.z =0

        distance_moved = 0.0
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    


     #  First, we capture the initial transformation before starting the motion.
     # we call this transformation "init_transform"
     # It is important to "waitForTransform" otherwise, it might not be captured.
     
        try:
            #wait for the transform to be found

            listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0),rospy.Duration(10.0))
            #Once the transform is found,get the initial_transform transformation.
            (trans,rot) = listener.lookupTransform('/base_footprint', '/odom', rospy.Time(0))
            #listener.lookupTransform("/base_footprint", "/odom", rospy.Time(0),init_transform)
            start = 0.5 * sqrt(trans[0] ** 2 + trans[1] ** 2)

        except Exception:
            rospy.Duration(1.0)
        distance_moved = 0
        while True :
            
        #/***************************************
        # * STEP1. PUBLISH THE VELOCITY MESSAGE
        # ***************************************/
            self.velocityPublisher.publish(VelocityMessage)
            loop_rate.sleep()
        #/**************************************************
        # * STEP2. ESTIMATE THE DISTANCE MOVED BY THE ROBOT
        # *************************************************/
            try:

                #wait for the transform to be found
                listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0), rospy.Duration(10.0) )
                #Once the transform is found,get the initial_transform transformation.
                #listener.lookupTransform("/base_footprint", "/odom",rospy.Time(0))
                (trans,rot) = listener.lookupTransform('/base_footprint', '/odom', rospy.Time(0))
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                rospy.Duration(1.0)
        # Calculate the distance moved by the robot
        # There are two methods that give the same result
        #
        # Method 1: Calculate the distance between the two transformations
        # Hint:
        #    --> transform.getOrigin().x(): represents the x coordinate of the transformation
        #    --> transform.getOrigin().y(): represents the y coordinate of the transformation
        #
        # calculate the distance moved
            #distance_moved = math.sqrt(math.pow((current_transform.getOrigin().x()-init_transform.getOrigin().x()), 2) +
             #   math.pow((current_transform.getOrigin().y()-init_transform.getOrigin().y()), 2))
            #angular = 4 * atan2(trans[1], trans[0])
            end = 0.5 * sqrt(trans[0] ** 2 + trans[1] ** 2)
            distance_moved = distance_moved+abs(abs(float(end)) - abs(float(start)))
            rospy.loginfo(type(end))

            rospy.loginfo(distance_moved)
            if not (distance_moved<distance):
                break
            
            #finally, stop the robot when the distance is moved
        VelocityMessage.linear.x =0 
        self.velocityPublisher.publish(VelocityMessage)

    
    def rotate(self):
        
        rotateMessage = Twist()
        
            rotateMessage.linear.x = 0
            rotateMessage.angular.z = radians(45); #45 deg/s in radians/s
        
            rospy.loginfo("Turtlebot Turning")
            r = rospy.Rate(5)

            for x in range(0,10):

                self.velocityPublisher.publish(rotateMessage)
                r.sleep()            
        #rospy.loginfo(angular)
        #rospy.loginfo(distance_moved)        


    def calculateYaw( x1, y1, x2,y2):
        bearing = atan2((y2 - y1),(x2 - x1))
        #if(bearing < 0) bearing += 2 * PI
        bearing *= 180.0 / pi
        return bearing


    def moveSquare(self,sideLength):

        for i in range(0, 4):
            self.move_v2(0.3, sideLength, True)
            rospy.sleep(1.0)
            self.rotate ()
   
    def __init__(self):
        # initiliaze
        rospy.init_node('free_space_navigation', anonymous=True)

        # What to do you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        self.turtlebot_odom_pose = Odometry()
        pose_message = Odometry()
        self.velocityPublisher = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber("/odom", Odometry, self.poseCallback)     
            
        # The odom frame is usually just /odom
            self.odom_frame = rospy.get_param('~odom_frame', '/odom')
            # Set the odom frame
            self.odom_frame = '/odom'
        self.base_frame = '/base_footprint'

        # 2 HZ
        r = rospy.Rate(2)
        
        r.sleep()

        while not rospy.is_shutdown():
            sideLength=0.3
            self.moveSquare(sideLength)       

        
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop Drawing Squares")
        self.velocityPublisher.publish(Twist())
        rospy.sleep(1)
    
 

    

if __name__ == '__main__':
    try:
        free_space_navigation()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")