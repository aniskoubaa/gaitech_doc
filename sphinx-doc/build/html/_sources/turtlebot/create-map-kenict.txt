
.. _create-map:

===============================
Building a Map with a Turtlebot
===============================

In this tutorial, you will learn how to build your own map using 3D sensor attached to your Turtlebot. 

.. tip ::

   In this tutorial, you will:

      * Learn how to build a map with a Turtlebot
      * Understand the stucture of a map in navigation stack of ROS
      * Recongnize the configuration files responsible for the building the map in ROS. 

.. WARNING::
    Make sure that you already made the tutorial on :ref:`openKinect-turtlebot`.

As mentioned in :ref:`openKinect-turtlebot`, ROS indigo supports by default ``Asus Live Pro`` 3D sensor and has no default support to ``Kinect`` 3D sensor. 
First, you need to check which 3D sensor you Turtlebot is having, and make appropriate configuration. For more details about the configuration of the 3D sensor on Turtlebot, refer to :ref:`openKinect-turtlebot`.


Running the Map Building Experiments
====================================

Overview
--------

First, you need to start the robot drivers and then start the ROS node responsible for building the map. 
It has to be noted that to build a map ROS uses the ``gmapping`` software package, that is fully integrated with ROS. 
The gmapping package contains a ROS wrapper for OpenSlam's Gmapping. 
The  package provides laser-based SLAM (Simultaneous Localization and Mapping), as a ROS node called ``slam_gmapping``. Using ``slam_gmapping``, you can create a 2-D occupancy grid map (like a building floorplan) from laser and pose data collected by a mobile robot. 

SLAM Background
---------------
SLAM refers to Simultaneous Localization and Mapping. It is the process of building a map using range sensors (e.g. laser sensors, 3D sensors, ultrasonic sensors) while the robot is moving around and exploring an unknown area.
The range sensor is used to detect the distance to obstacle whose estimated locations will be stored into a data structure (e.g/ 2D array) and when the robot is moving, it keeps updating this data structure my setting cell either occupied or empty based on the estimation of its location and the estimation of the distance to the obstacle. 
Usually, this process uses filtering techniques like Kalman filters or praticle filters to improve the estimation of obstacle while moving and removing noise and errors from measurements.
An example of error of measurement is the measure of odometry which known to be imprecise and is subject to cumulative errors over time. In addition, range sensors are another source of errors.
The filtering technique allow to attenuate the effect of these errors onto the precision of the map. Large errors of odomerty and/or range sensors will result into inaccurate and skewed maps.   

.. hint::
   For a more technical introduction to SLAM, consider the following references
      * `SLAM for Dummies <http://ocw.mit.edu/courses/aeronautics-and-astronautics/16-412j-cognitive-robotics-spring-2005/projects/1aslam_blas_repo.pdf>`_: An easy introduction to SLAM problem and solution. 
      * `Simultaneous Localisation and Mapping (SLAM): Part I The Essential Algorithms <https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/Durrant-Whyte_Bailey_SLAM-tutorial-I.pdf>`_: a technical and mathematical introduction to SLAM. 
      

Starting the nodes
------------------
To start the robot, on the master node (the robot machine) run the following commands, on three terminals: 

.. code-block:: bash
	
	roscore
	roslaunch turtlebot_bringup minimal.launch
	roslaunch turtlebot_navigation gmapping_demo.launch

To drive the robot from your workstation, then, on your workstation (the host node), run the following commands:

.. code-block:: bash

	roslaunch turtlebot_rviz_launchers view_navigation.launch
	roslaunch turtlebot_teleop keyboard_teleop.launch

.. WARNING::
    If you execute the following command on your workstation (recommended), you must make sure to have correctly set-up the network configuration as explained in :ref:`network-config-doc`.
    It is not recommended to start ``view_navigation`` launch file on the robot machine as rviz may overload the robot. 


If all is fine, start moving the robot around using ``keyboard_teleop`` application or a joytsick and watch the ``RViz`` GUI as the map starts to be built-up. 

Finally you will end-up with a map looking like this one:

.. image:: images/kenict_map.png
    :align: center

Now, save the built map you just created by running the following command:

.. code-block:: bash
	
	rosrun map_server map_saver -f /tmp/my_map

.. NOTE::
	The ``tmp`` folder gets cleaned everytime the system is rebooted, so after saving the map you can move the files to another location. Alternatively, you can specify another folder of your choice to save the map when running the ``map_saver`` command. 

You can double click on the ``pgm`` file to see the generated map. 



Analyzing the Generated Map
===========================

The previous command will generate **two files** with the name you specified in the ``map_server`` commnd. 
So in this case, the two files' names are ``my_map.pgm`` and ``my_map.yaml``. 
If you open the ``.yaml`` file you will see something like this:

.. code-block:: yaml

	image: /tmp/my_map.pgm
	resolution: 0.050000
	origin: [-12.200000, -12.200000, 0.000000]
	negate: 0
	occupied_thresh: 0.65
	free_thresh: 0.196

The ``.yaml`` contains meta data about the map, including the location of image file of the map, its resolution, its origin, the occupied cells threshold, and the free cells threshold. 
Here are the details for the different parameters:

   * ``image``: has a pgm format which contains numeric values between 0 and 255. It represents the path to the image file containing the occupancy data; can be absolute, or relative to the location of the YAML file
   * ``resolution``: it is the resolution of the map and is expressed in ``meters/pixel``, which means in our example 5 centimers for each cell (pixel).  
   * ``origin``: The 2-D pose of the lower-left pixel in the map, as (x, y, yaw), with yaw as counterclockwise rotation (yaw=0 means no rotation). Many parts of the system currently ignore yaw.
   * ``occupied_thresh``: Pixels with occupancy probability greater than this threshold are considered completely occupied.
   * ``free_thresh``: Pixels with occupancy probability less than this threshold are considered completely free.
   * ``negate`` : Whether the white/black free/occupied semantics should be reversed (interpretation of thresholds is unaffected)

Now, for the second file, that is the ``.pgm`` image file, it is just a gray-scale image of the map which you can open using any image editor program and it will look like this:

.. image:: images/pgm_map.png
	:align: center 
   
.. TIP::
   It is recommended to use the `The GNU Image Manipulation Program <https://www.gimp.org/>`_ to open and edit PGM files. 
   
The gray area represents an unknown non-explored space. 
The white area represents the free space, and the black area represents obstacles (e.g. walls). 

You can open this file with any text editor like ``gedit`` or ``kate`` to see its content. 
In what follow, we present the four first lines of a typical ``pgm`` file. 
 
.. code-block:: xml
   
   P5
   # CREATOR: GIMP PNM Filter Version 1.1
   600 600
   255
   
The first line, ``P5`` identifies the file type. 
The third line identifies the width and the length in number of pixels. 
The last line represents the maximum gray scale, which is this case 255 that represents the darkest value. The value 0 in a PGM file will represent a free cell. 

.. TIP::
   For more details about ``pgm`` file format, refer to `PGM documentation <http://netpbm.sourceforge.net/doc/pgm.html>`_. 

What is in the background?
==========================
When you run the command

.. code-block:: bash
   
   roslaunch turtlebot_navigation gmapping_demo.launch
   
the ``gmapping_launch`` file will be exectued. Here is the content of that file:

.. code-block:: xml

   <launch>
      <include file="$(find turtlebot_bringup)/launch/3dsensor.launch">
            <arg name="rgb_processing" value="false" />
            <arg name="depth_registration" value="false" />
            <arg name="depth_processing" value="false" />
            <arg name="scan_topic" value="/scan" />
        </include>
        <include file="$(find turtlebot_navigation)/launch/includes/gmapping.launch.xml"/>
        <include file="$(find turtlebot_navigation)/launch/includes/move_base.launch.xml"/>
   </launch>

You can observe that it first starts the ``3dsensor`` launch file which will runs either ``Asus Xtion Live Pro`` or ``Kinect`` 3D sensor of the Turtlebot. 
It sets some parameters to their default values and specifies that the scan topic is refered to as ``/scan``.
Then, it will start the ``gmapping.launch.xml`` that contains the specific parameters of the ``gmapping`` SLAM algorithm (parameters of the particle filter) that is responsible for building the map.
Finally, it will start the ``move_base.launch.xml`` that will initialize the parameters of the navigation stack, including the global planner and the local planner. 

Practical Considerations and Observations
=========================================
When building a map with a Turtlebot it is possible to get a good or bad map depending on several factors. 
First of all, make sure that your Turtlebot robot and its laptop have full batteries before starting the mapping tasks. 
In fact, ``gmapping`` and ``rviz`` both consume alot of power resources.

The quality of the generated map greatly depends on quality of range sensors and odometry sensors. 
For the Turtlebot, it has either the Kinect or Asus Xtion Live Pro camera with only 4 meters of range, and only 57 degree of laser beam angle, which render it not appropriate for scanning large and open space environments. 
Thus, if you use Turtlebot to build the map for a small environment where walls are not far from each others, it is likely that you will get an accurate map. 

However, if you build the map for a large and open space environment, then it is likely that your map will not be accurate at a certain point of time.
In fact, in large and open space environment, you need to drive the robot for long distance, and thus, the odometry will play a more cruicial role in building the map.
Considering the fact that the odometry of the Turtlebot is not reliable and is prone to errors, these errors will be cumulative over time and will quickly compromise the quality of generated maps. 
 
It will interesting to try using your Turtlebot to build maps for both small environment and large environment and observe the accuracy of the map for each case. 

References
==========
Here are some useful reference to learn more about building maps using ROS. 

   * `gmapping package <http://wiki.ros.org/gmapping>`_: This package contains a ROS wrapper for OpenSlam's Gmapping. The gmapping package provides laser-based SLAM (Simultaneous Localization and Mapping), as a ROS node called slam_gmapping. Using slam_gmapping, you can create a 2-D occupancy grid map (like a building floorplan) from laser and pose data collected by a mobile robot.
   * `slam_gmapping package <http://wiki.ros.org/slam_gmapping>`_: slam_gmapping contains a wrapper around gmapping which provides SLAM capabilities.
   * `OpenSLAM Gmapping <https://www.openslam.org/gmapping.html>`_: GMapping is a highly efficient Rao-Blackwellized particle filer to learn grid maps from laser range data. 
   * `map_server <http://wiki.ros.org/map_server>`_: map_server provides the map_server ROS Node, which offers map data as a ROS Service. It also provides the map_saver command-line utility, which allows dynamically generated maps to be saved to file.

Video Demonstration
===================
.. youtube:: QzZif1e767k

Review questions
================
   * Apply this tutorial to build a map of your office or room. Observe the map and provide comments on its accuracy.
   * Use `The GNU Image Manipulation Program <https://www.gimp.org/>`_ to edit the generated map. Try to enhance the walls structure and remove erronous obstacle. Save the new file as PGM. 
   * Open the new PGM file and observe its content. 
   * What is the role of the ``map_server`` package?
   * Whick package is responsible for building the map in ROS? 
   * Explain briefly the need for a range sensor and motion sensor to build the map of a moving robot. 
   * How a map is represented in ROS? What is the relation between the ``yaml`` file and the ``pgm`` file?
   * Which specific launch file is responsible for executing the gmapping algorithm and initialize its parameters?  

