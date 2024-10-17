#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import sys

def publish_joint_positions(joint1_position, joint2_position):

    # Initialize the ROS node
    rospy.init_node('joint_position_commander', anonymous=True)

    # Publishers for joint 1 and joint 2
    pub_joint1 = rospy.Publisher('/joint_1_controller/command', Float64, queue_size=10)
    pub_joint2 = rospy.Publisher('/joint_2_controller/command', Float64, queue_size=10)

    # Wait for a short time to ensure the publishers are registered
    rospy.sleep(1.0)

    # Publish position to joint 1 first
    rospy.loginfo(f"Publishing {joint1_position} radians to joint 1")
    pub_joint1.publish(joint1_position)
    
    # Delay before sending the second command
    rospy.sleep(2.0)  # Add a delay of 2 seconds before sending to joint 2 (adjust as needed)

    # Publish position to joint 2
    rospy.loginfo(f"Publishing {joint2_position} meters to joint 2")
    pub_joint2.publish(joint2_position)

    # Sleep to allow time for the last message to be sent
    rospy.sleep(1.0)


if __name__ == "__main__":
    try:
        # Ensure two arguments are passed (positions for both joints)
        if len(sys.argv) < 3:
            rospy.logerr("Please provide positions for both joint 1 and joint 2.")
            sys.exit(1)

        # Get joint positions from command-line arguments
        joint1_position = float(sys.argv[1])  # Position for joint 1
        joint2_position = float(sys.argv[2])  # Position for joint 2

        # Publish the joint positions one after the other
        publish_joint_positions(joint1_position, joint2_position)

    except rospy.ROSInterruptException:
        pass
