# Previously

cmake_minimum_required(VERSION 2.8.3)

project(solidworks2ros_try22)

# new
find_package(catkin REQUIRED COMPONENTS
	roscpp
	rospy
	std_msgs
)

catkin_package()

include_directories(

	${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
	scripts/calculator.py
	scripts/joint_position_contoller.py
	scripts/joint_position_contoller2.py
	scripts/joint_position_contoller3_short.py
	scripts/joint_position_contoller4_short.py

	
	DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


add_executable(calculator src/calculator.cpp)
target_link_libraries(calculator ${catkinn_LIBRARIES})

# up to this

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
