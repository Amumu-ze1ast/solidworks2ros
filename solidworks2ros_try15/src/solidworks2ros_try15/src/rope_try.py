#!/usr/bin/env python3
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys

def move_rope(z):
    rospy.init_node('move_rope', anonymous=True)
    pub = rospy.Publisher('/rope_position_controller/command', JointTrajectory, queue_size=10)
    rate = rospy.Rate(1)

    traj = JointTrajectory()
    traj.joint_names = ['joint_1', 'joint_2', 'joint_3']

    point = JointTrajectoryPoint()

    m_to_inch = 0.025
    z_inch = z*m_to_inch

    point.positions = [z_inch, 0, z_inch]

    point.time_from_start = rospy.Duration(5.0)
    traj.points.append(point)

    while not rospy.is_shutdown():
        pub.publish(traj)
        rate.sleep()

if __name__ == '__main__':
    try:
        
        z_axis = float(sys.argv[1])
        move_rope(z_axis)

    except rospy.ROSInterruptException:
        pass
