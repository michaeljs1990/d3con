#!/usr/bin/env python
"""
    Pip module setup
"""
from setuptools import setup

INSTALL_REQUIRES = [
    'docopt >= 0.6.1, < 0.7',
    'PyYAML >= 3.10, < 4',
]

setup(name='d3con',
      version='0.0.1',
      description='Poloniex trading platform',
      url='http://github.com/michaeljs1990/d3con',
      author='Michael Schuett',
      author_email='michaelj1990@gmail.com',
      license='MIT',
      install_requires=INSTALL_REQUIRES,
      packages=["d3con", "d3con/cli"],
      entry_points={
        'console_scripts': [
            'd3con=d3con.cli.main:main',
        ],
      },)
