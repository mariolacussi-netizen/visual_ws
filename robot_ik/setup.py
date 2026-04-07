from setuptools import find_packages, setup

package_name = 'robot_ik'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mariola',
    maintainer_email='adrian.cussi@ucb.edu.bo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'ik_node = robot_ik.ik_node:main',
            'ik_nodebio = robot_ik.ik_nodebio:main',
        ],
    },
)
