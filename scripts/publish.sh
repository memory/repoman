#!/bin/sh -ex

if ! [ -f venv/bin/activate ]; then
  virtualenv --python=$(which python2.7) venv
fi
./venv/bin/pip install -U pip setuptools wheel
./venv/bin/python setup.py sdist bdist_wheel

if ! [ -f venv3/bin/activate ]; then
  virtualenv --python=$(which python3) venv3
fi
./venv3/bin/pip install -U pip setuptools wheel twine
./venv3/bin/python setup.py bdist_wheel

./venv3/bin/twine upload dist/*
