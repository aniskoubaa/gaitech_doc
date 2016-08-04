
.. _openKinect-turtlebot:

======================================
Setting-up 3D Sensor for the Turtlebot
======================================

In this tutorial you will learn how to configure your turtlebot robot to display image from 3D sensor, including Asus Xtion Pro Live camera and Kinect Camera.
Prio to ROS Indigo, the Turtlebot ROS package provided a default support for Kinect camera. 
However, for ROS Indigo and later versions, Turtlebot package provides a default support for Asus Xtion Pro Live 3D sensor, 
and it requires some additional configuration to work with Kinect. 
In this tutorial, we will introduce how to set-up and test both sensors for ROS Indigo and later versions. 

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials, your network set-up is working fine between the ROS Master node and the host node.


.. NOTE::

   In this tutorial you will learn how to:

      * Set-up, configure and test Asus Xtion Pro Live 3D sensor for a Turtlebot
      * Set-up, configure and test Kinect Xbox 360 sensor for a Turtlebot
       

Asus Xtion Pro Live 3D Sensor
=============================

The default sensor that is used with ROS Indigo is the Asus Xtion Pro Live 3D sensor. The image below is for the Asus sensor.

.. image:: images/asus_camera.png
	:align: center

To use this sensor with the turtlebot robot you will have to add the following lines in the ``.bashrc`` script file:

.. code-block:: bash

	export TURTLEBOT_BASE=create
	export TURTLEBOT_STACKS=circles
	export TURTLEBOT_3D_SENSOR=asus_xtion_pro

Installing the Openni Package
-----------------------------

If you are going to use the Asus sensor then you will need to install the ``oppeni`` package, so run the following command:

.. code-block:: bash

	sudo apt-get install ros-indigo-openni-* ros-indigo-openni2-*

Both the packages will be installed in the same folder and you can find this file in the following path ``/opt/ros/indigo/share/openni2_camera`` and ``/opt/ros/indigo/share/openni_camera``. You will find more ``oppeni`` folders which also belongs to the same package.

Explanning the 3dsensor.launch File
-----------------------------------

You will find the file by typing the following commands:

.. code-block:: bash

	roscd turtlebot_bringup/launch/
	sudo gedit 3dsensor.launch

The code is well explained but we will have a look at the following point in the code. 
In line number 21 :

.. code-block:: xml

	<arg name="3d_sensor"   default="$(env TURTLEBOT_3D_SENSOR)"/>  <!-- kinect, asus_xtion_pro -->

The ``TURTLEBOT_3D_SENSOR`` variable is set in the previous steps in the ``.bashrc`` file according your sensor type. And the same variable will affect more variables' initialization afterwards in the same ``.launch`` file.


Testing the Asus Sensor
-----------------------

After all the installation steps you can test your environment by typing the following commands:

.. code-block:: bash

	roslaunch turtlebot_bringup 3dsensor.launch
	roslaunch turtlebot_rviz_launchers view_robot.launch

After launching the ``RViz`` simulator press on the `Image` icon on the left list and you would be able to see something like this:

.. image:: images/rviz_camera.png
	:align: center




Kinect 3D Sensor
================

By default, ROS indigo supports ``Asus Live Pro`` 3D sensor and has no default support to ``Kinect`` 3D sensor. 
If you use ``Asus Live Pro`` 3D sensor, then skip the Kinect configuration step below. 
The following image is for the ``Kinect`` 3D sensor:

.. image:: images/kinect_camera.jpg
	:align: center 

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
--------------------------

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