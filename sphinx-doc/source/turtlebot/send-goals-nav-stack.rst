.. _send-goals-nav-stack:

=====================================
Sending Goals to the Navigation Stack
=====================================

In this tutorial you will learn how to send destination goals to your robot through the navigation stack without crashing in any obstacle that maybe in the robot's world. We will use the RViz as a simulator to test our programs first. The user will have the option either to set the goal by clicking on the location on the map and the robot has to deal with the rest or by setting the goal by writing a code for the robot which is the aim of this tutorial. 

.. WARNING::
    Make sure that you completed installing all the required packages in the previous tutorials, your network set-up is working fine between the ROS Master node and the host node and your navigation stack is working properly.

Create a Package
================

You need to create a file for the program in the following directory ``src/turtlebot/navigation/map_navigation/map_navigation.cpp`` and write the following. The code is well commented so no need for furthur explanation:

.. code-block:: cpp
	
	#include <ros/ros.h>
	
	//The following line is where we import the ``MoveBaseAction`` library which is responsible for accepting goals from users and move the robot to the specified location in its world.
	#include <move_base_msgs/MoveBaseAction.h>

	#include <actionlib/client/simple_action_client.h>

	//this line is where we create the client that will communicate with actions that adhere to the base station interface
	typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;

	int main(int argc, char** argv){
  	ros::init(argc, argv, "map_navigation");

  	//tell the action client that we want to spin a thread by default
  	MoveBaseClient ac("move_base", true);

  	//wait for the action server to come up and then start the process
  	while(!ac.waitForServer(ros::Duration(5.0))){
    	ROS_INFO("Waiting for the move_base action server to come up");
  	}

  	//This is where you create the goal to send to move_base using move_base_msgs::MoveBaseGoal messages to tell the robot to move one meter forward in the coordinate frame.
  	move_base_msgs::MoveBaseGoal goal;

  	//we'll send a goal to the robot to move 1 meter forward
  	goal.target_pose.header.frame_id = "base_link";
  	goal.target_pose.header.stamp = ros::Time::now();

  	goal.target_pose.pose.position.x = 0.2;
  	goal.target_pose.pose.orientation.w = 0.2;

  	ROS_INFO("Sending goal");

  	//this command sends the goal to the move_base node to be processed
  	ac.sendGoal(goal);

  	//After finalizing everything you have to wait for the goal to finish processing
  	ac.waitForResult();

  	//here we check for the goal if it succeded or failed and send a message according to the goal status.
  	if(ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
    	ROS_INFO("Hooray, the base moved 1 meter forward");
  	else
    	ROS_INFO("The base failed to move forward 1 meter for some reason");

  	return 0;
	}

Build the package and Run it
============================

In order to build up your file you just created need to edit your ``CMakeLists.txt`` file. Open the file and add the following lines to the bottom of the file.

.. code-block:: python
	
	add_executable(map_navigation src/turtlebot/navigation/map_navigation/map_navigation.cpp)
	target_link_libraries(map_navigation ${catkin_LIBRARIES})


Build your workspace:

.. code-block:: linux
	
	catkin_make

After that you need to start your Navigation Stack and check that the name of the action is similar to what we wrote in the program above or not:

.. code-block:: linux
	
	rostopic list | grep move_base/goal

If you saw some results then you have no errors otherwise just change the name of the action in the ``map_navigation.cpp`` file to match the one in the robot navigation stack.

Then run the executable file you created before:

.. code-block:: linux
	
	./bin/map_navigation

And you will notice your robot moving forward for 1 meter. 		
