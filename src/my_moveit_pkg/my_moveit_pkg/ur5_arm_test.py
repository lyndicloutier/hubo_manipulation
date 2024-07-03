# Christian tested this this file to see if imports work

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-name-in-module
# pylint: disable=consider-using-f-string
# pylint: disable=trailing-whitespace

import rclpy
from rclpy.node import Node
# from rclpy.logging import get_logger
from geometry_msgs.msg import PoseStamped
from moveit.planning import (
    MoveItPy,
)

class RobotArm(Node):
    def __init__(self):
        super().__init__('ur5_arm_test')
        self.robot_arm_publisher = self.create_publisher(PoseStamped, 'ur5_arm', 10)
        # timer_period = 0.5
        # self.timer = self.create_timer(timer_period, self.pose_callback)

    def motion(self):
        msg = PoseStamped()

        self.robot_arm_publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)
        


def main():

    # Initialize rclpy and create a publisher
    rclpy.init()
    
    robot_arm = RobotArm()
    rclpy.spin(robot_arm)
    robot_arm.destroy_node()

    # Instantiate MoveItPy and get planning component 
    robot = MoveItPy(node_name="ur5_arm_test")
    robot_arm = robot.get_planning_component("robot_arm")

    # set plan start state to current state
    robot_arm.set_start_state_to_current_state()

    # Create PoseStamped message that will hold the target Pose
    pose_goal = PoseStamped()
    pose_goal.header.frame_id = "robot_link0"

    # Describe the target pose for the end-effector
    pose_goal.pose.orientation.w = 1.0
    pose_goal.pose.position.x = 0.28
    pose_goal.pose.position.y = -0.2
    pose_goal.pose.position.z = 0.5

    # Set the target pose
    robot_arm.set_goal_state(pose_stamped_msg=pose_goal, pose_link="robot_link8")

    # Create a plan to the target pose
    plan_result = robot_arm.plan()

    # If the plan is successful, get the trajectory and execute the plan
    if plan_result:
        robot_trajectory = plan_result.trajectory
        robot.execute(robot_trajectory, blocking=True, controllers=[])
    # else:
        # logger.error("Planning failed")

    rclpy.shutdown()

if __name__ == "__main__":
    main()
