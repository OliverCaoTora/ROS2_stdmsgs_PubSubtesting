#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Int32MultiArray
import enum

class SystemState(enum.Enum):
    PAUSED = 0
    READY = 1
    EMERGENCY = 2
    FAULT = 3
    DOOR_OPEN = 4
    HUMAN_INTERVENTION = 5

class test_Subscriber(Node):
    def __init__(self, name):
        super().__init__(name)
        self.sub = self.create_subscription(Int32, "/system_state", self.sub_callback, 10)
        self.sub2 = self.create_subscription(Int32MultiArray, "/error_codes", self.sub2_callback, 10)
        self.system_state = 1
        self.error_codes = None

    def sub_callback(self, msg):
        self.get_logger().info(f"Subscription: {msg.data}")
        self.system_state = msg.data
        if self.system_state == SystemState.READY.value:
            self.get_logger().info(f"System state is Ready.")

    def sub2_callback(self, msg):
        self.get_logger().info(f"Subscription error codes: {msg.data}")
        self.error_codes = msg.data
        self.get_logger().info(f"Subscription error codes2: {self.error_codes}")
        for error_code in self.error_codes:
            self.get_logger().info(f"Subscription error codes2: {error_code}")

        # self.error_code = msg.data
        # if self.system_state == SystemState.READY.value:
        #     self.get_logger().info(f"System state is Ready.")

def main(args = None):
    rclpy.init(args=args)
    node = test_Subscriber("test_subscriber")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()