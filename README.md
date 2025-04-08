# vikings_bot_gazebo

<hr>

### Description
This package contains `vikings_bot` project gazebo related files - worlds, models, launch files, etc.

<hr>

## Installation

Download source and install dependencies:
```
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
```
ros2 launch vikings_bot_gazebo start_world.launch.py
```

To spawn robot in Gazebo world:
```
ros2 launch vikings_bot_gazebo spawn.launch.xml
```


