#!/usr/bin/env python3

# Send the command simultiniously to both joints at the same time.
import rospy
from std_msgs.msg import Float64

def publish_joint_positions(joint1_position, joint2_position):

    # Initialize the ROS node
    rospy.init_node('joint_position_commander', anonymous=True)

    # Publishers for joint 1 and joint 2
    pub_joint1 = rospy.Publisher('/joint_1_controller/command', Float64, queue_size=10)
    pub_joint2 = rospy.Publisher('/joint_2_controller/command', Float64, queue_size=10)

    # Wait for a short time to ensure the publishers are registered
    rospy.sleep(1.0)

    # Publish to both joints simultaneously
    rospy.loginfo(f"Publishing {joint1_position} radians to joint 1")
    rospy.loginfo(f"Publishing {joint2_position} meters to joint 2")
    
    pub_joint1.publish(joint1_position)
    pub_joint2.publish(joint2_position)

    # Sleep to allow time for messages to be sent
    rospy.sleep(1.0)


if __name__ == "__main__":
    try:
        # Example usage: set joint 1 to 1.57 radians and joint 2 to 1.57 meter
        publish_joint_positions(0, 0)
    except rospy.ROSInterruptException:
        pass
