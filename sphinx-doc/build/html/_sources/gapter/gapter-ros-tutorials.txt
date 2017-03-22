
.. _gapter-ros-tutorials:

=====================
GAPTER: ROS Tutorials
=====================


.. toctree::
   :hidden:
   
   MAVROS Basics <mavros-basics.rst>
   Teleoperation <gapter-ros-teleop.rst>
   Obstacle Avoidance <gapter-ros-obstacle-avoidance.rst>
   Moving in Shapes <gapter-ros-moving-in-shapes.rst>

Controlling Gapter MAVROS
=========================

In this tutorial, we will provide the main steps to follow to configure MAVROS and to control Gapter using ROS terminal commands.

Configuring Desktop with MAVROS
-------------------------------

Prerequisites: Tested on ubuntu 14.04 with ROS Indigo installed

Installing MAVROS
-----------------

* Open the terminal in your desktop and install the following

.. code-block:: bash

	user $: sudo apt-get install python-catkin-tools python-rosinstall-generator

* Create a workspace

.. code-block:: bash

	user $: mkdir -p ~/catkin_ws/src
	user $: cd ~/catkin_ws
	/catkin_ws $: catkin init
	/catkin_ws $: wstool init src

* Get source (upstream – released)

.. code-block:: bash 

	/catkin_ws $: rosinstall_generator --upstream-development mavros | tee /tmp/mavros.rosinstall


* install latest released mavlink package

.. code-block:: bash 

	/catkin_ws $: rosinstall_generator mavlink | tee -a /tmp/mavros.rosinstall workspace & deps
	/catkin_ws $: wstool merge -t src /tmp/mavros.rosinstall
	/catkin_ws $: wstool update -t src
	/catkin_ws $: rosdep install --from-paths src --ignore-src --rosdistro indigo -y finally – build
	/catkin_ws $: catkin build

ROS Network configuration
-------------------------

Before controlling Gapter using ROS, you should first configure ROS network in your desktop.

* Open bashrc in your desktop

.. code-block:: bash 

	1. user $: sudo gedit ~/.bashrc

* Add these lines at the end

.. code-block:: bash 

	1. export ROS_HOSTNAME=192.168.x.xxx
	2. export ROS_MASTER_URI=http://192.168.1.100:11311

where ``192.168.x.xxx`` is your desktop's ip address and ``192.168.1.100`` is gapter's ip address.

For more comprehensive tutorial on Network Configuration on ROS, refer to :ref:`network-config-doc`

Controling Gapter using MAVROS
------------------------------

In this tutorial, we will control Gapter using MAVROS. 
For this you don't have to install MAVROS on your desktop, but rather on Gapter, because we control Gapter via ssh with Gapter's onboard computer (Odroid XU4). 

Follow these steps:

* First, connect to the WiFi ``gapternet`` from your desktop which will be shown in Wi-Fi list. If prompt for password type ``gaitech``

* Open the terminal and connect to Gapter's computer by typing following

.. code-block:: bash 

	user $: ssh odroid@192.168.1.100

If prompts for password, type ``gaitech``

.. NOTE::
   Before controlling Gapter, parameters need to be changed based on indoor or outdoor operation

* Now in the same terminal type following to start mavproxy ground station:

.. code-block:: bash 

	odroid $: mavproxy.py --master=/dev/ttyUSB0 --baudrate 57600 --out 192.168.x.xx:5000  --aircraft MyCopter	

You must enter your desktop's IP address in place of ``192.168.x.xx``

* You can notice heartbeat form Gapter which shows mavlink has been connected

*Type these lines in the same terminal where you can see ``MAV>`` tab on left side

*For outdoor operation*

.. code-block:: bash 

	MAV> load param /home/odroid/gapter_param/gapter_outdoor.param 

*For indoor operation*

.. code-block:: bash 

	MAV> load param /home/odroid/gapter_param/gapter_indoor.param
	
* Once parameters loaded you can stop mavlink by pressing ``ctrl+c``

* In the same terminal launch mavros to connect Gapter using mavros

.. code-block:: bash 

	odroid $ : roslaunch mavros apm2.launch gcs_url:=udp://@192.168.x.xxx:5000 fcu_url:=/dev/ttyUSB0:57600

Type your desktop ip address in place of ``192.168.x.xxx``

* Gapter should be in GUIDED mode to control it from desktop. 

* Follow these steps in a new terminal.

  * You should ssh to gapter before running following lines.
  * This is to arm Gapter

	* ``odroid $: rosrun mavros mavsafety arm``

You can see Gapter's propellers are rotating

  * Change Gapter's mode to GUIDED mode

        * ``odroid $: rosrun mavros mavsys mode -c GUIDED``

  * For takeoff  at 3 meters height from current positione

        * ``odroid $: rosrun mavros mavcm takeoffcur 0 0 3``

  * For landing Gapter 

        * ``odroid $: rosrun mavros mavsys mode -c Land``




