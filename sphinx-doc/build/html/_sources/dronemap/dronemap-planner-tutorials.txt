.. _dronemap-tutorials:

=========
Tutorials
=========

.. NOTE::

   In this tutorial you will learn how to work with Dronemap Planner with Gapter drone and SITL Simulaor
   
   For any query, please feel free to post your questions in the `Gaitech EDU Forum <http://forum.gaitech.hk/>`_

.. figure:: images/dronemap-logo-transparent.png
    :align: center
    :width: 100pt


Start Dronemap Planner
======================

The first thing, you need to start Dronemap Planner on your local machine or your cloud server as explained in the tutorial :ref:`dronemap-configuration`.
Using command line, go to the folder where Dronemap Planner jar file is located, and execute the following command

.. code-block:: bash
   
   java -jar dronemap-planner.jar dronemap-config.xml

then, you should be able to see all the Dronemap Planner services started as illustrated in the following figure (*output might be slightly different based on version*):

.. figure:: images/dronemap-planner-execution.png
    :align: center
    :width: 700 



.. Note::
   Take note of the ``IP address`` of your server machine where Dronemap Planner is executed as you will need it later for creating a MAVLink output stream from the drone the cloud. 



Using SITL Simulator
====================

The `SITL (software in the loop) simulator <http://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html>`_ allows you to emulate Ardupilot drones without the need for a hardware.
As Gapter uses the Pixhawk autopilot powered by Ardupilot, you can use STIL to emulate Gapter drone and work with Dronemap Planner.

.. Warning::
   First, of all make sure that you have SITL installed on your computer. SITL can be installed on `Linux <http://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html>`_ or `Windows <http://ardupilot.org/dev/docs/sitl-native-on-windows.html>`_. 

.. NOTE::

   In this tutorial assumes that you are familiar with SITL simulator.
   If you are not, you need to see the tutorials available on the `SITL page <http://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html>`_
   in particular, it is recommended that you perform `Copter SITL/MAVProxy Tutorial <http://ardupilot.org/dev/docs/copter-sitl-mavproxy-tutorial.html>`_
   
   For a quick introduction about SITL, you can watch our tutorial videos on :ref:`gapter-mavlink-tutorials`

 
Execute SITL simulator. If you are using ``Gaitech Virtual Machine``, you can try this command:
 
.. code-block:: bash
      
      cd ~/ardupilot/ArduCopter
      sim_vehicle.sh --console --map --aircraft test
    
You should see an output similar to the following: 
 
.. figure:: images/sitl.png
   :align: center
   :width: 500pt
 
The next step is to add a MAVLink output stream from the drone to the cloud server. For this, you need to know the IP address of your server machine.
Let us assume that it is ``192.168.1.10``. Remember that in the ``dronemap-config.xml`` configuration file of the tutorial :ref:`dronemap-configuration`, the port number of the UDP server of the MAVLink protocol was set to the default value ``14550``.  So, we will use this port to send the MAVLink stream from the drone to the server.
In the terminal command of SITL simulator, write the following instruction to add a new output stream:

.. code-block:: bash
      
      output add 192.168.1.10:14550

.. WARNING::
   Replace the IP address with the correct one of your cloud server where Dronemap Planner is running. 

You should see an output similar to the following: 
 
.. figure:: images/output-add.png
   :align: center
   :width: 500pt
   
At this stage, the drone should be streaming its status using the MAVLink protocol to the cloud server and you are now able to control and monitor it using the Dronemap Planner Web interface

Control and Monitoring using Dronemap Planner Web Interface
===========================================================



 