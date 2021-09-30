#!/usr/bin/env bash
# Convenience script for running Travis-like checks.

set -eu
set -x

datacube metadata add https://raw.githubusercontent.com/GeoscienceAustralia/digitalearthau/develop/digitalearthau/config/metadata-types.odc-type.yaml
datacube metadata add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/master/products/nrt/sentinel/eo_s2_nrt.odc-type.yaml

for prod_def_yaml in /env/config/products/*; do
    datacube product add prod_def_yaml
done

if [ $(datacube product list | wc -l) -eq 74 ]; then
    echo 'equal'
fi

set +x
