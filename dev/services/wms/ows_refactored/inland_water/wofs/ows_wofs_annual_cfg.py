from ows_refactored.inland_water.wofs.bands_wo_cfg import bands_wofs_sum
from ows_refactored.ows_legend_cfg import (legend_idx_percentage_by_20,
                                           legend_idx_thirtyplus_4ticks,
                                           legend_idx_twentyplus_3ticks)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

style_annual_wofs_summary_frequency = {
    "name": "annual_WOfS_frequency",
    "title": "Water Summary",
    "abstract": "WOfS annual summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["frequency"],
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
    "legend": legend_idx_percentage_by_20,
}


style_annual_wofs_summary_frequency_blue = {
    "name": "annual_WOfS_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS annual summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "include_in_feature_info": False,
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
    "legend": legend_idx_percentage_by_20,
}


style_wofs_summary_wet = {
    "name": "annual_water_observations",
    "title": "Wet Count",
    "abstract": "WOfS annual summary showing the count of water observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_wet",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["count_wet"],
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
    "legend": legend_idx_twentyplus_3ticks,
}

style_wofs_summary_clear = {
    "name": "annual_clear_observations",
    "title": "Clear Count",
    "abstract": "WOfS annual summary showing the count of clear observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_clear",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["count_clear"],
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
    "legend": legend_idx_thirtyplus_4ticks,
}


layers = {
    "title": "Annual water observations source data",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "DEA Annual Wet Observations Statistics (Landsat)",
            "name": "wofs_annual_summary_wet",
            "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, Annual, Wet)
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.
For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf
https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_annual_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "annual_water_observations",
                "styles": [
                    style_wofs_summary_wet,
                ],
            },
        },
        {
            "title": "DEA Annual Clear Observations Statistics (Landsat)",
            "name": "wofs_annual_summary_clear",
            "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, Annual, Clear)
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary. This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green. For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf
https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_annual_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "annual_clear_observations",
                "styles": [
                    style_wofs_summary_clear,
                ],
            },
        },
    ],
}


statistics_layer = {
    "title": "DEA Annual Water Observations Frequency Statistics (Landsat)",
    "name": "wofs_annual_summary_statistics",
    "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, Annual, Frequency)
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.
For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf

https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "wofs_annual_summary",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "annual_WOfS_frequency",
        "styles": [
            style_annual_wofs_summary_frequency,
            style_annual_wofs_summary_frequency_blue,
        ],
    },
}

c3_statistics_layer = {
    "title": "DEA Annual Water Observations Frequency Statistics (Landsat, C3)",
    "name": "ga_ls_wo_fq_cyear_3",
    "abstract": """
DEA Annual Water Observation Statistics 30m 3.1.6 (Landsat, Annual, Frequency) is a set of annual statistical summaries of the DEA Water Observation product which help the understanding of surface water dynamics over the years. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage).

No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_wo_fq_cyear_3",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "annual_WOfS_frequency",
        "styles": [
            style_annual_wofs_summary_frequency,
            style_annual_wofs_summary_frequency_blue,
        ],
    },
}

c3_layers = {
    "title": "DEA Annual Water Observations source data (C3)",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "DEA Annual Wet Observations Statistics (Landsat, C3)",
            "name": "wofs_annual_summary_wet_c3",
            "abstract": """DEA Annual Water Observation Statistics 30m 3.1.6 (Landsat, Annual, Wet) is a set of annual statistical summaries of the DEA Water Observation product which help the understanding of surface water dynamics over the years. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains wet observation count: how many times water was detected in observations that were clear.

No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ga_ls_wo_fq_cyear_3",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "annual_water_observations",
                "styles": [
                    style_wofs_summary_wet,
                ],
            },
        },
        {
            "title": "DEA Annual Clear Observations Statistics (Landsat, C3)",
            "name": "wofs_annual_summary_clear_c3",
            "abstract": """DEA Annual Water Observation Statistics 30m 3.1.6 (Landsat, Annual, Clear) is a set of annual statistical summaries of the DEA Water Observation product which help the understanding of surface water dynamics over the years. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains wet observation count: how many times water was detected in observations that were clear.

No clear observations causes an area to appear transparent,
1-15 total clear observations correlates with red and yellow colours,
18-22 clear observations correlates with light green,
23+ clear observations correlates with inreasingly dark shades of green.

https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ga_ls_wo_fq_cyear_3",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "annual_clear_observations",
                "styles": [
                    style_wofs_summary_clear,
                ],
            },
        },
    ],
}
