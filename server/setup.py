import sys, os, logging
try:
    from setuptools import setup, find_packages, Extension
    from setuptools.command.build_ext import build_ext as _build_ext
except ImportError:
    logging.warning("Setuptools not installed. Defaulting to distutils.")
    from distutils.core import setup

if find_packages:
    setup(name='testing_flask',
          version='1.0.0',
          description='testing_flask',
          install_requires=[
              'flask',
              'flask-mysql'],
          py_modules=['core_module'],
          packages=find_packages()
        )
else:
    raise NotImplementedError("Currently no distutils support. Install setuptools.")

