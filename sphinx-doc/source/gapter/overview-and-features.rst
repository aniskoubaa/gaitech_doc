
.. _gapter-overview-features:

================================================
GAPTER: Educational Copter using ROS and MAVLINK
================================================

Overview
========

Gapter is an unprecendanted drone with was carfeully designed to meet the requirements of researchers, students and teachers as an educational and research aerial platform. 
Gapter is a modular research and educational drone platform. It supports Robot Operating System (ROS), the MAVLink protocol, and the mavros wrapper layer between ROS and MAVLink.

It is based on the Pixhawk platform independent autopilot software using the Ardupilot software, and reenforced with an embedded computer Odroid XU4, which is proven to be more powerful than other single board computers, like Raspberry PI, typically used in other drones. 

Unlike other UAVs Gapter can work both indoor and outdoor with its inbuilt sensors like GPS and optical flow sensors. 
It has different types of connectors like power, USB and I2C allowing the user to extend their platform by connecting their own modules or sensors.

Users can connect to Gapter easily to its WiFi and also connected to Internet using 3G/4G router.

 
What makes GAPTER different from other drones?
==============================================

Gapter has several features, when combined together, makes it a unique and different platform. 

.. image:: images/features/ros.png
    :target: http://robots.ros.org/gapter/
    :align: left
    :width: 100pt
    

**ROS-Enabled Drone**: Gapter EDU is a perfect platform to learn drone programming with `ROS <http://robots.ros.org/gapter/>`_. 

| 

.. image:: images/features/mavlink.png
    :align: left
    :width: 100pt

**Supports the MAVLink Protocol**: Gapter fully support the MAVLink protocol allowing its control and monitoring through MAVLink ground stations. You can easly define and control autonmous missions of Gapter drone through Internet or Telemtry devices.

.. image:: images/features/3g4g.png
    :align: left
    :width: 70pt
    
**Internet Connectivity**: Using a 3G/4G WiFi model you can make Gapter accessible through Internet or Local Area Network. Using Dronemap Planner software along with the 3G/4G WiFi router, you can control and monitor Gapter anywhere in the world through the Internet.


.. image:: images/features/pixhawk.jpeg
    :align: left
    :width: 120
    
**Pixhawk**: Pixhawk is open-source flight controller platform providing a high-quality autopilot widely accepted in robotics community. Pixhawk contains a vast array of integrated sensors including 3D accelerometer, gyroscorp, magnetometer, barometer and much more. It is nativaley support the Ardupilo flight controller software and the MAVLink protocol

.. image:: images/features/xu4.jpg
    :align: left
    :width: 100pt
    

**Ordoid XU4 SBC**: Odroid XU4 single-board computer is integrated with Pixhawk to provide the best performance possible for the autopilot. XU4 is a powerful single board computer which is know to be four times faster than Raspberry PI2 and also equipped with 1GB Ethernet network interface and 2G of RAM. Gapter leverages the integrated use of XU4 and Pixhawk to provide an ultimate experience and a flexible and modular platform for users and developers.

.. .. image:: images/features/asus.jpg
    :align: left
    :width: 140
    
.. **3D Sensor**: This is a unique feature in Gapter as compared to other COTS drone platforms, as 3D sensor allows both to have onboard camera in addition to a laser range finder used to avoid obstable and navigate more safely. In addition, Asus Live Pro 3D sensor is fully compatible with ROS. 


.. image:: images/features/rplidar.jpg
    :align: left
    :width: 140

|
|
|

**Laser scanner**: Rplidar laser scan sensor allows to build map and navigate within the generated map autonomously

|
|
|

.. image:: images/features/software.png
    :target: http://wiki.ros.org/gapter
    :align: left
    :width: 100pt
    




**Software and Educational Tools**: Gapter EDU was designed with research and education in mind. Gapter comes with a comprehensive documentation and `software packages <http://wiki.ros.org/gapter>`_ that allows a user to easily start working and developing with Gapter. Software packages including both ROS and MAVLink in addtion to MAVROS. Gaitech EDU portal provides an technical resources to start developing applications with Gapter, user manual and guides. Furthemore, Gaitech Forum provides customers with continuous technical support and responses to their queries.

Mechanical Specification
========================

.. image:: images/gapter-3d-model-01.jpg
    :align: center
    :width: 200pt
    
.. image:: images/gapter-3d-model-02.jpg
    :align: center
    :width: 200pt

Hardware
________

* **Dimensions:** 450 mm
* **Frame:** Carbon Fiber
* **Weight:**  1.7 Kg (with 4S battery)
* **Payload:** 1.5 Kg
* **Type:** X-Quad
* **Propellers:** 9" or 10" props
* **Color:** Black
* **3D sensor:** Intel RealSense R200
* **Battery type:** Lipo Battery (3S, 4S and 6S)

Autopilot Platform
__________________

* **Flight Controller:** Pixhawk 2
* **Flight Stack:** Adrupilot APM  
* **Onboard Computer:** : Odroid XU4 with 2 GHz and Octa core CPUs
* **RAM:** 2GB
* **Internal Sensors:** Gyroscope, Barometer, 3D accelerometer 
* **External Sensors:** GPS, Optical Flow
* **Operating System:** Ubuntu 14.04 LTS
* **Connectors:** 2x USB 3.0, HDMI 1.4a for display, Gigabit Ethernet port
* **Communication with PC:** WiFi, Telemetry


