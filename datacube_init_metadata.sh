#!/usr/bin/env bash

set -eu
set -x

# when datacube system init is run 3 default metadata are created
# - eo3
# - telemetry
# - eo
# https://github.com/opendatacube/datacube-core/blob/6d75b686656d8688cc830897d596bfd26cfea336/datacube/index/default-metadata-types.yaml

datacube metadata add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/master/products/baseline_satellite_data/nrt/sentinel/eo_s2_nrt.odc-type.yaml
datacube metadata add https://raw.githubusercontent.com/GeoscienceAustralia/digitalearthau/develop/digitalearthau/config/eo3/eo3_landsat_ard.odc-type.yaml
datacube metadata add https://explorer.dev.dea.ga.gov.au/metadata-types/gqa_eo.odc-type.yaml
datacube metadata add https://explorer.dev.dea.ga.gov.au/metadata-types/eo_plus.odc-type.yaml