#!/usr/bin/env python

from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

__supported_langs = ['en_US', 'pt_BR']
setup(name='wordninja',
      version='0.3.1',
      description="""Probabilistically split concatenated words using NLP
                     based uni-gram frequencies.""",
      author='Matheus Cunha',
      author_email='matheus.cunha@archlinux.com.br',
      packages=['wordninja'],
      url='https://github.com/macunha1/wordninja',
      package_data={'wordninja': [
          '%s/wordninja_words.txt.gz' % lang for lang in __supported_langs]},
      package_dir={'wordninja': 'wordninja'},
      include_package_data=True,
      py_modules=['wordninja'],
      )
