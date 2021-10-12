#!/usr/bin/env bash

set -eu
set -x

for prod_def_yaml in $(find /env/config/products -name '*.yaml'); do
    if [[ $prod_def_yaml != "/env/config/products/land_and_vegetation/mangrove/mangrove.nci.yaml" && $prod_def_yaml != *"decommissioned/"* ]]; then
        datacube product add $prod_def_yaml
    fi
done

datacube product list

set +x
