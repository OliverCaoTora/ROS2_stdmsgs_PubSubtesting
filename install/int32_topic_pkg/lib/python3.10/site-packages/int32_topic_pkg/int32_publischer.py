#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import Int32, Int32MultiArray
import enum

class SystemState(enum.Enum):
    PAUSED = 0
    READY = 1
    EMERGENCY = 2
    FAULT = 3
    DOOR_OPEN = 4
    HUMAN_INTERVENTION = 5


class test_Publisher(Node):
    def __init__(self,name):
        super().__init__(name)
        self.pub = self.create_publisher(Int32, "/system_state", 10)
        self.pub2 = self.create_publisher(Int32MultiArray, "/error_codes", 10)
        self.time = self.create_timer(0.5, self.time_callback)

    def time_callback(self):

        system_state = SystemState.READY
        system_state = SystemState.DOOR_OPEN
        msg = Int32()
        msg2 = Int32MultiArray(data = [-32004, -32005, -32006])
        # msg.data = 2
        self.pub.publish(Int32(data=system_state.value))
        self.pub2.publish(msg2)
        self.get_logger().info(f"Publishing: {msg.data} and {system_state.value}")
        self.get_logger().info(f"Publishing error code: {msg2.data}")

def main(args=None):
    rclpy.init(args=args)
    node = test_Publisher("test_publicher")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()