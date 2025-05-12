# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
# import os

# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument
# from launch.actions import IncludeLaunchDescription
# from launch.substitutions import LaunchConfiguration
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from ament_index_python.packages import get_package_prefix

# def generate_launch_description():

   
#     ### Launch argument substitutions ###
#     gazebo_world = LaunchConfiguration('world')

#     pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
#     pkg_vikings_bot_gazebo = get_package_share_directory('vikings_bot_gazebo')

#     # We get the whole install dir
#     # We do this to avoid having to copy or softlink manually the packages so that gazebo can find them
#     description_package_name = "vikings_bot_description"
#     install_dir = get_package_prefix(description_package_name)

#     # Set the path to the WORLD model files. Is to find the models inside the models folder in my_box_bot_gazebo package
#     gazebo_models_path = os.path.join(pkg_vikings_bot_gazebo, 'models')
#     # os.environ["GAZEBO_MODEL_PATH"] = gazebo_models_path

#     if 'GAZEBO_MODEL_PATH' in os.environ:
#         os.environ['GAZEBO_MODEL_PATH'] =  os.environ['GAZEBO_MODEL_PATH'] + ':' + install_dir + '/share' + ':' + gazebo_models_path
#     else:
#         os.environ['GAZEBO_MODEL_PATH'] =  install_dir + "/share" + ':' + gazebo_models_path

#     if 'GAZEBO_PLUGIN_PATH' in os.environ:
#         os.environ['GAZEBO_PLUGIN_PATH'] = os.environ['GAZEBO_PLUGIN_PATH'] + ':' + install_dir + '/lib'
#     else:
#         os.environ['GAZEBO_PLUGIN_PATH'] = install_dir + '/lib'

    

#     print("GAZEBO MODELS PATH=="+str(os.environ["GAZEBO_MODEL_PATH"]))
#     print("GAZEBO PLUGINS PATH=="+str(os.environ["GAZEBO_PLUGIN_PATH"]))


#     ### launch argumnets ###
#     gazebo_world_arg = DeclareLaunchArgument(
#                 'world',
#                 default_value=[os.path.join(pkg_vikings_bot_gazebo, 'worlds', gazebo_world), ''],
#                 description='SDF world file')
    

#     # To increase update rate
#     #gazebo_params_file = os.path.join(pkg_vikings_bot_gazebo, "config", "gazebo_params.yaml")

#     gazebo = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource([
#             os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
#         ]),
#         # launch_arguments={
#         #     "extra_gazebo_args": "--ros-args --param-file " + gazebo_params_file
#         # }.items()
#     )
#     # gazebo = IncludeLaunchDescription(
#     #             PythonLaunchDescriptionSource([os.path.join(
#     #                 get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
#     #                 launch_arguments={'extra_gazebo_args': '--ros-args --params-file ' + gazebo_params_file}.items()
#     # )


#     return LaunchDescription([
#         gazebo_world_arg,
#         gazebo,
#     ])


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
