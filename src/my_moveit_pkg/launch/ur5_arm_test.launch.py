# pylint: disable=missing-function-docstring, missing-module-docstring, line-too-long

from __future__ import annotations
# from typing import Callable

import os
# from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
# from moveit_configs_utils import MoveItConfigsBuilder

def generate_launch_description():
    #position_yaml = PathJoinSubstitution([FindPackageShare("my_moveit_pkg"), "config", "ur5_arm_test_goal_config.yaml"])
    position_yaml = os.path.join(get_package_share_directory('my_moveit_pkg'), 'config', 'ur5_arm_test_goal_config.yaml')

    with open(position_yaml, "rt") as file:
        print(file.read())

    return LaunchDescription(
        [
            Node(
                name="new_arm_test",
                package="my_moveit_pkg",
                executable="new_arm_test",
                output="screen",
                parameters=[position_yaml],
            )
        ]
    )