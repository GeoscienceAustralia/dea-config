#!/usr/bin/env bash
# Convenience script for running Travis-like checks.

set -eu
set -x

find . -path '**/coverage_test' -prune -false -o -name '*.py' | xargs -n1 pylint -j 2 --reports no --disable=W,C,R

set +x
