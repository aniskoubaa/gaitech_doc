
.. _gapter-setup-simulation:

====================================
GAPTER: Set-up GapterSim Environment
====================================



A. Prerequisites 
----------------

1. Ubuntu 14.04 LTS (Trusty Tahr)  
2. `Ros indigo`_ 

.. _Ros indigo: http://wiki.ros.org/indigo/Installation/

**Configure Ubuntu**

.. code-block:: bash

	sudo apt-get update 

.. code-block:: bash

	sudo apt-get install gawk make git curl cmake -y

**ROS dependencies and required packages:**

.. code-block:: bash

	sudo apt-get install python-rosinstall ros-indigo-octomap-msgs ros-indigo-joy ros-indigo-geodesy ros-indigo-octomap-ros ros-indigo-mavlink  ros-indigo-control-toolbox  ros-indigo-transmission-interface ros-indigo-joint-limits-interface unzip ros-indigo-mavros-msgs ros-indigo-mavros-extras ros-indigo-mavros -y

**Mavproxy**

*Install dependencies*

.. code-block:: bash

	sudo apt-get install g++ python-pip python-matplotlib python-serial python-wxgtk2.8 python-scipy python-opencv python-numpy python-pyparsing ccache realpath libopencv-dev -y

*Install MavProxy*

.. code-block:: bash

	sudo pip install future 


.. code-block:: bash

	sudo apt-get install libxml2-dev libxslt1-dev -y

.. code-block:: bash

	sudo pip2 install pymavlink catkin_pkg --upgrade

.. code-block:: bash
	
	sudo pip install MAVProxy==1.5.2

B. Ardupilot
------------

.. code-block:: bash

	mkdir -p ~/gapter_sim


.. code-block:: bash

	cd gapter_sim


.. code-block:: bash

	git clone https://github.com/gaitech-robotics/gapter_ardupilot -b sim_ros_gazebo


C. Creating ros work space
--------------------------

.. code-block:: bash

	mkdir -p ~/gapter_sim/ros_ws/src

.. code-block:: bash

	cd ~/gapter_sim/ros_ws/src

.. code-block:: bash

	catkin_init_workspace

.. code-block:: bash

	cd ..


.. code-block:: bash

	catkin_make

**Now download all repositories required**

.. code-block:: bash

	cd src/

.. code-block:: bash

	git clone https://github.com/gaitech-robotics/gapter_ardupilot_sitl_gazebo_plugin

.. code-block:: bash
		
	git clone https://github.com/gaitech-robotics/gapter_rotors_simulator -b sonar_plugin

.. code-block:: bash

	git clone https://github.com/PX4/mav_comm.git

.. code-block:: bash

	git clone https://github.com/ethz-asl/glog_catkin.git

.. code-block:: bash

	git clone https://github.com/catkin/catkin_simple.git

.. code-block:: bash

	git clone https://github.com/gaitech-robotics/mavros


D. Installing Gazebo
--------------------

**Setup your computer**


.. code-block:: bash

	sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'

**Setup Keys**

.. code-block:: bash


	wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -


**Install gazebo**

.. code-block:: bash

	sudo apt-get update

.. code-block:: bash

	sudo apt-get remove .*gazebo.* '.*sdformat.*' '.*ignition-math.*' 

.. code-block:: bash

	sudo apt-get update 

.. code-block:: bash

	sudo apt-get install gazebo4 libgazebo4-dev drcsim -y

E. Compile workspace
--------------------

.. code-block:: bash

	source ~/gapter_sim/ros_ws/devel/setup.bash

.. code-block:: bash

	cd ~/gapter_sim/ros_ws

.. code-block:: bash

	catkin_make --pkg mav_msgs mavros_msgs gazebo_msgs

.. code-block:: bash

	source devel/setup.bash

.. code-block:: bash

	catkin_make -j 4

F. launch Gapter Simulation
---------------------------

Open the terminal and type following:

.. code-block:: bash

	source ~/gapter_sim/ros_ws/devel/setup.bash

.. code-block:: bash

	user $: cd ~/gapter_sim/gapter_ardupilot/ArduCopter

.. code-block:: bash

	user $: ../Tools/autotest/sim_vehicle.sh -j 4 -f Gazebo


In another terminal lauch following:

.. code-block:: bash

	source ~/gapter_sim/ros_ws/devel/setup.bash

.. code-block:: bash

	roslaunch ardupilot_sitl_gazebo_plugin gapter_spawn.launch

Once mavproxy launched completely in the first terminal load parameters from Ardupilot directory

.. code-block:: bash

	param load /your home directory/gapter_sim/gapter_ardupilot/Tools/Frame_params/gapter.param

.. code-block:: bash
	
	param set ARMING_CHECK 0

**Takeoff gapter**

In mavproxy terminal type following:

.. code-block:: bash

	mode Guided

.. code-block:: bash

	arm throttle

.. code-block:: bash

	takeoff 5

You can see in gazebo that gapter flying at 5 meter height.





