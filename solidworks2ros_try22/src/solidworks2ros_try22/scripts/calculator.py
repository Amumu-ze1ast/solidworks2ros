#!/usr/bin/env python3

joint_position = 3.2


    # Smooth the joint positions based on the input
joint5 = min(0.5, joint_position * 0.167)  # Joint 5's limit is 0.5
joint6 = min(1, joint_position * 0.333)    # Joint 6's limit is 1
joint7 = min(1.5, joint_position * 0.5)    # Joint 7's limit is 1.5
joint8 = min(2, joint_position * 0.667)    # Joint 8's limit is 2
joint9 = min(2.5, joint_position * 0.833)  # Joint 9's limit is 2.5
joint10 = min(3, joint_position)           # Joint 10's limit is 3
joint11 = joint_position                   # Joint 11 directly tracks joint_position

print(joint5)
print(joint6)
print(joint7)
print(joint8)
print(joint9)
print(joint10)
print(joint11)

print ("All sum")
print(joint5 + joint6 + joint7 + joint8 + joint9 + joint10 + joint11)