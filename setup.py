#!/usr/bin/env python

from setuptools import setup, find_packages

__name__ = 'apt-repoman'
__version__ = '1.0.7'

setup(
    name=__name__,
    packages=find_packages(),
    version=__version__,
    description=('A high performance Debian APT repository based '
                 'on Amazon Web Services'),
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author='Nathan J. Mehl',
    author_email='pypi@memory.blank.org',
    url='https://github.com/memory/repoman',
    download_url='https://github.com/memory/repoman/tarball/%s' % __version__,
    keywords=['apt', 'debian', 'dpkg', 'packaging'],
    package_data={'': ['*.json']},
    setup_requires=[
        "wheel",
    ],
    install_requires=[
        'PGPy==0.5.2',
        'ansicolors==1.1.8',
        'boto3==1.4.4',
        'configargparse==0.12.0',
        'pydpkg==1.3.3',
        'pysectools==0.4.2',
        'tabulate==0.7.7'
    ],
    extras_require={
        'test': [
            'mock==2.0.0',
            'pep8==1.7.0',
            'pylint==1.7.1',
            'pytest==3.1.1',
        ]
    },
    entry_points={
        'console_scripts': ['repoman-cli=apt_repoman.cli:main'],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: System :: Archiving :: Packaging",
        ]
)
