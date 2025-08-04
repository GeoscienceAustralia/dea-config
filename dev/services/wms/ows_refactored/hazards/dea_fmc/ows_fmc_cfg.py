from ows_refactored.ows_reslim_cfg import reslim_for_sentinel2

bands_fmc = {
    "fmc": ["fmc"],
}

style_fmc = {
    "name": "style_fmc",
    "title": "Fuel Moisture Content",
    "abstract": "the percentage of water in vegetation by weight",
    "needed_bands": ["fmc"],

    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "kwargs": {"band": "fmc"}},
    "color_ramp": [{"value": 0, "color": "#ca0020"},
                   {"value": 75, "color": "#FFFFBA"},
                   {"value": 150, "color": "#0571b0"}],
    "pq_masks": [{"band": "land",
                  "invert": True,
                  "values": [0]}],
    "legend": {
        "title": "Fuel Moisture Content (Weight Percent)",
        "begin": "0",
        "end": "150",
        "ticks": ["0", "50", "100", "150"],
        "tick_labels": {
            "default": {
                "suffix": "%"}}}
}

style_fmc_old = {
    "name": "style_fmc_old",
    "title": "FMC - old style",
    "abstract": "the percentage of water in vegetation by weight",
    "needed_bands": ["fmc"],

    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "kwargs": {"band": "fmc"}},
    "color_ramp": [{"value": 0, "color": "#DD0000"},
                   {"value": 75, "color": "#FFFFBA"},
                   {"value": 150, "color": "#2A9DF4"}],
    "pq_masks": [{"band": "land",
                  "invert": True,
                  "values": [0]}],
    "legend": {
        "title": "Fuel Moisture Content (Weight Percent)",
        "begin": "0",
        "end": "150",
        "ticks": ["0", "50", "100", "150"],
        "tick_labels": {
            "default": {
                "suffix": "%"}}}
}


s2a_layer = {
    "title": "DEA Fuel Moisture Content (Sentinel 2a)",
    "name": "ga_s2am_fmc",
    "abstract": """DEA Fuel Moisture Content (Sentinel 2a)""",
    "product_name": "ga_s2am_fmc",
    "bands": bands_fmc,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False
    },
    "flags": [{
        "band": "land",
        "product": "geodata_coast_100k",
        "ignore_time": True,
        "ignore_info_flags": []
    }],
    "styling": {
        "default_style": "style_fmc",
        "styles": [style_fmc, style_fmc_old]
    }
    "feature_info": {
        "include_custom": {
            "description": {
                "function": "ows_refactored.hazards.dea_fmc.fmc_feat_desc.class_labels",
            }
        }
}
}

s2b_layer = {
    "title": "DEA Fuel Moisture Content (Sentinel 2b)",
    "name": "ga_s2bm_fmc",
    "abstract": """DEA Fuel Moisture Content (Sentinel 2b)""",
    "product_name": "ga_s2bm_fmc",
    "bands": bands_fmc,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False
    },
    "flags": [{
        "band": "land",
        "product": "geodata_coast_100k",
        "ignore_time": True,
        "ignore_info_flags": []
    }],
    "styling": {
        "default_style": "style_fmc",
        "styles": [style_fmc, style_fmc_old]
    }
}

s2c_layer = {
    "title": "DEA Fuel Moisture Content (Sentinel 2c)",
    "name": "ga_s2cm_fmc",
    "abstract": """DEA Fuel Moisture Content (Sentinel 2c)""",
    "product_name": "ga_s2cm_fmc",
    "bands": bands_fmc,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False
    },
    "flags": [{
        "band": "land",
        "product": "geodata_coast_100k",
        "ignore_time": True,
        "ignore_info_flags": []
    }],
    "styling": {
        "default_style": "style_fmc",
        "styles": [style_fmc, style_fmc_old]
    }
}
