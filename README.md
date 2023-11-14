# Robot_cleaner
Prerequisites

Ubuntu 20.04 
Gazebo >= version 11.14.0
ROS Noetic
following ROS packages were used and the process of obtaining them is detailed below:
gmapping
turtlebot_teleop
turtlebot_rviz_launcher
turtlebot_gazebo


├── README.md
│   ├── catkin_ws
│   ├── include 
│   └── src
│       ├── robot_cleaner pkg
│       └── CMakeLists.txt
   robot_cleaner pkg
│   └── src
│       ├── "The cleaning code will be added here"
│       
│   ├── Worlds
         ├── cleaning_environment.world ""I'm still editing the code to get the right environment for the project""
         
│   ├── package.xml
│   ├── model.sdf
│   └──  launch 
          ├── cleaning_robot.launch
├── slam_gmapping
│   ├── gmapping
│   |── ... ...
├── turtlebot
│   |── turtlebot_teleop
│   |── turtlebot3_simulations  
    |── turtlebot3_navigation
    |── turtlebot3_slam
    |── turtlebot3_description
├── turtlebot_interactions
│   |── turtlebot_rviz_launchers
│   |── ... ...
|── turtlebot_simulator
│   ├── turtlebot_gazebo
│     
│

├── my_robot
│   ├── maps
│   │    ├── tb3_house_map.pgm
│   │    └── tb3_house_map.yaml
│   ├── worlds
│   │    └─house.world   "The navigation process was tried on this environment and the creation of previous maps ( I have not yet created a map for my project on which I was working"
│   └── ...
 
 
 

Since the folder presented here comprises only of ROS package, one needs to first create a catkin workspace and initialize it. Also, note that the official ROS packaged are already included here, but their dependencies need to be installed; steps for this are given below.

Within your home directory, execute the following:

mkdir -p catkin_ws/src
cd catkin_ws/src
catkin_init_workspace
Install dependencies:

sudo apt update
sudo apt-get install ros-noetic-turtlebot
sudo apt-get install ros-noetic-turtlebot-*
sudo apt-get install ros-noetic-teleop-twist-keyboard
sudo apt-get install gazebo11
sudo apt-get install ros-noetic-rviz
sudo apt-get install ros-noetic-navigation
sudo apt-get install ros-noetic-gmapping
sudo apt-get install ros-noetic-amcl
sudo apt-get install ros-noetic-map-server


creat work space : 
cd catkin_ws/
catkin_make


The workspace has been built and the urdf robot has been built 

The idea of the project is to build a suitable environment for a cleaning robot and he must get to know it well and then create a suitable code for the robot to clean this environment and avoid all obstacles
But I worked on a test-ready environment, which is the : roslaunch turtlebot3_gazebo turtlebot3_house.launch
-roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
save map : -rosrun map-server -f ~/tb3_house.map
- roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/rima/catkin_ws/src/tb3_house_map.yaml
 "But there is a problem with the local and global maps in this map, which makes the robot can not track the route well by 2D nav"
