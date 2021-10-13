# Digital Earth Australia ODC Workspaces

Digital Earth Australia Program maintains multiple datacubes at NCI and AWS. This folder contains the product manifest of those datacubes in CSV format.

The CSV's have the following columns:

- product : The string name of the product in the datacube.
- definition : The YAML product definition for the product, typically stored in `dea-config` git repository `products` folder.
- location : S3-prefix for AWS or Lustre `/g/data` path for NCI where this product is stored.

## Workspaces

Development: [dea-products.csv](dev-products.csv)
Production: [prod-products.csv](prod-products.csv)

# product metadata files
The YAML product metadata definition typically stored in `dea-config` git repository `product_metadata` folder.
## Other files

DEA-Access Products Catalog for products available via DEA-Access: [collections.csv](collections.csv)
