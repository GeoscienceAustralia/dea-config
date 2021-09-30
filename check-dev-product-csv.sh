#!/usr/bin/env bash
# Convenience script for running Travis-like checks.

set -eu
set -x

datacube metadata add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/41a6cdcd08043e9b2ee292024320db175a86c9d2/workspaces/sandbox-metadata.yaml
datacube metadata add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/master/products/nrt/sentinel/eo_s2_nrt.odc-type.yaml

while IFS=, read -r product definition location; do
    if [[ $definition == *"http"* ]]; then
        datacube product add $definition
    fi
done < /env/config/dev-products.csv

if [ $(datacube product list | wc -l) -eq 74 ]; then
    echo 'equal'
fi

set +x
