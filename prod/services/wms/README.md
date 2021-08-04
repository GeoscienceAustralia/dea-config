## Purpose
These are configuration files for OGC web application https://github.com/opendatacube/datacube-ows

## Environment
The web service these configuration files are used at is https://ows.dea.ga.gov.au/

## About inventory.json
`inventory.json`:
    `product`: ows layer odc product name, if this field has two items, it indicates it is a combined virtual product
    `styles_count`: number of styles available for the product
    `styles_list`: the name of each style available for the product
    `total_layers_count`: total number of all the ows layers available from this service.
