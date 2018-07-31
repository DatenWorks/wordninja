#!/usr/bin/env python

from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

__supported_langs = ['en_US', 'pt_BR']
setup(name='wordninja',
      version='0.2.1',
      description="""Probabilistically split concatenated words using NLP
                     based on Wikipedia uni-gram frequencies.""",
      author='Derek Anderson',
      author_email='public@kered.org',
      packages=['wordninja'],
      url='https://github.com/keredson/wordninja',
      package_data={'wordninja': [
          '%s/wordninja_words.txt.gz' % lang for lang in __supported_langs]},
      package_dir={'wordninja': 'wordninja'},
      include_package_data=True,
      py_modules=['wordninja'],
      )
