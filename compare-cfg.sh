#!/usr/bin/env bash
# Convenience script for running Travis-like checks.

set -eu
set -x

while IFS=, read -r product definition; do
  # do something... Don't forget to skip the header line!
  datacube product add $definition
done < workspaces/dev-products.csv

datacube-ows-cfg check -i /env/config/inventory.json

set +x
