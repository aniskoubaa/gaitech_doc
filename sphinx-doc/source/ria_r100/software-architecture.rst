
.. _ria-r100-software-architecture:

=====================
Software Architecture
=====================

RIA-R100 PC has been set with Ubuntu 14.04 and ROS-Indigo running on it. All the required libraries and software packages has been configured completely to work RIA. source files have been provided at catkin_ws folder in home directory. It’s easy to add required packages into this folder and compiling them. Make sure base folder remains same. Altering contents in this folder may lose required parameters controlling RIA motors.
	

All packages required to use RIA is configured at RIA folder and rest which are required to use after integrating sensors are kept outside RIA folder. Additional packages are suggested to keep outside RIA folder which helps to backup and segregate easily when required.


Following are launch files and their description

.. code-block:: bash

	roslaunch ria_bringup minimal.launch

This will launch RIA base controller, IMU and joystick to control RIA base. This will be launched automatically when RIA is turned on. So that you can directly control robot once turned on. No file required to be launched.

.. code-block:: bash

	roslaunch ria_bringup sensors.launch

This will launch RIA sensors (RGBD and LIDAR)

.. code-block:: bash

	roslaunch ria_navigation slam_gmapping.launch/slam_hector.launch

It is used to create map using lidar data. It has two variants gmapping and hector slam. you can use either one. To create complete map robot has to be moved using joystick teleop.

.. code-block:: bash

	roslaunch ria_navigation move_base.launch

It launches move_base files which are configured according to RIA physical properties which navigates RIA autonomously by avoiding obstacles.

.. code-block:: bash

	roslaunch ria_description description_base/description_complete.launch

This launches RIA URDF model which gives graphical view of RIA and camera view during navigation. Another launch file view.launch file need to be launch to view this file in rviz.
