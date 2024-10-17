#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import sys


def publish_joint_positions(joint_position):

    # Initialize the ROS node
    rospy.init_node('joint_position_commander', anonymous=True)

    # Publishers for all joints
    pub_joint5 = rospy.Publisher('/joint_5_controller/command', Float64, queue_size=10)
    pub_joint6 = rospy.Publisher('/joint_6_controller/command', Float64, queue_size=10)
    pub_joint7 = rospy.Publisher('/joint_7_controller/command', Float64, queue_size=10)
    pub_joint8 = rospy.Publisher('/joint_8_controller/command', Float64, queue_size=10)
    pub_joint9 = rospy.Publisher('/joint_9_controller/command', Float64, queue_size=10)
    pub_joint10 = rospy.Publisher('/joint_10_controller/command', Float64, queue_size=10)
    pub_joint11 = rospy.Publisher('/joint_11_controller/command', Float64, queue_size=10)

    # Wait for a short time to ensure the publishers are registered
    rospy.sleep(1.0)

    # Smooth the joint positions based on the input
    joint5 = min(0.5, joint_position * 0.167)  # Joint 5's limit is 0.5
    joint6 = min(1, joint_position * 0.333)    # Joint 6's limit is 1
    joint7 = min(1.5, joint_position * 0.5)    # Joint 7's limit is 1.5
    joint8 = min(2, joint_position * 0.667)    # Joint 8's limit is 2
    joint9 = min(2.5, joint_position * 0.833)  # Joint 9's limit is 2.5
    joint10 = min(3, joint_position)           # Joint 10's limit is 3
    joint11 = joint_position                   # Joint 11 directly tracks joint_position

    # Publish joint positions
    pub_joint5.publish(joint5)
    pub_joint6.publish(joint6)
    pub_joint7.publish(joint7)
    pub_joint8.publish(joint8)
    pub_joint9.publish(joint9)
    pub_joint10.publish(joint10)
    pub_joint11.publish(joint11)

    # Sleep to allow time for messages to be sent
    rospy.sleep(1.0)

if __name__ == "__main__":
    try:

        # Get joint positions from command-line arguments
        joint_rope_position = 3.2-float(sys.argv[1])  # Position for joint 2

        # Publish the joint positions
        publish_joint_positions(joint_rope_position)
     
    except rospy.ROSInterruptException:
        pass
