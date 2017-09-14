.. _roslink-dronemap:

=======================================
Configure ROSLink with Dronemap Planner
=======================================

ROSLink Bridge
==============

The ROSLink Bridge consists of fully-functional ROS script written in Python, which is executed as ROS node in the client. For more details about ROSLink Bridge see :ref:`roslink-gapter`.


ROSLink Configuration
=====================
1. configure periods of updating the ROSLink messages:

open the file ``roslink/configuration/ROSLINK_MESSAGE_PERIOD.py``

This file contains period of every message in seconds:

.. code-block:: Python

	ROSLINK_HEARTBEAT_MESSAGE_RATE = 1
	ROSLINK_ROBOT_STATUS_MESSAGE_RATE = 0.5
	ROSLINK_GLOBAL_MOTION_MESSAGE_RATE = 0.5
	ROSLINK_GPS_RAW_INFO_MESSAGE_RATE = 0.5
	ROSLINK_RANGE_FINDER_DATA_MESSAGE_RATE = 0.5

The user can set these values as appropriate for the application.

``ROSLINK_HEARTBEAT_MESSAGE_RATE`` specify the period for heartbeat message.
``ROSLINK_ROBOT_STATUS_MESSAGE_RATE`` specify the period for the robot status message
``ROSLINK_GLOBAL_MOTION_MESSAGE_RATE`` specify the period for the global motion message
``ROSLINK_GPS_RAW_INFO_MESSAGE_RATE`` specify the period for the GPS indo message
``ROSLINK_RANGE_FINDER_DATA_MESSAGE_RATE`` specify the period for the range finder message

2. configure ROSLink parameters

open the file ``roslink/launch/gapter_roslink.launch``

.. code-block:: bash 

 <launch>
  <node pkg="roslink" name="udp_client_gapter_node" type="roslink_bridge_gapter.py" output="screen"/>
  <param name="ground_station_ip" value='192.168.100.6' />
  <param name="ground_station_port" value='25500' />
  <param name="roslink_version" value="1" />
  <param name="ros_version" value="8" />
  <param name="system_id" value='12' />
  <param name="robot_name" value="Gapter Drone" />
  <param name="type" value="0" />
  <param name="owner_id" value="3" />
  <param name="key" value="1243-0000-0000-FGFG" />
 </launch>

``ground_station_ip`` to identify the IP address of your server machine, replace it with the correct IP addrees of the Dronemap Planner. Refer to :ref:`this page <dronemap-configuration>` to know how to configure Dronemap Planner .

``ground_station_port`` to identify the port number. 25500 is the port of the Datagram Socket Server on Dronemap Planner

``system_id`` to specify specifies the ID of the robot. It helps in differentiating robots from each other at the server side.

``key`` field is used to identify a robot, and to map it to a user. A user that would like to have access to a robot, must use the same key that the robot is using in its Heartbeat message.


Run Dronemap planner cloud
==========================
Follow the tutorial in :ref:`this page <dronemap-configuration>` to run Dronemap planner cloud

Run ROSLink
===========
After setting all the parameter, now you can launch Gapter simulator as explained in: :ref:`gapter-setup-simulation`

Then launch you roslink bridge

.. code-block:: bash  

  $ roslaunch roslink gapter_roslink.launch

Start Webapp
============

1- Run your web servers app (xampp or wamp)

2- open your brower and enter the link of the dronmemap planner main website.
