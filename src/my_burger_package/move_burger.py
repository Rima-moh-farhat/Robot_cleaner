#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('move_turtlebot_node')
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

# Move forward
vel_msg = Twist()
vel_msg.linear.x = 0.2  # 0.2 m/s
t0 = rospy.Time.now().to_sec()
while rospy.Time.now().to_sec() - t0 < 2:
    velocity_publisher.publish(vel_msg)

# Stop moving
vel_msg.linear.x = 0
velocity_publisher.publish(vel_msg)

# Wait for 2 seconds
time.sleep(2)

# Move backward
vel_msg.linear.x = -0.2
t0 = rospy.Time.now().to_sec()
while rospy.Time.now().to_sec() - t0 < 2:
    velocity_publisher.publish(vel_msg)

# Stop moving
vel_msg.linear.x = 0
velocity_publisher.publish(vel_msg)
