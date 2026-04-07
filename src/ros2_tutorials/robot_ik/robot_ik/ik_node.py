import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import numpy as np


class InverseKinematics(Node):

    def __init__(self):
        super().__init__('inverse_kinematics')

        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.callback,
            10
        )

        # 🎯 Target (puedes cambiarlo)
        self.target = np.array([1.5, 0.5, 3.0])

        # 📏 Longitudes (Robot A)
        self.l1 = 3.0
        self.l2 = 1.5
        self.l3 = 1.5

    def callback(self, msg):

        try:
            q1 = msg.position[0]
            q2 = msg.position[1]
            q3 = msg.position[2]

            # 🔥 CINEMÁTICA DIRECTA (FK)
            x = np.cos(q1) * (self.l2 * np.cos(q2) + self.l3 * np.cos(q2 + q3))
            y = np.sin(q1) * (self.l2 * np.cos(q2) + self.l3 * np.cos(q2 + q3))
            z = self.l1 + self.l2 * np.sin(q2) + self.l3 * np.sin(q2 + q3)

            current = np.array([x, y, z])

            error = np.linalg.norm(self.target - current)

            # 📢 PRINT COMO EN CLASE
            self.get_logger().info(f"q: {[q1, q2, q3]}")
            self.get_logger().info(f"Posición: {current}")
            self.get_logger().info(f"Error: {error}")

        except Exception as e:
            self.get_logger().error(str(e))


def main(args=None):
    rclpy.init(args=args)
    node = InverseKinematics()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()