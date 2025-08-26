#!/usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

def draw_line():
    rospy.init_node('line_drawer', anonymous=True)
    marker_pub = rospy.Publisher('/visualization_marker', Marker, queue_size=10)

    marker = Marker()
    marker.header.frame_id = "base_link"  # The reference frame (e.g., "world" or "base_link")
    marker.type = Marker.LINE_STRIP  # Or Marker.LINE_LIST for individual segments
    marker.action = Marker.ADD
    marker.scale.x = 0.01  # Line width
    marker.color.a = 1.0  # Transparency
    marker.color.r = 1.0  # Red color
    marker.color.g = 0.0
    marker.color.b = 0.0

    # Define two points
    point1 = Point()
    point1.x = 3.0
    point1.y = 3.0
    point1.z = 3.0

    point2 = Point()
    point2.x = 2.0
    point2.y = 2.0
    point2.z = 2.0

    marker.points.append(point1)
    marker.points.append(point2)

    while not rospy.is_shutdown():
        marker_pub.publish(marker)
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        draw_line()
    except rospy.ROSInterruptException:
        pass
