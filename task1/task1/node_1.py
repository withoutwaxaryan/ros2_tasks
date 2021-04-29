# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class Node_A(Node):

    def __init__(self):
        super().__init__('node_A')

        # Publisher from Node A on topic_1
        self.publisher_ = self.create_publisher(Int64, 'topic_1', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        # Subscriber from Node A of topic_2
        self.subscription = self.create_subscription(
                                                    Int64,
                                                    'topic_2',
                                                    self.listener_callback,
                                                    10)
        self.subscription  # prevent unused variable warning

    def timer_callback(self):
        number = Int64()
        number.data = 12
        self.publisher_.publish(number)
        self.get_logger().info('Publishing: %d' % number.data)
        self.i += 1

    def listener_callback(self, msg):
        self.get_logger().info('Answer: %d' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node_A = Node_A()

    rclpy.spin(node_A)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node_A.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()