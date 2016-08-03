
.. _ar-parrot-2-ros:

===============================
Work with AR Parrot 2 using ROS
===============================


In this tutorial you will learn how to work with AR Parrot 2 using in ROS. 

.. NOTE::
	This tutorial tested on ROS indigo under Ubuntu 14.04 LTS.

Required Packages
=================

Install and compile following package:

	* `ardrone_autonomy <http://wiki.ros.org/ardrone_autonomy>`_ is the ROS driver for Parrot AR­Drone 1.0 and 2.0.

Working with real drone
=======================

Create new package (e.g. ``drone_application``)

.. code-block:: bash

	catkin_create_pkg drone_application std_msgs rospy roscpp

create a launch file (e.g: ``launch_drone.launch``) and paste following lines:

.. code-block:: bash
	
	<launch>
 		<arg name="droneip" default="192.168.1.1" />
 		<node name="ardrone_driver" pkg="ardrone_autonomy" type="ardrone_driver" output="screen" args="-ip $(arg droneip)">
   			<param name="navdata_demo" value="False" />
   			<param name="realtime_navdata" value="True" />
   			<param name="realtime_video" value="True" />
   			<param name="looprate" value="30" />
 		</node>
	</launch>

Now launch the robot, in terminal:

.. code-block:: bash
	
	roslaunch drone_application launch_drone.launch

This message will appear if it works fine

.. code-block:: bash
	
	[ INFO] [1456020168.671768680]: Successfully connected to 'My ARDrone' (AR-Drone 2.0 - Firmware: 2.4.8) - Battery(%): 85

.. image:: images/Real_drone_1.png
	:align: center

You can view the robot camera using following command:

.. code-block:: bash
	
	rosrun image_view image_view image:=/ardrone/image_raw

.. image:: images/2a.png
	:align: center

In new terminal you can control the robot by sending messages through topics, for example:
	* To takeoff:

		.. code-block:: bash

			rostopic pub -1 ardrone/takeoff std_msgs/Empty

	* To land:

		.. code-block:: bash

			rostopic pub -1 ardrone/land std_msgs/Empty

Control the robot from your code in python
==========================================

To write simple code to takeoff, create your .py file (e.g: ``takeoff.py``) and paste following code:

.. code-block:: python

	#!/usr/bin/env python 
	import rospy 
	from std_msgs.msg import String 
	from std_msgs.msg import Empty 

	def takeoff(): 
   		pub = rospy.Publisher("ardrone/takeoff", Empty, queue_size=10 ) 
   		rospy.init_node('takeoff', anonymous=True) 
   		rate = rospy.Rate(10) # 10hz 
   		while not rospy.is_shutdown(): 
       		  pub.publish(Empty()) 
       		  rate.sleep() 

	if __name__ == '__main__': 
   		try: 
       		  takeoff() 
   		except rospy.ROSInterruptException: 
       		  pass

Launch the drone

.. code-block:: bash

	roslaunch drone_application launch_drone.launch

Run you code in new terminal:

.. code-block:: bash
	
	rosrun drone_application takeoff.py

Control the robot using tum_ardrone package
===========================================

Create a launch file (e.g: ``launch_tum_drone.launch``) and paste following lines:	

.. code-block:: bash

	<launch>

 		<arg name="droneip" default="192.168.1.1" />
 		<node name="ardrone_driver" pkg="ardrone_autonomy" type="ardrone_driver" output="screen" args="-ip $(arg droneip)">
   			<param name="navdata_demo" value="False" />
   			<param name="realtime_navdata" value="True" />
   			<param name="realtime_video" value="True" />
   			<param name="looprate" value="30" />
 		</node>

 		<node name="drone_stateestimation" pkg="tum_ardrone" type="drone_stateestimation">
 		</node>
 		<node name="drone_autopilot" pkg="tum_ardrone" type="drone_autopilot">
 		</node>
 		<node name="drone_gui" pkg="tum_ardrone" type="drone_gui">
 		</node>

	</launch>

In terminal:

.. code-block:: bash

	roslaunch drone_application tum_drone.launch

.. image:: images/Tum_drone_launch.png
	:align: center

It is straightforward using ``tum_ardrone_GUI`` to command the robot

.. image:: images/Tum_ardrone_GUI.png
	:align: center

.. NOTE:: 

	For more information you can visit `AR.Drone ROS Documentation <http://ardrone-autonomy.readthedocs.io/en/latest/installation.html>`_ , `ROS Driver for AR.Drone <https://github.com/AutonomyLab/ardrone_autonomy>`_ and `Up and flying with the AR.Drone and ROS: Getting started <http://robohub.org/up-and-flying-with-the-ar-drone-and-ros-getting-started/>`_