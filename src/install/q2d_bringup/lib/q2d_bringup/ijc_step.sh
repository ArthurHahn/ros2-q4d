#!/bin/bash

ros2 topic pub /shoulder_controller/command std_msgs/msg/Float64 "{data: $1}" -1 &
ros2 topic pub /elbow_controller/command std_msgs/msg/Float64 "{data: $2}" -1
