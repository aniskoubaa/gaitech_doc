
#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/String.h>
#include "boost/thread/mutex.hpp"
#include "boost/thread/thread.hpp"
#include "ros/console.h"
#include <string>

std_msgs::String readCommand;

class RobotVoiceTeleop
{
public:
	RobotVoiceTeleop();

private:
	void commandCallBack(const std_msgs::String& command);
	void publish();

	ros::NodeHandle nodeHandle;


	int linearVelocity, angularVelocity;
	ros::Publisher velocityPublisher;
	ros::Subscriber voiceCommandSubscriber;
	geometry_msgs::Twist cmd_vel;


};
/** constructor **/
RobotVoiceTeleop::RobotVoiceTeleop():
		  nodeHandle("~"),
		  linearVelocity(1),
		  angularVelocity(0)
{
	nodeHandle.param("linear_velocity", linearVelocity, linearVelocity);
	nodeHandle.param("angular_velocity", angularVelocity, angularVelocity);

	velocityPublisher = nodeHandle.advertise<geometry_msgs::Twist>("/cmd_vel", 1);
	voiceCommandSubscriber = nodeHandle.subscribe("/recognizer/output", 1000, &RobotVoiceTeleop::commandCallBack, this);


	ros::Rate rate(5);
	while (ros::ok()){
		velocityPublisher.publish(cmd_vel);
		rate.sleep();
	}

}
/** callback **/
void RobotVoiceTeleop::commandCallBack(const std_msgs::String& command)
{ 
	geometry_msgs::Twist vel;

	if(command.data.compare("stop") == 0)
	{
		vel.angular.z = 0;
		vel.linear.x = 0;
	}
	else if(command.data.compare("forward") == 0)
	{
		vel.linear.x = 0.3;
		vel.angular.z = 0;
	}
	else if(command.data.compare("backward") == 0)
		{
			vel.linear.x = -0.3;
			vel.angular.z = 0;
		}
	else if(command.data.compare("left") == 0)
		{
			vel.linear.x = 0.0;
			vel.angular.z = 0.5;
		}
	else if(command.data.compare("right") == 0)
			{
				vel.linear.x = 0.0;
				vel.angular.z = -0.5;
			}
	else {
		vel.angular.z = 0;
		vel.linear.x = 0;
	}

	printf("vel.linear.x = %.2f, vel.angular.z = %.2f", vel.linear.x, vel.angular.z);

}


int main(int argc, char** argv)
{
	ros::init(argc, argv, "voice_teleop_node");
	RobotVoiceTeleop voice_teleop;
	ros::spin();
}
