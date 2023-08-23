# Retrofit Pioneer 3 AT Robot


## Project Description
The Retrofit Pioneer 3 AT Robot project aims to transform the existing robot by keeping chassis, wheels, and motors and replacing the control electronics with a Jetson board for advanced control and communication capabilities. The Jetson board operates using ROS (Robot Operating System), providing a robust framework for robotics applications. The main objectives of this project that have been met are as follows:
1. Integrate a Jetson board with a motor controller to enable precise wheel control.
2. Establish a wireless connection between a joystick and the Jetson board using ROS for driving the Pioneer robot.
3. Achieve closed-loop Control.
4. Initial integration of a LiDAR sensor for obstacle detection. (forward and backward within a range of 0.1 to 1.0 meters.)


Since these foundational tasks are completed, the project opens up opportunities for further enhancements, including:
- Enhance LiDAR for accurate obstacle detection and avoidance. Opening possibilities for remote inspection and monitoring.
- Extending the project to include multiple Pioneer robots with Jetson boards that can communicate and coordinate actions.
- Implementing multi-robot control strategies and integrating additional sensors such as cameras for improved perception and data collection.


## Table of Contents
- Project Description
- Use/Purpose
- Getting Started
   - Prerequisites
   - Installation
- Usage
   - Joystick Control
   - Obstacle Sensing
   - Multi-Robot Control
- Contributing


## Use/Purpose: Remote Inspection and Monitoring (Subject to change as per RSL use)
The Retrofit Pioneer 3 AT Robot serves as a versatile platform for remote inspection and monitoring tasks. Equipped with various sensors and controlled through advanced electronics, the robot can be deployed in scenarios such as:
- Monitoring air quality and pollution levels in urban areas or remote locations.
- Conducting inspections in hazardous or hard-to-reach environments where human access is limited.
- Responding to emergencies by gathering critical data and mapping changed environments.


By automating these tasks, the robot saves time, reduces risks to human inspectors, and provides valuable insights for decision-making in various situations.


## Getting Started


### Prerequisites
Before you begin, make sure you have the following components and software:
- Pioneer 3 AT robot chassis with wheels and motors
- Jetson board with ROS installed
- Motor controller compatible with the Jetson board
- Wireless joystick for remote control
- Additional sensors as needed (cameras, etc.)


### Installation


1. **Clone the Repository**: Clone this repository to your Jetson board.
git clone https://github.com/irahulone/WheelyMcRedBot.git 



- Packages present so far in the workspace:
   1. locomotion_core
   2. navigation_core
   3. rover_launch
   4. rplidar_ros
   5. rsl_roboteq
   6. teleop_twist_joy


### Usage
- Joystick Control
To control the Pioneer robot using a wireless joystick, follow these steps:
Turn on the Pioneer robot and ensure the Jetson board is powered and connected.
Connect the RPLiDAR to the control board.


cd into ros2_ws
Source the Workspace and environment as needed.


Launch the launch file that launched all 6 packages.
--> ros2 launch rover_launch rover.launch.py


Use the wireless joystick to drive the Pioneer robot.


Enabling communication between multiple Pioneer robots (Not integrated thus far):
    Deploy Jetson-equipped Pioneer robots as per prerequisites.
    Configure ROS network settings for communication between robots.
    Launch the multi-robot control node.


### Contributing
follow these steps:
    Fork the repository and create a new branch.
    Make your changes and test thoroughly.
    Submit a pull request describing your changes.

