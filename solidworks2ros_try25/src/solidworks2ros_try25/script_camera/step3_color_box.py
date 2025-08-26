#!/usr/bin/env python3
import rospy, cv2, numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class HSVRangesDetector:
    """
    Detects blobs whose HSV falls inside ANY of the provided ranges.
    Pass ranges as a list of 6-tuples/lists:
      [[Hlo,Slo,Vlo,Hhi,Shi,Vhi], ...]
    """
    def __init__(self):
        self.bridge = CvBridge()
        self.rgb_topic = rospy.get_param("~rgb_topic", "/rgbd_camera2/rgb/image_raw")

        # ---- Example HSV ranges ----
        default_ranges = [ 

            [27, 0, 0, 180, 255, 255], # Optional values from opencv windows
            
            # [0,   0,   0, 180,  60, 120],   # dark gray (low S, moderately low V)
            
            # --- Uncomment to detect other colors ---
            # [0,   0,   0, 180, 255,  60],   # pure black (low V)
            # [0,120,80, 10,255,255],         # Red (lower range)
            # [170,120,80, 180,255,255],      # Red (upper range, hue wraps)
            # [20,100,100, 30,255,255],       # Yellow
            # [40, 40, 40, 70,255,255],       # Green
            # [100,150, 0, 140,255,255],      # Blue
            # [140, 50, 50, 170,255,255],     # Purple / Violet
            # [10, 50, 50, 20,255,255],       # Orange
        ]
        # ----------------------------

        self.ranges = rospy.get_param("~ranges", default_ranges)
        self.min_area = rospy.get_param("~min_area", 800)

        self.sub = rospy.Subscriber(self.rgb_topic, Image, self.cb, queue_size=1)
        self.pub = rospy.Publisher("~debug_image", Image, queue_size=1)
        rospy.loginfo("HSVRangesDetector listening on %s", self.rgb_topic)
        rospy.loginfo("HSV ranges: %s", self.ranges)

    def cb(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Build mask = OR of all provided ranges
        mask_total = np.zeros(hsv.shape[:2], dtype=np.uint8)
        for r in self.ranges:
            hL,sL,vL,hH,sH,vH = r
            mask = cv2.inRange(hsv, (hL,sL,vL), (hH,sH,vH))
            mask_total = cv2.bitwise_or(mask_total, mask)

        # Clean up
        mask_total = cv2.medianBlur(mask_total, 5)
        mask_total = cv2.morphologyEx(
            mask_total, cv2.MORPH_OPEN,
            cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        )

        # # Draw green box for only one object
        # cnts, _ = cv2.findContours(mask_total, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # if cnts:
        #     c = max(cnts, key=cv2.contourArea)
        #     if cv2.contourArea(c) >= self.min_area:
        #         x,y,w,h = cv2.boundingRect(c)
        #         cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        #         cx, cy = x + w//2, y + h//2
        #         cv2.circle(img, (cx,cy), 4, (0,0,255), -1)
        #         cv2.putText(img, "object", (x, y-8),
        #                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

            
        # Draw green box For multi opbjects        
        cnts, _ = cv2.findContours(mask_total, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        kept = 0
        for c in cnts:
            area = cv2.contourArea(c)
            if area < self.min_area:
                continue
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            cx, cy = x+w//2, y+h//2
            cv2.circle(img, (cx,cy), 4, (0,0,255), -1)
            cv2.putText(img, f"obj {kept+1}", (x, y-8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
            kept += 1

        stacked = np.hstack((img, cv2.cvtColor(mask_total, cv2.COLOR_GRAY2BGR)))
        self.pub.publish(self.bridge.cv2_to_imgmsg(stacked, "bgr8"))

if __name__ == "__main__":
    rospy.init_node("step3_hsv_ranges_detector")
    HSVRangesDetector()
    rospy.spin()