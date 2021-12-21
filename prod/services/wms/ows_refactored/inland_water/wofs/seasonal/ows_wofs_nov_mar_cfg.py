from ows_refactored.inland_water.wofs.bands_wo_cfg import bands_wofs_sum
from ows_refactored.ows_legend_cfg import (legend_idx_percentage_by_20,
                                           legend_idx_thirtyplus_4ticks,
                                           legend_idx_twentyplus_3ticks)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

style_seasonal_wofs_wet_3 = {
    "name": "seasonal_wos_wet_3",
    "title": "Wet Count",
    "abstract": "Water Observations seasonal summary showing the count of water observations",
    "needed_bands": ["count_wet"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_wet",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#990000",
            "alpha": 1,
        },
        {"value": 2, "color": "#990000"},
        {"value": 4, "color": "#E38400"},
        {"value": 6, "color": "#E3DF00"},
        {"value": 8, "color": "#00E32D"},
        {"value": 10, "color": "#00E3C8"},
        {"value": 12, "color": "#0097E3"},
        {"value": 14, "color": "#005FE3"},
        {"value": 16, "color": "#000FE3"},
        {"value": 18, "color": "#000EA9"},
        {
            "value": 20,
            "color": "#5700E3",
        },
    ],
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "values": [0],
        }
    ],
    "legend": legend_idx_twentyplus_3ticks,
}

style_seasonal_wofs_clear_3 = {
    "name": "seasonal_wos_clear_3",
    "title": "Clear Count",
    "abstract": "Water Observations seasonal summary showing the count of clear observations",
    "needed_bands": ["count_clear"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_clear",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#FFFFFF", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#B21800",
            "alpha": 1,
        },
        {"value": 1, "color": "#B21800"},
        {"value": 4, "color": "#ef8500"},
        {"value": 8, "color": "#ffb800"},
        {"value": 10, "color": "#ffd000"},
        {"value": 13, "color": "#fff300"},
        {"value": 16, "color": "#fff300"},
        {"value": 20, "color": "#c1ec00"},
        {"value": 24, "color": "#6ee100"},
        {"value": 28, "color": "#39a500"},
        {
            "value": 30,
            "color": "#026900",
        },
    ],
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "values": [0],
        }
    ],
    "legend": legend_idx_thirtyplus_4ticks,
}

style_seasonal_wofs_summary_frequency_3 = {
    "name": "seasonal_wos_frequency_3",
    "title": " Water Summary",
    "abstract": "Water Observations seasonal summary showing the frequency of Wetness",
    "needed_bands": ["frequency"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 0.02, "color": "#000000", "alpha": 0.0},
        {"value": 0.05, "color": "#8e0101", "alpha": 0.25},
        {"value": 0.1, "color": "#cf2200", "alpha": 0.75},
        {"value": 0.2, "color": "#e38400"},
        {"value": 0.3, "color": "#e3df00"},
        {"value": 0.4, "color": "#62e300"},
        {"value": 0.5, "color": "#00e32d"},
        {"value": 0.6, "color": "#00e3c8"},
        {"value": 0.7, "color": "#0097e3"},
        {"value": 0.8, "color": "#005fe3"},
        {"value": 0.9, "color": "#000fe3"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "values": [0],
        }
    ],
    "legend": legend_idx_percentage_by_20,
}

style_seasonal_wofs_summary_frequency_cvf_3 = {
    "name": "seasonal_wos_frequency_cvf_3",
    "title": "Water Summary (colour vision friendly)",
    "abstract": "Water Observations seasonal summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "needed_bands": ["frequency"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0.0, "color": "#FFFFFF", "alpha": 0.0},
        {"value": 0.02, "color": "#FFFFFF", "alpha": 0.0},
        {"value": 0.05, "color": '#aee3c0', "alpha": 0.25},
        {"value": 0.1, "color": '#6dd3ad', "alpha": 0.75},
        {"value": 0.2, "color": '#44bcad'},
        {"value": 0.3, "color": '#35a1ab'},
        {"value": 0.4, "color": '#3487a6'},
        {"value": 0.5, "color": '#366da0'},
        {"value": 0.6, "color": '#3d5296'},
        {"value": 0.7, "color": '#403974'},
        {"value": 0.8, "color": '#35264c'},
        {"value": 0.9, "color": '#231526'},
    ],
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "values": [0],
        }
    ],
    "legend": legend_idx_percentage_by_20,
}

style_seasonal_wofs_summary_frequency_blue_3 = {
    "name": "seasonal_wos_frequency_blue_3",
    "title": "Water Summary (blue)",
    "abstract": "Water Observations seasonal summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "needed_bands": ["frequency"],
    "color_ramp": [
        {
            "value": 0.0,
            "color": "#ffffff",
            "alpha": 0.0,
        },
        {
            "value": 0.001,
            "color": "#d5fef9",
            "alpha": 0.0,
        },
        {
            "value": 0.02,
            "color": "#d5fef9",
        },
        {"value": 0.2, "color": "#71e3ff"},
        {"value": 0.4, "color": "#01ccff"},
        {"value": 0.6, "color": "#0178ff"},
        {"value": 0.8, "color": "#2701ff"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "values": [0],
        }
    ],
    "legend": legend_idx_percentage_by_20,
}

c3_statistics_layer = {
    "title": "DEA Water Observations November to March (Landsat)",
    "name": "ga_ls_wo_fq_nov_mar_3",
    "abstract": """DEA Water Observations Statistics 30m 3.1.6 (Landsat, November - March, Frequency)
The DEA Water Observations November - March Statistic is a set of seasonal statistical summaries of the DEA Water Observations product that combines the many years of observations into summary products that help the understanding of surface water across Australia. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains:
1) Water summary- what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage).
No clear observations of water causes an area to appear transparent,
red through to yellow represent areas seen to be wet up to 30% of the time,
green through to light blue represent areas seen to be wet 40-60% of the time,
deep blue and purple correspond to an area being wet through 80%-100% of clear observations.

2) Wet observation count- how many times water was detected in observations that were clear.
No clear observations of water causes an area to appear transparent,
1-6 total clear observations of water correlate with red and yellow colours,
7-12 clear observations of water correlate with green through to light blue,
12+ clear observations of water correlates with increasingly dark shades of blue.

3) Clear observation count- how many times an area could be clearly seen (i.e. not affected by clouds, shadows or other satellite observation problems).
No clear observations causes an area to appear transparent,
1-15 total clear observations correlates with red and yellow colours,
18-22 clear observations correlates with light green,
23+ clear observations correlates with inreasingly dark shades of green.


https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_wo_fq_nov_mar_3",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "time_resolution": "year",
    "flags": [
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": [],
        },
    ],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "seasonal_wos_frequency_3",
        "styles": [
            style_seasonal_wofs_summary_frequency_3,
            style_seasonal_wofs_summary_frequency_cvf_3,
            style_seasonal_wofs_summary_frequency_blue_3,
            style_seasonal_wofs_wet_3,
            style_seasonal_wofs_clear_3,
        ],
    },
}