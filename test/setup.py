#!/usr/bin/env python3
from setuptools import setup

setup(
    name='my-app',
    version='0.1.0',
    description='Sample Python app depending on pydantic',
    py_modules=['my_app'],
    install_requires=[
        'pydantic>=2.13.4',
    ],
    entry_points={
        'console_scripts': [
            'my-app=my_app:main',
        ],
    },
)
