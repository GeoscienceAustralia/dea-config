# This file is mounted to `docker-compose.productcsv.yaml`
# Used for system maintainer for range of consistency checks
# each section can be commented out for targetted testing
# to execute, `docker-compose exec -it dea-config_datacube_1 bash`
# then `cd /env/config` and execute this script
# 1. first section checks against live database
# 2. second section checks within products folder for duplicate product definitions

# set -eu
# set -x

datacube product list -f csv > /tmp/product_list.csv

# SECTION 1
# check against live db
while IFS=, read -r id name description ancillary_quality latgqa_cep90 product_type gqa_abs_iterative_mean_xy gqa_ref_source sat_path gqa_iterative_stddev_xy time sat_row orbit gqa instrument gqa_abs_xy crs resolution tile_size spatial_dimensions; do
    if [[ $(wget https://explorer.dev.dea.ga.gov.au/products/$name.odc-product.yaml -O-) ]] 2>/dev/null
        then
            datacube product add https://explorer.dev.dea.ga.gov.au/products/$name.odc-product.yaml
    fi
done < /tmp/product_list.csv

# SECTION 2
# check against folder search for duplicates
while IFS=, read -r id name description ancillary_quality latgqa_cep90 product_type gqa_abs_iterative_mean_xy gqa_ref_source sat_path gqa_iterative_stddev_xy time sat_row orbit gqa instrument gqa_abs_xy crs resolution tile_size spatial_dimensions; do
    echo $name
    grep -rnw '/env/config/products' -e "name: $name"
done < /tmp/product_list.csv

# set +x