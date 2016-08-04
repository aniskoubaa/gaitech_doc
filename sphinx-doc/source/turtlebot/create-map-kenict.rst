
.. _create-map-kenict:

===============================
Building a Map with a Turtlebot
===============================

In this tutorial, you will learn how to build your own map using Kinect sensor attached to your turtlebot. 

.. WARNING::
    Make sure that you already made the tutorial on :ref:`openKinect-turtlebot`.

As mentioned in :ref:`openKinect-turtlebot`, ROS indigo supports by default ``Asus Live Pro`` 3D sensor and has no default support to ``Kinect`` 3D sensor. 
If you use ``Asus Live Pro`` 3D sensor, then skip the Kinect 3D sensor configuration step below. 

Kinect 3D sensor configuration
==============================

In order to connect the ``Kinect`` sensor with the ROS Indigo environment, you can type the following three commands in your ``.bashrc`` file:

.. code-block:: bash

	export TURTLEBOT_3D_SENSOR=kinect
	export TURTLEBOT_BASE=kobuki
	export TURTLEBOT_STACKS=hexagons

Then save, exit and close the terminal.
Open a new terminal. 

Start Mapping ROS Nodes
=======================

On the master node (the robot machine) run the following commands:

.. code-block:: bash
	
	roscore
	roslaunch turtlebot_bringup minimal.launch
	roslaunch turtlebot_navigation gmapping_demo.launch

On your workstation (the host node), run the following commands:

.. WARNING::
    If you execute the following command on your workstation (recommended), you must make sure to have correctly set-up the network configuration as explained in :ref:`network-config-doc`.


.. code-block:: bash

	roslaunch turtlebot_rviz_launchers view_navigation.launch
	roslaunch turtlebot_teleop keyboard_teleop.launch

.. TIP::
	OR connect to the Master node using the ``ssh turtlebot_PC_name@TURTLEBOT_IP`` command before running any command in every terminal you use and run all the previous commands, except for the ``RViz`` command run it in a normal terminal(without using ``ssh``).

Start moving the robot around using ``keyboard teleop`` application or a joytsick and watch the RViz simulator as the map starts to be built-up. 

Finally you will end-up with a map looking like this one:

.. image:: images/kenict_map.png
    :align: center

You can save the map you just created by running the following command:

.. code-block:: bash
	
	rosrun map_server map_saver -f /tmp/my_map

.. NOTE::
	The ``tmp`` file gets cleaned everytime the system is booted so after saving the map you can move the files to another location or save it in another location directly.

The previous command will generate two file in the name you specify so in this case the two file's names are ``my_map.pgm`` and ``my_map.yaml``. 
If you opened the ``.yaml`` file you will see something like this:

.. code-block:: yaml

	image: /tmp/my_map.pgm
	resolution: 0.050000
	origin: [-12.200000, -12.200000, 0.000000]
	negate: 0
	occupied_thresh: 0.65
	free_thresh: 0.196

Everyline specify a certain information from the map's file which is the ``.pgm`` file, the resolution of the map, the starting location of the turtlebot robot to how much space does the obstacles/free space occupy from the map.

The ``.pgm`` is just an image of the map which you can open using any image editor program and it will look like this:

.. image:: images/pgm_map.png
	:align: center 

Video Demonstration
===================
.. youtube:: QzZif1e767k