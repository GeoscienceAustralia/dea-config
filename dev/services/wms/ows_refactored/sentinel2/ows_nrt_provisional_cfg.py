from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules
from ows_refactored.sentinel2.style_s2_cfg import styles_s2_provisional_list

bands_sentinel2 = {
    "nbar_coastal_aerosol": ["nbar_coastal_aerosol", "nbar_narrow_blue"],
    "nbar_blue": ["nbar_blue"],
    "nbar_green": ["nbar_green"],
    "nbar_red": ["nbar_red"],
    "nbar_red_edge_1": ["nbar_red_edge_1"],
    "nbar_red_edge_2": ["nbar_red_edge_2"],
    "nbar_red_edge_3": ["nbar_red_edge_3"],
    "nbar_nir_1": ["nbar_nir_1", "nbar_near_infrared_1"],
    "nbar_nir_2": ["nbar_nir_2", "nbar_near_infrared_2"],
    "nbar_swir_2": ["nbar_swir_2", "nbar_shortwave_infrared_2"],
    "nbar_swir_3": ["nbar_swir_3", "nbar_shortwave_infrared_3"],
    "nbart_coastal_aerosol": [
        "nbart_coastal_aerosol",
        "coastal_aerosol",
        "nbart_narrow_blue",
        "narrow_blue",
    ],
    "nbart_blue": ["nbart_blue", "blue"],
    "nbart_green": ["nbart_green", "green"],
    "nbart_red": ["nbart_red", "red"],
    "nbart_red_edge_1": ["nbart_red_edge_1", "red_edge_1"],
    "nbart_red_edge_2": ["nbart_red_edge_2", "red_edge_2"],
    "nbart_red_edge_3": ["nbart_red_edge_3", "red_edge_3"],
    "nbart_nir_1": ["nbart_nir_1", "nir", "nir_1", "nbart_near_infrared_1"],
    "nbart_nir_2": ["nbart_nir_2", "nir_2", "nbart_near_infrared_2"],
    "nbart_swir_2": ["nbart_swir_2", "swir_2", "nbart_shortwave_infrared_2"],
    "nbart_swir_3": ["nbart_swir_3", "swir_3", "nbart_shortwave_infrared_3"],
    "oa_fmask": ["oa_fmask"],
}

multi_layers = {
    "name": "s2_nrt_provisional_granule_nbar_t",
    "title": "Near Real-Time (Provisional) Surface Reflectance (Sentinel 2 (A and B combined))",
    "abstract": """
This is a provisional version of 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For service status information, see https://status.dea.ga.gov.au
""",
    "multi_product": True,
    "product_names": ["ga_s2am_ard_provisional_3", "ga_s2bm_ard_provisional_3"],
    "bands": bands_sentinel2,
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
    "bands": bands_sentinel2,
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
    "bands": bands_sentinel2,
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
