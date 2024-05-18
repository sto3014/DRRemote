#!/usr/bin/env bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source "${SCRIPT_DIR}"/build.env

cd ~/Projekte/${PROJECT} || exit 1
export PATH=`echo $PATH | tr ":" "\n" |  grep -v "venv" | tr "\n" ":"`
./clean.sh
./package.sh

# Install global
pip3 install dist/${PROJECT}*.whl --force-reinstall



