
.. _dronemap-overview:

=========================
Dronemap Planner Overview
=========================



.. NOTE::

   In this tutorial you will learn:

      * Why Dronemp Planner is needed?
      * What is Dronemap Planner?
      * The main features of Dronemap Planner. 
   
   For any query, please feel free to post your questions in the `Gaitech EDU Forum <http://forum.gaitech.hk/>`_

.. figure:: images/dronemap-logo-transparent.png
    :align: left
    :width: 100pt

Why Dronemap Planner?
=====================

The typical use of drones is to establish a point-to-point connection with them either through telemtery device or a WiFi connection to the WiFi hotspot of the drone.
This represents the common approach to connect to drone. In this way, the communication range between the drone and the ground station will be limited to a maximum of few hundred meters at best. 
In addition, when the drone flies far from the ground station, the bandwidth and throughput decrease drastically. 

Furthermore, the drone typically has limited storage and processing capabilities onboard, which restricts the performance of applications running on it, in particular with high computation requirements. 
This is in addition to being battery-powered, which compromise its flight and mission lifetime.

The following figure illustrates these issues.  

.. figure:: images/why.png
    :align: center
    :width: 500pt
    
    Figure 1. Problem with typical drone-ground station point-to-point connection

``Dronemap Planner`` fills the gap by bridging drones with the Internet to allow their remote control anywhere and anytime. 
Figure 2 illustrates the concept and the system architecture. 

.. figure:: images/dronemap-architecture.png
    :align: center
    :width: 500pt
    
    Figure 2. Dronemap Planner System Architecture

``Dronemap Planner`` is deployed into a cloud infrastructure and plays the role of a proxy between the robots/drones and the user applications. 
The robot/drone broadcasts its internal status through the MAVLink or ROSLink protocols to the Dronemap Planner cloud. 
The Dronemap Planner cloud manages the sessions of robots/drones that join the cloud dynamically as they enter of leave. 
It also allow the user to select a robot/drone through Dronemap Planner client interface and monitor and control it remotely through the Internet anywhere anytime without any restrictions on the communication range. 
Considering its Service-Oriented Architectur (SOA) desig, Dronemap Planner cloud provides Web services API to easily develop applications through the cloud on robots and drones. 

Dronemap Planner is a comprehensive and unique framework for the management of robots/drones over the Internet. It represents an illustration of the concept of Internet-of-Drones. 



What is Dronemap Planner?
=========================

``Dronemap Planner`` is cloud-based management systems for robots and drones. It supports any type of robots/drones provided that they use the MAVLink protocol for communication or Robot Operating System (ROS).
For ROS-enabled robots, the ROSLink protocol is used to communicate between the robot and the cloud. 


.. TIP::
   
   The MAVLink protocol (MAVLink Micro Air Vehicle Communication Protocol) lightweight, header-only message serialization library for micro air vehicles.
   It is a protocol for communicating with small unmanned vehicles. It is designed as a header-only message marshaling library. MAVLink was first released early 2009 by Lorenz Meier under LGPL license.
   This protocol is used as a standard to communicate between drones and ground stations like QGroundControl, DroidPlanner, Mission Planner, ...
   For an introduction abou the MAVLink protocol, you can follow our :ref:`gapter-mavlink-tutorials`.

.. TIP::
   The ROSLink protocol is also a JSON serialization library that allows the communication between the ROS-enabled robots and the ``Dronemap Planner`` cloud. 
   For an introduction abou the ROSLink protocol, you can follow our :ref:`roslink` tutorials.
   
   

For technical details about ``Dronemap Planner`` system and architecture, you can refer to our publication

A. Koubâa, B. Qureshi, M. F. Sriti, Y. Javed and E. Tovar, "`A Service-Oriented Cloud-based Management System for the Internet-of-Drones <http://ieeexplore.ieee.org/document/7964096/>`_," 2017 IEEE International Conference on Autonomous Robot Systems and Competitions (ICARSC), Coimbra, 2017, pp. 329-335.

You can also watch the following video presentation about ``Dronemap Planner``

.. youtube:: T9jyowdPSJk



Features
========

Dronemap Planner provides several features:

* Enables the remote control and monitoring of robots/drones over the Internet
* Supports the MAVLink protocol to control small unmanned aerial vehicles
* Supports the ROSLink protocol to control ROS-enabled robots
* Provides APIs to develop cloud applications to control and monitor robots over Dronemap Planner using Web services
* Enables the integration of robots/drones into the Internet-of-Things (IoT)

Acknowledgement
===============

We acknowledge the support of Prince Sultan University (Saudi Arabia) and King AbdulAziz City for Sciences and Technology (Saudi Arabia) for Dronemap research project. 

