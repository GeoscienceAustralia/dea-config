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

ga_s2_fmc_layer = {
    "title": "DEA Fuel Moisture Content (Sentinel-2A, 2B & 2C)",
    "name": "ga_s2_fmc_layer",
    "abstract": """DEA Fuel Moisture Content (Sentinel-2A, 2B & 2C)

This product is a remotely sensed proxy for FUel Mosture Content (FMC). Fuel moisture content (FMC) is a metric used to understand flammability and fire risk. It describes the water contained within the leaf material of plants and it changes seasonally and with climate variations. FMC is traditionally determined by collecting plant sample in the field and analysing them in a laboratory. DEA FMC is  based on satellite imagery. It provides consistent, continent wide information on fuel condition that can be used in combination with other information to understanding vegetation flammability and fire potential. 

DEA FMC is presented as a weight percentage. This meas the value given represent the weight of water in leaf material relative to non-water mateial. Values range from 0 – 300, where 300 would mean there is three times as much water (by weight) than dry plant material.

This product presents the calculated FMC values for each individual Sentinel-2 (A, B and C) satellite image on each individual day since 2015.

For service status information, see https://status.dea.ga.gov.au""",
    "multi_product": False,
    "product_names": "ga_s2_fmc_3",
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
    "title": "DEA Fuel Moisture Content Most Recent Available Data Mosaic (Sentinel 2 a, b & c)",
    "name": "ga_s2m_fmc_mosaic",
    "abstract": """DEA Fuel Moisture Content (Sentinel-2A, 2B & 2C) Most Recent Mosaic

This product is a remotely sensed proxy for FUel Mosture Content (FMC). Fuel moisture content (FMC) is a metric used to understand flammability and fire risk. It describes the water contained within the leaf material of plants and it changes seasonally and with climate variations. FMC is traditionally determined by collecting plant sample in the field and analysing them in a laboratory. DEA FMC is  based on satellite imagery. It provides consistent, continent wide information on fuel condition that can be used in combination with other information to understanding vegetation flammability and fire potential. 

DEA FMC is presented as a weight percentage. This meas the value given represent the weight of water in leaf material relative to non-water mateial. Values range from 0 – 300, where 300 would mean there is three times as much water (by weight) than dry plant material.

This layer displays the most recently processed FMC observation from the Sentinel 2 satelites for every part of Australia.""",
    "multi_product": False,
    "product_names": "ga_s2_fmc_3",
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
