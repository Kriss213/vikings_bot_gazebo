# vikings_bot_gazebo

<hr>

### Description
This package contains `vikings_bot` project gazebo related files - worlds, models, launch files, etc.

<hr>

## Installation

Download source and install dependencies:
```
cd <path/to/your/ros_ws>
git clone git@github.com:Hercogs/vikings_bot_gazebo.git src/vikings_bot_gazebo
rosdep update
rosdep install --ignore-src --default-yes --from-path src
```

Build package:
```
colcon build
source install/setup.bash
```

<hr>

### Usage

To start Gazebo world:
```ros2 launch vikings_bot_gazebo start_world.launch.py```

To spawn robot in Gazebo world:
```ros2 launch vikings_bot_gazebo spawn.launch.xml```

To spawn 2 robots in Gazebo world:
```ros2 launch vikings_bot_gazebo spawn_two_robots.launch.xml```


To run first robot:
```ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=vikings_bot_1/cmd_vel```

To run second robot:
```ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=vikings_bot_1/cmd_vel```

