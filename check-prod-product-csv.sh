#!/usr/bin/env bash

set -eu
set -x

while IFS=, read -r product definition location; do
    if [[ $definition == *"http"* ]]; then
        datacube product add $definition
    fi
done < /env/config/prod-products.csv

if [ $(datacube product list | wc -l) -eq 69 ]; then
    echo 'equal'
fi

set +x
