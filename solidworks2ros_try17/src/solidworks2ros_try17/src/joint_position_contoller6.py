#!/usr/bin/env python3

# Both together from just one input
import rospy
from std_msgs.msg import Float64
import sys

def publish_joint_position(position):

    topic_name1 = '/joint_1_controller/command'
    topic_name2 = '/joint_2_controller/command'
    topic_name3 = '/joint_3_controller/command'
    topic_name4 = '/joint_4_controller/command'
    
    rospy.init_node('joint_position_commander', anonymous=True)
    
    pub1 = rospy.Publisher(topic_name1, Float64, queue_size=10)
    pub2 = rospy.Publisher(topic_name2, Float64, queue_size=10)
    pub3 = rospy.Publisher(topic_name3, Float64, queue_size=10)
    pub4 = rospy.Publisher(topic_name4, Float64, queue_size=10)

    rospy.sleep(1.0)
    rospy.loginfo(f"Publishing {position} radians to joint_1, and {position} meteres to joint_2 and joint_3")
    
    pub1.publish(position)
    pub2.publish(position)
    pub3.publish(position)
    pub4.publish(-0.5)
                
    rospy.sleep(1.0)

if __name__ == "__main__":
    try:
        publish_joint_position(float(sys.argv[1]))
    except rospy.ROSInterruptException:
        pass