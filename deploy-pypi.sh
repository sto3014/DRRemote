#!/usr/bin/env bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source "${SCRIPT_DIR}"/build.env

cd ~/Projekte/${PROJECT} || exit 1

./clean.sh
./package.sh
python3 -m pip install --upgrade twine
# deploy
# user:__token__
python3 -m twine upload --repository pypi dist/*


