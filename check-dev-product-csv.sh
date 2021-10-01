#!/usr/bin/env bash

set -eu
set -x


while IFS=, read -r product definition location; do
    if [[ $definition == *"http"* ]]; then
        datacube product add $definition
    fi
done < /env/config/dev-products.csv

if [ $(datacube product list | wc -l) -ne 74 ]; then
    exit 1
fi

set +x
