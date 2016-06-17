.. _speech-doc:

=============================
Turtlebot Voice Teleoperation
=============================

This tutorial will introduce how to control your turtlebot robot using speech recognition.

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials and your network set-up is working fine between the ROS Master node and the host node.

.. NOTE::

   In this tutorial you will learn how to:

      * Teleoprate a real and simulated turtlebot with voice commands
      * Create a custom voice-command vocabulary  
      * Work with pocket-sphinx package in ROS 


Install PocketSphinx for Speech Recognition
===========================================

In order to download the ``pocketsphinx`` package on Ubuntu you need to install the ``gstreamer0.10-pocketsphinx`` and the ROS sound drivers.

.. code-block:: bash

    sudo apt-get install gstreamer0.10-pocketsphinx
    sudo apt-get install ros-indigo-pocketsphinx
    sudo apt-get install ros-indigo-audio-common
    sudo apt-get install libasound2

You do not need to worry about connecting the audio input stream with your PC or publishing a topic because the node recognizer.py in the ``pocketsphinx`` package does all the work for you.


Test the PocketSphinx Recognizer
================================
First, you need to test of the recognizer is working. To get the best result it is better to have an external Mic connected to you PC either by USB, standard audio or Bluetooth.

.. NOTE::
    Make sure that the Mic you are using is the one that is selected in the sound settings in your PC. Try to test your Mic before hands to make sure that the quality is good and check the volume meter.

Note that ``pocketsphinx`` comes as a packages in ROS Indigo. For more details, refer to `the pocketsphinx package <http://wiki.ros.org/pocketsphinx>`_ on ROS WiKi.
You can find browse the directory of ``pocketsphinx`` package with the command:

.. code-block:: bash

   roscd pocketsphinx

In the directory ``demo/``, you can observe the voice commands and dictionary. You may want to have a look at their content using ``more`` or ``nano`` text viewers. 
Then, run the following command:

.. code-block:: bash

   roslaunch pocketsphinx robocup.launch

The ``robocup.dic`` contains the following code:  

.. code-block:: xml

   <launch>
     <node name="recognizer" pkg="pocketsphinx" type="recognizer.py" output="screen">
       <param name="lm" value="$(find pocketsphinx)/demo/robocup.lm"/>
       <param name="dict" value="$(find pocketsphinx)/demo/robocup.dic"/>
     </node>
   </launch>
   
This command will run the ``recognizer.py`` script with loading the dictionary ``robocup.dic``.
A list of INFO messages will appear showing the loading of the recognition model. The last few messages will look like this:

.. code-block:: bash

    INFO: ngram_search_fwdtree.c(186): Creating search tree
    INFO: ngram_search_fwdtree.c(191): before: 0 root, 0 non-root channels, 12 single-phone words
    INFO: ngram_search_fwdtree.c(326): after: max nonroot chan increased to 328
    INFO: ngram_search_fwdtree.c(338): after: 77 root, 200 non-root channels, 11 single-phone words

Now, you can start saying some words to check if the recognizer will be able to understand what you are saying. For example, try to say the following words:

.. code-block:: python

   hello
   go to the room
   my name is 
   door
   follow room

You can also try different words. 

.. WARNING::
   It might be possible that the recognizer will detect words different from what you pronounced. This may be due to (1) bad microphone, in this case try to get a high-quality microphone, (2) your pronounciation is not enough clear. In this case, try to repeat the word. 

If the recognizer successfuly detected your spoken word, you can move to the next step to talk to your robot. 

The spoken words found by the recognizer will be published to the topic ``/recognizer/output``. Type 

.. code-block:: bash

   rostopic echo /recognizer/output 

in another terminal to see the results as follows:

.. code-block:: bash

    data: go to the room
    --
    data: hello
    --

To see all the predefined commands in the RoboCup demo, run the following commands:

.. code-block:: c
   
   roscd pocketsphinx/demo
   more robocup.corpus

Try saying a word that is not in the list such as "the food is hot" and see the results on the topic ``/recognizer/output``, which will show something different. The recognizer will always try to find the nearest match to the word you say.

.. WARNING::
  Make sure that you mute the recognizer when not using it because this will send random data to the robot.


Code and dependencies
=====================
The scripts of voice teleoperation can be found in ``gaitech_doc/src/turtlebot/voice_teleop/`` that you imported from GITHUB. Make sure that you imported the code from GITHUB. 
If you did not import the code from GITHUB, you can still create a new ROS package as follow:
* Go to your catkin workspace and then go to ``~/catkin_ws/src/`` 
* Create new a ROS package called ``gaitech_doc`` (or choose any other name) which depends on ``pocketsphinx``, ``roscpp``, ``rospy``, ``sound_play`` and ``std_msgs`` as follow:

.. code-block:: bash

      catkin_create_pkg gaitech_doc roscpp rospy pocketsphinx sound_play std_msgs

 
 
* In the ``~/catkin_ws/src/``, write the following command to see all the files and folders created:

.. code-block:: bash

      tree gaitech_doc

*  Now, compile your newly added package:

.. code-block:: bash

      $ cd ~/catkin_ws
      ~/catkin_ws$ catkin_make

*  Finally, open your ``package.xml`` file and add all the required dependencies (otherwise, your project will not find required packages):

.. code-block:: xml

    <!-- Remove the commented parts -->
    <package>
     <name>gaitech_doc</name>
     <version>0.0.1</version>
     <description>gaitech_doc</description>
     <maintainer email="ros@todo.todo">ros</maintainer>
     <license>TODO</license>
     <buildtool_depend>catkin</buildtool_depend>
     <build_depend>pocketsphinx</build_depend>
     <build_depend>roscpp</build_depend>
     <build_depend>rospy</build_depend>
     <build_depend>sound_play</build_depend>
     <build_depend>std_msgs</build_depend>
     <run_depend>pocketsphinx</run_depend> 
     <run_depend>roscpp</run_depend>
     <run_depend>rospy</run_depend>
     <run_depend>sound_play</run_depend>
     <run_depend>std_msgs</run_depend>
    </package>

Now, you are done with creating the ROS package. 


Create Your Vocabulary of Commands
==================================

In this section, you will learn how to add a vocabulary or corpus as it is specified in the ``PocketSphinx``. 
In partiuclar, we will create a simple vocabulary of commands to move the turtlebot robot forward, backward, and rotate it left and right. 

Create a folder and call it ``config`` and inside this folder create a ``txt`` file called ``motion_commands.txt`` 
and put the following commands (which you can extend more later) for the robot motion:

.. code-block:: python

    move forward
    move backwards
    turn right
    turn left

Feel free to add/delete/change any command you want as long as you follow the conventions.

.. TIP::
    Do not use punctuation marks and pay attention to the upper and lower case letters. 
    If you want to add a number you will have to spell it so you can not write 1, 55, 87..etc instead write one, fifty five, eighty seven.

After editing the ``motion_commands.txt`` file, you have to compile it into special dictionary and pronounciation files so it matches the specification for the ``PocketSphinx``. 
The online CMU language model (lm) tool is very useful in this case, visit their `website <http://www.speech.cs.cmu.edu/tools/lmtool-new.html>`_  and  upload your file. 
Click on the Compile Knowledge Base button, then download the file labeled ``COMPRESSED TARBALL`` that contains all the language model files 
that you need and the ``PocketSphinx`` can understand.

Extract these files into the config subdirectory of the ``gaitech_doc`` package (or your package where you are working this example). These files must be provided as an input parameter to ``recognizer.py`` node. 
To do so, you need to create a launch file as follow. 
   * First, create a folder and call it ``launch`` where to create launch files 
   * Then, create a file called ``recognizer.launch``, and add the following XML code: 

.. code-block:: xml

    <launch>
        <node name="recognizer" pkg="pocketsphinx" type="recognizer.py" output="screen">
          <param name="lm" value="$(find gaitech_doc)/turtlebot/voice_teleop/config/motion_commands.lm"/>
          <param name="dict" value="$(find gaitech_doc)/turtlebot/voice_teleop/config/motion_commands.dic"/>
        </node>
   </launch>

.. NOTE::
      If your package name is different from ``gaitech_doc`` make sure to consider this in the instruction ``value="$(find gaitech_doc)`` of the launch file. Otherwise, ROS will not be able to find the parameters.
      Make sure that you put the correct path for the ``lm`` and ``dic`` files. 

This file runs the ``recognizer.py`` node from the ``pocketsphinx`` package mentioned before in this tutorial. 
The last parameter which is ``output="screen"`` is used to let us see in real-time the recognition results in the launch window.

Launch the ``recognizer.launch`` file:

.. code-block:: bash
   
   roslaunch gaitech_doc recognizer.launch

and in another terminal run the following command to see the published topics after giving the robot a couple of commands:

.. code-block:: bash
   
   rostopic echo /recognizer/output

.. NOTE:: Make sure to close all the running launch files and all the demos running from previous examples before you run the previous commands.


A Voice-Control Navigation Script
=================================

In this section, we will present a small program ``src/turtlebot/voice_teleop/voice_teleop.py`` (``voice_teleop.cpp`` for C++) that will allow you to control your turtlebot robot using voice commands. 
The idea is simple. The program will subscribe to the topic ``/recognizer/output``, which is published by the node ``recognizer.py`` node of the ``pocketsphinx`` package using the dictionary of words that we create above.
Once a command is received, the callback function of the subscribed topic ``/recognizer/output`` will be executed to set the velocity of the robot based on the command received. 


Code Explanation
================

This is the content of the ``voice_teleop.py`` file in ``src/turtlebot/voice_teleop/`` directory:

.. code-block:: python

    #!/usr/bin/env python

    import rospy
    from geometry_msgs.msg import Twist
    from std_msgs.msg import String

    class RobotVoiceTeleop:
        #define the constructor of the class
        def  __init__(self):
            #initialize the ROS node with a name voice_teleop
            rospy.init_node('voice_teleop')
        
            # Publish the Twist message to the cmd_vel topic
            self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
            
            # Subscribe to the /recognizer/output topic to receive voice commands.
            rospy.Subscriber('/recognizer/output', String, self.voice_command_callback)
        
            #create a Rate object to sleep the process at 5 Hz
            rate = rospy.Rate(5)
        
            # Initialize the Twist message we will publish.
            self.cmd_vel = Twist()
            #make sure to make the robot stop by default
            self.cmd_vel.linear.x=0;
            self.cmd_vel.angular.z=0;
        
        
        
            # A mapping from keywords or phrases to commands
            #we consider the following simple commands, which you can extend on your own
            self.commands =             ['stop',
                                    'forward',
                                    'backward',
                                    'turn left',
                                    'turn right',
                                    ]
            rospy.loginfo("Ready to receive voice commands")
            # We have to keep publishing the cmd_vel message if we want the robot to keep moving.
            while not rospy.is_shutdown():
                self.cmd_vel_pub.publish(self.cmd_vel)
                rate.sleep()


        def voice_command_callback(self, msg):
            # Get the motion command from the recognized phrase
            command = msg.data
            if (command in self.commands):
                if command == 'forward':
                    self.cmd_vel.linear.x = 0.2
                    self.cmd_vel.angular.z = 0.0
                elif command == 'backward':
                    self.cmd_vel.linear.x = -0.2
                    self.cmd_vel.angular.z = 0.0
                elif command == 'turn left':
                    self.cmd_vel.linear.x = 0.0
                    self.cmd_vel.angular.z = 0.5
                elif command == 'turn right':
                    self.cmd_vel.linear.x = 0.0
                    self.cmd_vel.angular.z = -0.5
                elif command == 'stop':
                    self.cmd_vel.linear.x = 0.0
                    self.cmd_vel.angular.z = 0.0

            else: #command not found
                #print 'command not found: '+command
                self.cmd_vel.linear.x = 0.0
                self.cmd_vel.angular.z = 0.0
            print ("linear speed : " + str(self.cmd_vel.linear.x))
            print ("angular speed: " + str(self.cmd_vel.angular.z))



    if __name__=="__main__":
        try:
          RobotVoiceTeleop()
          rospy.spin()
        except rospy.ROSInterruptException:
          rospy.loginfo("Voice navigation terminated.")


     
To execute the code, we create the following launch file called ``turtlebot_voice_teleop_stage.launch`` that will run the ``recognizer.py`` node, ``voice_teleop.py`` node and ``turtlebot_stage`` simulator. 

.. code-block:: xml
    
    <launch>
       <node name="recognizer" pkg="pocketsphinx" type="recognizer.py" output="screen">
          <param name="lm" value="$(find gaitech_doc)/src/turtlebot/voice_teleop/config/motion_commands.lm"/>
          <param name="dict" value="$(find gaitech_doc)/src/turtlebot/voice_teleop/config/motion_commands.dic"/>
      </node>
   
      <node name="voice_teleop" pkg="gaitech_doc" type="voice_teleop.py" output="screen">
         <remap from="/cmd_vel" to="/cmd_vel_mux/input/teleop"/>
      </node>
      
      <include file="$(find turtlebot_stage)/launch/turtlebot_in_stage.launch"/> 
   </launch>

The first node starts the ``recognizer.py`` with the ``motion_command`` dictionary that we created previously.
The scond node starts the ``voice_teleop.py`` node that will receives the voice commands and map them to velocities. 
The third node starts the ``turtlebot_in_stage`` simulator and brings-up the turtlebot robot in simulatiion. This is equivalent to the command ``roslaunch turtlebot_stage turtlebot_in_stage.launch``. It also possible to run the ``voice_teleop.py`` node with Turtlebot Gazebo simulator by changing the last line of the launch file with

.. code-block:: xml
    
    <launch>
    ...
      <include file="$(find turtlebot_gazebo)/launch/turtlebot_world.launch"/>
    </launch>


.. TIP::
    It is important to note the topic remapping instruction ``<remap from="/cmd_vel" to="/cmd_vel_mux/input/teleop"/>`` in the launch file for the ``voice_teleop.py`` node. 
    In fact, the ``voice_teleop.py`` node publishes velocities to the topic ``/cmd_vel``, whereas the turtlebot_stage simulator wait for velocities on the topic ``/cmd_vel_mux/input/teleop``.
    This is the reason why we need to remap  the topic ``/cmd_vel`` to ``/cmd_vel_mux/input/teleop``. For more information about the ``<remap>`` tag, refer to `<remap> page in ROS WiKi <http://wiki.ros.org/roslaunch/XML/remap>`_.


Testing the Voice-Control in the Gazebo and Stage Simulators
============================================================
To test the voice teleopration using ``Turtlebot Stage simulator``, simply launch the launch file specified above as follows:

.. code-block:: bash

   roslaunch gaitech_doc turtlebot_voice_teleop_stage.launch

.. image:: images/voice_teleop_stage.png
    :align: center

Or, if you want to test with ``Turtlebot Gazebo Simulator``, simply run the following: 

.. code-block:: bash

   roslaunch gaitech_doc turtlebot_voice_teleop_gazebo.launch

.. image:: images/voice_teleop_gazebo.png
    :align: center

This is equivalent to running the following three commands in three terminals:

.. code-block:: bash

   roslaunch gaitech_doc recognizer.launch
   rosrun gaitech_doc voice_teleop.py
   roslaunch turtlebot_stage turtlebot_in_stage.launch 

.. NOTE::
     These simulators requires a powerful PC with a good graphics card that can launch them. They also may crash once you start them but don't worry this is very normal, just rerun the script until it launches.
     Make sure to check your Mic settings as described above. If you got an error running the ``recognizer`` node then try installing the following package:

     .. code-block:: bash

        sudo apt-get install gstreamer0.10-gconf


To able to view the commands that are recognizable by the robot we have to run the ``rqt_console`` using the following command:

.. code-block:: bash

   rqt_console &


Now, test your robot by giving it any command from the list of commands you create above.

.. NOTE::
   Note that it is possible that commands are not correctly recognized if your voice is not clear or your microphone is not good enough. Try with high quality microphone for more reliable results.

You can then update the code to add more commands, such as ``faster``, to increase the speed of the robot, ``slower``, to decrease the speed of the robot. The file  ``voice_teleop_advanced.py`` contains a more elaborated example with more commands. 


Testing the Voice-Control with a Real Turtlebot Robot
=====================================================

Now, you will test the voice teleoperation with a real turtlebot robot. 

.. WARNING::
    Before you test the robot make sure that your robot is in an open space with no obstacles or edges next to it.
    Also, make sure that your computer machine is correctly configured to work with the Turtlebot laptop as in the :ref:`network-config-doc`.

From the ROS Master gaitech_doc laptop run the following commands:

.. code-block:: bash

   roslaunch turtlebot_bringup minimal.launch

To make the monitoring process easier bring up ``rqt_console`` by running:

.. code-block:: bash

   rqt_console &

On the host node(the user PC) run the ``voice_teleop.launch`` file:

.. code-block:: bash

   roslaunch gaitech_doc voice_teleop.launch

.. TIP::
    Try a simple command at first like the rotate right to avoid any accidents. 
    You can change the robot's speed by giving the command "go faster" or "slow down" and this will change the parameters for speed in the ``turtlebot_voice_teleop.launch`` file. 
    However, you will have to add the commands as mentioned previously in the ``config/voice_teleop.txt`` file and redo all he steps again.

Video Demonstration
===================

.. youtube :: mZ4-HIYWWOI

Hands-on Activities
===================

In these section, you will extend the example above and implement a smarter version of the voice teleoperation application. 

Question 1: Extending Voice Vocabulary
--------------------------------------

Extend the example above to consider more voice commands to control the robot motion. Implement the following commands:

* define the following variables:

   * ``start_speed`` : the initial speed used when starting the script. 
   * ``linear_increment`` : a certain increment to add/substract to linear velocity. The default value is 0.05
   * ``angular_increment`` : a certain increment to add/substract the angular velocity. The default value is 0.4
   * ``max_speed``: the maximum linear velocity allowed
   * ``max_angular_speed`` : the maximum angular velocity allowed
* **rotate left**: makes the robot rotate to the left  (with a linear velocity equal to zero)
* **rotate right**: makes the robot rotate to the right  (with a linear velocity equal to zero)
* **turn left**: if the linear velocity is different from zero, it increases the angular velocity with ``linear_increment``. If the linear velocity is zero, it sets the angular velocity to the default angular speed (e.g. 0.5)
* **turn right**: if the linear velocity is different from zero, it decreases the angular velocity with ``angular_increment``. If the linear velocity is zero, it sets the angular velocity to the default negative angular speed (e.g. -0.5) 
* **slower**: decreases the linear velocity by the increment ``linear_increment``and the angular velocity by the increment ``angular_increment``
* **faster**: increases the linear velocity by the increment ``linear_increment``and the angular velocity by the increment ``angular_increment``
* **half**: sets the linear and angular velocities to the half of their current values. 
* **full**: sets the linear speeds to the maximum speed value

Make sure that all speeds are within the range of the minimum and maximum speeds allowed. 

After modification, test you code as illustrated above on both simulated and real turtlebot robot. 


Question2: Leveraging the Use of Launch Files
---------------------------------------------
The variables defined above ``linear_increment``, ``angular_increment``, ``max_speed`` and ``max_angular_speed`` are set based on the user's preference. 
It is more appropriate to set these values as parameters into the launch file and then read these parameters from your program or script before using them.

Modify the code so that to allow the user to define these parameters from the launch file. 

.. Hint::
   You should use ``rospy.get_param("~param_name", default_value)`` in Python to read a parameter from a launch file and
   use ``nh.getParam("/global_name", global_name)``  in C++. For more details refer to `Python Parameter Server <http://wiki.ros.org/rospy/Overview/Parameter%20Server>`_   and `C++ Parameter Server <http://wiki.ros.org/roscpp/Overview/Parameter%20Server>`_. 


Question3: Enabling/Disabling Voice Teleopration
------------------------------------------------

Now, you will add a new functionality to either enable or disable the voice teleopration. 
For this, you need to add two keywords into the vocabulary. 
   * ``pause``: when the user says ``pause`` the voice teleoperation should be paused. It means even if the user says more voice commands, they will not be executed
   * ``resume``: when the user says ``resume``, the voice teleopration is resumed and voice commands will be executed again.  

Make necessary changes to provide these functionalities. 
                         
                                    


