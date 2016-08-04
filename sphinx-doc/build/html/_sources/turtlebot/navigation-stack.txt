
.. _navigation-stack:

================
Navigation Stack
================

http://wiki.ros.org/turtlebot_navigation/Tutorials/indigo/Setup%20the%20Navigation%20Stack%20for%20TurtleBot

In this tutorial you will learn how to use the navigation stack on a robot and how to configure it on your ROS environment.

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials and your network set-up is working fine between the ROS Master node and the host node.

.. NOTE::
	The robot must be using ``tf`` to publish information about the coordination of the frames.

The idea behind Navigation Stack is to have a robot that can move in a world without crashing into obstacles,  drawing a map for this world or following a predefined map, send locations to the robot to go there and collect information about this world from the robot. For this to happen, Navigation stack collects different types of information from several topics and channels.

1. Sensor Information
=====================

The robot uses the ``sensor_msgs/LaserScan`` or ``sensor_msgs/PointCloud`` messgaes from the sensors to communicate with ROS. There are a couple of sensors that have ROS drivers to take care of this issue such as the `SCIP2.2-compliant Hokuyo Laser Devices`, `Hokuyo Model (04LX or 30LX)` and `SICK LMS2xx Lasers`.

.. NOTE::
	To understand how to publish the previous type of messages to ROS follow the ``Publishing Sensor Streams Over ROS`` tutorial [*****Reference Later*****]

2. Odometry Information
=======================

The odometry information's messages ``nav_msgs/Odometry`` are published using ``tf``. There are a couple of platforms for odometry with the supporting driviers such as `Videre Erratic` or `PR2`. 

.. NOTE::
	To understand how to publish the previous message to ROS follow the ``Publishing Odometry Information Over ROS`` tutorial [*****Reference Later*****]

3. Base Controller
==================

The navigation stack uses the ``geometry_msgs/Twist`` messages to control the velocity of the robot over the topic ``cmd_vel`` that is able to take the `vx`, `vy`, `vtheta` --> `cmd_vel.linear.x`, `cmd_vel.linear.y`, `cmd_vel.angular.z` velocities and convert them to motor commands sent to the mobile base. There are a couple of platforms for base control with the supporting driviers such as `Videre Erratic` or `PR2`.

4. World's Map
==============

As mentioned before, the navigation stack can function without having a predefined map but let's assume that you have a map.

.. NOTE::
	To understand how to build a map follow the ``How to Build a Map Using Logged Data`` tutorial [*****Reference Later*****]

Navigation Stack Hierarchy
==========================

.. image:: images/nav_stack_layout.png
    :align: center

The previous sections discribed a little bit about this hierarchy and in the following sections you will learn about the rest of them.



