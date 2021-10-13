from ows_refactored.land_and_vegetation.fc.band_fc_cfg import \
    bands_fc_percentile
from ows_refactored.land_and_vegetation.fc.flag_fc_cfg import \
    fc_percentile_flags
from ows_refactored.land_and_vegetation.fc.style_fc_cfg import (
    style_fc_simple_rgb, styles_fc_bare_list, styles_fc_gv_list,
    styles_fc_ngv_list)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

fcp_seasonal_layers = {
    "title": "Seasonal Fractional Cover Summaries",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Fractional Cover Percentiles (Landsat, Seasonal, Green Vegetation)",
            "name": "fcp_seasonal_green_veg",
            "abstract": """Fractional Cover 25m Percentiles 2.2.1 (Landsat, Seasonal, Green Vegetation)
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

 This contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.
https://cmi.ga.gov.au/data-products/dea/120/dea-fractional-cover-percentiles-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "fc_percentile_albers_seasonal",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": fc_percentile_flags,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {"default_style": "green_veg_10", "styles": styles_fc_gv_list},
        },
        {
            "title": "DEA Fractional Cover Percentiles (Landsat, Seasonal, Non-Green Vegetation)",
            "name": "fcp_seasonal_non_green_veg",
            "abstract": """Fractional Cover 25m Percentiles 2.2.1 (Landsat, Seasonal, Non-Green Vegetation)
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

 This contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.
https://cmi.ga.gov.au/data-products/dea/120/dea-fractional-cover-percentiles-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "fc_percentile_albers_seasonal",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": fc_percentile_flags,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "non_green_veg_10",
                "styles": styles_fc_ngv_list,
            },
        },
        {
            "title": "DEA Fractional Cover Percentiles (Landsat, Seasonal, Bare Ground)",
            "name": "fcp_seasonal_bare_ground",
            "abstract": """Fractional Cover 25m Percentiles 2.2.1 (Landsat, Seasonal, Bare Ground)
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover FC-PERCENTILE-SEASONAL-SUMMARY, this contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.
https://cmi.ga.gov.au/data-products/dea/120/dea-fractional-cover-percentiles-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "fc_percentile_albers_seasonal",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": fc_percentile_flags,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "bare_ground_10",
                "styles": styles_fc_bare_list,
            },
        },
    ],
}

fcp_seasonal_rgb_layer = {
    "title": "DEA Fractional Cover Percentiles (Landsat, Seasonal)",
    "name": "fcp_seasonal_rgb",
    "abstract": """Fractional Cover 25m Percentiles 2.2.1 (Landsat, Seasonal)
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program. FC-PERCENTILE-SEASONAL-SUMMARY, this contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.
https://cmi.ga.gov.au/data-products/dea/120/dea-fractional-cover-percentiles-landsat
For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "fc_percentile_albers_seasonal",
    "bands": bands_fc_percentile,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "flags": fc_percentile_flags,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "simple_rgb",
        "styles": [style_fc_simple_rgb],
    },
}
