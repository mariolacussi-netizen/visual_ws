from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(package='pubsub2', executable='sensor1'),
        Node(package='pubsub2', executable='sensor2'),
        Node(package='pubsub2', executable='sensor3'),
        Node(package='pubsub2', executable='filtered_sensor'),
        Node(package='pubsub2', executable='filtered_subscriber'),

    ])