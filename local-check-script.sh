#!/usr/bin/env bash
# This file is mounted to `docker-compose.productcsv.yaml`
# Used for system maintainer for range of consistency checks
# each section can be commented out for targetted testing
# to execute, `docker-compose exec -it dea-config_datacube_1 bash`
# then `cd /env/config` and execute this script
# 1. first section checks against live database
# 2. second section checks within products folder for duplicate product definitions

# set -eu
# set -x
datacube system init
./datacube_init_metadata.sh

# SECTION 1
# check against live db
datacube product list -f csv > /tmp/product_list.csv
while IFS=, read -r id name description ancillary_quality latgqa_cep90 product_type gqa_abs_iterative_mean_xy gqa_ref_source sat_path gqa_iterative_stddev_xy time sat_row orbit gqa instrument gqa_abs_xy crs resolution tile_size spatial_dimensions; do
    if [[ $(wget https://explorer.dev.dea.ga.gov.au/products/$name.odc-product.yaml -O-) ]] 2>/dev/null
        then
            datacube product add https://explorer.dev.dea.ga.gov.au/products/$name.odc-product.yaml
    fi
done < /tmp/product_list.csv

# SECTION 2
# check against folder search for indexed products and filter out duplicate product files
datacube product list -f csv > /tmp/product_list.csv
while IFS=, read -r id name description ancillary_quality latgqa_cep90 product_type gqa_abs_iterative_mean_xy gqa_ref_source sat_path gqa_iterative_stddev_xy time sat_row orbit gqa instrument gqa_abs_xy crs resolution tile_size spatial_dimensions; do
    echo $name
    grep -rnw '/env/config/products' -e "name: $name"
done < /tmp/product_list.csv

# SECTION 3
# check for duplicates within decommissioned folder
for prod_def_yaml in $(find /env/config/products/decommissioned ! -path '*/duplicates/*' -name '*.yaml'); do
    datacube product add $prod_def_yaml
done

datacube product list -f csv > /tmp/product_list.csv

while IFS=, read -r id name description ancillary_quality latgqa_cep90 product_type gqa_abs_iterative_mean_xy gqa_ref_source sat_path gqa_iterative_stddev_xy time sat_row orbit gqa instrument gqa_abs_xy crs resolution tile_size spatial_dimensions; do
    echo $name
    if [  ${#name} -ge 1 ];then
        grep -rnw '/env/config/products/decommissioned' -e "name: $name"
    fi
done < /tmp/product_list.csv

set +x


set -eu

while IFS=, read -r product definition location; do
    if [[ $definition == *"http"* ]]; then
        datacube product add $definition
    fi
done < /env/config/dev-products.csv

datacube product list

wget https://explorer.dev.dea.ga.gov.au/audit/storage.csv -O /tmp/live-dev-db-products.csv

# check if workspace csv has all the products in live db
while IFS=, read -r name count location license definition summary metadata_type; do
    if ! grep -q $name /env/config/dev-products.csv; then
        echo missing $name from live dev database
    fi
done < /tmp/live-dev-db-products.csv

# check if workspace csv has extra products NOT in live db
while IFS=, read -r product definition location; do
    if ! grep -q $product /tmp/live-dev-db-products.csv; then
        echo csv has $product but not in live dev db
    fi
done < /env/config/dev-products.csv


wget https://explorer.sandbox.dea.ga.gov.au/audit/storage.csv -O /tmp/live-prod-db-products.csv

# check if workspace csv has all the products in live db
while IFS=, read -r name count location license definition summary metadata_type; do
    if ! grep -q $name /env/config/prod-products.csv; then
        echo missing $name from live prod database
    fi
done < /tmp/live-prod-db-products.csv

# check if workspace csv has extra products NOT in live db
while IFS=, read -r product definition location; do
    if ! grep -q $product /tmp/live-prod-db-products.csv; then
        echo csv has $product but not in live prod db
    fi
done < /env/config/prod-products.csv
