.. _line-follower:

=======================
Turtlebot Line Follower
=======================

This tutorial will introduce how to control your turtlebot robot to follow a line using the ``cv_bridge`` package.

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials and your network set-up is working fine between the ROS Master node and the host node.

.. NOTE::

   In this tutorial you will learn how to:

      * Teleoprate a real and simulated turtlebot with line following program
      * Create your own path
      * Test your program on Gazebo Simulator

The ``cv_bridge`` package is used to convert images coming on the topic ``sensor_msgs/Image`` to messages that ``OpenCV`` can open and display them.

Introducing the OpenCV
======================

OpenCV is a popular open source computer vision library. We will use this library to view images and stream from the turtlbot robot so it can follow a line on the ground. In order to do that we will need to see the line, define the centre of this line and finally move the robot to follow the robot.
Messages from the camera are published on the ``the sensor_msgs/Image`` topic so we will need to write a node that subscribe to the same topic.

Open any text editor you like and type the following in a file called ``follower.py``:

.. code-block:: python

	#!/usr/bin/env python
	import rospy
	from sensor_msgs.msg import Image

	def image_callback(msg):
		pass

	rospy.init_node('follower')
	image_sub = rospy.Subscriber('camera/rgb/image_raw', Image, image_callback)
	rospy.spin()

This a very simple subscriber node that does nothing. 
Run the following commands:

.. code-block:: bash
	
	roscore
Start up your Gazebo simulator:

.. code-block:: bash

	roslaunch turtlebot_gazebo turtlebot_world.launch

then type this command to see all the topics published so far.

.. code-block:: bash

	rostopic list 

You will see something like the following.

.. image:: images/rostopic_list.png
	:align: center
We are only interested about the ``camera`` topics.

Now run your python script:

.. code-block:: bash

	python your_path/follower.py

To be able to make sure that it is working run the following command:

.. code-block:: bash

	rosnode list

This will give you a list of all the active nodes on your ROS environment and you will find your ``follower`` node between them.

Now you need to create a ``python`` script to view the images from the turtlebot. Save the following ``python`` script in a file called ``follower_opencv.py`` :

.. code-block:: python
	
	#!/usr/bin/env python

	#This script uses the cv_bridge package to convert images coming on the topic
	#sensor_msgs/Image to OpenCV messages and display them on the screen

	import rospy
	from sensor_msgs.msg import Image
	import cv2, cv_bridge
	class Follower:
		def __init__(self):
			self.bridge = cv_bridge.CvBridge()
			cv2.namedWindow("window", 1)
			self.image_sub = rospy.Subscriber('camera/rgb/image_raw',
			Image, self.image_callback)
	
		def image_callback(self, msg):
			image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
			cv2.imshow("window", image)
			cv2.waitKey(3)
	rospy.init_node('follower')
	follower = Follower()
	rospy.spin()

Run the ``python`` script after saving the changes. You will be able to see an image of whatever infront of the robot.



