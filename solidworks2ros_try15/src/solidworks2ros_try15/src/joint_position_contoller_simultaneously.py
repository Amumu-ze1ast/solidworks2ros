#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import sys


def publish_joint_positions(joint_position):

    # Initialize the ROS node
    rospy.init_node('joint_position_commander', anonymous=True)

    # Publishers for joint 1 and joint 2
    pub_joint1 = rospy.Publisher('/joint_1_controller/command', Float64, queue_size=10)
    # pub_joint2 = rospy.Publisher('/joint_2_controller/command', Float64, queue_size=10)
    pub_joint3 = rospy.Publisher('/joint_3_controller/command', Float64, queue_size=10)
    pub_joint4= rospy.Publisher('/joint_4_controller/command', Float64, queue_size=10)


    # Wait for a short time to ensure the publishers are registered
    rospy.sleep(1.0)

    pub_joint1.publish(joint_position)
    pub_joint3.publish(joint_position)
    pub_joint4.publish(joint_position)

    # Sleep to allow time for messages to be sent
    rospy.sleep(1.0)


if __name__ == "__main__":
    try:

        # Get joint positions from command-line arguments
        joint2_position = float(sys.argv[1])  # Position for joint 2

        # Publish the joint positions
        publish_joint_positions(joint2_position)

        

    except rospy.ROSInterruptException:
        pass
