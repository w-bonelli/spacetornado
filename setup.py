#!/usr/bin/env python

from distutils.core import setup

setup(name='spacetornado',
      version='0.1',
      description='A minimal Tornado API for Spacy text analytics.',
      author='Wes Bonelli',
      url='https://w-bonelli.github.io',
      packages=['spacetornado'],
      entry_points={
        'console_scripts':[
            'spacetornado = spacetornado.spacetornado:space_tornado'
        ]
      },
      install_requires=['tornado','spacy'])
