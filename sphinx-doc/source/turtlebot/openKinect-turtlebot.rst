.. _openKinect-turtlebot:

=============================
ROS OpenKinect with Turtlebot
=============================

In this tutorial you will learn how to configure your turtlebot robot to display image from Microsoft Kinect. 

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials, your network set-up is working fine between the ROS Master node and the host node.

Installing ROS OpenNI and OpenKinect Drivers 
============================================

You need to download the ROS OpenNI and OpenKinect drivers by running the following commands:

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