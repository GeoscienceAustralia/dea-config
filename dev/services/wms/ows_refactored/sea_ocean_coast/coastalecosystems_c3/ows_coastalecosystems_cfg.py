from ows_refactored.ows_reslim_cfg import reslim_wms_unlimited
from ows_refactored.sea_ocean_coast.coastalecosystems_c3.style_coastalecosystems_cfg import \
    styles_coastalecosystems_list

bands_coastalecosystems = {
    "classification": [],
    "mangrove_prob": [],
    "saltmarsh_prob": [],
    "seagrass_prob": [],
    "saltflat_prob": [],
    "qa_count_clear": [],
}

abstract_coastalecosystems = """Geoscience Australia Sentinel-2 Coastal Ecosystems Calendar Year Collection 3

The Digital Earth Australia Coastal Ecosystems product suite includes a categorical classification of four coastal ecosystems, supported by probability layers for individual ecosystems and selected quality assurance layers to support product interpretation, for the years 2021 and 2022 and 10 m spatial resolution.

Product documentation: https://knowledge.dea.ga.gov.au/data/product/dea-coastalecosystems/

Service status information: https://status.dea.ga.gov.au"""

dea_coastalecosystems_layer = {
    "title": "DEA Coastal Ecosystems (Sentinel-2)",
    "name": "ga_s2_coastalecosystems_cyear_3_v1",
    "abstract": abstract_coastalecosystems,
    "product_name": "ga_s2_coastalecosystems_cyear_3_v1",
    "bands": bands_coastalecosystems,
    "time_resolution": "summary",
    "resource_limits": reslim_wms_unlimited,
    "native_crs": "EPSG:3577",
    "native_resolution": [10, -10],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "coastalecosystems_classification",
        "styles": styles_coastalecosystems_list,
    },
}
