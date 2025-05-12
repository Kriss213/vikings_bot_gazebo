# #!/usr/bin/python3
# # -*- coding: utf-8 -*-

import os

from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Package directories
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_vikings_bot_gazebo = get_package_share_directory('vikings_bot_gazebo')
    description_package_name = "vikings_bot_description"
    install_dir = get_package_prefix(description_package_name)

    # Environment setup
    gazebo_models_path = os.path.join(pkg_vikings_bot_gazebo, 'models')

    os.environ['GAZEBO_MODEL_PATH'] = ':'.join(filter(None, [
        os.environ.get('GAZEBO_MODEL_PATH', ''),
        os.path.join(install_dir, 'share'),
        gazebo_models_path
    ]))

    os.environ['GAZEBO_PLUGIN_PATH'] = ':'.join(filter(None, [
        os.environ.get('GAZEBO_PLUGIN_PATH', ''),
        os.path.join(install_dir, 'lib')
    ]))

    print("GAZEBO_MODEL_PATH = " + os.environ["GAZEBO_MODEL_PATH"])
    print("GAZEBO_PLUGIN_PATH = " + os.environ["GAZEBO_PLUGIN_PATH"])

    # Declare launch argument (world file name only)
    gazebo_world_arg = DeclareLaunchArgument(
        'world',
        default_value='empty.world',
        description='SDF world file name inside vikings_bot_gazebo/worlds/'
    )

    # Launch Gazebo with the selected world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={
            'world': PathJoinSubstitution(
                        [FindPackageShare('vikings_bot_gazebo'),
                        'worlds',
                        LaunchConfiguration('world')
                    ])
        }.items()
    )

    

    return LaunchDescription([
        gazebo_world_arg,
        gazebo
    ])
