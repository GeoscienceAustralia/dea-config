#!/usr/bin/env bash
# Convenience script for running Travis-like checks.

set -eu
set -x

datacube-ows-cfg-parse -i /env/config/inventory.json

set +x

