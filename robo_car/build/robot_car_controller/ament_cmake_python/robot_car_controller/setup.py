from setuptools import find_packages
from setuptools import setup

setup(
    name='robot_car_controller',
    version='0.0.0',
    packages=find_packages(
        include=('robot_car_controller', 'robot_car_controller.*')),
)
