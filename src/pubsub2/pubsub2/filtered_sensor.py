import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from rosidl_runtime_py.utilities import get_message
from pubsub2_interfaces.msg import FiltroSensor 

class SensorFilter(Node):

    def __init__(self):
        super().__init__('sensor_filter')

        self.sub1 = self.create_subscription(Float64, '/sensor_1', self.cb1, 10)
        self.sub2 = self.create_subscription(Float64, '/sensor_2', self.cb2, 10)
        self.sub3 = self.create_subscription(Float64, '/sensor_3', self.cb3, 10)

        self.pub = self.create_publisher(FiltroSensor, '/FiltroSensor', 10)

        self.s1 = None
        self.s2 = None
        self.s3 = None

    def cb1(self, msg):
        self.s1 = msg.data
        self.compute()

    def cb2(self, msg):
        self.s2 = msg.data
        self.compute()

    def cb3(self, msg):
        self.s3 = msg.data
        self.compute()

    def compute(self):
        if self.s1 is not None and self.s2 is not None and self.s3 is not None:
            avg = (self.s1 + self.s2 + self.s3) / 3.0

            msg = FiltroSensor()
            msg.sensor_value = avg
            msg.name = "average"

            self.pub.publish(msg)

            self.get_logger().info(f'Promedio: {avg}')

def main(args=None):
    rclpy.init(args=args)
    node = SensorFilter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    