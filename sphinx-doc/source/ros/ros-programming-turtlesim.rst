
.. _ros-programming-turtlesim:
==============================
Turtlesim Cleaning Application
==============================

In this tutorial, you will learn more advanced concepts on ROS by developing a first application on ROS using the Turtlesim simulator.
The objective of the application is to emulate a cleaning application like Vaccum cleaning robots (e.g. Roomba). 
The robot should cover the whole area to be cleaned. 
For this, we will develop, step-by-step, several functions to make the robot move straight and rotate and use these functions in developing the cleaning application.
You can then extend this application to make it even smarter and more comprehensive.  

The code of this tutorial is available in ``src/turtlesim/cleaning_app/robot_cleaner.cpp`` of ``gaitech_doc`` package.


.. warning:: 
   It is assumed that you already know the main concepts on ROS including ROS topics, ROS nodes, ROS messages and ROS services. 
   If not, you need to first take the first tutorials on :ref:`ROS Background <ros-bakground>` and :ref:`ROS Programming Basics <ros-programming>`. 
 

.. NOTE:: The following tutorial aims at introducing necessary and fundamental concepts of ROS beyond the simple talker/listener tutorial, like navigation, motion control, distance estimation, rotated angle estimation, and some ROS packages including TF. 
   This tutorial consists of a series of fives videos that you need to watch in order to get the main lessons and outcomes. 
   The tutorial could be completed in 2 to 4 hours. 
   
.. Warning:: It would be appreciated if you already have some background knowledge on introductory robotics courses. As pre-requisite, you should already know what a 2D/3D frame is, and what a transformation between frame is, in addition to basic knowledge on 2D kinematics.  

Lecture 1: Introducing the Cleaning Application
===============================================
In this video, you will:

   * understand the objectives and tasks of the turtlesim cleaning applications
   * recognize the different functions to be developed for the clearning application 

.. youtube:: qtVDso-iBNA

 

Lecture 2: Moving in a Straight Line
====================================
In this video, you will:

   * develop a function to make the robot move in a straight line forward and backward
   * understand how to choose the right ROS topic to publish a message for a certain functionality
   * use the Twist message to send linear velocity commands to move in straight line
   * control the distance traveled by the robot

.. youtube:: PGZMlzBlMmw

 

Lecture 3: Rotating Left and Right
==================================
In this video, you will learn:

   * understand rotation conventional assumptions
   * develop a function to make the robot rotate left and right
   * use the Twist message to send angular velocity commands to rotate
   * set the desired orientation of the robot after rotation
   * develop and use some basic functions related to rotation
   
.. youtube:: Ddqwq2WXFEk
   
 

Lecture 4: Go to Goal Location (PID Controller)
===============================================
In this video, you will:

   * understand the essential of PID controllers
   * develop a PID controller to make the robot head towards a specified location
   
For a good introduction on PID controllers for mobile robots, it is recommended to watch Lecture 1 and Lecture of the online course on `Control of Mobile Robots, provided by Georgia Institute of Technology <https://www.youtube.com/watch?v=KZEWLZJwYNc&list=PLciAw3uhNCiD3dkLTPJgHoMnsu8XgCt1m>`_.

.. youtube:: Qh15Nol5htM


Lecture 5: Grid and Spiral Cleaning Application
===============================================
In this video, you will:

   * use the move and rotate functions to develop the clearning applications and area coverage
   * develop a new function to make the robot cover the area in spiral form 

.. youtube:: ehH8oLfsz-w

Review Questions
================
   * What are the steps followed to develop the cleaning application?
   * Explain how the Twist message is used to make the robot move stright and rotate?
   * What is the equation used to make the robot move in spiral form? How this implemented in ROS?
   * What is the drawback of method used to control the traveled distance and rotated angle? Explain and justify your claim.  
   

Do-It-Yourself
==============
You are requested to extend the cleaning application by making it smarter. 
We want to program the robot such that it moves 1 meter, then rotates 360 degrees in place, and repeat the process until the area is cleaned. 
You need to use a loop to control the robot motion until the end of the mission. 





