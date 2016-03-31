from setuptools import setup
from setuptools import find_packages


setup(name='psb-adr',
      version='0.0',
      description='Library for ADR classification',
      author='Zhang et al.',
      url='https://github.com/tjflexic/psb-adr',
      install_requires=['beautifulsoup4', 'nltk', 'pandas'],
      packages=['zhang_adr', 'zhang_adr.tweetnlp'],
      package_dir={
          'zhang_adr': 'src'
      },
      package_data={
          'zhang_adr': ['data/*.txt'],
          'zhang_adr.tweetnlp': ['ark-tweet-nlp-0.3.2.jar'],
      }
      )

