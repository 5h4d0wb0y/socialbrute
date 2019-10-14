#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'selenium>=3.141.0',
]

setup_requirements = [ ]

test_requirements = [ ]

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'socialbrute', '__init__.py')) as f:
    exec(f.read(), about)

setup(
    author=about['__author__'],
    author_email=about['__email__'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description=about['__description__'],
    entry_points={
        'console_scripts': [
            'socialbrute=socialbrute.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='socialbrute',
    name='socialbrute',
    packages=find_packages(include=['socialbrute']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/5h4d0wb0y/socialbrute',
    version=about['__version__'],
    zip_safe=False,
)
