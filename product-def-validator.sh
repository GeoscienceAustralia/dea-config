#!/usr/bin/env bash
# Convenience script for running Travis-like checks.

# set -eu
# set -x

while IFS=, read -r product definition location; do
  # do something... Don't forget to skip the header line!
  datacube product add $definition
done < /env/config/products.csv

# set +x
