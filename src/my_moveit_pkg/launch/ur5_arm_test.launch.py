# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long

from __future__ import annotations
# from typing import Callable

# import os
# from launch.actions import ExecuteProcess
# from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
# from moveit_configs_utils import MoveItConfigsBuilder

def generate_launch_description():
    position_goals = PathJoinSubstitution([FindPackageShare("my_moveit_pkg"), "config", "ur5_arm_test_goal_config.yaml"])

    return LaunchDescription(
        [
            Node(
                name="ur5_arm_test_2",
                package="my_moveit_pkg",
                executable="ur5_arm_test_2",
                output="screen",
                parameters=[position_goals],
            )
        ]
    )
