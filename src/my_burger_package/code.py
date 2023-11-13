#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Point
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
import math

def point_callback(point):
    # Get x and y coordinates from the received point
    x = point.x
    y = point.y
    rospy.loginfo("Received point: (%f, %f)", x, y)

    # Make the robot move in a circular trajectory
    radius = 1.0  # radius of the circle
    num_points = 20  # number of points to use for the circle
    angular_speed = 0.5  # angular speed of the robot
    linear_speed = 0.2  # linear speed of the robot

    # Create a client to send navigation goals to the move_base node
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    client.wait_for_server()

    # Calculate the angle between each point on the circle
    angle_increment = 2 * math.pi / num_points

    # Move the robot in a circular trajectory
    for i in range(num_points):
        angle = i * angle_increment
        x_goal = x + radius * math.cos(angle)
        y_goal = y + radius * math.sin(angle)
        theta_goal = angle + math.pi / 2
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x_goal
        goal.target_pose.pose.position.y = y_goal
        goal.target_pose.pose.orientation.z = math.sin(theta_goal / 2.0)
        goal.target_pose.pose.orientation.w = math.cos(theta_goal / 2.0)
        client.send_goal(goal)
        client.wait_for_result()

    # Navigate to a specific point
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 2.0  # set the x-coordinate of the goal point
    goal.target_pose.pose.position.y = 3.0  # set the y-coordinate of the goal point
    goal.target_pose.pose.orientation.w = 1.0  # set the orientation of the goal point
    client.send_goal(goal)
    client.wait_for_result()

if __name__ == "__main__":
    # Initialize the ROS node
    rospy.init_node("navigation_node")

    # Subscribe to the point topic
    rospy.Subscriber("point_topic", Point, point_callback)

    # Spin the node to receive messages
    rospy.spin()
