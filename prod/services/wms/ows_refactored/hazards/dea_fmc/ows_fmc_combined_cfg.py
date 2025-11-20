from ows_refactored.ows_reslim_cfg import reslim_for_sentinel2

bands_fmc = {
    "fmc": ["fmc"],
}

FMC_daily = {
    "name": "FMC_daily",
    "title": "DEA FMC Sentinel-2 (A, B & C)",
    "abstract": "Fuel Moisture Content observations grouped by day of collection.",
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

FMC_mosaic = {
    "name": "FMC_mosaic",
    "title": "DEA FMC Sentinel-2 Most Recent Observation",
    "abstract": "displays the most recently processed data for DEA FMC as a continental mosaic",
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

ga_s2_fmc_layer = {
    "title": "DEA FMC Sentinel-2 (A, B & C)",
    "name": "ga_s2_fmc_layer",
    "abstract": """DEA FMC Sentinel-2 (A, B & C)

This product calculates the Fuel Moisture Content (FMC) of vegetation which is the percentage of water mass relative to dry mass in living vegetation.

Values range from 0–300%, representing, by weight percent, the amount of water in leaves compared to dry plant material. A value of 0% would indicate that there is no water content. A value of 100% indicates there is an equal weight of water and dry plant material. A value of 300% would mean there is approximately three times as much water as dry plant material. Values in the range of 0–150% are particularly relevant to fire behaviour analysis, as this range is strongly associated with changes in vegetation flammability and the likelihood of ignition.

This product presents pixel-level FMC values for each corresponding Sentinel-2 (A, B and C) scene since July 2015.

For more information, see https://knowledge.dea.ga.gov.au/data/product/dea-fuel-moisture-content/

For service status information, see https://status.dea.ga.gov.au""",
    "multi_product": False,
    "product_name": "ga_s2_fmc_3_v1",
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
        "default_style": "FMC_daily",
        "styles": [FMC_daily]
    }
}

ga_s2m_fmc_mosaic_layer = {
    "title": "DEA FMC Sentinel-2 Most Recent Observation",
    "name": "ga_s2m_fmc_mosaic",
    "abstract": """DEA FMC Sentinel-2 (A, B & C) Most Recent Observation

This product calculates the Fuel Moisture Content (FMC) of vegetation which is the percentage of water mass relative to dry mass in living vegetation.

Values range from 0–300%, representing, by weight percent, the amount of water in leaves compared to dry plant material. A value of 0% would indicate that there is no water content. A value of 100% indicates there is an equal weight of water and dry plant material. A value of 300% would mean there is approximately three times as much water as dry plant material. Values in the range of 0–150% are particularly relevant to fire behaviour analysis, as this range is strongly associated with changes in vegetation flammability and the likelihood of ignition.

This product is a mosaic of the most recent available data from Sentinel-2 satellites (A, B and C) captured over the Australian continent. You can click on the map to view date of observation information for each pixel.

For more information, see https://knowledge.dea.ga.gov.au/data/product/dea-fuel-moisture-content/

For service status information, see https://status.dea.ga.gov.au""",
    "multi_product": False,
    "product_name": "ga_s2_fmc_3_v1",
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
            "default_time": "latest",
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
        "product": "geodata_coast_100k",
        "ignore_time": True,
        "ignore_info_flags": []
    }],
    "styling": {
        "default_style": "FMC_mosaic",
        "styles": [FMC_mosaic]
    }
}
