#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ShowRGB(object):
    def __init__(self):
        self.bridge = CvBridge()
        self.rgb_topic = rospy.get_param("~rgb_topic", "/rgbd_camera2/rgb/image_raw")
        self.pub = rospy.Publisher("~debug_image", Image, queue_size=1)
        self.sub = rospy.Subscriber(self.rgb_topic, Image, self.cb, queue_size=1)
        rospy.loginfo("Step1: subscribing to %s", self.rgb_topic)

    def cb(self, msg: Image):
        # Convert ROS -> OpenCV (BGR)
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        # (Optional) draw a tiny crosshair in the center so we know it’s us
        h, w = frame.shape[:2]
        cv2.drawMarker(frame, (w//2, h//2), (0, 255, 0), cv2.MARKER_CROSS, 12, 2)
        # Publish back to ROS
        self.pub.publish(self.bridge.cv2_to_imgmsg(frame, encoding="bgr8"))

if __name__ == "__main__":
    rospy.init_node("step1_show_rgb")
    ShowRGB()
    rospy.spin()