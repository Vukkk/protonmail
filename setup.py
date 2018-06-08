"""
Copyright (c) 2018, Jairus Martin.

Distributed under the terms of the BSD License.

The full license is in the file LICENSE, distributed with this software.

Created on May, 2018
"""
from setuptools import setup, find_packages


setup(
    name='protonmail',
    version='0.1.0',
    author='frmdstryr',
    author_email='frmdstryr@gmail.com',
    url='https://gitlab.com/frmdstryr/protonmail',
    description='A python client for protonmail',
    license="BSD",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['treq', 'pgpy', 'bcrypt', 'atom', 'crochet'],
    packages=find_packages(),
)
