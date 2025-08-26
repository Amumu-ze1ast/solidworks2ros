# Install script for directory: /home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try27/src/solidworks2ros_try27

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try27/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try27/build/solidworks2ros_try27/catkin_generated/installspace/solidworks2ros_try27.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/solidworks2ros_try27/cmake" TYPE FILE FILES
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try27/build/solidworks2ros_try27/catkin_generated/installspace/solidworks2ros_try27Config.cmake"
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try27/build/solidworks2ros_try27/catkin_generated/installspace/solidworks2ros_try27Config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/solidworks2ros_try27" TYPE FILE FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try27/src/solidworks2ros_try27/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/solidworks2ros_try27" TYPE PROGRAM FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try27/build/solidworks2ros_try27/catkin_generated/installspace/moment_of_inertia.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/solidworks2ros_try27" TYPE PROGRAM FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try27/build/solidworks2ros_try27/catkin_generated/installspace/joint_position_contoller_forward.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/solidworks2ros_try27" TYPE PROGRAM FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try27/build/solidworks2ros_try27/catkin_generated/installspace/joint_position_contoller_backward.py")
endif()

