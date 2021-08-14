## Purpose
These are configuration files for OGC web application https://github.com/opendatacube/datacube-ows

## Environment
The web service these configuration files are used at is https://ows.dev.dea.ga.gov.au/

## About inventory.json
`inventory.json`:
    `product`: ows layer odc product name, if this field has two items, it indicates it is a combined virtual product
    `styles_count`: number of styles available for the product
    `styles_list`: the name of each style available for the product
    `total_layers_count`: total number of all the ows layers available from this service.

## Testing
1. clone datacube-ows `git clone https://github.com/opendatacube/datacube-ows.git`
2. go to datacube-ows folder `cd datacube-ows`
3. prepare `.env` file `cp .env_ows_root .env`
4. update `.env` file with the correct datacube environment config and ensure `OWS_CFG_FOLDER` is pointing to the correct path.
5. `docker-compose up`

Note: this requires an indexed datacube database and `.env` configuration needs to point to the database.