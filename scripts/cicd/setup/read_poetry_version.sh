#!/usr/bin/env bash

set -eux

POETRY_VERSION=$(cat .poetry-version)
export "$POETRY_VERSION"
