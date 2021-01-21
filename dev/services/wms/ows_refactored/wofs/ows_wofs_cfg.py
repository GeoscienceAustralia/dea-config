from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35
from ows_refactored.ows_legend_cfg import (
    legend_idx_percentage_by_20,
    legend_idx_percentage_by_25,
    legend_idx_twentyplus_3ticks,
    legend_idx_thirtyplus_4ticks,
)

bands_wofs_filt_sum = {"confidence": [], "wofs_filtered_summary": []}

bands_wofs_sum = {
    "count_wet": [],
    "count_clear": [],
    "frequency": [],
}

bands_wofs_obs = {
    "water": [],
}

style_wofs_filt_freq = {
    "name": "WOfS_filtered_frequency",
    "title": "Filtered Water Summary",
    "abstract": "WOfS filtered summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "wofs_filtered_summary",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["wofs_filtered_summary"],
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 0.002, "color": "#000000", "alpha": 0.0},
        {"value": 0.005, "color": "#8e0101", "alpha": 0.25},
        {"value": 0.01, "color": "#cf2200", "alpha": 0.75},
        {"value": 0.02, "color": "#e38400"},
        {"value": 0.05, "color": "#e3df00"},
        {"value": 0.1, "color": "#a6e300"},
        {"value": 0.2, "color": "#62e300"},
        {"value": 0.3, "color": "#00e32d"},
        {"value": 0.4, "color": "#00e384"},
        {"value": 0.5, "color": "#00e3c8"},
        {"value": 0.6, "color": "#00c5e3"},
        {"value": 0.7, "color": "#0097e3"},
        {"value": 0.8, "color": "#005fe3"},
        {"value": 0.9, "color": "#000fe3"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "legend": {
        "url": "https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/wofs_full_summary_legend.png",
    },
}

style_wofs_filt_freq_blue = {
    "name": "WOfS_filtered_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS filtered summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "wofs_filtered_summary",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["wofs_filtered_summary"],
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

style_wofs_count_wet = {
    "name": "water_observations",
    "title": "Wet Count",
    "abstract": "WOfS summary showing the count of water observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_wet",
        },
    },
    "needed_bands": ["count_wet"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {"value": 2, "color": "#890000"},
        {"value": 5, "color": "#990000"},
        {"value": 10, "color": "#E38400"},
        {"value": 25, "color": "#E3DF00"},
        {"value": 50, "color": "#A6E300"},
        {"value": 100, "color": "#00E32D"},
        {"value": 150, "color": "#00E3C8"},
        {"value": 200, "color": "#0097E3"},
        {"value": 250, "color": "#005FE3"},
        {"value": 300, "color": "#000FE3"},
        {"value": 350, "color": "#000EA9"},
        {
            "value": 400,
            "color": "#5700E3",
        },
    ],
    "legend": {
        "begin": "0",
        "end": "400",
        "decimal_places": 0,
        "ticks_every": 100,
        "tick_labels": {
            "400": {"prefix": ">"},
        },
    },
}

style_wofs_count_clear = {
    "name": "clear_observations",
    "title": "Clear Count",
    "abstract": "WOfS summary showing the count of clear observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_clear",
        },
    },
    "needed_bands": ["count_clear"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0, "color": "#FFFFFF", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 10,
            "color": "#b21800",
            "alpha": 1,
        },
        {"value": 100, "color": "#ef8500"},
        {"value": 200, "color": "#ffb800"},
        {"value": 300, "color": "#ffd300"},
        {"value": 400, "color": "#ffe300"},
        {"value": 500, "color": "#fff300"},
        {"value": 600, "color": "#d0f800"},
        {"value": 700, "color": "#a0fd00"},
        {"value": 800, "color": "#6ee100"},
        {"value": 901, "color": "#39a500"},
        {
            "value": 1000,
            "color": "#026900",
        },
    ],
    "legend": {
        "begin": "0",
        "end": "1000",
        "decimal_places": 0,
        "ticks_every": 100,
        "strip_location": [0.05, 0.5, 0.89, 0.15],
        "tick_labels": {
            "1000": {"prefix": ">"},
        },
    },
}


style_wofs_frequency = {
    "name": "WOfS_frequency",
    "title": " Water Summary",
    "abstract": "WOfS summary showing the frequency of Wetness",
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
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 0.002, "color": "#000000", "alpha": 0.0},
        {"value": 0.005, "color": "#8e0101", "alpha": 0.25},
        {"value": 0.01, "color": "#cf2200", "alpha": 0.75},
        {"value": 0.02, "color": "#e38400"},
        {"value": 0.05, "color": "#e3df00"},
        {"value": 0.1, "color": "#a6e300"},
        {"value": 0.2, "color": "#62e300"},
        {"value": 0.3, "color": "#00e32d"},
        {"value": 0.4, "color": "#00e384"},
        {"value": 0.5, "color": "#00e3c8"},
        {"value": 0.6, "color": "#00c5e3"},
        {"value": 0.7, "color": "#0097e3"},
        {"value": 0.8, "color": "#005fe3"},
        {"value": 0.9, "color": "#000fe3"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "legend": {
        "url": "https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/wofs_full_summary_legend.png",
    },
}

style_wofs_frequency_blue = {
    "name": "WOfS_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS summary showing the frequency of Wetness",
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

style_wofs_confidence = {
    "name": "wofs_confidence",
    "title": "Confidence",
    "abstract": "WOfS Confidence",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "confidence",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["confidence"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#000000",
        },
        {"value": 0.01, "color": "#000000"},
        {"value": 0.02, "color": "#990000"},
        {"value": 0.05, "color": "#CF2200"},
        {"value": 0.1, "color": "#E38400"},
        {"value": 0.25, "color": "#E3DF00"},
        {"value": 0.5, "color": "#A6E300"},
        {"value": 0.75, "color": "#62E300"},
        {"value": 1.0, "color": "#00E32D"},
    ],
    "legend": legend_idx_percentage_by_25,
}

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

style_wofs_obs = {
    "name": "observations",
    "title": "Observations",
    "abstract": "Observations",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {
                    "or": {
                        "terrain_or_low_angle": True,
                        "cloud_shadow": True,
                        "cloud": True,
                        "high_slope": True,
                        "noncontiguous": True,
                    }
                },
                "color": "#707070",
            },
            {
                # Possible Sea Glint, also mark as invalid
                "title": "",
                "abstract": "",
                "flags": {"dry": True, "sea": True},
                "color": "#707070",
            },
            {
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                    "sea": False,
                },
                "color": "#D99694",
            },
            {
                "title": "Wet",
                "abstract": "Wet or Sea",
                "flags": {"or": {"wet": True, "sea": True}},
                "color": "#4F81BD",
            },
        ]
    },
}

style_wofs_obs_wet_only = {
    "name": "wet",
    "title": "Wet Only",
    "abstract": "Wet Only",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {
                    "or": {
                        "terrain_or_low_angle": True,
                        "cloud_shadow": True,
                        "cloud": True,
                        "high_slope": True,
                        "noncontiguous": True,
                    }
                },
                "color": "#707070",
                "mask": True,
            },
            {
                # Possible Sea Glint, also mark as invalid
                "title": "",
                "abstract": "",
                "flags": {"dry": True, "sea": True},
                "color": "#707070",
                "mask": True,
            },
            {
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                    "sea": False,
                },
                "color": "#D99694",
                "mask": True,
            },
            {
                "title": "Wet",
                "abstract": "Wet or Sea",
                "flags": {"or": {"wet": True, "sea": True}},
                "color": "#4F81BD",
            },
        ]
    },
}

layers = {
    "title": "Water Observations from Space",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "Water Observations from Space 25m Filtered Water Summary (WOfS Filtered Statistics)",
            "name": "wofs_filtered_summary",
            "abstract": """
Water Observations from Space (WOfS) Filtered Statistics helps provide the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. WOfS Filtered Statistics consists of a Confidence layer that compares the WOfS Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the WOfS Statistics water summary where Confidence is low. This layer is Filtered Water Summary: A simplified version of the Water Summary, showing the frequency of water observations where the Confidence is above a cutoff level. No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations. The Filtered Water Summary layer is a noise-reduced view of surface water across Australia. Even though confidence filtering is applied to the Filtered Water Summary, some cloud and shadow, and sensor noise does persist. For more information please see: https://data.dea.ga.gov.au/?prefix=WOfS/filtered_summary/v2.1.0/Product%20Description.pdf For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_filtered_summary",
            "bands": bands_wofs_filt_sum,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["wofs_filtered_summary"],
            },
            "styling": {
                "default_style": "WOfS_filtered_frequency",
                "styles": [
                    style_wofs_filt_freq,
                    style_wofs_filt_freq_blue,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Wet Count (WOfS Statistics)",
            "name": "wofs_summary_wet",
            "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products which help the understanding of surface water across Australia.  The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains Wet Count: how many times water was detected in observations that were clear. No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary.

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_35,
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
                "default_style": "water_observations",
                "styles": [
                    style_wofs_count_wet,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Clear Count (WOfS Statistics)",
            "name": "wofs_summary_clear",
            "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products which help the understanding of surface water across Australia.  The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains Clear Count: how many times an area could be clearly seen (ie. not affected by clouds, shadows or other satellite observation problems). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary.

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_35,
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
                "default_style": "clear_observations",
                "styles": [
                    style_wofs_count_clear,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Water Summary (WOfS Statistics)	",
            "name": "Water Observations from Space Statistics",
            "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product which combines WOfS observations into summary products that help the understanding of surface water across Australia. WOfS Statistics is calculated from the full depth time series (1986 – 2018). The water detected for each location is summed through time and then compared to the number of clear observations of that location. The result is a percentage value of the number of times water was observed at the location. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time (water summary).

This layer contains the Water Summary: the percentage of clear observations which were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary.

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_35,
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
                "default_style": "WOfS_frequency",
                "styles": [
                    style_wofs_frequency,
                    style_wofs_frequency_blue,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Confidence (WOfS Filtered Statistics)",
            "name": "wofs_filtered_summary_confidence",
            "abstract": """
Water Observations from Space (WOfS) Filtered Statistics helps provide the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. WOfS Filtered Statistics consists of a Confidence layer that compares the WOfS Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the WOfS Statistics water summary where Confidence is low. This layer is Confidence: the degree of agreement between water shown in the Water Summary and other national datasets. Areas where there is less than 1% confidence appears black, areas with confidence for between 1% 10% confidence are styled between black and red, areas with 25% confidence are styled yellow, areas with 75% confidence and above correspond to green. The Confidence layer provides understanding of whether the water shown in the Water Summary agrees with where water should exist in the landscape, such as due to sloping land or whether water has been detected in a location by other means. For more information please see: https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/Product%20Description.pdf For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_filtered_summary",
            "bands": bands_wofs_filt_sum,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["confidence"],
            },
            "styling": {
                "default_style": "wofs_confidence",
                "styles": [
                    style_wofs_confidence,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Wet Count (WOfS Annual Statistics)",
            "name": "wofs_annual_summary_wet",
            "abstract": """
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.
For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_annual_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_35,
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
                "default_style": "annual_water_observations",
                "styles": [
                    style_wofs_summary_wet,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Clear Count (WOfS Annual Statistics)",
            "name": "wofs_annual_summary_clear",
            "abstract": """
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary. This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green. For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_annual_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_35,
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
                "default_style": "annual_clear_observations",
                "styles": [
                    style_wofs_summary_clear,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Water Summary (WOfS Annual Statistics)",
            "name": "wofs_annual_summary_statistics",
            "abstract": """
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.
For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_annual_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_35,
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
                "default_style": "annual_WOfS_frequency",
                "styles": [
                    style_annual_wofs_summary_frequency,
                    style_annual_wofs_summary_frequency_blue,
                ],
            },
        },
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
            "resource_limits": reslim_wms_min_zoom_35,
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
            "resource_limits": reslim_wms_min_zoom_35,
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
            "resource_limits": reslim_wms_min_zoom_35,
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
            "resource_limits": reslim_wms_min_zoom_35,
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
            "resource_limits": reslim_wms_min_zoom_35,
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
            "resource_limits": reslim_wms_min_zoom_35,
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
            "title": "Water Observations from Space 25m albers (WOfS Daily Observations)",
            "name": "wofs_albers",
            "abstract": """
Water Observations from Space (WOfS) provides surface water observations derived from satellite imagery for all of Australia. The current product (Version 2.1.5) includes observations taken from 1986 to the present, from the Landsat 5, 7 and 8 satellites. WOfS covers all of mainland Australia and Tasmania but excludes off-shore Territories.

The WOfS product allows users to get a better understanding of where water is normally present in a landscape, where water is seldom observed, and where inundation has occurred occasionally.

Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water. The details of the WOfS algorithm and derived statistics are available at http://dx.doi.org/10.1016/j.rse.2015.11.003.

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_albers",
            "bands": bands_wofs_obs,
            "resource_limits": reslim_wms_min_zoom_35,
            "dynamic": True,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_bitflag",
                "always_fetch_bands": [],
                "manual_merge": False,
                "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["water"],
            },
            "styling": {
                "default_style": "observations",
                "styles": [style_wofs_obs, style_wofs_obs_wet_only],
            },
        },
    ],
}
