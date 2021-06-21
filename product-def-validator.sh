#!/usr/bin/env bash
# Convenience script for running Travis-like checks.

while IFS=, read -r product definition location; do
  # do something... Don't forget to skip the header line!
  datacube product add $definition
done < /env/config/products.csv

# set -eu
# set -x

datacube product list | wc -l
cat /env/config/products.csv | wc -l
# set +x
