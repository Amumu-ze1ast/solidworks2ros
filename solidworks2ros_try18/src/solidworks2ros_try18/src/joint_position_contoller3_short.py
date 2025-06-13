#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64MultiArray
import sys

def send_joint_commands(x, y, z):
    # Initialize the ROS node
    rospy.init_node('send_joint_commands')

    # Create a publisher for the joint group controller command
    pub = rospy.Publisher('/joint_group_controller/command', Float64MultiArray, queue_size=10)

    # Wait for the publisher to be ready
    rospy.sleep(1)

    # Prepare the joint position command for joints 5 to 11
    joint_positions = Float64MultiArray()

    joint_positions.data = [
        x,                            # [0] joint_1 = x_axis
        y,                            # [1] joint_2 = y_axis
        0.0,                          # [2] joint_3 = pulley_trolley
        0.0,                          # [3] joint_4 = rope_holder
        min(0.5, z * (0.5/3)),        # [4] joint 5 = limit is 0.5 = z_axis
        min(1.0, z * (1.0/3)),        # [5] joint 6 = limit is 1.0 = z_axis
        min(1.5, z * (1.5/3)),        # [6] joint 7 = limit is 1.5 = z_axis
        min(2.0, z * (2.0/3)),        # [7] joint 8 = limit is 2.0 = z_axis
        min(2.5, z * (2.5/3)),        # [8] joint 9 = limit is 2.5 = z_axis
        min(2.9, z * (2.5/3)),        # [9] joint 10 = limit is 2.9 = z_axis
        z,                            # [10] joint 11 = gripper_holder = z_axis
        0.0,                          # [11] joint 12 = power_screw 
        0.0,                          # [12] joint 13 = gripper_finger_1
        0.0]                          # [13] joint 14 = gripper_finger_2  

    # Publish the joint positions
    pub.publish(joint_positions)

    rospy.loginfo("Sent joint commands: %s", joint_positions.data)

if __name__ == '__main__':
    try:
        # Get joint positions from command-line arguments

        x_axis = float(sys.argv[1])     # Position for x_axis
        y_axis = float(sys.argv[2])     # Position for y_axis
        z_axis = 2.9-float(sys.argv[3]) # Position for z_axis

        send_joint_commands(x_axis, y_axis, z_axis)

    except rospy.ROSInterruptException:
        pass
