#!/usr/bin/env bash

set -eux

PYTHON_VERSION=$(cat .python-version)
echo "::set-output name=PYTHON_VERSION::$PYTHON_VERSION"
