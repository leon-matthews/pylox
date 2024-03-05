#!/bin/bash

# Run 'flake8' style-checker over package and test code
# http://www.mypy-lang.org/

set -o nounset
set -o errexit
set +o xtrace


ruff check $@ .
