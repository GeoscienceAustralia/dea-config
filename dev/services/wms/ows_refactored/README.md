# OWS CFG refactored
Goal: Split mega single file ows_cfg.py into multiple manageable/maintainable config files.

## Structure
### root config
This file will act as an assembler which include all the categories required for the ows service. `ows_root_cfg.py`, this file lists all 6 categories.

#### Resuable parts shared across all categories
- legend definition `ows_legend_cfg.py`
- resource limit definition `ows_reslim_cfg.py`
- custom functions `ows_util_tools.py`

### Categories
There are 6 categories each contain `ows_category_root_cfg.py`, the 6 categories are:

- `baseline_satellite_data`
- `hazards`
- `inland_water`
- `land_and_vegetation`
- `others`
- `sea_ocean_coast`

### layers
Each layer within its category needs to be included in its categories `ows_category_root_cfg.py` file.

### Best practices
#### individual style
each style definition for layers is to be declared following naming convention `style_*`

#### Grouping of styles
Some layers share common style definitions and in the configuration file they should be declared following naming convention `styles_*`

#### bands
each product's bands definition is to be declared following naming convention `bands_*`

#### abstract
if several layers have long abstract move them to `abstract_*_cfg.py` and declared following naming convention `abstract_*`

### Resource Limit
any unique resource limiting configuration should be declared in `ows_reslim_cfg.py` and be declared following naming convention `reslim_*`

### common legend definition
reusable legend definition should be declared in `ows_legend_cfg.py` and be declared following naming convention `legend_*`
