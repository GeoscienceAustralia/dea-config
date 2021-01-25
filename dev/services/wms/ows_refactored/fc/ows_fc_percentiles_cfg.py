from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules
from ows_refactored.fc.style_fc_cfg import (
    style_fc_simple,
    style_fc_simple_rgb,
    styles_fc_bare_list,
    styles_fc_gv_list,
    styles_fc_ngv_list,
)

from ows_refactored.ows_legend_cfg import (
    legend_idx_0_100_pixel_fc_25ticks,
    legend_idx_0_100_pixel_fc_bs_25ticks,
    legend_idx_0_100_pixel_fc_ngv_25ticks,
)

bands_fc_percentile = {
    "PV_PC_10": [],
    "PV_PC_50": [],
    "PV_PC_90": [],
    "NPV_PC_10": [],
    "NPV_PC_50": [],
    "NPV_PC_90": [],
    "BS_PC_10": [],
    "BS_PC_50": [],
    "BS_PC_90": [],
}

fcp_g_layers = {
    "title": "Fractional Cover Percentiles - Green Vegetation",
    "abstract": "",
    "layers": [
        {
            "title": "Fractional Cover Percentiles - Green Vegetation 25m 100km tile (Fractional Cover Percentiles - Green Vegetation)",
            "name": "fcp_green_veg",
            "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

This contains the percentage of green vegetation per pixel at the 10th, 50th (median) and 90th percentiles for observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "fc_percentile_albers_annual",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": {
                "band": "land",
                "product": "geodata_coast_100k",
                "ignore_time": True,
                "ignore_info_flags": [],
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["PV_PC_10", "PV_PC_50", "PV_PC_90"],
                "native_resolution": [25, -25],
            },
            "styling": {"default_style": "green_veg_10", "styles": styles_fc_gv_list},
        },
    ],
}

fcp_ngv_layers = {
    "title": "Fractional Cover Percentiles - Non Green Vegetation",
    "abstract": "",
    "layers": [
        {
            "title": "Fractional Cover Percentiles - Non Green Vegetation 25m 100km tile (Fractional Cover Percentiles - Non Green Vegetation)",
            "name": "fcp_non_green_veg",
            "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

This contains the percentage of non-green vegetation per pixel at the 10th, 50th (median) and 90th percentiles for observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "fc_percentile_albers_annual",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": {
                "band": "land",
                "product": "geodata_coast_100k",
                "ignore_time": True,
                "ignore_info_flags": [],
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["PV_PC_10", "PV_PC_50", "PV_PC_90"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "non_green_veg_10",
                "styles": styles_fc_ngv_list,
            },
        }
    ],
}

fcp_bs_layers = {
    "title": "Fractional Cover Percentiles - Bare Soil",
    "abstract": "",
    "layers": [
        {
            "title": "Fractional Cover Percentiles - Bare Soil 25m 100km tile (Fractional Cover Percentiles - Bare Soil)",
            "name": "fcp_bare_ground",
            "abstract": """
	Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover This contains the percentage of bare soil per pixel at the 10th, 50th (median) and 90th percentiles for observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year. Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year. For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "fc_percentile_albers_annual",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": {
                "band": "land",
                "product": "geodata_coast_100k",
                "ignore_time": True,
                "ignore_info_flags": [],
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["BS_PC_10", "BS_PC_50", "BS_PC_90"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "bare_ground_10",
                "styles": styles_fc_bare_list,
            },
        }
    ],
}
fcp_median_layers = {
    "title": "Fractional Cover Percentiles - Median",
    "abstract": "",
    "layers": [
        {
            "title": "Fractional Cover Percentiles - Median 25m 100km tile (Fractional Cover Percentiles - Median)",
            "name": "fcp_rgb",
            "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.

Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program.

This contains a three band combination of the 50th Percentile for green vegetation, non green vegetation and bare soil observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "fc_percentile_albers_annual",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": {
                "band": "land",
                "product": "geodata_coast_100k",
                "ignore_time": True,
                "ignore_info_flags": [],
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["BS_PC_50", "PV_PC_50", "NPV_PC_50"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "fc_rgb",
                "styles": [style_fc_rgb],
            },
        }
    ],
}
fcp_seasonal_layers = {
    "title": "Fractional Cover Percentiles Seasonal",
    "abstract": "",
    "layers": [
        {
            "title": "Fractional Cover Percentiles Seasonal 25m 100km tile (Green Vegetation)",
            "name": "fcp_seasonal_green_veg",
            "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

 FC-PERCENTILE-SEASONAL-SUMMARY, this contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "fc_percentile_albers_seasonal",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": {
                "band": "land",
                "product": "geodata_coast_100k",
                "ignore_time": True,
                "ignore_info_flags": [],
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": [
                    "NPV_PC_10",
                    "NPV_PC_50",
                    "NPV_PC_90",
                ],
                "native_resolution": [25, -25],
            },
            "styling": {"default_style": "green_veg_10", "styles": styles_fc_gv_list},
        },
        {
            "title": "Fractional Cover Percentiles Seasonal 25m 100km tile (Non Green Vegetation)",
            "name": "fcp_seasonal_non_green_veg",
            "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

 FC-PERCENTILE-SEASONAL-SUMMARY, this contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "fc_percentile_albers_seasonal",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": {
                "band": "land",
                "product": "geodata_coast_100k",
                "ignore_time": True,
                "ignore_info_flags": [],
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": [
                    "NPV_PC_10",
                    "NPV_PC_50",
                    "NPV_PC_90",
                ],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "non_green_veg_10",
                "styles": styles_fc_ngv_list,
            },
        },
        {
            "title": "Fractional Cover Percentiles Seasonal 25m 100km tile (Bare Soil)",
            "name": "fcp_seasonal_bare_ground",
            "abstract": """
	Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover FC-PERCENTILE-SEASONAL-SUMMARY, this contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year. For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "fc_percentile_albers_seasonal",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": {
                "band": "land",
                "product": "geodata_coast_100k",
                "ignore_time": True,
                "ignore_info_flags": [],
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["BS_PC_10", "BS_PC_50", "BS_PC_90"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "bare_ground_10",
                "styles": styles_fc_bare_list,
            },
        },
        {
            "title": "Fractional Cover Percentiles Seasonal 25m 100km tile (Median)",
            "name": "fcp_seasonal_rgb",
            "abstract": """
	Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program. FC-PERCENTILE-SEASONAL-SUMMARY, this contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year. For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "fc_percentile_albers_seasonal",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "flags": {
                "band": "land",
                "product": "geodata_coast_100k",
                "ignore_time": True,
                "ignore_info_flags": [],
            },
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["BS_PC_50", "PV_PC_50", "NPV_PC_90"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": [style_fc_simple_rgb],
            },
        },
    ],
}
