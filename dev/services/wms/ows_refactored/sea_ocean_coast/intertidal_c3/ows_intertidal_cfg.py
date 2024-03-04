from ows_refactored.sea_ocean_coast.intertidal_c3.landsat_annual.style_intertidal_cfg import style_intertidal_elevation
from ows_refactored.ows_reslim_cfg import reslim_standard

bands_intertidal = {"elevation": []}

layer = {
    "title": "DEA Intertidal (Sentinel-2, Landsat)",
    "name": "ga_s2ls_intertidal_cyear_3",
    "abstract": """Testing""",
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
        "styles": [
            style_intertidal_elevation,
        ],
    },
}
