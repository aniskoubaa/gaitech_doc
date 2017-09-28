.. _roslink-dronemap:

=======================================
Configure ROSLink with Dronemap Planner
=======================================

.. NOTE::

   In this tutorial you will learn:

      * Parameter Configuration of ROSLink Bridge
      * Run the ROSLink Bridge
   
   For any query, please feel free to post your questions in the `Gaitech EDU Forum <http://forum.gaitech.hk/>`_

ROSLink Bridge
==============

The ROSLink Bridge consists of fully-functional ROS script written in Python, which is executed as ROS node in the client. For more details about ROSLink Bridge see :ref:`roslink-gapter`.


ROSLink Configuration
=====================
The first step is to configure ROSLink parameters and the periods of updating the ROSLink messages:

open the file ``roslink/launch/gapter_roslink.launch``

.. code-block:: bash 

 <launch>
  <node pkg="roslink" name="udp_client_gapter_node" type="roslink_bridge_gapter.py" output="screen"/>

  <param name="ground_station_ip" value='192.168.100.6' />
  <param name="ground_station_port" value='25500' />

  <param name="heartbeat_msg_period" value="1" />
  <param name="robot_status_msg_period" value="0.5" />
  <param name="global_motion_msg_period" value="0.5" />
  <param name="gps_raw_info_msg_period" value="0.5" />
  <param name="range_finder_data_msg_period" value="0.5" />

  <param name="roslink_version" value="1" />
  <param name="ros_version" value="8" />
  <param name="system_id" value='12' />
  <param name="robot_name" value="Gapter Drone" />
  <param name="type" value="0" />
  <param name="owner_id" value="3" />
  <param name="key" value="1243-0000-0000-FGFG" />
 </launch>

The user can set these values as appropriate for the application.


``ground_station_ip`` to identify the IP address of your server machine, replace it with the correct IP addrees of the Dronemap Planner. Refer to :ref:`this page <dronemap-configuration>` to know how to configure Dronemap Planner .

``ground_station_port`` to identify the port number. 25500 is the port of the Datagram Socket Server on Dronemap Planner

``heartbeat_msg_period`` specify the period for heartbeat message.

``robot_status_msg_period`` specify the period for the robot status message.

``global_motion_msg_period`` specify the period for the global motion message.

``gps_raw_info_msg_period`` specify the period for the GPS indo message.

``range_finder_data_msg_period`` specify the period for the range finder message.

``system_id`` to specify specifies the ID of the robot. It helps in differentiating robots from each other at the server side.

``key`` field is used to identify a robot, and to map it to a user. A user that would like to have access to a robot, must use the same key that the robot is using in its Heartbeat message.


Run Dronemap planner cloud
==========================
Follow the tutorial in :ref:`this page <dronemap-configuration>` to run Dronemap planner cloud

Run ROSLink
===========
After setting all the parameter, now you can launch Gapter simulator as explained in: :ref:`gapter-setup-simulation` by first run the following commands:

.. code-block:: bash  

	 $ cd ~/gapter_ardupilot/ArduCopter

	 $ ../Tools/autotest/sim_vehicle.sh -j 4 -f Gazebo

.. figure:: images/roslink_sim_vehicle_gazebo.png
    :align: center
    :width: 600pt

Then in another terminal lauch following:

.. code-block:: bash  

	$ roslaunch ardupilot_sitl_gazebo_plugin gapter_spawn.launch

.. figure:: images/roslink_gapter_spawn.png
    :align: center
    :width: 600pt

Gazebo window will opened now and you should see Gapter model.

.. figure:: images/roslink_gapter_sim.png
    :align: center
    :width: 600pt

Now launch you roslink bridge

.. code-block:: bash  

  $ roslaunch roslink gapter_roslink.launch

You will see something like the following in the terminal:

.. figure:: images/roslink_start_bridge.png
    :align: center
    :width: 600pt

Start Webapp
============

1- Run your web servers app (xampp or wamp)

2- open your brower and enter the link of the dronmemap planner main website.

.. figure:: images/roslink_robots.png
    :align: center
    :width: 600pt

To be able to control Gapter, click on |link| button.

.. |link| image:: images/roslink_link.png 
		:width: 30pt


.. figure:: images/roslink_control.png
    :align: center
    :width: 600pt
