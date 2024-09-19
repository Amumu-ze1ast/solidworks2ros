#!/usr/bin/env python3

# Both together from just one input
import rospy
from std_msgs.msg import Float64
import sys

def publish_joint_position(position):

    topic_name1 = '/joint_1_controller/command'
    topic_name2 = '/joint_2_controller/command'
    
    rospy.init_node('joint_position_commander', anonymous=True)
    
    pub1 = rospy.Publisher(topic_name1, Float64, queue_size=10)
    pub2 = rospy.Publisher(topic_name2, Float64, queue_size=10)

    argv = sys.argv[1:] 

    rospy.sleep(1.0)
    rospy.loginfo(f"Publishing {position} radians to joint_1 and {position} meteres to joint_2")
    
    pub1.publish(position)
    rospy.sleep(2.0)
    pub2.publish(position)
                
    rospy.sleep(1.0)

if __name__ == "__main__":
    try:
        publish_joint_position(float(sys.argv[1]))
    except rospy.ROSInterruptException:
        pass