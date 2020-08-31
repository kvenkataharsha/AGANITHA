import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name = 'spokentowrittenenglish',
      packages = ['spokentowrittenenglish'],
      description='Convert Spoken English to Written English ',

    )
