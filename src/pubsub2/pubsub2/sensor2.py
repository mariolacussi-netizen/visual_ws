import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class Sensor2Publisher(Node):

    def __init__(self):
        super().__init__('sensor2')
        self.publisher_ = self.create_publisher(Float64, '/sensor_2', 10)
        self.timer = self.create_timer(1.0, self.publish_value)

    def publish_value(self):
        msg = Float64()
        msg.data = random.uniform(0.0, 10.0)

        self.publisher_.publish(msg)

        self.get_logger().info(f'Sensor 2: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Sensor2Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    