#!/usr/bin/env bash
# as venv is activated we must reset PATH
echo current python is: `which python`
export PATH=`echo $PATH | tr ":" "\n" | grep -v "venv/bin" | tr "\n" ":"`
echo switched to: `pyenv which python`
export PROJECT=drremote
cd ~/Projekte/${PROJECT} || exit 1
if [ -d dist ]; then
  rm -r dist
fi
if [ -d ${PROJECT}.egg-info ]; then
   rm -r ${PROJECT}.egg-info
fi
if [ -d build ]; then
  rm -r build
fi
#
# install from local
python setup.py sdist
pip install dist/${PROJECT}*.gz --force-reinstall
#
# upload to pypi
#
# wheel must be installed before:pip install wheel
#python setup.py bdist_wheel
# twine must be installed before:pip install twine
# user:__token__
#python3 -m twine upload --repository testpypi dist/*
#python3 -m twine upload --repository pypi dist/*

# cleanup
if [ -d dist ]; then
  rm -r dist
fi
if [ -d ${PROJECT}.egg-info ]; then
   rm -r ${PROJECT}.egg-info
fi
if [ -d build ]; then
  rm -r build
fi


