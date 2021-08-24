from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules
from ows_refactored.sentinel2.band_s2_cfg import bands_sentinel2_provisional
from ows_refactored.sentinel2.style_s2_cfg import styles_s2_provisional_list

multi_layers = {
    "name": "s2_nrt_provisional_granule_nbar_t",
    "title": "Near Real-Time (Provisional) Surface Reflectance (Sentinel 2 (A and B combined))",
    "abstract": """
This is a provisional version of 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For service status information, see https://status.dea.ga.gov.au
""",
    "multi_product": True,
    "product_names": ["ga_s2am_ard_provisional_3", "ga_s2bm_ard_provisional_3"],
    "bands": bands_sentinel2_provisional,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "oa_fmask",
            "products": ["ga_s2am_ard_provisional_3", "ga_s2bm_ard_provisional_3"],
            "ignore_time": False,
            "ignore_info_flags": [],
        },
        {
            "band": "land",
            "products": ["geodata_coast_100k", "geodata_coast_100k"],
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "wcs": {
        "default_bands": [
            "nbart_red",
            "nbart_green",
            "nbart_blue",
        ],
    },
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_provisional_list},
}

s2b_layer = {
    "name": "s2b_nrt_provisional_granule_nbar_t",
    "title": "Near Real-Time (Provisional) Surface Reflectance (Sentinel 2B)",
    "abstract": """
This is a provisional version of 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_s2bm_ard_provisional_3",
    "bands": bands_sentinel2_provisional,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "oa_fmask",
            "product": "ga_s2bm_ard_provisional_3",
            "ignore_time": False,
            "ignore_info_flags": []
        },
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "wcs": {
        "default_bands": [
            "nbart_red",
            "nbart_green",
            "nbart_blue",
        ],
    },
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_provisional_list},
}

s2a_layer = {
    "name": "s2a_nrt_provisional_granule_nbar_t",
    "title": "Near Real-Time (Provisional) Surface Reflectance (Sentinel 2A)",
    "abstract": """
This is a provisional version of 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_s2am_ard_provisional_3",
    "bands": bands_sentinel2_provisional,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "oa_fmask",
            "product": "ga_s2am_ard_provisional_3",
            "ignore_time": False,
            "ignore_info_flags": []
        },
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "wcs": {
        "default_bands": [
            "nbart_red",
            "nbart_green",
            "nbart_blue",
        ],
    },
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_provisional_list},
}
