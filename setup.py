#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pipsearch
    PyPI.org packages search app
 - File: setup.py
 - Author: Havocesp <https://github.com/havocesp/pipsearch>
 - Created: 2022-09-10
 -
"""
from setuptools import find_packages, setup

exclude_pkgs = [
    '.idea*',
    'build*',
    '*.vs',
    '*.code',
    '*.atom',
    'pipsearch.egg-info*',
    'dist*',
    'venv*'
]

setup(
    name='pipsearch',
    version='0.0.3',
    packages=find_packages(exclude=exclude_pkgs),
    url=f'https://github.com/havocesp/{__package__}',
    license='UNLICENSE',
    packages_dir={'': __package__},
    author='Havocesp',
    author_email='umpierrez@pm.me',
    long_description='PyPI.org packages search app',
    description='PyPI.org packages search app',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
    ],
    entry_points={
        'console_scripts': [
            'pipsearch = pipsearch.main:run'
        ]
    },
    install_requires=['bs4', 'requests', 'tabulate', 'dateutils'],
)
