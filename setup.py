#!/usr/bin/env python
"""Setup for the willamette micro-service, part of the Quaerere Platform
"""

import os

from setuptools import find_packages, setup

PROJECT_NAME = 'quaerere-willamette'
PROJECT_VERSION = '0.0.0a0.dev0'
PROJECT_RELEASE = '.'.join(PROJECT_VERSION.split('.')[:2])
INSTALL_REQUIRES = [
    'Flask-Classful>=0.14.2',
    'flask-marshmallow>=0.10.0',
    'python-arango>=4.4']
SETUP_REQUIRES = [
    'pytest-runner',
    'Sphinx>=1.8.0',
    'setuptools']
TESTS_REQUIRES = [
    'pytest>=4.2.0',
    'pytest-cov>=2.6.0']


def _create_build_dirs():
    build_dir = os.environ.get('BUILD_ROOT', 'build')
    build_sub_dirs = [
        'coverage',
        'pytest',
        'sphinx']
    for sub_dir in build_sub_dirs:
        path = os.path.join(os.path.dirname(__file__), build_dir, sub_dir)
        if not os.path.exists(path):
            os.makedirs(path)


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name=PROJECT_NAME,
      version=PROJECT_VERSION,
      description='A component of the Quaerere Platform',
      long_description=readme(),
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Programming Language :: Python :: 3.6', ],
      author="Caitlyn O'Hanna",
      author_email='caitlyn.ohanna@virtualxistenz.com',
      url='https://github.com/QuaererePlatform/willamette',
      packages=find_packages(exclude=['docs', 'tests']),
      zip_safe=False,
      test_suite='tests',
      python_requires='~=3.6',
      install_requires=INSTALL_REQUIRES,
      setup_requires=SETUP_REQUIRES,
      tests_require=TESTS_REQUIRES,
      entry_points={
          'distutils.commands': [
              'build_sphinx = sphinx.setup_command:BuildDoc']},
      command_options={
          'build_sphinx': {
              'project': ('setup.py', PROJECT_NAME),
              'version': ('setup.py', PROJECT_VERSION),
              'release': ('setup.py', PROJECT_RELEASE),
              'source_dir': ('setup.py', 'docs')}})
