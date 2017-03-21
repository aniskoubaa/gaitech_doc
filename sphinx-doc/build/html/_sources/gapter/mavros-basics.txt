.. _mavros-basics:

=============
MAVROS Basics
=============

This tutorial will introduce the basic operations of MAVROS.

.. NOTE::

	This tutorial was developed for ROS `Indigo <http://wiki.ros.org/indigo>`_ version, and tested on ubuntu 14.04


First launch the simulation, see following links for further details: 

TO BE PROVIDED


.. figure:: images/gapter_ros_teleop_fig_1.png
    :align: center
    :width: 400pt

    Figure 1: Launch the simulator

Then in new terminal, launch the following ROS node (python):

.. code-block:: bash

	rosrun gapter_py gapter_pilot.py 

.. figure:: images/gapter_mavros_basics_fig_1.png
    :align: center
    :width: 400pt

    Figure 2: MAVROS Basics

This node allows you to set the mode and to takeoff and land the drone.

Code Explanation
================

The source code could be found in `github_link`_.

.. _github_link: https://github.com/



.. code-block:: python

 if __name__ == '__main__':
    rospy.init_node('gapter_pilot_node', anonymous=True)
    rospy.Subscriber("/mavros/global_position/raw/fix", NavSatFix, globalPositionCallback)
    velocity_pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel', TwistStamped, queue_size=10)
    
    myLoop()

As any ROS node, it starts with initialization of the ROS node for the process. ``myLoop()`` function is used to display the main menu and to get the input from the user:

.. code-block:: python

 def myLoop():
    x='1'
    while ((not rospy.is_shutdown())and (x in ['1','2','3','4','5','6','7'])):
        menu()
        x = raw_input("Enter your input: ");
        if (x=='1'):
            setGuidedMode()
        elif(x=='2'):
            setStabilizeMode()
        elif(x=='3'):
            setArm()
        elif(x=='4'):
            setDisarm()
        elif(x=='5'):
            setTakeoffMode()
        elif(x=='6'):
            setLandMode()
        elif(x=='7'):
            global latitude
            global longitude
            print ("longitude: %.7f" %longitude)
            print ("latitude: %.7f" %latitude)
        else: 
            print "Exit"
        
The service ``/mavros/set_mode`` is used to set the mode (Guided or Stabilized). The service is called by creating a ``rospy.ServiceProxy`` with the name of the service. Often ``rospy.wait_for_service()`` is called first to block until a service is available:

.. code-block:: Python

 def setGuidedMode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='GUIDED') #return true or false
    except rospy.ServiceException, e:
        print "service set_mode call failed: %s. GUIDED Mode could not be set. Check that GPS is enabled"%e

Same code used to set Stabilized mode, just replace ``custom_mode='GUIDED'`` with ``custom_mode='STABILIZE'`` in ``setStabilizeMode()`` function:

.. code-block:: Python

 def setStabilizeMode():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        flightModeService = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)
        isModeChanged = flightModeService(custom_mode='STABILIZE') #return true or false
    except rospy.ServiceException, e:
        print "service set_mode call failed: %s. GUIDED Mode could not be set. Check that GPS is enabled"%e


To arm or disarm the drone, the service ``/mavros/cmd/arming`` is used in same way as to set the mode:

.. code-block:: python

 def setArm():
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        armService = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
        armService(True)
    except rospy.ServiceException, e:
        print "Service arm call failed: %s"%e

 def setDisarm():
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        armService = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
        armService(False)
    except rospy.ServiceException, e:
        print "Service arm call failed: %s"%e


To takeoff the drone, the ``/mavros/cmd/takeoff`` service is used, and it takes the ``altitude``, ``latitude``, ``longitude``, ``min_pitch``, and ``yaw`` as parameters:
 
.. code-block:: python

 def setTakeoffMode():
    rospy.wait_for_service('/mavros/cmd/takeoff')
    try:
        takeoffService = rospy.ServiceProxy('/mavros/cmd/takeoff', mavros_msgs.srv.CommandTOL) 
        takeoffService(altitude = 2, latitude = 0, longitude = 0, min_pitch = 0, yaw = 0)
    except rospy.ServiceException, e:
        print "Service takeoff call failed: %s"%e

To land the drone, the ``/mavros/cmd/land`` service is used, and it takes the ``altitude``, ``latitude``, ``longitude``, ``min_pitch``, and ``yaw`` as parameters:

.. code-block:: python

 def setLandMode():
    rospy.wait_for_service('/mavros/cmd/land')
    try:
        landService = rospy.ServiceProxy('/mavros/cmd/land', mavros_msgs.srv.CommandTOL)
        #http://wiki.ros.org/mavros/CustomModes for custom modes
        isLanding = landService(altitude = 0, latitude = 0, longitude = 0, min_pitch = 0, yaw = 0)
    except rospy.ServiceException, e:
        print "service land call failed: %s. The vehicle cannot land "%e
