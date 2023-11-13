
#!/usr/bin/env python3
import rospy
import yaml


with open('laser_config.yaml', 'r') as file:
    config = yaml.load(file)


angle_min = config['laser']['-1.570']
angle_max = config['laser']['1.5708']
range_min = config['laser']['0.1']
range_max = config['laser']['10.0']
scan_time = config['laser']['0.1']

rospy.init_node('sensor_node')

    rospy.spin()
