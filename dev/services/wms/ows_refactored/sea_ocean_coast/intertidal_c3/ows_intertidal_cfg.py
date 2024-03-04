from ows_refactored.ows_reslim_cfg import reslim_standard
from ows_refactored.sea_ocean_coast.intertidal_c3.style_intertidal_cfg import \
    styles_intertidal_list

bands_intertidal = {
    "elevation": [],
    "elevation_uncertainty": [],
    "exposure": [],
    "extents": [],
    "ta_hat": [],
    "ta_hot": [],
    "ta_lat": [],
    "ta_lot": [],
    "ta_offset_high": [],
    "ta_offset_low": [],
    "ta_spread": [],
}

abstract_intertidal = """Geoscience Australia Sentinel-2 Landsat Intertidal Calendar Year Collection 3"""

dea_intertidal_layer = {
    "title": "DEA Intertidal (Sentinel-2, Landsat)",
    "name": "ga_s2ls_intertidal_cyear_3",
    "abstract": abstract_intertidal,
    "product_name": "ga_s2ls_intertidal_cyear_3",
    "bands": bands_intertidal,
    "time_resolution": "summary",
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [10, -10],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "style_intertidal_elevation",
        "styles": styles_intertidal_list,
    },
}
