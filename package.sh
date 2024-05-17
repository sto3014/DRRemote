#!/usr/bin/env bash
clear
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source "${SCRIPT_DIR}"/build.env
echo current python is: `which python3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      `


cd ~/Projekte/${PROJECT} || exit 1

# install/update necessary packages
python3 -m pip install --upgrade build
python3 -m pip install --upgrade pip

# Create build
python3 -m build
