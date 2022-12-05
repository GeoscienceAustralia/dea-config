[![codecov](https://codecov.io/gh/GeoscienceAustralia/dea-config/branch/master/graph/badge.svg?token=zuk7FaS1HA)](https://codecov.io/gh/GeoscienceAustralia/dea-config)
# DEA Config
Config files for dea services

This is a central space used to store configuration for our services and products.


## Formatting for Terria Data Description section in `ows config`
#### Bold
```
**Overview**
```
#### Italic
```
*Overview*
```

## Testing

### products metadata and products definition testing

#### testing workspace csv
First, create an `.env` file for the `docker-compose` setup
```bash
    vi .env
    # inside .env
ENV=prod
EXPLORER_ENDPOINT=explorer.sandbox.dea.ga.gov.au
```
then bring up the testing tool
```bash
    docker-compose -f docker-compose.productscsv.yaml up -d
    docker exec -it dea-config_datacube_1 bash
    # within the docker container run
    datacube system init
    cd /env/config
    ./datacube_init_metadata.sh
    ./check-product-csv.sh
```

#### audit checks (local-check-script.sh)
```bash
    docker-compose -f docker-compose.productscsv.yaml up -d
    docker exec -it dea-config_datacube_1 bash
    # within the docker container run
    datacube system init
    cd /env/config
    ./datacube_init_metadata.sh
    ./local-check-script.sh
```


### ows config testing
First, create an `.env` file for the `docker-compose` setup

```bash
    vi .env
    # inside .env
OWS_CFG_PATH=dev/services/wms/ows_refactored
DATACUBE_OWS_CFG=ows_refactored.ows_root_cfg.ows_cfg
PYTHON_PATH=dev/services/wms/
```

then bring up the testing tool

```bash
    docker-compose -f docker-compose.ows.yaml up -d
    docker exec -it dea-config_ows_1 bash
    # within the docker container run
    cd /env/config
    datacube system init
    ./compare-cfg.sh
```

## Pull Request Template
There are three pull request Templates available for the following changes:
- ows config changes (ows_cfg.md)
- terria json changes (terria.md)
- product yaml file changes (product.md)

To access the PR templates
- open up a new pull request page and add `&template=ows_cfg.md`, `&template=terria.md` or `&template=product.md` at the end of the url

for example https://github.com/GeoscienceAustralia/dea-config/compare/ows-fix-depreciated?expand=1&template=ows_cfg.md
# Usage
Files should be referenced by the raw tag on the master branch i.e.


https://raw.githubusercontent.com/GeoscienceAustralia/dea-config/master/prod/products/nrt/landsat/products.yaml

# Dependants

[Datacube EKS](https://github.com/opendatacube/datacube-k8s-eks) - Containerised Web Services for DEA running on
AWS EKS.
