# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'VERSION.txt')) as f:
    VERSION = f.read().strip()

with open(os.path.join(here, 'requirements.txt')) as f:
    REQUIREMENTS = [line for line in iter(f) if not line.startswith('--')]

with open(os.path.join(here, 'README.rst')) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='fast_queue',
    version=VERSION,
    description='Simple Task Producer',
    long_description=LONG_DESCRIPTION,
    author="Gustavo Maia Neto (Guto Maia)",
    author_email="guto@guto.net",
    license="MIT",
    install_requires=REQUIREMENTS,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "examples"]),
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    url='http://github.com/gutomaia/fast_queue/',
)
