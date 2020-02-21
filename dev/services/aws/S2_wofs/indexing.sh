datacube product add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/master/dev/products/wofs/sentinel2_wofs_def.yaml
#datacube product add https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/dsg2/dev/products/wofs/sentinel2_wofs_def.yaml

s3-find 's3://dea-public-data-dev/wofs/ga_s2am_wofs_2/*/*/*/*/*/*/*.odc-metadata.yaml'  | s3-to-tar --xz > test_wofls.tar.xz

dc-index-from-tar --xz --ignore-lineage --eo3 test_wofls.tar.xz
