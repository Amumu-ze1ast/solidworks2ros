#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def publish_joint_position(position):

    topic_name1 = '/joint_1_controller/command'
    topic_name2 = '/joint_2_controller/command'
    topic_name3 = '/joint_3_controller/command'

    rospy.init_node('joint_position_commander', anonymous=True)

    pub1 = rospy.Publisher(topic_name1, Float64, queue_size=10)
    pub2 = rospy.Publisher(topic_name2, Float64, queue_size=10)
    pub3 = rospy.Publisher(topic_name3, Float64, queue_size=10)

    rospy.sleep(1.0)
    
    rospy.loginfo(f"Publishing {position} radians to joint_1, {position} meteres to joint_2 and joint_3")
    
    pub1.publish(position)
    rospy.sleep(2.0)
    pub2.publish(position)
    rospy.sleep(2.0)
    pub3.publish(position)

    rospy.sleep(1.0)

if __name__ == "__main__":
    try:
        # Example usage: set the joint "joint1" and "joint2" to 0.5 radians and 1.57 meters
        publish_joint_position(1.57)
    except rospy.ROSInterruptException:
        pass