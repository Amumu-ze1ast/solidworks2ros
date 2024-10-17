#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import sys


def publish_joint_positions(joint_position):

    # Initialize the ROS node
    rospy.init_node('joint_position_commander', anonymous=True)

    # Publishers for joint 1 and joint 2
    pub_joint1 = rospy.Publisher('/joint_1_controller/command', Float64, queue_size=10)
    pub_joint2 = rospy.Publisher('/joint_2_controller/command', Float64, queue_size=10)
    pub_joint3 = rospy.Publisher('/joint_3_controller/command', Float64, queue_size=10)
    pub_joint5 = rospy.Publisher('/joint_5_controller/command', Float64, queue_size=10)
    pub_joint6 = rospy.Publisher('/joint_6_controller/command', Float64, queue_size=10)
    pub_joint7 = rospy.Publisher('/joint_7_controller/command', Float64, queue_size=10)
    pub_joint8 = rospy.Publisher('/joint_8_controller/command', Float64, queue_size=10)
    pub_joint9 = rospy.Publisher('/joint_9_controller/command', Float64, queue_size=10)
    pub_joint10 = rospy.Publisher('/joint_10_controller/command', Float64, queue_size=10)
    pub_joint11 = rospy.Publisher('/joint_11_controller/command', Float64, queue_size=10)



    # Wait for a short time to ensure the publishers are registered
    rospy.sleep(1.0)



    if joint_position <= 0.5:
       pub_joint5.publish(joint_position)
       pub_joint6.publish(joint_position)
       pub_joint7.publish(joint_position)
       pub_joint8.publish(joint_position) 
       pub_joint9.publish(joint_position)
       pub_joint10.publish(joint_position)
       pub_joint11.publish(joint_position)

    elif 0.5 < joint_position <= 1:
        pub_joint5.publish(0.5)
        pub_joint6.publish(joint_position)
        pub_joint7.publish(joint_position)
        pub_joint8.publish(joint_position)
        pub_joint9.publish(joint_position)
        pub_joint10.publish(joint_position)
        pub_joint11.publish(joint_position)

    elif 1 < joint_position <= 1.5:
        pub_joint5.publish(0.5)
        pub_joint6.publish(1)
        pub_joint7.publish(joint_position)
        pub_joint8.publish(joint_position)
        pub_joint9.publish(joint_position)
        pub_joint10.publish(joint_position)
        pub_joint11.publish(joint_position)

    elif 1.5 < joint_position <= 2:
        pub_joint5.publish(0.5)
        pub_joint6.publish(1)
        pub_joint7.publish(1.5)
        pub_joint8.publish(joint_position)
        pub_joint9.publish(joint_position)
        pub_joint10.publish(joint_position)
        pub_joint11.publish(joint_position)

    elif 2 < joint_position <= 2.5:
        pub_joint5.publish(0.5)
        pub_joint6.publish(1)
        pub_joint7.publish(1.5)
        pub_joint8.publish(2)
        pub_joint9.publish(joint_position)
        pub_joint10.publish(joint_position)
        pub_joint11.publish(joint_position)

    elif 2.5 < joint_position <= 3:
        pub_joint5.publish(0.5)
        pub_joint6.publish(1)
        pub_joint7.publish(1.5)
        pub_joint8.publish(2)
        pub_joint9.publish(2.5)
        pub_joint10.publish(joint_position)
        pub_joint11.publish(joint_position)

    elif joint_position > 3:
        pub_joint5.publish(0.5)
        pub_joint6.publish(1)
        pub_joint7.publish(1.5)
        pub_joint8.publish(2)
        pub_joint9.publish(2.5)
        pub_joint10.publish(3)
        pub_joint11.publish(joint_position)


    # Sleep to allow time for messages to be sent
    rospy.sleep(1.0)


if __name__ == "__main__":
    try:

        # Get joint positions from command-line arguments
        joint2_position = 3.2-float(sys.argv[1])  # Position for joint 2

        # Publish the joint positions
        publish_joint_positions(joint2_position)

        

    except rospy.ROSInterruptException:
        pass
