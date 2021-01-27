#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='pyplugnotas',
    version='0.1',
    author='Startup Code',
    author_email='suporte@startupcode.com.br',
    url='https://github.com/startupcodebr',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'requests',
    ],
    zip_safe=False,
    python_requires='>3',
)