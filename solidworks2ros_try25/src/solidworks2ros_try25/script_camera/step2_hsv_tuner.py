#!/usr/bin/env python3
import rospy, cv2, numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class HSVTunerNode:
    def __init__(self):
        rospy.init_node("hsv_tuner")

        self.bridge = CvBridge()
        self.sub = rospy.Subscriber("/rgbd_camera/rgb/image_raw", Image, self.cb, queue_size=1)

        cv2.namedWindow("tuner", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("tuner", 1200, 500)

        for name, val, mx in [
            ("H_low", 0, 180), ("S_low", 0, 255), ("V_low", 0, 255),
            ("H_high", 180, 180), ("S_high", 255, 255), ("V_high", 255, 255)
        ]:
            cv2.createTrackbar(name, "tuner", val, mx, lambda x: None)

        cv2.createTrackbar("MinArea", "tuner", 800, 20000, lambda x: None)

        rospy.loginfo("HSV tuner running. Use sliders to adjust thresholds.")

    def cb(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        # --- read sliders ---
        hL = cv2.getTrackbarPos("H_low", "tuner")
        sL = cv2.getTrackbarPos("S_low", "tuner")
        vL = cv2.getTrackbarPos("V_low", "tuner")
        hH = cv2.getTrackbarPos("H_high", "tuner")
        sH = cv2.getTrackbarPos("S_high", "tuner")
        vH = cv2.getTrackbarPos("V_high", "tuner")
        min_area = cv2.getTrackbarPos("MinArea", "tuner")

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (hL,sL,vL), (hH,sH,vH))

        cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        vis = frame.copy()
        for idx, c in enumerate(cnts, start=1):
            if cv2.contourArea(c) < min_area: continue
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(vis, (x,y), (x+w,y+h), (0,255,0), 2)
            cx, cy = x+w//2, y+h//2
            cv2.circle(vis, (cx,cy), 4, (0,0,255), -1)
            cv2.putText(vis, f"obj {idx}", (x, y-8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        stacked = np.hstack((vis, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)))
        cv2.imshow("tuner", stacked)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            print(f"lower: [{hL},{sL},{vL}]  upper: [{hH},{sH},{vH}]  min_area: {min_area}")
        elif key in (27, ord('q')):  # ESC or q
            rospy.signal_shutdown("User quit")
            cv2.destroyAllWindows()

if __name__ == "__main__":
    HSVTunerNode()
    rospy.spin()