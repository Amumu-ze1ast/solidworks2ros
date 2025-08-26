#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64, Float64MultiArray
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

def send_joint_commands(x, y, z, o):
    global current_joint_positions

    # Initialize the ROS node
    rospy.init_node('send_joint_commands')

    # Create a publisher for the joint group controller command

    pub_x_axis = rospy.Publisher('/joint_Xaxis_position_controller/command', Float64, queue_size=10)
    pub_y_axis = rospy.Publisher('/joint_Yaxis_position_controller/command', Float64, queue_size=10)
    pub_rope   = rospy.Publisher('/joint_ropeGroup_position_controller/command', Float64MultiArray, queue_size=10)
    pub_z_axis = rospy.Publisher('/joint_Zaxis_position_controller/command', Float64, queue_size=10)

    pub_trolley = rospy.Publisher('/joint_trolley_position_controller/command', Float64, queue_size=10)
    pub_gripper = rospy.Publisher('/joint_gripper_right_position_controller/command', Float64, queue_size=10)

    # Subscribe to the joint states topic to receive feedback
    rospy.Subscriber("/joint_states", JointState, joint_state_callback)

    # Wait for the publisher and subscriber to be ready
    rospy.sleep(1)

    # Ensure we have received current joint positions
    if not current_joint_positions:
        rospy.logwarn("No joint states received yet.")
        return

    joint_positions = Float64MultiArray()
    joint_rope = Float64MultiArray()

    # Copy the current joint states into a modifiable list
    joint_positions.data = list(current_joint_positions)

    # Modify only the x-axis (joint 1)
    joint_positions.data[0] = x  # x-axis is joint 1
    pub_x_axis.publish(x)
    rospy.loginfo("Sent x-axis command: %s", joint_positions.data)


    # Wait until joint 1 reaches the target
    while not has_reached_target(0, x):
        rospy.sleep(0.1)  # Check every 100ms

    # Modify only the y-axis (joint 2), keep others unchanged
    joint_positions.data[1] = y  # y-axis is joint 2
    pub_y_axis.publish(y)
    rospy.loginfo("Sent y-axis command: %s", joint_positions.data)

    # Wait until joint 2 reaches the target
    while not has_reached_target(1, y):
        rospy.sleep(0.1)

    # Modify only the rope (joints 5 to 91)
    joint_positions.data[4] = min(0.5, z * (0.5 / 3))  # z-axis joint 5
    joint_positions.data[5] = min(1.0, z * (1.0 / 3))  # z-axis joint 6
    joint_positions.data[6] = min(1.5, z * (1.5 / 3))  # z-axis joint 7
    joint_positions.data[7] = min(2.0, z * (2.0 / 3))  # z-axis joint 8
    joint_positions.data[8] = min(2.5, z * (2.5 / 3))  # z-axis joint 9
    joint_positions.data[9] = min(3.0, z * (3.0 / 3))  # z-axis joint 10

    joint_rope.data = joint_positions.data[3:10]

    # print(joint_rope.data)

    pub_rope.publish(joint_rope)
    pub_trolley.publish(-0.5)
    rospy.loginfo("Sent ropes commands: %s", joint_positions.data)

    # Modify only the z-axis (joint 92)
    joint_positions.data[10] = z  # x-axis is joint 1
    pub_z_axis.publish(z)
    rospy.loginfo("Sent z-axis command: %s", joint_positions.data)

    # Optionally, wait for the z-axis joints to reach their target if needed
    while not has_reached_target(10, z):
        rospy.sleep(0.1)

    pub_trolley.publish(0.0)

    rospy.sleep(2)

    if open == 0:
        pub_gripper.publish(0)
    else:
        pub_gripper.publish(0.11)


if __name__ == '__main__':
    try:
        # Get joint positions from command-line arguments
        x_axis = float(sys.argv[1])  # Position for x_axis
        y_axis = float(sys.argv[2])  # Position for y_axis
        z_axis = float(sys.argv[3])  # Position for z_axis
        open   = float(sys.argv[4])  # Opening and closing of the gripper

        send_joint_commands(x_axis, y_axis, z_axis, open)

    except rospy.ROSInterruptException:
        pass
