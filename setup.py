"""Convert a CSV file into HTML pages of cards, for subsequent printing


"""

from distutils.core import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='gamecards',
      version='0.0.2',
      description='Convert CSV file into game cards using a template',
      long_description=long_description,
      url='https://github.com/encodis/gamecards',
      author='Philip Hodder',
      author_email='philip.hodder@encodis.com',
      license='MIT',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Games/Entertainment :: Role-Playing'
      ],
      keywords='gamecards cards games playing',
      py_modules=['gamecards'],
      )