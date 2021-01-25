from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules
from ows_refactored.wofs.bands_wo_cfg import bands_wofs_obs

style_s2_water_classifier = {
    "name": "water_classifier",
    "title": " Water Summary",
    "abstract": "WOfS NRT",
    "needed_bands": ["water"],
    "value_map": {
        "water": [
            {"title": "Wet", "abstract": "(100%)", "color": "#5700E3"},
        ]
    },
}

layers = {
    "name": "s2_nrt_wofs",
    "title": "	Near Real-Time Water Classifier (Sentinel 2 WOfS NRT)",
    "abstract": """	Sentinel 2 NRT Water Classifier. For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "sentinel2_wofs_nrt",
    "bands": bands_wofs_obs,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "wcs": {
        "native_crs": "EPSG:3577",
        "native_resolution": [10.0, 10.0],
        "default_bands": ["water"],
    },
    "styling": {
        "default_style": "water_classifier",
        "styles": [style_s2_water_classifier],
    },
}
