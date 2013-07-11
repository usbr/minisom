#!/usr/bin/env python

from distutils.core import setup

setup(name='MiniSom',
  version='0.1',
  description='Minimalistic implementation of the Self Organizing Maps (SOM)',
  author='Giuseppe Vettigli',
  package_data={'': ['Readme.md']},
  include_package_data=True,
  license="MIT",
  py_modules=['minisom'],
  requires = ['numpy']
 )
