"""Convert a CSV file into HTML pages of cards, for subsequent printing

"""

import pypandoc
from distutils.core import setup

long_description = pypandoc.convert('README.md', 'rst')

setup(name='gamecards',
      version='0.1.0',
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