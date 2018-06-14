#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Learn from: https://github.com/kennethreitz/setup.py

import os
import sys

from shutil import rmtree
from setuptools import setup, Command

here = os.path.abspath(os.path.dirname(__file__))

packages = ['emotlib']

requires = []

about = {}
with open(os.path.join(here, 'emotlib', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    python_requires=">=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    license=about['__license__'],
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Traditional)',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications',
        'Topic :: Communications :: BBS',
        'Topic :: Communications :: Chat',
        'Topic :: Communications :: Email',
        'Topic :: Communications :: Internet Phone'
    ),
    cmdclass={
        'upload': UploadCommand
    }
)
