cmake_minimum_required(VERSION 2.8.3)
project(gaitech_doc)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)


add_executable(voice_teleop_node src/turtlebot/voice_teleop/voice_teleop.cpp)
add_executable(joy_teleop src/turtlebot/voice_teleop/joy_teleop.cpp)

target_link_libraries(voice_teleop_node ${catkin_LIBRARIES})
target_link_libraries(joy_teleop ${catkin_LIBRARIES})

#add_executable(send_goals src/send_goals.cpp)
#target_link_libraries(send_goals ${catkin_LIBRARIES})

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES gaitech_doc
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)


include_directories(
  ${catkin_INCLUDE_DIRS}
)
