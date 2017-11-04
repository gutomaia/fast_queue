# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='fast_queue',
    version='0.0.1',
    description='Simple Task Producer',
    author="Gustavo Maia Neto (Guto Maia)",
    author_email="guto@guto.net",
    license="GPL3",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "examples"]),
    classifiers=[
    ],
    url='http://github.com/gutomaia/fast_queue/',
)
