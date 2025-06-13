cmake_minimum_required(VERSION 3.0.2)
project(solidworks2ros_try23)


find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package(

)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
  PROGRAMS
  scripts/moment_of_inertia.py
  scripts/joint_position_contoller_forward.py
  scripts/joint_position_contoller_backward.py
  
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


