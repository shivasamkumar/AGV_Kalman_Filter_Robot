from setuptools import find_packages
from setuptools import setup

setup(
    name='robot_car_localization',
    version='0.0.0',
    packages=find_packages(
        include=('robot_car_localization', 'robot_car_localization.*')),
)