# DEA Config
Config files for dea services

This is a central space used to store configuration for our services and products.

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
