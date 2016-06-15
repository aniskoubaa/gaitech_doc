.. _network-config-doc:

=====================
Network Configuration
=====================

This tutorial will introduce to you how to chat with your turtlebot robot.

.. NOTE::
   Make sure that you completed installing all the required packets in the previous tutorials.

ROS offer the ability to have a two way communication network between different ROS nodes. All what you have to do is to know the IP address for the ROS master node and the IPs for other ROS nodes.

.. tip :: For Ubuntu users: to know the IP address for your device in the network you are connected to, you can open a terminal and type "ifconfig" and you will find something similar to the following:

.. code-block:: linux

   lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:6658055 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6658055 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:587372914 (587.3 MB)  TX bytes:587372914 (587.3 MB)

   `wlan1`   Link encap:Ethernet  HWaddr 48:5d:60:75:58:90
          inet addr:`10.0.129.17`  Bcast:10.0.129.255  Mask:255.255.254.0
          inet6 addr: fe80::4a5d:60ff:fe75:5890/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:101983 errors:0 dropped:0 overruns:0 frame:0
          TX packets:37244 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:49326141 (49.3 MB)  TX bytes:7588044 (7.5 MB)

the highlighted network is the one you are connected to and the highlighted IP address is your device's IP.

The next part maybe a little bit tricky: To be able to use ROS in any project/environment you must have a ROS master node which is the main node that a user can communicate with either in the same device or by another devices.
All you have to do is to specify in the ``/.bashrc`` file the IP address for the Master node and the host node (the other device).

Open the ``/.bashrc file`` in the PC that has the master node and connected to the turtlebot robot. Scroll to the bottom of the file and add these lines:

.. code-block:: linux

   #The localhost IP address = IP address for the Master node
   export ROS_MASTER_URI=http://localhost:11311
   #The IP address for the Master node
   export ROS_HOSTNAME=192.168.8.101

In the your PC (the host device) open the ``/.bashrc`` file and scroll to the bottom of the file and add these lines:

.. code-block:: linux

   source /opt/ros/indigo/setup.bash
   #The IP address for the Master node
   export ROS_MASTER_URI=http://192.168.8.100:11311
   #The IP address for your device/host IP address
   export ROS_HOSTNAME=192.168.8.101
   #The IP address for your device/host IP address
   export ROS_IP=192.168.8.101


Try to run the following command in your Master node (the one connected to the turtlebot): 

.. code-block:: linux

    roscore

In your host node type this command:

.. code-block:: linux

    rostopic list

to test whether the connection is established and the host node can communicate with the Master node or not.

.. NOTE::
    If the connection is successful you will be able to see a list of all the ROS topics published from the Master node if it fails then make sure that the ROS_MASTER_URI is set to the right value.

To check whether the Master node can receive data from the host node run this command in a host node terminal:

.. code-block:: linux

    rostopic pub -r10 /hello std_msgs/String "hello"

on the Maser node run the following command in a new terminal:

.. code-block:: linux

    rostopic echo /hello

The message "hello" should appear about 10 times per second.

.. Tip::
   If something is wrong with executing the previous step, make sure that the ROS_HOSTNAME in the host node is correct.


In case you faced any strange behaviour from the robot during transmitting data from a host node to the Master node, you can download:

Chrony:  

.. code-block:: linux

    sudo apt-get install chrony

or

manually sync NTP: 

.. code-block:: linux

    sudo ntpdate ntp.ubuntu.com

to fix the Clock synchronization problem.
