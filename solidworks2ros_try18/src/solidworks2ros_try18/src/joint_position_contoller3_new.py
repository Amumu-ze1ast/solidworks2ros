#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import JointState
import sys

# Global variable to store the latest joint state feedback
current_joint_positions = []

def joint_state_callback(msg):
    global current_joint_positions
    current_joint_positions = msg.position  # Update current joint positions

def has_reached_target(joint_index, target_position, tolerance=0.01):
    global current_joint_positions
    if len(current_joint_positions) > joint_index:
        # Check if the current position is within the tolerance of the target
        return abs(current_joint_positions[joint_index] - target_position) < tolerance
    return False

def send_joint_commands(x, y, z, gripper):
    global current_joint_positions

    # Initialize the ROS node
    rospy.init_node('send_joint_commands')

    # Create a publisher for the joint group controller command
    pub = rospy.Publisher('/joint_group_controller/command', Float64MultiArray, queue_size=10)

    # Subscribe to the joint states topic to receive feedback
    rospy.Subscriber("/joint_states", JointState, joint_state_callback)

    # Wait for the publisher and subscriber to be ready
    rospy.sleep(1)

    # Ensure we have received current joint positions
    if not current_joint_positions:
        rospy.logwarn("No joint states received yet.")
        return

    joint_positions = Float64MultiArray()

    # Copy the current joint states into a modifiable list
    joint_positions.data = list(current_joint_positions)

    # Modify only the x-axis (joint 1)
    joint_positions.data[0] = x  # x-axis is joint 1
    joint_positions.data[1] = y  # y-axis is joint 2

    # Modify only the z-axis (joints 5 to 11)
    joint_positions.data[4] = min(0.5, z * (0.5 / 3))  # z-axis joint 5
    joint_positions.data[5] = min(1.0, z * (1.0 / 3))  # z-axis joint 6
    joint_positions.data[6] = min(1.5, z * (1.5 / 3))  # z-axis joint 7
    joint_positions.data[7] = min(2.0, z * (2.0 / 3))  # z-axis joint 8
    joint_positions.data[8] = min(2.5, z * (2.5 / 3))  # z-axis joint 9
    joint_positions.data[9] = min(2.9, z * (2.9 / 3))  # z-axis joint 10
    joint_positions.data[10] = z                       # z-axis joint 11

    pub.publish(joint_positions)

    rospy.loginfo("Sent x-axis command: %s", joint_positions.data)
    rospy.loginfo("Sent y-axis command: %s", joint_positions.data)
    rospy.loginfo("Sent z-axis commands: %s", joint_positions.data)
    


    # Wait until joints reaches the target
    while not has_reached_target(0, x):
        rospy.sleep(0.1)  # Check every 100ms
    
    while not has_reached_target(1, y):
        rospy.sleep(0.1)

    while not has_reached_target(10, z):
        rospy.sleep(0.1)

    rospy.sleep(1.5)
    
    joint_positions.data[11] = 0                       # joint 12 = power_screw
    joint_positions.data[12] = gripper                 # joint 13 = gripper_finger_1
    joint_positions.data[13] = gripper                 # joint 14 = gripper_finger_2

    pub.publish(joint_positions)
    rospy.loginfo("Sent gripper fingers commands: %s", joint_positions.data)

if __name__ == '__main__':
    try:
        # Get joint positions from command-line arguments
        x_axis = float(sys.argv[1])  # Position for x_axis
        y_axis = float(sys.argv[2])  # Position for y_axis
        z_axis = 2.9 - float(sys.argv[3])  # Position for z_axis
        gripper_close_open = float(sys.argv[4])  # Position for z_axis

        send_joint_commands(x_axis, y_axis, z_axis, gripper_close_open)

    except rospy.ROSInterruptException:
        pass
