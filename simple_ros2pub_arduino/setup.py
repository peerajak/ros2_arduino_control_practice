from setuptools import find_packages, setup

package_name = 'simple_ros2pub_arduino'

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
    maintainer='peerajak',
    maintainer_email='peerajak@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
entry_points={
        'console_scripts': [
                'ros2pub_arduino = simple_ros2pub_arduino.simple_ros2pub_arduino:main',
        ],
},
)
