# vikings_bot_gazebo

<hr>

Usage:
1. Use `git clone` to clone this package
2. Source your ROS distro: `source /opt/ros/${ROS_DISTRO}/setup.bash`
3. In your workspace execute: `colcon build`

<hr>

Depends on: `vikings_bot_description` ROS2 package


To start Gazebo: 'ros2 launch vikings_bot_gazebo start_world.launch.py'
To spawn 2 robots in Gazebo: `ros2 launch vikings_bot_gazebo spawn_two_robots.launch.xml`

To spawn robot for debug purpose: 'ros2 launch vikings_bot_gazebo spawn_robot_ros2.launch.xml'git status

To run first robot:
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=vikings_bot_1/cmd_vel

To run second robot:
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=vikings_bot_1/cmd_vel

To see all topic:
ros2 topic list
