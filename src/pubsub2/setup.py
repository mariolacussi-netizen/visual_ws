from setuptools import setup, find_packages
from glob import glob
import os
package_name = 'pubsub2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', 'pubsub2', 'msg'), glob('msg/*.msg')),


        (os.path.join('share', 'pubsub2', 'launch'), glob('launch/*.py')),
       
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adrian',
    maintainer_email='adrian@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'sensor1= pubsub2.sensor1:main',
            'sensor2= pubsub2.sensor2:main',
            'sensor3 = pubsub2.sensor3:main',
            'filtered_sensor = pubsub2.filtered_sensor:main',
            'filtered_subscriber = pubsub2.filtered_subscriber:main',
        ],
    },
)
