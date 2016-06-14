.. _build-map:

================================
Building a Map using Logged Data
================================

In this tutorial you will learn how to build your own map using logged transform and laser scan data. 

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials, your network set-up is working fine between the ROS Master node and the host node.

Building your Map
=================    

If you are working from source checkout, run this command:

.. code-block:: linux
	
	rosmake gmapping

Download an bag to be able to test with:

.. code-block:: linux
	
	wget http://pr.willowgarage.com/data/gmapping/basic_localization_stage.bag

Bring up your ROS master node:

.. code-block:: linux
	
	roscore

.. NOTE:: 
	Before running any nodes, make sure that the ``use_sim_time`` parameter is set to true which is responsible for the ``/clock`` topic which represent the `simulation time`:

	.. code-block:: linux

		rosparam set use_sim_time true

Bring up ``slam_gmapping`` to be able to take in laser scans and produce a map:

.. code-block:: linux
	
	rosrun gmapping slam_gmapping scan:=base_scan

.. NOTE:: 
	This step may take a couple of minutes.

To feed the data to ``slam_gmapping`` you need to run in a new terminal:

.. code-block:: linux
	
	rosbag play --clock <name_of_the_bag_that_you_downloaded>

After ``rosbag`` finishes save and exit using the ``map_saver`` from the ``map_server`` package:

.. code-block:: linux
	
	rosrun map_server map_saver

After this step you have a working map in a ``map.pgm`` file that you can view in any image viewer.


