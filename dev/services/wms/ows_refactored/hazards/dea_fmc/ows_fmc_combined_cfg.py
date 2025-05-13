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
    "color_ramp": [{"value": 0, "color": "#DD0000"},
                   {"value": 150, "color": "#FFFFBA"},
                   {"value": 300, "color": "#2A9DF4"}],
    "pq_masks": [{"band": "land",
                  "invert": True,
                  "values": [0]}
                ]
    "legend": {
        "title": "Fuel Moisture Content (Weight Percent)",
        "begin": "0",
        "end": "300",
        "ticks": ["0", "50", "100", "150", "200", "250", "300"],
        "tick_labels": {
            "default": {
                "suffix": "%"}}}
}


ga_s2_fmc_layer = {
    "title": "DEA Fuel Moisture Content (Sentinel 2 a & b)",
    "name": "ga_s2_fmc_layer",
    "abstract": """DEA Fuel Moisture Content (Sentinel 2 a & b)
    this layer combines data from both Sentinel 2 a and Sentinel 2 b """,
    "multi_product": True,
    "product_names": ["ga_s2am_fmc", "ga_s2bm_fmc"],
    "bands": bands_fmc,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": True
    },
    "flags": [{
        "band": "land",
        "products": "geodata_coast_100k",
        "ignore_time": True,
        "ignore_info_flags": []
    }],
    "styling": {
        "default_style": "style_fmc",
        "styles": [style_fmc]
    }
}

ga_s2m_fmc_mosaic_layer = {
    "title": "DEA Fuel Moisture Content Most Recent Available Data Mosaic (Sentinel 2 a & b)",
    "name": "ga_s2m_fmc_mosaic",
    "abstract": """DEA Fuel Moisture Content (Sentinel 2 a & b)
    This product produces a mosaic of the most recent available data from both Sentinel-2 satelites captured over the Australian continent""",
    "multi_product": True,
    "product_names": [
        "ga_s2am_fmc",
        "ga_s2bm_fmc"
    ],
    "mosaic_date_func": {
        # 6 day rolling window.  5 days should give full continental coverage
        # of Sentinel-2, plus an extra day to allow for patchy coverage on
        # most recent day.
        # Note that the window is calculated from the most-recent available
        # day, not the the calendar's idea of what "today" might be.
        "function": "datacube_ows.ogc_utils.rolling_window_ndays",
        "pass_layer_cfg": True,
        "kwargs": {
            "ndays": 6,
        }
    },
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
        "products": "geodata_coast_100k",
        "ignore_time": True,
        "ignore_info_flags": []
    }],
    "styling": {
        "default_style": "style_fmc",
        "styles": [style_fmc]
    }
}
