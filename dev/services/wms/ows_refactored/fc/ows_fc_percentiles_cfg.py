from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15
from ows_refactored.fc.style_fc_cfg import style_fc_simple, style_fc_simple_rgb

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

style_fc_gv_10 = {
    "name": "green_veg_10",
    "title": "10th Percentile",
    "abstract": "10th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "PV_PC_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["PV_PC_10"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffcc",
        },
        {
            "value": 25,
            "color": "#c2e699",
        },
        {
            "value": 50,
            "color": "#78c679",
        },
        {
            "value": 75,
            "color": "#31a354",
        },
        {
            "value": 100,
            "color": "#006837",
        },
    ],
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
    "legend": legend_idx_0_100_pixel_fc_25ticks,
}

style_fc_gv_50 = {
    "name": "green_veg_50",
    "title": "50th Percentile",
    "abstract": "50th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "PV_PC_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["PV_PC_50"],
    "color_ramp": [
        {"value": 0, "color": "#ffffcc"},
        {"value": 25, "color": "#c2e699"},
        {"value": 50, "color": "#78c679"},
        {"value": 75, "color": "#31a354"},
        {"value": 100, "color": "#006837"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_25ticks,
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
}

style_fc_gv_90 = {
    "name": "green_veg_90",
    "title": "90th Percentile",
    "abstract": "90th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "PV_PC_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["PV_PC_90"],
    "color_ramp": [
        {"value": 0, "color": "#ffffcc"},
        {"value": 25, "color": "#c2e699"},
        {"value": 50, "color": "#78c679"},
        {"value": 75, "color": "#31a354"},
        {"value": 100, "color": "#006837"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_25ticks,
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
}

style_fc_ngv_10 = {
    "name": "non_green_veg_10",
    "title": "10th Percentile",
    "abstract": "10th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "NPV_PC_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["NPV_PC_10"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffd4",
        },
        {"value": 25, "color": "#fed98e", "legend": {}},
        {
            "value": 50,
            "color": "#fe9929",
        },
        {
            "value": 75,
            "color": "#d95f0e",
        },
        {
            "value": 100,
            "color": "#993404",
        },
    ],
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
}

style_fc_ngv_50 = {
    "name": "non_green_veg_50",
    "title": "50th Percentile",
    "abstract": "50th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "NPV_PC_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["NPV_PC_50"],
    "color_ramp": [
        {"value": 0, "color": "#ffffd4"},
        {"value": 25, "color": "#fed98e"},
        {"value": 50, "color": "#fe9929"},
        {"value": 75, "color": "#d95f0e"},
        {"value": 100, "color": "#993404"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
}

style_fc_ngv_90 = {
    "name": "non_green_veg_90",
    "title": "90th Percentile",
    "abstract": "90th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "NPV_PC_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["NPV_PC_90"],
    "color_ramp": [
        {"value": 0, "color": "#ffffd4"},
        {"value": 25, "color": "#fed98e"},
        {"value": 50, "color": "#fe9929"},
        {"value": 75, "color": "#d95f0e"},
        {"value": 100, "color": "#993404"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
}

style_fc_bs_10 = {
    "name": "bare_ground_10",
    "title": "10th Percentile",
    "abstract": "10th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "BS_PC_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["BS_PC_10"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#feebe2",
        },
        {
            "value": 25,
            "color": "#fbb4b9",
        },
        {
            "value": 50,
            "color": "#f768a1",
        },
        {
            "value": 75,
            "color": "#c51b8a",
        },
        {
            "value": 100,
            "color": "#7a0177",
        },
    ],
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
}

style_fc_bs_50 = {
    "name": "bare_ground_50",
    "title": "50th Percentile",
    "abstract": "50th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "BS_PC_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["BS_PC_50"],
    "color_ramp": [
        {"value": 0, "color": "#feebe2"},
        {"value": 25, "color": "#fbb4b9"},
        {"value": 50, "color": "#f768a1"},
        {"value": 75, "color": "#c51b8a"},
        {"value": 100, "color": "#7a0177"},
    ],
    # Old behaviour was wrong - this is what Leo and Emma have requested.
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
}

style_fc_bs_90 = {
    "name": "bare_ground_90",
    "title": "90th Percentile",
    "abstract": "90th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "BS_PC_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["BS_PC_90"],
    "color_ramp": [
        {"value": 0, "color": "#feebe2"},
        {"value": 25, "color": "#fbb4b9"},
        {"value": 50, "color": "#f768a1"},
        {"value": 75, "color": "#c51b8a"},
        {"value": 100, "color": "#7a0177"},
    ],
    # Old behaviour was wrong - this is what Leo and Emma have requested.
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
}

style_fc_rgb = {
    "name": "fc_rgb",
    "title": "Three-band fractional cover",
    "abstract": "Fractional cover medians - red is bare soil, green is green vegetation and blue is non-green vegetation",
    "components": {
        "red": {"BS_PC_50": 1.0},
        "green": {"PV_PC_50": 1.0},
        "blue": {"NPV_PC_50": 1.0},
    },
    "scale_range": [0.0, 100.0],
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
    "legend": {
        "show_legend": True,
        "url": "https://data.dea.ga.gov.au/fractional-cover/FC_legend.png",
    },
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
            "resource_limits": reslim_wms_min_zoom_15,
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
                "default_style": "green_veg_10",
                "styles": [
                    style_fc_gv_10,
                    style_fc_gv_50,
                    style_fc_gv_90,
                ],
            },
        },
    ],
}

fcp_ngv_layers ={
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
                "resource_limits": reslim_wms_min_zoom_15,
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
                    "styles": [
                        style_fc_ngv_10,
                        style_fc_ngv_50,
                        style_fc_ngv_90,
                    ],
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
            "resource_limits": reslim_wms_min_zoom_15,
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
                "styles": [
                    style_fc_bs_10,
                    style_fc_bs_50,
                    style_fc_bs_90,
                ],
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
            "resource_limits": reslim_wms_min_zoom_15,
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
            "resource_limits": reslim_wms_min_zoom_15,
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
                "default_style": "green_veg_10",
                "styles": [
                    style_fc_gv_10,
                    style_fc_gv_50,
                    style_fc_gv_90,
                ],
            },
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
            "resource_limits": reslim_wms_min_zoom_15,
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
                "styles": [
                    style_fc_ngv_10,
                    style_fc_ngv_50,
                    style_fc_ngv_90,
                ],
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
            "resource_limits": reslim_wms_min_zoom_15,
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
                "styles": [
                    style_fc_bs_10,
                    style_fc_bs_50,
                    style_fc_bs_90,
                ],
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
            "resource_limits": reslim_wms_min_zoom_15,
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
