#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup pymdown-extensions."""

from setuptools import setup, find_packages


def get_requirements(req):
    """Load list of dependencies."""

    install_requires = []
    with open(req) as f:
        for line in f:
            if not line.startswith("#"):
                install_requires.append(line.strip())
    return install_requires


setup(
    name='stella-extensions',
    version="0.0.1",
    description='Extension pack for Python Markdown.',
    python_requires='>=3.6',
    url='https://github.com/facelessuser/pymdown-extensions',
    packages=find_packages(exclude=['tools', 'test*']),
    install_requires=get_requirements("requirements/project.txt"),
    license='MIT License',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
    ]
)
