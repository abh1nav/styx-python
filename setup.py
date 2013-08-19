#!/usr/bin/env python

import os
import sys

version = "0.1.2"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist register upload")
    sys.exit(1)

# These are required because sometimes PyPI refuses to bundle certain files
try:
    long_desc = open('README').read()
except:
    long_desc = ""

try:
    license = open('LICENSE.txt').read()
except:
    license = "Apache 2.0 License"

setup(
    name='styx',
    version=version,
    description='Distributed message queue based on Redis',
    long_description=long_desc,
    author='Abhinav Ajgaonkar',
    author_email='abhinav316@gmail.com',
    packages=['styx'],
    url='http://pypi.python.org/pypi/styx/',
    license=license,
    install_requires=[
        "redis == 2.7.6"
    ]
)