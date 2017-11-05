# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    REQUIREMENTS = [line for line in iter(f) if not line.startswith('--')]


setup(
    name='fast_queue',
    version='0.0.1',
    description='Simple Task Producer',
    author="Gustavo Maia Neto (Guto Maia)",
    author_email="guto@guto.net",
    license="GPL3",
    install_requires=REQUIREMENTS,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "examples"]),
    classifiers=[
    ],
    url='http://github.com/gutomaia/fast_queue/',
)
