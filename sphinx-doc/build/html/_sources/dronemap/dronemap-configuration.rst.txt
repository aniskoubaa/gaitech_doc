
.. _dronemap-configuration:

=======================
Setup and Configuration
=======================

.. NOTE::

   In this tutorial you will learn:

      * System requirements for Dronemap Planner
      * Deployement of Dronemap Planner
      * Parameter Configuration of Dronemap Planner 
   
   For any query, please feel free to post your questions in the `Gaitech EDU Forum <http://forum.gaitech.hk/>`_

.. figure:: images/dronemap-logo-transparent.png
    :align: center
    :width: 100pt

Hardware System Requirements
============================

The requirements for the server where to deploy Dronemap Planner software are:

* **Operating System**: Linux, MAC, Windows
* **RAM**: Minimum 2 GB RAM is required, but 4 GB and more is recommended. 
* **Disk Space**: 37 MB for jar file size. 
* **Hard Drive**: SSD hard drive is recommended for better performance

Software System Requirements
============================

``Dronemap Planner`` cloud software comes as a jar file. It requires:

* Java virtual machine to be executed. 
* Java version ``1.8``. It was tested to be working with Java version ``1.8.0_111`` and ``1.8.0_101`` (does not work with Java 1.6 and 1.7).


``Dronemap Planner`` Web application is based on PHP. It requires:

* PHP 5.6 or above 
* MySQL Database

It is recommended to use `xampp <https://www.apachefriends.org/>`_ or `wamp <http://www.wampserver.com/en/>`_ web servers to deploy the web application 

System Setup
============

Dronemap Planner Cloud System
+++++++++++++++++++++++++++++


Deploying Dronemap Planner cloud system is easy and fast. 
However, you need to carefully setup your parameters to make sure that it works correctly. 

.. NOTE ::
   You can execute Dronemap Planner into your local machine or on a cloud server on the Internet. 
   Nonetheless, if you want to access drones over the Internet, then, Dronemap Planner must be deployed into a server that has **a public IP address** to be accessible by robots and drones. 
   If you want to work with Dronemap Planner on a Local Aera Network (LAN), then you can run it on a localhost. The process is exactly the same, what differs if the IP address of the server used for configuration. 

Here are the steps to follow for setting up Dronemap Planner:

* **Step 1**: copy the Dronemap Planner ``jar`` file and ``dronemap-config.xml`` into a folder of your choice in the server where you will deploy it.
* **Step 2**: identify the IP address of your server machine. Let us assume that the IP address is ``192.168.10.10``. Use the correct address of your server machine instead.
* **Step 3**: open the file ``dronemap-config.xml`` and edit the IP address with the correct IP address of your server as shown in line 4 of ``XML`` script:

.. code-block:: xml
   :emphasize-lines: 4-5
   
   <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
   <dronemap-params>
      <server>
         <ip>192.168.10.10</ip>
         <port>14550</port>
      </server>
      <license>
         <key>X67-SKJ67-878UUJ</key>
      </license>
      <link_quality>
         <window_size>10</window_size>
      </link_quality>
      <watch_dog>
          <timer_ms>1000</timer_ms>
          <drone_max_delay_sec>10</drone_max_delay_sec>
          <google_geocode_timer_ms>10000</google_geocode_timer_ms>
          <initial_delay_ms>1000</initial_delay_ms>
      </watch_dog>
      <geolocation_api>YOUR_GOOGLE_GEOLOCATION_KEY</geolocation_api>
   </dronemap-params>

.. WARNING ::
   If you do not use the correct IP address of your server machine, Dronemap Planner will not correctly start. 
   
* **Step 4**: Line 5 of the ``XML`` script contains the **port number** of Dronemap Planner cloud UDP server. 

This is the port number that the drone will use to connect to the cloud using the MAVLink protocol. You should keep this value at its default ``14550``. 
You can change the port number to any other value. We will discuss more the port number during the execution of Dronemap Planner cloud services. 

* **Step 5**: Line 8 of the ``XML`` represents your license key of Dronemap Planner software. Make sure to put your correct license key.

* **Step 6**: For ``<link_quality>`` and ``<watch_dog>`` tags, they represent some configuration parameters for the assessing the link quality between the drone and the cloud, and some routine management tasks in the Dronemap Planner cloud, respectively. Do not change these values unless really needed. 

* **Step 7**: The ``<geolocation_api>`` tag specifies the Google Geolocation API Key which is needed to correctly transform a GPS location into an address. You need to get your own `Google Geolocation API key <https://developers.google.com/maps/documentation/geolocation/get-api-key>`_ and paste it 

Once all these parameters are set correctly, you are now ready to execute and run Dronemap Planner jar file. 

Using command line, go to the folder where Dronemap Planner jar file is located, and execute the following command

.. code-block:: bash
   
   java -jar dronemap-planner.jar dronemap-config.xml

then, you should be able to see all the Dronemap Planner services started as illustrated in the following figure (*output might be slightly different based on version*):

.. figure:: images/dronemap-planner-execution.png
    :align: center
    :width: 700 

.. WARNING ::
   Make sure that you are using the correct Java version 1.8.
   

Now, your Dronemap Planner cloud is up and running and you can start connecting robots and drones to it.
The figure shows the list of network services and web services that are started in the Dronemap Planner cloud. 

The next tutorials will take you step by step to control robots and drones using Dronemap Planner. 
   

Dronemap Planner Web Client Application
+++++++++++++++++++++++++++++++++++++++
Dronemap Planner Web client application enables you to control and monitor the drone using a Web interface through the Dronemap Planner cloud system. 
The Web application provides all necessary functionalities of a ground station to perform all operations on the drone, and monitor its status in real-time. 

We will presents the steps you need to follow to set-up and deploy the Web application. 


