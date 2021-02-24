from ows_refactored.ows_reslim_cfg import (
    reslim_wms_min_zoom_15_cache_rules,
    reslim_wms_min_zoom_35,
)
from ows_refactored.ows_legend_cfg import (
    legend_idx_percentage_by_20,
    legend_idx_percentage_by_25,
    legend_idx_twentyplus_3ticks,
    legend_idx_thirtyplus_4ticks,
)
from ows_refactored.wofs.bands_wo_cfg import (
    bands_wofs_filt_sum,
    bands_wofs_sum,
    bands_wofs_obs,
)

style_wofs_seasonal_wet = {
    "name": "seasonal_water_observations",
    "title": "Wet Count",
    "abstract": "WOfS seasonal summary showing the count of water observations",
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
    "legend": legend_idx_twentyplus_3ticks,
}

style_wofs_seasonal_clear = {
    "name": "seasonal_clear_observations",
    "title": "Clear Count",
    "abstract": "WOfS seasonal summary showing the count of clear observations",
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
    "legend": legend_idx_thirtyplus_4ticks,
}

style_seasonal_wofs_summary_frequency = {
    "name": "seasonal_WOfS_frequency",
    "title": " Water Summary",
    "abstract": "WOfS seasonal summary showing the frequency of Wetness",
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
    "legend": legend_idx_percentage_by_20,
}

style_seasonal_wofs_summary_frequency_blue = {
    "name": "seasonal_WOfS_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS seasonal summary showing the frequency of Wetness",
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
    "legend": legend_idx_percentage_by_20,
}


layers = {
    "title": "Water Observations from Space Seasonal",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "Water Observations from Space 25m Wet Count (WOfS April - October Statistics)",
            "name": "wofs_apr_oct_summary_wet",
            "abstract": """
Water Observations from Space - April to October Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_apr_oct_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["count_wet"],
            },
            "styling": {
                "default_style": "seasonal_water_observations",
                "styles": [
                    style_wofs_seasonal_wet,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Clear Count (WOfS April - October Summary Statistics)",
            "name": "wofs_apr_oct_summary_clear",
            "abstract": """
Water Observations from Space - April to October Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary. This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green. For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_apr_oct_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["count_clear"],
            },
            "styling": {
                "default_style": "seasonal_clear_observations",
                "styles": [
                    style_wofs_seasonal_clear,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Water Summary (WOfS April - October Statistics)",
            "name": "wofs_apr_oct_summary_statistics",
            "abstract": """
	Water Observations from Space - Seasonal Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary. This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations. For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_apr_oct_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["frequency"],
            },
            "styling": {
                "default_style": "seasonal_WOfS_frequency",
                "styles": [
                    style_seasonal_wofs_summary_frequency,
                    style_seasonal_wofs_summary_frequency_blue,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Wet Count (WOfS November - March Statistics)	",
            "name": "wofs_nov_mar_summary_wet",
            "abstract": """
Water Observations from Space - November to March Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_nov_mar_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["count_wet"],
            },
            "styling": {
                "default_style": "seasonal_water_observations",
                "styles": [
                    style_wofs_seasonal_wet,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Clear Count (WOfS November - March Summary Statistics)",
            "name": "wofs_nov_mar_summary_clear",
            "abstract": """
	Water Observations from Space - November to March Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary. This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green. For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_nov_mar_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["count_clear"],
            },
            "styling": {
                "default_style": "seasonal_clear_observations",
                "styles": [
                    style_wofs_seasonal_clear,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Water Summary (WOfS November - March Statistics)",
            "name": "wofs_nov_mar_summary_statistics",
            "abstract": """
Water Observations from Space - Seasonal Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary. This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations. For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_nov_mar_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["frequency"],
            },
            "styling": {
                "default_style": "seasonal_WOfS_frequency",
                "styles": [
                    style_seasonal_wofs_summary_frequency,
                    style_seasonal_wofs_summary_frequency_blue,
                ],
            },
        },
    ],
}
