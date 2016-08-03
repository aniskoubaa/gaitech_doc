
.. _openKinect-turtlebot:

======================================
Setting-up 3D Sensor for the Turtlebot
======================================

In this tutorial you will learn how to configure your turtlebot robot to display image from 3D sensor, including Asus Live Pro camera and Kinect Camera.
Prio to ROS Indigo, the Turtlebot ROS package provided a default support for Kinect camera. 
However, for ROS Indigo and later versions, Turtlebot package provides a default support for Asus Live Pro 3D sensor, 
and it requires some additional configuration to work with Kinect. 
In this tutorial, we will introduce how to set-up and test both sensors for ROS Indigo and later versions. 

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials, your network set-up is working fine between the ROS Master node and the host node.


.. NOTE::

   In this tutorial you will learn how to:

      * Set-up, configure and test Asus Live Pro 3D sensor for a Turtlebot
      * Set-up, configure and test Kinect sensor for a Turtlebot
       

Asus Live Pro 3D Sensor
=======================
Present the following
   * explain that this is the default sensor
   * show a picture of it
   * installation process
   * what are the configuration needed of environment variable to start Turtlebot with Kinect for Indigo and later versions
   * the location of the openni package
   * explain the 3dsensor.launch file in the turtlebot_bringup package
   * how to run with some screen shorts 
   * Illustrate the above execution with a small video demo


Kinect 3D Sensor
================
Present the following
   * explain that this is the default sensor
   * show a picture of it
   * installation process
   * the location of the openni package
   * explain the 3dsensor.launch file in the turtlebot_bringup package
   * how to run with some screen shorts  
   * Illustrate the above execution with a small video demo


By default, ROS indigo supports ``Asus Live Pro`` 3D sensor and has no default support to ``Kinect`` 3D sensor. 
If you use ``Asus Live Pro`` 3D sensor, then skip the Kinect configuration step below. 

Kinect 3D sensor configuration
------------------------------
In order to connect the ``Kinect`` sensor with the ROS Indigo environment, you can type the following three commands in your ``.bashrc`` file:

.. code-block:: bash

   export TURTLEBOT_3D_SENSOR=kinect
   export TURTLEBOT_BASE=kobuki
   export TURTLEBOT_STACKS=hexagons

Then save, exit and close the terminal.
Open a new terminal. 

Installing ROS OpenNI and OpenKinect Drivers
--------------------------------------------

First, you need to download the ROS OpenNI and OpenKinect drivers by running the following commands:

.. code-block:: bash

	sudo apt-get install ros-indigo-openni-* ros-indigo-openni2-* \ ros-indigo-freenect-*
	rospack profile

Now you can test your camera. Type the following command:

.. code-block:: bash
	
	roslaunch freenect_launch freenect.launch


You should see these lines in the terminal:

.. code-block:: bash
	
	process[camera/camera_nodelet_manager-1]: started with pid [18070]
	[INFO] [1420555647.969035762]: Initializing nodelet with 4 worker
	threads.
	process[camera/driver-2]: started with pid [18078]
	Warning: USB events thread - failed to set priority. This might cause
	loss of data...
	process[camera/rectify_color-3]: started with pid [18112]
	process[camera/depth_rectify_depth-4]: started with pid [18126]
	etc.

.. NOTE::
	Do not worry about the warning appearing in the terminal after running the previous command.

Testing Your Kinect Camera
==========================

After running the previous command you can now run this command to know all the topics published by the camera:

.. code-block:: bash

	rostopic list

The following examples are to demonstrate the difference between a couple of topics:

	* To test the RGB image from camera type the following command: 

	.. code-block:: bash

		rosrun image_view image_view image:=/camera/rgb/image_raw

	You will see something like this:

	.. image:: images/camera-rgb.png
    	 :align: center


	* To test the Mono image from camera type the following command: 

	.. code-block:: bash

		rosrun image_view image_view image:=/camera/rgb/image_rect_mono

	You will see something like this:

	.. image:: images/camera-mono.png
         :align: center


	* To test the depth image from camera type the following command: 

	.. code-block:: bash

		rosrun image_view image_view image:=/camera/depth/image_rect

	You will see something like this:

	.. image:: images/camera-depth.png
         :align: center

    .. NOTE::
    	The darker the object is the closer it is to the turtlebot.