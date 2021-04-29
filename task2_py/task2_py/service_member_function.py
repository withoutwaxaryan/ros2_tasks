from interface.srv import MultiplyTwoInts    

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(MultiplyTwoInts, 'multiply_two_ints', self.multiply_two_ints_callback)

    def multiply_two_ints_callback(self, request, response):
        response.product = request.a * request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()