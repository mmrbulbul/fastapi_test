#!/bin/bash

set -e
set -x

isort app
ruff check app --fix
ruff format app --check