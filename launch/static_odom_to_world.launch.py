#! /usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import OpaqueFunction

def launch_setup(context, *args, **kwargs):

    namespace = LaunchConfiguration('vikings_bot_name').perform(context)
    #odom_frame_name = namespace + "/odom"
 

    # Spawn ROBOT Set Gazebo
    st_pub = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        namespace=namespace,
        name="static_transform_publisher",
        output='screen',
        emulate_tty=True,
        arguments=['0', '0', '0', '0', '0', '0', 'world', f"{namespace}/odom"]
    )


    return [st_pub]


def generate_launch_description(): 

    vikings_bot_name_arg = DeclareLaunchArgument('vikings_bot_name', default_value='vikings_bot')

    return LaunchDescription([
        vikings_bot_name_arg,
        OpaqueFunction(function = launch_setup)
        ])