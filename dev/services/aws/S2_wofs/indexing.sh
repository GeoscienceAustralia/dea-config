#datacube product add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/dsg2/dev/products/wofs/sentinel2_wofs_def.yaml #

tar c ga_s2am_wofs_2-2-1_54HUF_2018-01-02_interim.odc-metadata.yaml | dc-index-from-tar -E  odc_conf_test --protocol file --eo3


#datacube dataset add --confirm-ignore-lineage s3://dea-public-data-dev/wofs/ga_s2am_wofs_2/54/HUF/2018/01/02/20180102T034621/ga_s2am_wofs_2-2-1_54HUF_2018-01-02_interim.odc-metadata.yaml