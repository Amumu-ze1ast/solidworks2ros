#include <iostream>
#include <algorithm> // for std::min

int main() {
    double joint_position = 3.2;

    // Smooth the joint positions based on the input
    double joint5 = std::min(0.5, joint_position * 0.167);  // Joint 5's limit is 0.5
    double joint6 = std::min(1.0, joint_position * 0.333);  // Joint 6's limit is 1
    double joint7 = std::min(1.5, joint_position * 0.5);    // Joint 7's limit is 1.5
    double joint8 = std::min(2.0, joint_position * 0.667);  // Joint 8's limit is 2
    double joint9 = std::min(2.5, joint_position * 0.833);  // Joint 9's limit is 2.5
    double joint10 = std::min(3.0, joint_position);         // Joint 10's limit is 3
    double joint11 = joint_position;                       // Joint 11 directly tracks joint_position

    // Print individual joint values
    std::cout << "Joint 5: " << joint5 << std::endl;
    std::cout << "Joint 6: " << joint6 << std::endl;
    std::cout << "Joint 7: " << joint7 << std::endl;
    std::cout << "Joint 8: " << joint8 << std::endl;
    std::cout << "Joint 9: " << joint9 << std::endl;
    std::cout << "Joint 10: " << joint10 << std::endl;
    std::cout << "Joint 11: " << joint11 << std::endl;

    // Print sum of all joint values
    double sum = joint5 + joint6 + joint7 + joint8 + joint9 + joint10 + joint11;
    std::cout << "All sum: " << sum << std::endl;

    return 0;
}
