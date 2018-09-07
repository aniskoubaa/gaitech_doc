
.. _gapter-brain-software-suite:

===========================
Gapter Brain Software Suite
===========================

In this tutorial, we present the different software frameworks that come pre-installed in Gapter Brain. 


.. NOTE::

   In this tutorial you will learn:

      * software framework of the Gapter brain
      * how to install a new software in Gapter brain
   
   For any query, please feel free to post your questions in the `Gaitech EDU Forum <http://forum.gaitech.hk/>`_

   
  
First, before being able to develop or deploy any program in Gapter Brain, you need to connect to it. Depending on the wireless mode, you can connect to Gapter by following instructions in :ref:`network-configuration`.
Then, you will have access to the software development frameworks of Gapter, which are presented in what follows.

The Ubuntu 14.04 LTS Operating System (OS)
==========================================
Gapter brain comes with Ubuntu 14.04 LTS operating system pre-installed. 


Robot Operating System (ROS)
============================

ROS is the defacto standard for developing software and applications for robots, including drones. ROS is already installed in Gapter. It can be located in this folder ``/opt/ros/``.
To know the version of ROS installed on your Gapter, you can perform the following command

.. code-block:: bash

   cd /opt/ros/
   ls 
   
Then, you will see the folder name which presents the ROS version. The default ROS version is ``indigo``. 

If you want to install another version of ROS on Gapter Brain, then make sure that you are connected to it in **WiFi infrastructre mode** as illustrated in the tutorial :ref:`network-configuration` and that you are connected to the Internet.
Then, you can install ROS by following the ROS tutorials (for Ubuntu 14.04 OS) `installation instructions of ROS Indigo <http://wiki.ros.org/indigo/Installation/Ubuntu>`_, then you must `configure your ROS environment <http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment>`_
The installation of ROS on Odroid XU4 is similar to installing it on any other computer with Ubuntu 14.04 OS. 

The default ``catkin`` workspace is located in ``/home/gapter/catkin_ws`` folder. You can create new ROS packages in ``/home/gapter/catkin_ws/src/`` as illustrated in the tutorial `Creating a ROS Package <http://wiki.ros.org/ROS/Tutorials/CreatingPackage>`_ .

To edit/create ROS programs, you can use the ``nano`` editor in command line terminal direcltly on Odroid XU4. 
If this is not enough convinient, then you can develop your ROS programs locally on your computer machine, and test them; then transfer the file to appropriate folder in the catkin workspace and ROS package. You can use FTP client to transfer files from your computer to Gapter (e.g. FileZilla or others), or you can transfer through using a USB device.


.. TIP::

   Note that you can run your programs first on Gapter simulator (see tutorial :ref:`gapter-simulation`) to make sure that they work as expected before running them on the real Gapter drone.

.. TIP::

   We already provide a sample of ROS programs on Gapter brain, which are available in the folder ``/home/gapter/catkin_ws/src/gaitech_edu/src/gapter/``.
   You can run and test these programs by following the :ref:`gapter-ros-tutorials`. 
 

MAVLink
=======

MAVLink is a communication protocol supported by the Ardupilot autopilot software between the drone and the ground station. 
As Gapter uses Pixhawk autopilot, which is embeds the Ardupilot autopilot, it uses the MAVLink protocol to communicate with the ground stations such as QGroundControl, DroidPlanner, Tower, AMP Planner, Mission Planner, ...

.. TIP::

   For more information about the MAVLink protocol, and Ardupilot system, we provide the following references:

   * `MAVLink and Ardupilot YouTube Video Tutorials of Anis Koubaa <https://www.youtube.com/watch?v=qLfxzeKu2Hg&index=1&list=PLSzYQGCXRW1Gk3C7fh7tVE92UKOn-chtg>`_ (recommended) 
   * `MAVLink Micro Air Vehicle Communication Protocol <http://qgroundcontrol.org/mavlink/start/>`_ 
   * `MAVLink in Wikipedia <https://en.wikipedia.org/wiki/MAVLink>`_ 
   * `MAVLink Messages <https://en.wikipedia.org/wiki/MAVLink>`_
   * `Ardupilot <http://ardupilot.org/>`_ 
   * `ArduCopter <http://ardupilot.org/copter/>`_ 

You can connect and control Gapter to any ground station that supports the MAVLink protocol. Here are links to the main ground stations and their tutorials to connect to them.
You just need to follow the steps of the tutorial for every ground station to control Gapter. 



* `QGroundControl <https://docs.qgroundcontrol.com/en/>`_ (Linux, MAC, Windows, Android, iOS)
* `MAVProxy <http://ardupilot.github.io/MAVProxy/html/index.html>`_ (Linux, MAC, Windows, Android, iOS)
* `APM Planner <http://ardupilot.org/planner2/>`_ (Linux, MAC, Windows)
* `Mission Planner <http://ardupilot.org/planner/docs/mission-planner-overview.html>`_ (Windows) 
* `Droid Planner <http://ardupilot.org/planner/docs/mission-planner-overview.html>`_ (Android)

You can find the list of `Ardupilot ground stations in this link <http://ardupilot.org/copter/docs/common-choosing-a-ground-station.html>`_. 

.. NOTE::
   Note that you can connect Gapter to the ground station either using the telemetry device or through Wifi. 
   
   You can start with the telemetry device as it is straighfoward. In this case, you need to connect one telemtery device to Gapter (should be already connected) and the other telemetry device to your computer or device having the ground station. 
   
   Doing so, Gapter will automatically connect to the ground station once you open the ground station software.
   If you connect through Wifi connection, the process is the same. However, make sure that both the ground station and Gapter are connected to the same local area network and that Gapter is streaming the MAVLink messages to the IP address of the ground station. 
  

MAVProxy
========

``MAVProxy`` is a lightweight terminal command ground station that supports the MAVLink protocol. You can get more details about * `MAVProxy <http://ardupilot.github.io/MAVProxy/html/index.html>`_. 
``MAVProxy`` comes pre-installed into Odroid XU4 computer of the Gapter Brain. It allows to connect to the Pixhawk autopilot through a serial link to get all the status of the autopilot through MAVLink message.
In addition, MAVProxy allows to broadcast MAVLink messages through WiFi connection using either UDP or TCP. Thus, MAVLink message can be broadcasted through the Internet, which can be processed by cloud platforms such as the ``Dronemap Planner`` cloud-based drone management system. 


DroneKit
========

`DroneKit <http://dronekit.io/>`_ helps creating applications for drones using the Ardupilot autopilot. It supports both Python and Android programming languages. 
DroneKit comes pre-installed in Gapter Brain. You can locate the DroneKit folder in path ``/home/gapter/dronekit/``.
Examples in Python are available in the folder ``/home/gapter/dronekit/dronekit-python/examples/``


