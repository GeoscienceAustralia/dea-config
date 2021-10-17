#!/usr/bin/env bash

set -eu

for prod_def_yaml in $(find /env/config/products -name '*.yaml'); do
    if [[ $prod_def_yaml != "/env/config/products/land_and_vegetation/mangrove/mangrove.nci.yaml" && $prod_def_yaml != *"decommissioned/"* ]]; then
        datacube product add $prod_def_yaml
    fi
done

cd /env/config/products
if [[ $(find . -type f ! -path './decommissioned/*' -name '*.yaml' -not -name '*.nci*' | wc -l) != $(datacube product list | wc -l) ]];then
    datacube product list | wc -l
fi