f#!/usr/bin/env python3
rom setuptools import setup

setup(
    name='robot_cleaner',
    version='0.0.0',
    packages=['robot_cleaner'],
    install_requires=['rospy'],
    package_dir={'': 'src'}
)
