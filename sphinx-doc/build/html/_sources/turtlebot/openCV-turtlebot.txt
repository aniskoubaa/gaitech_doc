.. _openCV-turtlebot:

=========================
ROS OpenCV with Turtlebot
=========================

In this tutorial you will learn how to configure your turtlebot robot with OpenCV to stream videos from Microsoft Kinect. 

.. WARNING::
    * Make sure that you completed installing all the required packages in the previous tutorials, your network set-up is working fine between the ROS Master node and the host node.
    * Make sure to complete the ROS OpenKinect with Turtlebot tutorial. 

Installing OpenCV packages
==========================

You need to download the OpenCV packages by running the following commands:

.. code-block:: bash

	sudo apt-get install ros-indigo-vision-opencv libopencv-dev \ python-opencv
	rospack profile

After installation type this command to make sure that you have successfully installed the packages:

.. code-block:: bash
	
	$ python
	>>> from cv2 import cv
	>>> quit()

You can type the following command to make sure that the OpenCV Python library is installed in its proper location:

.. code-block:: bash

	locate cv2.so | grep python

You will get an output like this:

.. image:: images/openCV-python.png
	:align: center 

Transform Image from ROS to OpenCV
==================================

In this section you will learn how to recieve and transform images from ROS and transform them to OpenCV.

.. NOTE::
	Make sure that you downloaded the ``gaitech_doc`` package from our GitHub `repository <https://github.com/aniskoubaa/gaitech_doc>`_

You will find a launch file called ``turtlebot_openCV`` in the following path ``gaitech_doc/src/turtlebot/openCV/launch/turtlebot_openCV.launch`` , run the file in a terminal:

.. code-block:: bash
	
	roslaunch gaitech_doc turtlebot_openCV.launch

.. NOTE::

	Make sure that your camera driver is running.
	
	.. code-block:: bash
	
		roslaunch freenect_launch freenect.launch

After a short time you will see	some thing like this:

.. image:: images/openCV.png
	:align: center

To understand the whole process of transformation you can open the ``python`` script in the following path ``gaitech_doc/src/turtlebot/openCV/scripts/turtlebot_openCV.py`` , the file is well documented so you will be able to understand everything written inside the code.

.. NOTE::
	This code is originally from the ``cv_bridge_opencv.py`` file in the ``rbx1_vision`` package but with some other modifications.