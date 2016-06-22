#!/usr/bin/env python

import rospy
import tf
import numpy
import geometry_msgs.msg
from geometry_msgs.msg import Twist
from math import radians,degrees
import math
from nav_msgs.msg import Odometry
from std_msgs.msg import String

class free_space_navigation():
    LINEAR_VELOCITY_MINIMUM_THRESHOLD  = 0.2
    ANGULAR_VELOCITY_MINIMUM_THRESHOLD = 0.4
    

    def poseCallback(self,pose_message):

        self.turtlebot_odom_pose.pose.pose.position.x=pose_message.pose.pose.position.x
        self.turtlebot_odom_pose.pose.pose.position.y=pose_message.pose.pose.position.y
        self.turtlebot_odom_pose.pose.pose.position.z=pose_message.pose.pose.position.z

        self.turtlebot_odom_pose.pose.pose.orientation.w=pose_message.pose.pose.orientation.w
        self.turtlebot_odom_pose.pose.pose.orientation.x=pose_message.pose.pose.orientation.x
        self.turtlebot_odom_pose.pose.pose.orientation.y=pose_message.pose.pose.orientation.y
        self.turtlebot_odom_pose.pose.pose.orientation.z=pose_message.pose.pose.orientation.z

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
            try:

                #wait for the transform to be found
                listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0), rospy.Duration(10.0) )
                #Once the transform is found,get the initial_transform transformation.
                listener.lookupTransform("/base_footprint", "/odom",rospy.Time(0), current_transform)
        
            except Exception:
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
            distance_moved = math.sqrt(math.pow((current_transform.getOrigin().x()-init_transform.getOrigin().x()), 2) +
                math.pow((current_transform.getOrigin().y()-init_transform.getOrigin().y()), 2));

        #cout<<"Method 1: distance moved: "<<distance_moved <<", "<<distance<<endl
        #cout<<turtlebot_odom_pose.pose.pose.position.x<<", "<<turtlebot_odom_pose.pose.pose.position.y<<endl
        #cout<<init_transform.getOrigin().x() <<", "<<init_transform.getOrigin().y()<<endl
        #cout<<current_transform.getOrigin().x() <<", "<<current_transform.getOrigin().y()<<endl<<endl

            if not (distance_moved<distance):
                break
            
            #finally, stop the robot when the distance is moved
        VelocityMessage.linear.x =0
        self.velocityPublisher.publish(VelocityMessage)

    
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
        VelocityMessage.linear.y , VelocityMessage.linear.z , VelocityMessage.angular.x , VelocityMessage.angular.y , VelocityMessage.angular.z =0

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
            rospy.spin()
            loop_rate.sleep()
        #/**************************************************
        # * STEP2. ESTIMATE THE DISTANCE MOVED BY THE ROBOT
        # *************************************************/
            try:

                #wait for the transform to be found
                listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0), rospy.Duration(10.0) )
                #Once the transform is found,get the initial_transform transformation.
                listener.lookupTransform("/base_footprint", "/odom",rospy.Time(0), current_transform)
        
            except Exception:
                rospy.Duration(1.0)

#*********************************Same Problem as rotate Method***********************************************************
         # Method 2: using transform composition. We calculate the relative transform, then we determine its length
         # Hint:
         #    --> transform.getOrigin().length(): return the displacement of the origin of the transformation
         #
            relative_transform = Transform.init_transform.inverse() * current_transform
            distance_moved= relative_transform.getOrigin().length()
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
        #initial coordinates (for method 3)
        initial_turtlebot_odom_pose = Odometry()
        
        # set the linear velocity to a positive value if isFoward is True
        if (isForward):
            VelocityMessage.linear.x =abs(speed)
        else: #else set the velocity to negative value to move backward
            VelocityMessage.linear.x =-abs(speed)
        #all velocities of other axes must be zero.
        VelocityMessage.linear.y , VelocityMessage.linear.z , VelocityMessage.angular.x , VelocityMessage.angular.y , VelocityMessage.angular.z =0

        distance_moved = 0.0
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)
       
        #we update the initial_turtlebot_odom_pose using the turtlebot_odom_pose global variable updated in the callback function poseCallback
        initial_turtlebot_odom_pose = self.turtlebot_odom_pose

        while True :
            
        #/***************************************
        # * STEP1. PUBLISH THE VELOCITY MESSAGE
        # ***************************************/
            self.velocityPublisher.publish(VelocityMessage)
            rospy.spin()
            loop_rate.sleep()
        # calculate the distance moved
            distance_moved = sqrt(pow((current_transform.getOrigin().x()-init_transform.getOrigin().x()), 2) +
                pow((current_transform.getOrigin().y()-init_transform.getOrigin().y()), 2))
            
            if not distance_moved<distance:
                break

            #finally, stop the robot when the distance is moved
        VelocityMessage.linear.x =0
        self.velocityPublisher.publish(VelocityMessage)

    
    def rotate(self,angular_velocity,radians, clockwise):

    #delcare a Twist message to send velocity commands
        velocityMessage = Twist()
    #declare tf transform listener: this transform listener will be used to listen and capture the transformation between
    # the odom frame (that represent the reference frame) and the base_footprint frame the represent moving frame
        TFListener = tf.TransformListener()
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
        desired_turn_axis=desired_turn_axis if (not clockwise)  else (-1*desired_turn_axis)
        
        rate=rospy.Rate(10)
        done = False
        
        while (not done):
            #send the drive command
            self.velocityPublisher.publish(velocityMessage)
            rate.sleep()
            # get the current transform
            try:

                # wait for the listener to get the first message
                TFListener.waitForTransform("base_footprint", "odom", rospy.Time(0),rospy.Duration(1.0))
                # record the starting transform from the odometry to the base frame
                TFListener.lookupTransform("base_footprint", "odom", rospy.Time(0),current_transform)
            except Exception:
                break

# *************************************** I need Help HERE **************************************************                

            # I cannot find how to initialize these variables      
            relative_transform = Transform.init_transform.inverse() * current_transform
            actual_turn_axis = relative_transform.getRotation().getAxis()
            angle_turned = relative_transform.getRotation().getAngle()
# ***********************************************************************************************************    

            if (fabs(angle_turned) < 1.0e-2):
                continue
            if (vdot(desired_turn_axis,actual_turn_axis) < 0 ):
                angle_turned = (2 * pi) - angle_turned
            
            if (not clockwise):
                velocityMessage.angular.z = (angular_velocity-ANGULAR_VELOCITY_MINIMUM_THRESHOLD) * (fabs(degrees(radians-angle_turned)/degrees(radians)))+ANGULAR_VELOCITY_MINIMUM_THRESHOLD
            elif (clockwise):
                velocityMessage.angular.z = (-angular_velocity+ANGULAR_VELOCITY_MINIMUM_THRESHOLD) * (fabs(degrees(radians-angle_turned)/degrees(radians)))-ANGULAR_VELOCITY_MINIMUM_THRESHOLD

            if (angle_turned > radians):
                done = True
                velocityMessage.linear.x , velocityMessage.linear.y , velocityMessage.angular.z = 0
                self.velocityPublisher.publish(velocityMessage)
        
        if (done):
            return angle_turned

        return angle_turned

    def calculateYaw( x1, y1, x2,y2):
        bearing = atan2((y2 - y1),(x2 - x1))
        #if(bearing < 0) bearing += 2 * PI
        bearing *= 180.0 / pi
        return bearing


    def moveSquare(self,sideLength):
        rospy.loginfo("hello world1")

        for i in range(0, 4):
            rospy.loginfo("hello world2")
            self.move(0.3, sideLength, True)
            rospy.loginfo("hello world3")

            self.rotate (0.3, radiansa(85), True)
   
    def __init__(self):
        # initiliaze
        rospy.init_node('free_space_navigation', anonymous=True)

        # What to do you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        self.turtlebot_odom_pose = Odometry()
    pose_message = Odometry()
        self.velocityPublisher = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber("/odom", Odometry, self.poseCallback)     
    # 2 HZ
        r = rospy.Rate(2)
        
        r.sleep()
    # create two different Twist() variables.  One for moving forward.  One for turning 45 degrees.

        
    # by default angular.z is 0 so setting this isn't required

        #let's turn at 45 deg/s
        turnMessage = Twist()
        turnMessage.linear.x = 0
        turnMessage.angular.z = radians(25) #45 deg/s in radians/s

    #two keep drawing squares.  Go forward for 2 seconds (10 x 5 HZ) then turn for 2 second
        while not rospy.is_shutdown():
            sideLength=1.0

            self.moveSquare(sideLength)
        

        # go forward 0.4 m (2 seconds * 0.2 m / seconds)
            #(roll,pitch,yaw) = tf.transformations.euler_from_quaternion(self.turtlebot_odom_pose.pose.pose.orientation)
            #rospy.loginfo(self.turtlebot_odom_pose.pose.pose.position.x,
             #         self.turtlebot_odom_pose.pose.pose.position.y,
              #        degrees(yaw))
          

        
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



