
.. _free-space-navigation:

===============================
Turtlebot Free Space Navigation
===============================

This tutorial is the first lesson in the series of robot navigation. We consider the case of an open space with no obstacles. 

The objective of this tutorial is to learn how to make the Turtlebot robot move using ROS. You will mainly learn how to publish a velocity message to make the robot move for a certain distance, or rotate for a certain angle. 
For this, you will create the functions ``move`` and ``rotate`` using different techniques. 
In particular, you will learn how to use ``TF`` package to estimate the distance traveled by the robot and the angle rotated by the robot using frame transformations. 

.. NOTE::

   In this tutorial you will learn how to:

      * Make the robot navigate in an open obstcale-free space
      * Develop functions to make the robot move straight for a certain distance
      * Develop functions to make the robot rotate for a certain angle. 
      * use ``TF`` package to estimate the traveled distance and the rotated angle by a robot

Background
==========
The objective is to develop functions to make the robot moves in an open space in straight line for a certain distance, and rotate left or right for certain angle. 
Using these primitives, it is possible to make the robot move in a free space. 

In :ref:`ros-programming-turtlesim` tutorial, we used the simple equation of ``distance=time*speed`` to make the robot move to a certain distance.
However, this method is not effective in case of a real robot considering the following reason: the inaccuracy of IMU sensor data that provide the speed of the robot in addition to the friction with the ground will 
compromise the accuracy of the calculated traveled distance in a certain time duration, which results in an estimation error. This issue is even worse in case of rotation. This estimation error will quickly cumulate over time leading to inacceptable localization error.  
Fortunately, in ROS, there is the frame transformation package, denoted as ``tf`` package, that provides several interesting and advanced functionalities to estimate the motion of a frame (in this case the frame attached to the robot), with respect to a fixed frame (i.e the reference frame). 
In this tutorial, we will use the ``tf`` package to estimate the traveled distance of the robot, in addition to the rotated angle of the robot. 

 
.. NOTE::

   It is important to have a prior knowledge on frame transformation first to understand the code. Check some online tutorials or ask your instructor. 



Tutorial Files
==============

You can find the whole ``cpp`` and ``python`` files in our `GitHub repository <https://github.com/aniskoubaa/gaitech_doc>`_. 
They are located in ``src/turtlebot/navigation/free_space_navigation``. 
In particular, we will use the launch file ``free_space_navigation_stage.launch`` that contains all the needed ROS nodes for this tutorial. 
Here is the content of the ``free_space_navigation_stage.launch`` file.

.. code-block:: bash
  
    <launch>
      <include file="$(find turtlebot_stage)/launch/turtlebot_in_stage.launch"/> 
      <node name="free_space_navigation" pkg="gaitech_doc" type="free_space_navigation_node" output="screen"/>
    </launch>

In the code you will find 3 ``move`` functions and a ``rotate`` function and each one of them has its own approach so you will be able to know 3 different ways of controlling and manipulating the turtlebot robot . 
The code is also well explained so you can easily understand what each line is doing in the code and what is its functionality.	

   
Anaylzing the code
==================

First Approach
--------------


We first analyze the ``move_v1`` function to make the robot moves with a certain speed for a certain distance in stragight line either forward or backward. 

The following code below sets the linear speed of the x-axis as positive value if the intention is to move forward, and negative value if the robot is to move backward, based on the value of ``isForward`` boolean variable. 
All other linear speeds and angular speeds must be set to zero, because we consider only a straight motion in the x-axis direction. 
It has to be noted that the x-axis of the linear speed is the axis that points to the front of the robot from its center. 

**C++ Code**

.. code-block:: c

    //set the linear velocity to a positive value if isFoward is true
   if (isForward)
      VelocityMessage.linear.x =abs(speed);
   else //else set the velocity to negative value to move backward
      VelocityMessage.linear.x =-abs(speed);
   //all velocities of other axes must be zero.
   VelocityMessage.linear.y =0;
   VelocityMessage.linear.z =0;
   //The angular velocity of all axes must be zero because we want  a straight motion
   VelocityMessage.angular.x = 0;
   VelocityMessage.angular.y = 0;
   VelocityMessage.angular.z =0;

**Python Code**

.. code-block:: python

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



The following code waits for ``tf::TransformListener listener`` to find the transformation between the ``/base_footprint`` frame and the ``/odom`` frame, which represents the reference frame.
Then, once the  the transformation is found between the two frames, we save its current state into the ``init_transform`` which is a ``tf::StampedTransform`` object. 
In simple words, this object captures the relation between the two frames in terms of translation and relative orientation.  


**C++ Code**

.. code-block:: c
   
   try{
         //wait for the transform to be found
         listener.waitForTransform("/base_footprint", "/odom", ros::Time(0), ros::Duration(10.0) );
         //Once the transform is found,get the initial_transform transformation.
         listener.lookupTransform("/base_footprint", "/odom",ros::Time(0), init_transform);
      }
      catch (tf::TransformException & ex){
         ROS_ERROR(" Problem %s",ex.what());
         ros::Duration(1.0).sleep();
      }


**Python Code**

.. code-block:: python 

      try:
         #wait for the transform to be found
         listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0),rospy.Duration(10.0))
         #Once the transform is found,get the initial_transform transformation.
          listener.lookupTransform("/base_footprint", "/odom", rospy.Time(0),init_transform)
      except Exception:
           rospy.Duration(1.0)


The following code estimates the traveled distance. 
It is known that the distance is ``sqrt((x1-x0)^2 + (y1-y0)^2)``.
``current_transform`` capture the current transformation between the ``/base_footprint`` and ``/odom`` frames. 
Using the ``tf`` function ``getOrigin().x()`` and ``getOrigin().y()`` we can find the ``x`` and ``y`` coordinates
of the frame ``/base_footprint`` with respect to ``/odom`` frame. 
Appying the distance equation, we will be able to find to distance traveled by the robot, 
considering that the ``init_transform`` was captured at the moment before starting the motion and
that the ``current_transform`` was captured at the moment of the motion. 


**C++ Code**

.. code-block:: c
   :emphasize-lines: 15
   
   do{
       /***************************************
       * STEP1. PUBLISH THE VELOCITY MESSAGE
       ***************************************/
      velocityPublisher.publish(VelocityMessage);
      ros::spinOnce();
      loop_rate.sleep();
      /**************************************************
       * STEP2. ESTIMATE THE DISTANCE MOVED BY THE ROBOT
       *************************************************/
      try{
         //wait for the transform to be found
         listener.waitForTransform("/base_footprint", "/odom", ros::Time(0), ros::Duration(10.0) );
         //Once the transform is found,get the initial_transform transformation.
         listener.lookupTransform("/base_footprint", "/odom",ros::Time(0), current_transform);
      }
      catch (tf::TransformException & ex){
         ROS_ERROR(" Problem %s",ex.what());
         ros::Duration(1.0).sleep();
      }
         
         /*
          * Calculate the distance moved by the robot
          * There are two methods that give the same result
          */
   
         /*
          * Method 1: Calculate the distance between the two transformations
          * Hint:
          *      --> transform.getOrigin().x(): represents the x coordinate of the transformation
          *      --> transform.getOrigin().y(): represents the y coordinate of the transformation
          */
         //calculate the distance moved
         distance_moved = sqrt(pow((current_transform.getOrigin().x()-init_transform.getOrigin().x()), 2) +
               pow((current_transform.getOrigin().y()-init_transform.getOrigin().y()), 2));
   
   
      }while((distance_moved<distance)&&(ros::ok()));


**Python Code**

.. code-block:: python
   :emphasize-lines: 17
  
    while True :
        rospy.loginfo("Turtlebot moves forwards") 
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

        # calculate the distance moved
        end = 0.5 * sqrt(trans[0] ** 2 + trans[1] ** 2)
        distance_moved = distance_moved+abs(abs(float(end)) - abs(float(start)))
        if not (distance_moved<distance):
            break


Second Approach
---------------


Now we will analyze the ``move_v2`` function to make the robot moves with a certain speed for a certain distance in stragight line either forward or backward. 

The following code below uses ``tf`` transform listener to calculate the relative transform, then we determine its length. After declaring the variable in the beginning of the function, you will find the following:

**C++ Code**

.. code-block:: c
   :emphasize-lines: 27,28
   
    do{
    /***************************************
     * STEP1. PUBLISH THE VELOCITY MESSAGE
     ***************************************/
    velocityPublisher.publish(VelocityMessage);
    ros::spinOnce();
    loop_rate.sleep();
    /**************************************************
     * STEP2. ESTIMATE THE DISTANCE MOVED BY THE ROBOT
     *************************************************/
    try{
      //wait for the transform to be found
      listener.waitForTransform("/base_footprint", "/odom", ros::Time(0), ros::Duration(10.0) );
      //Once the transform is found,get the initial_transform transformation.
      listener.lookupTransform("/base_footprint", "/odom",ros::Time(0), current_transform);
    }
    catch (tf::TransformException & ex){
      ROS_ERROR(" Problem %s",ex.what());
      ros::Duration(1.0).sleep();
    }

    /*
     * Method 2: using transform composition. We calculate the relative transform, then we determine its length
     * Hint:
     *    --> transform.getOrigin().length(): return the displacement of the origin of the transformation
     */
    tf::Transform relative_transform = init_transform.inverse() * current_transform;
    distance_moved= relative_transform.getOrigin().length();

    cout<<"Method 2: distance moved: "<<distance_moved <<", "<<distance<<endl;

    }while((distance_moved<distance)&&(ros::ok()));

As for the python code, because it doesn't allow operator overloading that is defining the logic of operators for objects. The approach that was applied here is to multiply the ``tf::Transform`` and convert the result to a matrix and then extract the information from this matrix as highlighted below.

**Python Code**

.. code-block:: python
    :emphasize-lines: 8,9,10,37,38,39,40,41,43,47
    
    try:
      #wait for the transform to be found

      listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0),rospy.Duration(10.0))
      #Once the transform is found,get the initial_transform transformation.
      (trans,rot) = listener.lookupTransform('/base_footprint', '/odom', rospy.Time(0))
      #listener.lookupTransform("/base_footprint", "/odom", rospy.Time(0),init_transform)
      trans1_mat = tf.transformations.translation_matrix(trans)
      rot1_mat   = tf.transformations.quaternion_matrix(rot)
      mat1 = numpy.dot(trans1_mat, rot1_mat)
      init_transform.transform.translation = trans
      init_transform.transform.rotation =rot

      except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            rospy.Duration(1.0)
     
      while True :
        rospy.loginfo("Turtlebot moves forwards") 
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
            
        trans1_mat = tf.transformations.translation_matrix(trans)
        rot1_mat   = tf.transformations.quaternion_matrix(rot)
        mat2 = numpy.dot(trans1_mat, rot1_mat)
        mat3 = numpy.dot(mat1, mat2)
        trans3 = tf.transformations.translation_from_matrix(mat3)
            
        rot3 = tf.transformations.quaternion_from_matrix(mat3)   

        current_transform.transform.translation = trans
        current_transform.transform.rotation =rot
        distance_moved = distance_moved + (0.5 * sqrt(trans3[0] ** 2 + trans3[1] ** 2))
            
        if not (distance_moved<distance):
          break



Third Approach
--------------

The last function we are going to analyze is the ``move_v3`` function to make the robot moves with a certain speed for a certain distance in stragight line either forward or backward. 

The following code below uses the ``pose`` coordinates of the robot to estimate the distance. After declaring the variable in the beginning of the function and equate the initial pose of the turtlebot before start moving with the ``turtlebot_odom_pose`` global variable, you will find the following:

**C++ Code**

.. code-block:: c
   :emphasize-lines: 2,8,9

      //we update the initial_turtlebot_odom_pose using the turtlebot_odom_pose global variable updated in the callback function poseCallback
      initial_turtlebot_odom_pose = turtlebot_odom_pose;

      do{
      velocityPublisher.publish(VelocityMessage);
      ros::spinOnce();
      loop_rate.sleep();
      distance_moved = sqrt(pow((turtlebot_odom_pose.pose.pose.position.x-initial_turtlebot_odom_pose.pose.pose.position.x), 2) +
        pow((turtlebot_odom_pose.pose.pose.position.y-initial_turtlebot_odom_pose.pose.pose.position.y), 2));

      }while((distance_moved<distance)&&(ros::ok()));
      //finally, stop the robot when the distance is moved
      VelocityMessage.linear.x =0;
      velocityPublisher.publish(VelocityMessage);
      }

**Python Code**

.. code-block:: python
   :emphasize-lines: 3,13,14

    #we update the initial_turtlebot_odom_pose using the turtlebot_odom_pose global variable updated in the callback function poseCallback
    #we will use deepcopy() to avoid pointers confusion
    initial_turtlebot_odom_pose = copy.deepcopy(self.turtlebot_odom_pose)

    while True :
        rospy.loginfo("Turtlebot moves forwards")
        self.velocityPublisher.publish(VelocityMessage)
         
        loop_rate.sleep()
                    
        rospy.Duration(1.0)
                    
        distance_moved = distance_moved+abs(0.5 * sqrt(((self.turtlebot_odom_pose.pose.pose.position.x-initial_turtlebot_odom_pose.pose.pose.position.x) ** 2) +
        ((self.turtlebot_odom_pose.pose.pose.position.x-initial_turtlebot_odom_pose.pose.pose.position.x) ** 2)))
                    
        #rospy.loginfo(self.turtlebot_odom_pose.pose.pose.position.x)
        #rospy.loginfo(initial_turtlebot_odom_pose.pose.pose.position.x)
        #rospy.loginfo(distance_moved)
                    
        if not (distance_moved<distance):
            break

Rotate Function
---------------

The following code defines the ``rotate`` function that gives the robot the ability to turn. It starts by delcaring a ``Twist`` message to send velocity commands and a declartion of ``tf`` transform listener to listen and capture the transformation between the ``odom`` frame and the ``base_footprint`` frame. Then change the angles to ``radians`` and then start publishing topics according to the right angles until the robot reaches a certain angle. The ``python`` code is a little different than the ``C++`` code but it does the same functionality.


**C++ Code**

.. code-block:: c
   :emphasize-lines: 15

   double rotate(double angular_velocity, double radians,  bool clockwise)
    {

    //delcare a Twist message to send velocity commands
    geometry_msgs::Twist VelocityMessage;
    //declare tf transform listener: this transform listener will be used to listen and capture the transformation between
    // the odom frame (that represent the reference frame) and the base_footprint frame the represent moving frame
    tf::TransformListener TFListener;
    //declare tf transform
    //init_transform: is the transformation before starting the motion
    tf::StampedTransform init_transform;
    //current_transformation: is the transformation while the robot is moving
    tf::StampedTransform current_transform;
    //initial coordinates (for method 3)
    nav_msgs::Odometry initial_turtlebot_odom_pose;

    double angle_turned =0.0;

    //validate angular velocity; ANGULAR_VELOCITY_MINIMUM_THRESHOLD is the minimum allowed
    angular_velocity=((angular_velocity>ANGULAR_VELOCITY_MINIMUM_THRESHOLD)?angular_velocity:ANGULAR_VELOCITY_MINIMUM_THRESHOLD);

    while(radians < 0) radians += 2*M_PI;
    while(radians > 2*M_PI) radians -= 2*M_PI;

    //wait for the listener to get the first message
    TFListener.waitForTransform("base_footprint", "odom", ros::Time(0), ros::Duration(1.0));


    //record the starting transform from the odometry to the base frame
    TFListener.lookupTransform("base_footprint", "odom", ros::Time(0), init_transform);


    //the command will be to turn at 0.75 rad/s
    VelocityMessage.linear.x = VelocityMessage.linear.y = 0.0;
    VelocityMessage.angular.z = angular_velocity;
    if (clockwise) VelocityMessage.angular.z = -VelocityMessage.angular.z;

    //the axis we want to be rotating by
    tf::Vector3 desired_turn_axis(0,0,1);
    if (!clockwise) desired_turn_axis = -desired_turn_axis;

    ros::Rate rate(10.0);
    bool done = false;
    while (!done )
    {
    //send the drive command
    velocityPublisher.publish(VelocityMessage);
    rate.sleep();
    //get the current transform
    try
    {
      TFListener.waitForTransform("base_footprint", "odom", ros::Time(0), ros::Duration(1.0));
      TFListener.lookupTransform("base_footprint", "odom", ros::Time(0), current_transform);
      }
      catch (tf::TransformException ex)
      {
      ROS_ERROR("%s",ex.what());
      break;
    }
    tf::Transform relative_transform = init_transform.inverse() * current_transform;
    tf::Vector3 actual_turn_axis = relative_transform.getRotation().getAxis();
    angle_turned = relative_transform.getRotation().getAngle();

    if (fabs(angle_turned) < 1.0e-2) continue;
    if (actual_turn_axis.dot(desired_turn_axis ) < 0 )
      angle_turned = 2 * M_PI - angle_turned;

    if (!clockwise)
      VelocityMessage.angular.z = (angular_velocity-ANGULAR_VELOCITY_MINIMUM_THRESHOLD) * (fabs(radian2degree(radians-angle_turned)/radian2degree(radians)))+ANGULAR_VELOCITY_MINIMUM_THRESHOLD;
    else
      if (clockwise)
        VelocityMessage.angular.z = (-angular_velocity+ANGULAR_VELOCITY_MINIMUM_THRESHOLD) * (fabs(radian2degree(radians-angle_turned)/radian2degree(radians)))-ANGULAR_VELOCITY_MINIMUM_THRESHOLD;

    if (angle_turned > radians) {
      done = true;
      VelocityMessage.linear.x = VelocityMessage.linear.y = VelocityMessage.angular.z = 0;
      velocityPublisher.publish(VelocityMessage);
    }


    }
    if (done) return angle_turned;
    return angle_turned;
    }

As for the python, we had the same problem as the second approach of the ``move`` functions, so the closest approach was to use the 
**Python Code**

.. code-block:: python
   :emphasize-lines: 29

    def rotate(self,angular_velocity,radians,clockwise):
        rotateMessage = Twist()
        
        #declare tf transform
        listener = tf.TransformListener()
        #init_transform: is the transformation before starting the motion
        init_transform = geometry_msgs.msg.TransformStamped()
        #current_transformation: is the transformation while the robot is moving
        current_transform = geometry_msgs.msg.TransformStamped()
        
        angle_turned = 0.0

        angular_velocity = (-angular_velocity, ANGULAR_VELOCITY_MINIMUM_THRESHOLD)[angular_velocity > ANGULAR_VELOCITY_MINIMUM_THRESHOLD]

        while(radians < 0):
            radians += 2* pi

        while(radians > 2* pi):
            radians -= 2* pi
        
        listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0), rospy.Duration(10.0) )
        (trans,rot) = listener.lookupTransform('/base_footprint', '/odom', rospy.Time(0))
        #listener.lookupTransform("/base_footprint", "/odom", rospy.Time(0),init_transform)
        
        init_transform.transform.translation = trans
        init_transform.transform.rotation =rot

        #since the rotation is only in the Z-axes 
        start_angle = 0.5 * sqrt(rot[2] ** 2)

        rotateMessage.linear.x = rotateMessage.linear.y = 0.0
        rotateMessage.angular.z = angular_velocity

        if (clockwise):
            rotateMessage.angular.z = -rotateMessage.angular.z
        
        
        loop_rate = rospy.Rate(10)
        
        while True:
            rospy.loginfo("Turtlebot is Rotating")

            self.velocityPublisher.publish(rotateMessage)
         
            loop_rate.sleep()
                    
            rospy.Duration(1.0)

            try:

                #wait for the transform to be found
                listener.waitForTransform("/base_footprint", "/odom", rospy.Time(0), rospy.Duration(10.0) )
                #Once the transform is found,get the initial_transform transformation.
                #listener.lookupTransform("/base_footprint", "/odom",rospy.Time(0))
                (trans,rot) = listener.lookupTransform('/base_footprint', '/odom', rospy.Time(0))
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                rospy.Duration(1.0)

            current_transform.transform.translation = trans
            current_transform.transform.rotation =rot
            
            #since the rotation is only in the Z-axes 
            end_angle = 0.5 * sqrt( rot[2] ** 2)
            
            angle_turned = angle_turned+abs(abs(float(end_angle)) - abs(float(start_angle)))
            
            if (angle_turned > radians):
                break



Running the code using Stage and RViz Simulators
================================================

Bring up your simulator:

.. code-block:: bash
	
	roslaunch turtlebot_stage turtlebot_in_stage.launch

If your PC is not fast enough to run the `Stage` with `RViz` you can run only the `Stage` using this command:

.. code-block:: bash
	
	roslaunch turtlebot_stage turtlebot_in_stage_no_rviz.launch

After that run the ``cpp`` node by typing the following command:

.. code-block:: bash
	
	roslaunch gaitech_doc free_space_navigation

or launch the ``free_space_navigation_stage.launch`` file to launch the simulators and the ``cpp`` node.

.. image:: images/stage-square-move-cpp.png
	:align: center


You can also choose to run the ``python`` script by running this command:

.. code-block:: bash
	
	python your_workspace/src/gaitech_doc/src/turtlebot/navigation/free_space_navigation/script/free_space_navigation.py

Or you can launch the ``free_space_navigation_stage_python_node.launch`` file to run the simulators and the ``python`` node.

.. code-block:: bash

    roslaunch gaitech_doc free_space_navigation_stage_python_node.launch

.. image:: images/stage-square-move-python.png
	:align: center

.. NOTE::
	
	You can try the three ``move`` methods by calling each one of them in the ``moveSquare`` method.
	You can try the same codes with `Gazebo` simulator but you need to have a fast PC. All you have to do is to launch `Gazebo` by typing the following command:
	
	.. code-block:: bash
	
		roslaunch turtlebot_gazebo turtlebot_world.launch

	Then run either one of the files as mentioned above. 	



.. youtube:: SHPCyqFDr1Q
