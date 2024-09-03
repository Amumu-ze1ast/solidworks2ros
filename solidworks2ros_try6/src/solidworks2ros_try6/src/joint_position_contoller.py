#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def publish_joint_position(joint_name, position):

    topic_name = '/joint_1_controller/command'
    rospy.init_node('joint_position_commander', anonymous=True)
    pub = rospy.Publisher(topic_name, Float64, queue_size=10)
    rospy.sleep(1.0)
    rospy.loginfo(f"Publishing {position} radians to {joint_name}")
    pub.publish(position)
    rospy.sleep(1.0)

if __name__ == "__main__":
    try:
        # Example usage: set the joint "joint1" to 0.5 radians
        publish_joint_position("joint_1", 1.57)
    except rospy.ROSInterruptException:
        pass