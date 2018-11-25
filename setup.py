# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='micpy',
    version='0.1.0',
    description='Compute MIC and its related indicators',
    long_description=readme,
    author='Yuta Masubuchi',
    author_email='yuuta.masubuti@gmail.com',
    install_requires=['pandas', 'minepy'],
    url='https://github.com/b-traut/micpy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

