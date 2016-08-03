
.. _network-config-doc:

=====================
Network Configuration
=====================

This tutorial will introduce to you to configure your turtlebot robot to communicate with your computer machine, so that you can execute program, which you develop and run on your machine, remotely on the Turtlebot.
We refer to your personal machine as **workstation** and the robot laptop as **robot machine**.
The objective of this configuration is to make the robot machine and your workstation use the same ``ROS Mater node`` so that any ROS topic or ROS service on the robot will also be available on the workstation. 
As such, any ROS program or script that runs on your machine, will have direct access to the ROS topics and ROS services, and thus, it can control and monitor the robot remotely from the workstation. 
To allow this, it is needed to configure the laptop of your robot and your machine to be able to communicate. 

.. NOTE::
   Make sure that you completed installing all the required packets in the previous tutorials.
   
Video Tutorial
==============
The following video tutorial illustrates in 10 minutes the steps to follow for network configuration in ROS and demonstrates it through an example. 

.. youtube:: 1KOrXSEDQ3k

Getting your IP address
=======================
ROS offers the ability to have a two-way communication network between different ROS nodes. All what you have to do is to know the IP address for the ROS master node and the IPs for other ROS nodes.

.. tip :: For Ubuntu users: to know the IP address for your device in the network you are connected to, you can open a terminal and type ``ifconfig`` and you will find something similar to the following:

.. code-block:: bash

   lo     Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:6658055 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6658055 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:587372914 (587.3 MB)  TX bytes:587372914 (587.3 MB)

   wlan1  Link encap:Ethernet  HWaddr 48:5d:60:75:58:90
          inet addr:10.0.129.17  Bcast:10.0.129.255  Mask:255.255.254.0
          inet6 addr: fe80::4a5d:60ff:fe75:5890/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:101983 errors:0 dropped:0 overruns:0 frame:0
          TX packets:37244 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:49326141 (49.3 MB)  TX bytes:7588044 (7.5 MB)

In the example above, the IP address of the machine is ``10.0.129.17`` with respect to the WiFi network interface ``wlan1``. It may happen to have a different WiFi interface like ``wlan0`` or others depending on network configuration of your local machine.

By applying the above instructions, find the IP address of your workstation, which we denote as ``WORKSTATION_IP`` and the IP address of your robot machine, which we denote as ``TURTLEBOT_IP``. 

Test your connection
====================
First, make sure that ssh server is already installed on your robot machine. To do so (if not installed), on your robot machine write the following:

.. code-block:: bash
    
    sudo apt-get install openssh-server
    
This will install openssh server if it is not installed. 

On your workstation PC, try to connect to the Turtlebot by typing the following command:

.. code-block:: bash

    ssh name_of_turtlebot_PC@TURTLEBOT_IP 

where ``TURTLEBOT_IP`` is the IP address of the turtlebot robot machine that you found in the previous step. 
You will be prompted and requested the password of the robot machine, which you need to type correctly. Once done, you should now be connected to the Turtlebot and any command you will write on the terminal will be physically executed on the robot machine. 
If this was successful, you can head to the next steps. 


Configure the robot and the workstation to use the same ROS Master
==================================================================
Now, we will configure the robot machine and the workstation to use the same ROS master node, so that any program on the workstation can use the ROS topics and ROS services available on the turtlebot robot.  

.. NOTE:: 

   Remember that the ROS Master node is started with ``roscore`` command and is the main node in ROS environment that  provides naming and registration services to the rest of the nodes in the ROS system. It tracks publishers and subscribers to topics as well as services. The role of the Master is to enable individual ROS nodes to locate one another. Once these nodes have located each other they communicate with each other peer-to-peer.
   More information can be found on `ROS Master node <http://wiki.ros.org/Master>`_
   
To be able to use ROS in any project/environment you must have a ROS master node which is the main node that a user can communicate with either in the same device or by another devices.
All you have to do is to specify in the ``.bashrc`` file the IP address for the Master node and the host node (the other device).

Open the ``.bashrc`` file in the robot machine (use the command ``gedit .bashrc``). Scroll to the bottom of the file and add these lines:

.. code-block:: bash

   #The localhost IP address = IP address for the Master node
   export ROS_MASTER_URI=http://localhost:11311
   #The IP address for the Master node
   export ROS_HOSTNAME=192.168.8.100

replace ``192.168.8.101``  with the correct IP address of the robot machine (see above for getting the IP address).
The line ``export ROS_MASTER_URI=http://localhost:11311`` means that the ROS master runs in the localhost of the robot machine. 
The line ``export ROS_HOSTNAME=192.168.8.100`` specifies the hostname of the robot machine, which must be exactly the same found with the ``ifconfig`` command

Now, in your workstation PC open the ``.bashrc`` file and scroll to the bottom of the file and add these lines:

.. code-block:: bash

   source /opt/ros/indigo/setup.bash
   #The IP address for the Master node
   export ROS_MASTER_URI=http://192.168.8.100:11311
   #The IP address for your device/host IP address
   export ROS_HOSTNAME=192.168.8.101

The line ``export ROS_MASTER_URI=http://192.168.8.100:11311`` means that the ROS master runs in the machine with IP address ``192.168.8.100`` which must correspond to the robot machine IP address.
The line ``export ROS_HOSTNAME=192.168.8.101`` specifies the hostname of the workstation machine, which must be exactly the same found with the ``ifconfig`` command

Make sure to close the terminal and open a new one so that changes take effect. You can also type ``source .bashrc``.

Testing the configuration
=========================
To test that the configuration works fine, run the following command in your robot machine that will contain the Master node (the one connected to the turtlebot): 

.. code-block:: bash

    roscore

In your workstation machine, write the following command:

.. code-block:: bash

    rostopic list

If all is fine, you should be able to see the list of topics available in the robot machine, which -in case of roscore running alone- should be:

.. code-block:: bash

   /rosout
   /rosout_agg

.. NOTE::
    If the connection is successful you will be able to see a list of all the ROS topics published from the Master node if it fails then make sure that the ``ROS_MASTER_URI`` is set to the right value.

To check whether the Master node can receive data from the host node, run this command in a workstation PC terminal:

.. code-block:: bash

    rostopic pub -r10 /hello std_msgs/String "hello"

on the robot machine that is already running the Maser node, run the following command in a new terminal:

.. code-block:: bash

    rostopic echo /hello

The message "hello" should appear about 10 times per second.

.. Tip::
   If something is wrong with executing the previous step, make sure that the ``ROS_HOSTNAME`` in the host node is correct.

You can also watch the example of running the turtlesim in the video tutorial above.

Sychronization Utilities
========================
In case you faced any strange behaviour from the robot during transmitting data from a Host node to the Master node, you can download:


Chrony:  

.. code-block:: bash

    sudo apt-get install chrony

or

manually sync NTP: 

.. code-block:: bash

    sudo ntpdate ntp.ubuntu.com

to fix the clock synchronization problem.
