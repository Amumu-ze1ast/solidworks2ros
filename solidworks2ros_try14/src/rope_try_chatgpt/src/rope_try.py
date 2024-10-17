#!/usr/bin/env python3
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys

def move_rope(z_axis):
    rospy.init_node('move_rope', anonymous=True)
    pub = rospy.Publisher('/rope_position_controller/command', JointTrajectory, queue_size=10)
    rate = rospy.Rate(1)

    traj = JointTrajectory()
    traj.joint_names = ['joint_0', 'joint_1', 'joint_2', 'joint_3', 'joint_4']

    point = JointTrajectoryPoint()

    a = z_axis

    point.positions = [a-0.4, a-0.3, a-0.2, a-0.1, a]

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
