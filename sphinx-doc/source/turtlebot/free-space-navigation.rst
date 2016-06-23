.. _free-space-navigation:

================================
Turtlebot free movement in Space
================================

This tutorial will introduce how to control your turtlebot robot using `Python` and `C++` code to move in a specific path you deside in your code. We chose to make the robot move in a square path but you can extend the code and write your own path.

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials and your network set-up is working fine between the ROS Master node and the host node.

.. NOTE::

   In this tutorial you will learn how to:

      * Teleoprate a real and simulated turtlebot
      * Create a custom path for the turtlebot to move in  

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