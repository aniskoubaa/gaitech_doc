
.. _ria-r100-installation:

============
Installation
============

**Note:** Following steps are based on UBUNTU 14.04 with ROS-INDIGO

* This step assumes that your PC has been configured with UBUNTU 14.04 and ROS-INDIGO with all required libraries
* Following steps need to be done in host PC
* Creating Work Space:

.. code-block:: bash

	$ mkdir –p ~/catkin_ws/src
	$ cd ~/catkin_ws/src
	$ git clone https://github.com/gaitech-robotics/RIA-R100.git
	$ cd ~/catkin_ws && catkin_make
	

Network Configuration
---------------------

* Connect to RIA robot from HOST PC to its network named “RIA-R100”. If prompt for password enter ‘riaedunet’
* Configure ROS network keeping RIA-R100 as MASTER
* Open bashrc in host PC and add these lines at the end
* In a terminal:

.. code-block:: bash

	$ sudo gedit ~/.bashrc

Then add these lines at the end

.. code-block:: bash

	export ROS_MASTER_URI=http://192.168.0.2:11311
	export ROS_HOSTNAME=IP_HOSTPC

in IP_HOSTPC replace it with your PC IP address

Whenever to control robot from HOST pc it should be connected to robot’s wifi from terminal via ssh server

.. code-block:: bash

	$ sudo ssh ria@192.168.0.2

If prompt for password enter “gaitechedu”


