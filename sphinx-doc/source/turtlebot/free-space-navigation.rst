.. _free-space-navigation:

===============================
Turtlebot Free Space Navigation
===============================

This tutorial is the first lesson in the series of robot navigation. We consider the case of an open space with no obstacles. 
The objective of this tutorial is to learn how to make the Turtlebot robot move using ROS. You will mainly learn how to publish a velocity message to make the robot move for a certain distance, or rotate for a certain angle. 
For this, you will create the functions ``move`` and ``rotate`` using different techniques. 
In particular, you will learn how to use ``TF`` package to estimate the distance traveled by the robot and the angle rotated by the robot using frame transformations. 

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials and your network set-up is working fine between the ROS Master node and the host node.

.. NOTE::

   In this tutorial you will learn how to:

      * Make the robot navigate in an open obstcale-free space
      * Develop functions to make the robot move straight for a certain distance
      * Develop functions to make the robot rotate for a certain angle. 
      * use ``TF`` package to estimate the traveled distance and the rotated angle by a robot

Background
==========
The objective is to develop functions to make the robot moves in an open space in straight line for a certain distance, and rotate left or right for certain angle. 
In the previous tutorial using the Turtlesim, we used the simple equation 



C++ and Python Code for the square path
=======================================

You can find the whole ``cpp`` and ``python`` files in our `GitHub repository <https://github.com/aniskoubaa/gaitech_doc>`_ in the following `path <https://github.com/aniskoubaa/gaitech_doc/tree/master/src/turtlebot/navigation/free_space_navigation>`_. Go to `scripts` to find the ``python`` code.

In the code you will find 3 `move` methods and each one of them has its approach so you will be able to know 3 different ways of controlling and manipulating the turtlebot robot . The code is also well explained so you can easily understand what each line is doing in the code and what is its functionality.	

After downloading the repository make sure you place it in your ``catkin_ws/src`` then run the following command:

.. code-block:: bash
	
	catkin_make

.. NOTE::
	
	You may find a couple of errors due to your need to install missing packages.

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

or launch the ``free_space_navigation_stage.launch`` file to launch both simulators and the ``cpp`` node.

.. image:: images/stage-square-move-cpp.png
	:align: center


You can also choose to run the ``python`` script by running this command:

.. code-block:: bash
	
	python your_workspace/src/gaitech_doc/src/turtlebot/navigation/free_space_navigation/script/free_space_navigation.py

.. image:: images/stage-square-move-python.png
	:align: center

.. NOTE::
	
	You can try the three ``move`` methods by calling each one of them in the ``moveSquare`` method.
	You can try the same codes with `Gazebo` simulator but you need to have a fast PC. All you have to do is to launch `Gazebo` by typing the following command:
	
	.. code-block:: bash
	
		roslaunch turtlebot_gazebo turtlebot_world.launch

	Then run either one of the files as mentioned above. 	



.. youtube:: SHPCyqFDr1Q