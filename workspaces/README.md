# Digital Earth Australia ODC Workspaces

Digital Earth Australia Program maintains multiple datacubes at NCI and AWS. This folder contains the product manifest of those datacubes in CSV format.

The CSV's have the following columns:

- product : The string name of the product in the datacube.
- definition : The YAML product definition for the product, typically stored in `dea-config` or `digitalearthau` git repositories.
- location : S3-prefix for AWS or Lustre `/g/data` path for NCI where this product is stored.

## Workspaces

Development Web Services / Sandbox: [dea-products.csv](dev-products.csv)
Production Web Services : [prod-products.csv](prod-products.csv)
Production Sandbox : [sandbox-products.csv](sandbox-products.csv)

## Other files

DEA-Access Products Catalog for products available via DEA-Access: [collections.csv](collections.csv)
Sandbox Products Metadata for all products in production sandbox : [sandbox-metadata.yaml](sandbox-metadata.yaml)