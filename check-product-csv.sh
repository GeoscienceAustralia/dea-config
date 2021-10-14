#!/usr/bin/env bash

set -eu
set -x

while IFS=, read -r product definition location; do
    if [[ $definition == *"http"* ]]; then
        datacube product add $definition
    fi
done < /env/config/${WORKSPACE_CSV_FILE}

# if [ $(datacube product list | wc -l) -ne 69 ]; then
#     exit 1
# fi

datacube product list

wget https://${EXPLORER_ENDPOINT}/audit/storage.csv -O /tmp/live-db-products.csv

# check if workspace csv has all the products in live db
while IFS=, read -r name count location license definition summary metadata_type; do
    if ! grep -q $name /env/config/${WORKSPACE_CSV_FILE}; then
        echo missing $name from live prod database
    fi
done < /tmp/live-db-products.csv

# check if workspace csv has extra products NOT in live db
while IFS=, read -r product definition location; do
    if ! grep -q $product /tmp/live-db-products.csv; then
        echo csv has $product but not in live prod db
    fi
done < /env/config//${WORKSPACE_CSV_FILE}


set +x
