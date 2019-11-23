# -*- coding: utf-8 -*-
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


requires = """
    tonnikala>=1.0.0b1
""".split()


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read().strip()


setup(
    name='django-tonnikala',
    version='0.0.2',
    description='Django backend for Tonnikala templating language',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rainer Koirikivi',
    author_email='rainer@koirikivi.fi',
    url='https://github.com/koirikivi/django-tonnikala',
    classifiers=[
        "Framework :: Django",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    install_requires=requires,
    setup_requires=[],
    include_package_data=True,
    packages=find_packages(exclude=['example_project']),
    tests_require=[],
)
