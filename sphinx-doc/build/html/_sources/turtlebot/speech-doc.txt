.. _speech-doc:

=============================
Turtlebot Voice Teleoperation
=============================

This tutorial will introduce how to control your turtlebot robot using speech recognition.

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials and your network set-up is working fine between the ROS Master node and the host node.

In this tutorial you will learn how to:

   * Teleoprate a real and simulated turtlebot with voice commands
   * Create a custom voice-command vocabulary  
   * Work with pocket-sphinx package in ROS 


Install PocketSphinx for Speech Recognition
===========================================

In order to download the ``pocketsphinx`` package on Ubuntu you need to install the ``gstreamer0.10-pocketsphinx`` and the ROS sound drivers.

.. code-block:: linux

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

.. code-block:: linux

   roscd pocketsphinx

In the directory ``demo/``, you can observe the voice commands and dictionary. You may want to have a look at their content using ``more`` or ``nano`` text viewers. 
Then, run the following command:

.. code-block:: linux

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

.. code-block:: linux

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

.. code-block:: linux

   rostopic echo /recognizer/output 

in another terminal to see the results as follows:

.. code-block:: linux

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

   .. code-block:: linux

      catkin_create_pkg gaitech_doc roscpp rospy pocketsphinx sound_play std_msgs

 
 
   * In the ``~/catkin_ws/src/``, write the following command to see all the files and folders created:

   .. code-block:: linux

      tree gaitech_doc

   *  Now, compile your newly added package:

   .. code-block:: linux

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
   * Then, create a file called ``voice_teleop.launch``, and add the following XML code: 

.. code-block:: xml

    <launch>
        <node name="recognizer" pkg="pocketsphinx" type="recognizer.py" output="screen">
          <param name="lm" value="$(find gaitech_doc)/turtlebot/voice_teleop/config/motion_commands.lm"/>
          <param name="dict" value="$(find gaitech_doc)/turtlebot/voice_teleop/config/motion_commands.dic"/>
        </node>
   </launch>

.. NOTE::
      If your package name is different from ``gaitech_doc`` make sure to consider this in the instruction ``value="$(find gaitech_doc)`` of the launch file. Otherwise, ROS will not be able to find the parameters
      Make sure that you put the correct path for the ``lm`` and ``dic`` files. 

This file runs the ``recognizer.py`` node from the ``pocketsphinx`` package mentioned before in this tutorial. 
The ``lm`` and ``dict`` parameters are mentioned how are they created and what is their use in the files ``motion_commands.lm`` and ``motion_commands.dic`` created in the previous step.
The last parameter which is ``output="screen"`` is used to let us see in real-time the recognition results in the launch window.

Launch the ``voice_teleop.launch`` file:

.. code-block:: linux
   
   roslaunch gaitech_doc voice_teleop.launch

and in another terminal run the following command to see the published topics after giving the robot a couple of commands:

.. code-block:: linux
   
   rostopic echo /recognizer/output

.. NOTE:: Make sure to close all the running launch files and all the demos running from previous examples before you run the previous commands.


A Voice-Control Navigation Script
=================================

As mentioned before the ``recognizer.py`` node in the `pocketsphinx` package publishes a topic called ``/recognizer/output``. But there must be a file that subscribes to this topic and gives orders to the robot according to the commands given by the user.
The ``voice_nav.py`` file in the `pocketsphinx` package maps the commands into `Twist` messages that can be used to control your turtlebot robot.
You can find this file in the ``turtlebot_cont_movement/nodes`` subdirectory.


Code Explanation
================

This is the content of the ``voice_nav.py`` file:

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
           self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=5)
           
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
                                       'rotate left',
                                       'rotate right',
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
               elif command == 'rotate left':
                   self.cmd_vel.linear.x = 0.0
                   self.cmd_vel.angular.z = 0.5
               elif command == 'rotate right':
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
   
[******* Anis: I STOPPED HERE  ********]   
Now create another launch file called ``turtlebot_voice_teleop.launch`` and its content should be:

.. code-block:: xml
    
    <launch>
     <node name="voice_nav" pkg="turtlebot_cont_movement" type="voice_nav.py" output="screen">
     <param name="scale_linear" value="0.5" type="double"/>
     <param name="scale_angular" value="1.5" type="double"/>
     <param name="max_speed" value="0.3"/>
     <param name="start_speed" value="0.1"/>
     <param name="linear_increment" value="0.05"/>
     <param name="angular_increment" value="0.4"/>
     </node>
    </launch>

This file controls the speed of the robot while moving.

.. NOTE:: 
    The increment speed parameters will be used when you add a command related to them such as `go faster`, `faster` or `go slower`, `slow`


Testing the Voice-Control in the Gazebo and Stage Simulators
============================================================

This section introduce how to test the voice recognition with the Gazebo and Stage simulators. 

Now let's bring up `Gazebo`  with the simulation config file:

.. code-block:: linux

   roslaunch turtlebot_gazebo turtlebot_world.launch

OR

Bring up `Stage`  simulator using the following command:

.. code-block:: linux

   roslaunch turtlebot_stage turtlebot_in_stage_no_rviz.launch

.. NOTE::
    These simulators requires a powerful PC with a good graphics card that can launch them. They also may crash once you start them but don't worry this is very normal, just rerun the script until it launches.

To able to view the commands that are recognizable by the robot we have to run the ``rqt_console`` using the following command:

.. code-block:: linux

   rqt_console &

.. NOTE:: 
    Make sure to check your Mic settings as discribed before. 

Run the ``cont_movement.launch`` file which runs the ``voice_nav.py`` file:

.. code-block:: linux

   roslaunch turtlebot_cont_movement cont_movement.launch

The following command is responsible for controlling the speed of the robot:

.. code-block:: linux

   roslaunch turtlebot_cont_movement turtlebot_voice_cont_movement.launch

Now test your robot by giving it any command from the list mentiond previously.

Testing the Voice-Control with a Turtlebot Robot
================================================

.. NOTE::
    Before you test the robot make sure that your robot is in an open space with no obstacles or edges next to it.

From the ROS Master node(the Turtlebot's laptop) run the following commands:

.. code-block:: linux

   roslaunch rbx1_bringup turtlebot_minimal_create.launch

To make the monitoring process easier bring up `rqt_console` by running:

.. code-block:: linux

   rqt_console &

.. NOTE::
    Check your sound settings as mentioned before.

On the host node(the user PC) run the ``cont_movement.launch`` file:

.. code-block:: linux

   roslaunch turtlebot_cont_movement cont_movement.launch

and in another terminal run the following command:

.. code-block:: linux

   roslaunch turtlebot_cont_movement turtlebot_voice_cont_movement.launch

.. TIP::
    Try a simple command at first like the rotate right to avoid any accidents. You can change the robot's speed by giving the command "go faster" or "slow down" and this will change the parameters for speed in the turtlebot_voice_nav.launch file. However, you will have to add the commands as mentioned previously in the `config/cont_movement.txt` file and redo all he steps again.


##import: speech-video in this location
