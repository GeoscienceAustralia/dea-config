#!/usr/bin/env bash

set -eu
set -x

# when datacube system init is run 3 default metadata are created
# - eo3
# - telemetry
# - eo
# https://github.com/opendatacube/datacube-core/blob/6d75b686656d8688cc830897d596bfd26cfea336/datacube/index/default-metadata-types.yaml

for metadata_yaml in $(find /env/config/product_metadata -name '*.yaml'); do
    datacube metadata add $metadata_yaml
done
