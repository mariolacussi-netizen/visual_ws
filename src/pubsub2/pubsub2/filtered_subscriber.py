import rclpy
from rclpy.node import Node
from rosidl_runtime_py.utilities import get_message
from pubsub2_interfaces.msg import FiltroSensor 

class Subscriber(Node):

    def __init__(self):
        super().__init__('filtered_subscriber')

        self.sub = self.create_subscription(
            FiltroSensor,
            '/FiltroSensor',
            self.cb,
            10
        )

    def cb(self, msg):
        self.get_logger().info(f'Valor: {msg.sensor_value}')

def main(args=None):
    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()