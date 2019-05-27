"""Convert a CSV file into HTML pages of cards, for subsequent printing

"""

from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='gamecards',
      version='1.0.0',
      description='Convert a CSV file into HTML pages of cards, for subsequent printing',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/encodis/gamecards',
      author='Philip Hodder',
      author_email='philip.hodder@encodis.com',
      license='MIT',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Games/Entertainment :: Role-Playing'
      ],
      keywords='gamecards cards games playing',
      py_modules=['gamecards'],
      entry_points={
        'console_scripts': [
            'gamecards = gamecards:main',
        ],
      }
      )
