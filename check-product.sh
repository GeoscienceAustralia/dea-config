#!/usr/bin/env bash
# Convenience script for running Travis-like checks.

set -eu
set -x

while IFS=, read -r product definition location; do
    if [[ $definition == *"http"* ]]; then
        datacube product add $definition
    fi
done < /env/config/products.csv

if [ $(datacube product list | wc -l) -eq 74 ]; then
    echo 'equal'
fi

set +x
