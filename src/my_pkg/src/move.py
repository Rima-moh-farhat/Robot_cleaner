#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('pub')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(2)
move = Twist()

move.angular.z = 0.5
move.linear.x = 2
while not rospy.is_shutdown():
    pub.publish(move)
    rate.sleep()
