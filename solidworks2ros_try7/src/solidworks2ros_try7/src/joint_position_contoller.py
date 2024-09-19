#!/usr/bin/env python3

# Command send to the joints one after the other
import rospy
from std_msgs.msg import Float64

def publish_joint_position1(joint_name, position):

    topic_name = '/joint_1_controller/command'
    rospy.init_node('joint_position_commander', anonymous=True)
    pub = rospy.Publisher(topic_name, Float64, queue_size=10)
    rospy.sleep(1.0)
    rospy.loginfo(f"Publishing {position} radians to {joint_name}")
    pub.publish(position)
    rospy.sleep(1.0)

def publish_joint_position2(joint_name, position):

    topic_name = '/joint_2_controller/command'
    rospy.init_node('joint_position_commander', anonymous=True)
    pub = rospy.Publisher(topic_name, Float64, queue_size=10)
    rospy.sleep(1.0)
    rospy.loginfo(f"Publishing {position} meteres to {joint_name}")
    pub.publish(position)
    rospy.sleep(1.0)


if __name__ == "__main__":
    try:
        # Example usage: set the joint "joint1" to 0.5 radians and "joint2" to 1 meter
        publish_joint_position1("joint_1", 0)
        publish_joint_position2("joint_2", 0)
    except rospy.ROSInterruptException:
        pass