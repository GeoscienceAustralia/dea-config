#!/usr/bin/env bash

set -eu
set -x

for prod_def_yaml in $(find /env/config/products -name '*.yaml'); do
    if [[ $prod_def_yaml != "/env/config/products/baseline_satellite_data/nrt/sentinel/eo_s2_nrt.odc-type.yaml" && $prod_def_yaml != "/env/config/products/land_and_vegetation/mangrove/mangrove.yaml" ]]; then
        datacube product add $prod_def_yaml
    fi
done

if [ $(datacube product list | wc -l) -eq 74 ]; then
    echo 'equal'
fi

set +x
