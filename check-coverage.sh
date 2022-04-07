#!/usr/bin/env bash
# Convenience script for running Travis-like checks.
set -ex

datacube system init 

# Run tests, taking coverage.
sleep 3
# Users can specify extra folders as arguments.


sleep 1
# run test
python3 -m pytest --cov=ows_refactored --cov-report=xml coverage_test/cfg_parser.py
cp /tmp/coverage.xml /mnt/artifacts

set +x