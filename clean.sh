#!/usr/bin/env bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source "${SCRIPT_DIR}"/build.env

cd ~/Projekte/${PROJECT} || exit 1
if [ -d dist ]; then
  rm -r dist
fi
if [ -d src/${PROJECT}.egg-info ]; then
   rm -r src/${PROJECT}.egg-info
fi

