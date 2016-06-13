
#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/String.h>
#include "boost/thread/mutex.hpp"
#include "boost/thread/thread.hpp"
#include "ros/console.h"
#include <string>

class TurtlebotTeleop
{
public:
  TurtlebotTeleop();

private:
  void commandCallBack(const std_msgs::String& command);
  void publish();

  ros::NodeHandle ph_, nh_;

  std_msgs::String readCommand;

  int linear_, angular_;
  double l_scale_, a_scale_;
  ros::Publisher vel_pub_;
  ros::Subscriber cmd_sub_;

  geometry_msgs::Twist last_published_;
  boost::mutex publish_mutex_;
  bool deadman_pressed_;
  bool zero_twist_published_;
  ros::Timer timer_;

};

TurtlebotTeleop::TurtlebotTeleop():
  ph_("~"),
  linear_(1),
  angular_(0),
  deadman_axis_(4),
  l_scale_(0.3),
  a_scale_(0.9)
{
  ph_.param("axis_linear", linear_, linear_);
  ph_.param("axis_angular", angular_, angular_);
  ph_.param("axis_deadman", deadman_axis_, deadman_axis_);
  ph_.param("scale_angular", a_scale_, a_scale_);
  ph_.param("scale_linear", l_scale_, l_scale_);

  deadman_pressed_ = false;
  zero_twist_published_ = false;

  vel_pub_ = ph_.advertise<geometry_msgs::Twist>("cmd_vel", 1, true);
  cmd_sub_ = nh_.subscribe<std_msgs::String>("command", 10, &TurtlebotTeleop::commandCallback, this);

  timer_ = nh_.createTimer(ros::Duration(0.1), boost::bind(&TurtlebotTeleop::publish, this));
}

void TurtlebotTeleop::commandCallBack(const std_msgs::String& command)
{ 
  readCommand = command;
  geometry_msgs::Twist vel;
  
  if(readCommand.data.compare("stop") == 0)
  {

    vel.angular.z = 0;
    vel.linear.x = 0;
  }
  else
  {
    vel.angular.z = 1;
    vel.linear.x = 1;
  }

//  vel.angular.z = a_scale_*joy->axes[angular_];
//  vel.linear.x = l_scale_*joy->axes[linear_];
//  last_published_ = vel;
//  deadman_pressed_ = joy->buttons[deadman_axis_];
}

void TurtlebotTeleop::publish()
{
  boost::mutex::scoped_lock lock(publish_mutex_);

  if (deadman_pressed_)
  {
    vel_pub_.publish(last_published_);
    zero_twist_published_=false;
  }
  else if(!deadman_pressed_ && !zero_twist_published_)
  {
    vel_pub_.publish(*new geometry_msgs::Twist());
    zero_twist_published_=true;
  }
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "voice_teleop");
  TurtlebotTeleop voice_teleop;

  ros::spin();
}