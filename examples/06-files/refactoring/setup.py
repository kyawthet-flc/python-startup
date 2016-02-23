#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script to install the process file command line tool
"""

from setuptools import setup, find_packages

setup(
    name='processFile',
    version=__version__,
    description='processFile is a cmd line tool to process data',
    long_description=open("README.md").read(),
    author='Pierre Roth',
    author_email='pierreroth64@gmail.com',
    url='https://github.com/pierreroth64/python-startup',
    license='MIT License',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "xmlutils",
    ],
    entry_points={
        'console_scripts': [
            'processfile=processfile.process_file:main',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)
