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

set +x