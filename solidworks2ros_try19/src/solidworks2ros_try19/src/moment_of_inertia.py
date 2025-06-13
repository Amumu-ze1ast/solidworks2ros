#! /usr/bin/env python3

import sys 
import rospy

def moment_of_inetria(m, h, d, w):
    ixx = (1/12)*m*(h**2+d**2)
    iyy = (1/12)*m*(d**2+w**2)
    izz = (1/12)*m*(h**2+w**2)

    print("ixx: ", ixx)
    print("iyy: ", iyy)
    print("izz: ", izz)
    
if __name__ == '__main__':
    try:
        mass = float(sys.argv[1])  
        height = float(sys.argv[2])
        depth = float(sys.argv[3])
        width = float(sys.argv[4])

        moment_of_inetria(mass, height, depth, width)

    except rospy.ROSInterruptException:
        pass