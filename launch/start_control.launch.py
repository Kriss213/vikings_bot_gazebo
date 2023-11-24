#!/usr/bin/python3
# -*- coding: utf-8 -*-
from launch_ros.actions import Node
from launch import LaunchDescription

from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import OpaqueFunction


def launch_setup(context, *args, **kwargs):

    vikings_bot_name = LaunchConfiguration("vikings_bot_name").perform(context)
    spawn_controller_1_name = vikings_bot_name + "_spawn_controller_joint_state_broadcaster"
    spawn_controller_2_name = vikings_bot_name + "_spawn_controller_diffdrive_base_controller"
    controller_manager_name = "controller_manager"

    #--controller-manager Name of the controller manager ROS node
    spawn_controller_1 = Node(
        package="controller_manager",
        executable="spawner",
        name=spawn_controller_1_name,
        namespace=vikings_bot_name,
        arguments=["joint_state_broadcaster", "--controller-manager", controller_manager_name],
        output="screen"
    )

    spawn_controller_2 = Node(
        package="controller_manager",
        executable="spawner",
        name=spawn_controller_2_name,
        namespace=vikings_bot_name,
        arguments=["diffdrive_base_controller", "--controller-manager", controller_manager_name],
        output="screen"
    )




    return [spawn_controller_1, spawn_controller_2]


def generate_launch_description(): 

    vikings_bot_name_arg = DeclareLaunchArgument("vikings_bot_name",
                    default_value="vikings_bot",
                    description="Robot name to make it unique")

    return LaunchDescription([
        vikings_bot_name_arg,
        OpaqueFunction(function = launch_setup)
        ])