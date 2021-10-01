#!/usr/bin/env bash

set -eu
set -x


while IFS=, read -r product definition location; do
    if [[ $definition == *"http"* ]]; then
        datacube product add $definition
    fi
done < /env/config/dev-products.csv

if [ $(datacube product list | wc -l) -eq 74 ]; then
    echo 'equal'
fi

set +x
