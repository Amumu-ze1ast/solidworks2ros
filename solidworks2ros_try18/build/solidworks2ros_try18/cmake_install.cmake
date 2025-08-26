# Install script for directory: /home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/src/solidworks2ros_try18

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install")
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
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install" TYPE PROGRAM FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install" TYPE PROGRAM FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/setup.bash;/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install" TYPE FILE FILES
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/setup.bash"
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/setup.sh;/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install" TYPE FILE FILES
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/setup.sh"
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/setup.zsh;/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install" TYPE FILE FILES
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/setup.zsh"
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/setup.fish;/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/local_setup.fish")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install" TYPE FILE FILES
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/setup.fish"
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/local_setup.fish"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/install" TYPE FILE FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/.rosinstall")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/solidworks2ros_try18.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/solidworks2ros_try18/cmake" TYPE FILE FILES
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/solidworks2ros_try18Config.cmake"
    "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/catkin_generated/installspace/solidworks2ros_try18Config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/solidworks2ros_try18" TYPE FILE FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/src/solidworks2ros_try18/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/solidworks2ros_try18/config" TYPE DIRECTORY FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/src/solidworks2ros_try18/config/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/solidworks2ros_try18/launch" TYPE DIRECTORY FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/src/solidworks2ros_try18/launch/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/solidworks2ros_try18/meshes" TYPE DIRECTORY FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/src/solidworks2ros_try18/meshes/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/solidworks2ros_try18/urdf" TYPE DIRECTORY FILES "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/src/solidworks2ros_try18/urdf/")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/gtest/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/live4jesus/me_solidworks2ros/solidworks2ros/solidworks2ros_try18/build/solidworks2ros_try18/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
