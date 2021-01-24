#!/usr/bin/env bash
# Convenience script for running Travis-like checks.

set -eu
set -x

find . -name "*.py"  -not -path "./dev/services/wms/ows_refactored/*" | xargs -n1 pylint -j 2 --reports no --disable=W,C,R

set +x
