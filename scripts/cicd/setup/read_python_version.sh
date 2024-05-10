#!/usr/bin/env bash

set -eux

PYTHON_VERSION=$(cat .python-version)
export "$PYTHON_VERSION"
