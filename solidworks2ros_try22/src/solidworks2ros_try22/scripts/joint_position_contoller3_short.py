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
        x,                            # x_axis = joint_1
        y,                            # y_axis = joint_2
        0.0,                          # pulley = joint_3
        0.0,                          # joint_4
        min(0.5, z * (0.5/3)),        # z_axis = joint 5's limit is 0.5
        min(1.0, z * (1.0/3)),        # z_axis = joint 6's limit is 1
        min(1.5, z * (1.5/3)),        # z_axis = joint 7's limit is 1.5
        min(2.0, z * (2.0/3)),        # z_axis = joint 8's limit is 2
        min(2.5, z * (2.5/3)),        # z_axis = joint 9's limit is 2.5
        min(3.0, z * (3.0/3)),        # z_axis = joint 10's limit is 3
        z]  

    # Publish the joint positions
    pub.publish(joint_positions)

    rospy.loginfo("Sent joint commands: %s", joint_positions.data)

if __name__ == '__main__':
    try:
        # Get joint positions from command-line arguments

        x_axis = float(sys.argv[1])     # Position for x_axis
        y_axis = float(sys.argv[2])     # Position for y_axis
        z_axis = 3.2-float(sys.argv[3]) # Position for z_axis

        send_joint_commands(x_axis, y_axis, z_axis)

    except rospy.ROSInterruptException:
        pass
