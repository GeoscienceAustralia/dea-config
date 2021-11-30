from ows_refactored.inland_water.wofs.bands_wo_cfg import (bands_wofs_filt_sum,
                                                           bands_wofs_sum)
from ows_refactored.ows_legend_cfg import (legend_idx_percentage_by_20,
                                           legend_idx_percentage_by_25)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

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


style_wofs_obs = {
    "name": "observations",
    "title": "Observations",
    "abstract": "Observations",
    "value_map": {
        "water": [
            {
                # Make noncontiguous data transparent
                "title": "",
                "abstract": "",
                "flags": {"noncontiguous": True},
                "alpha": 0.0,
                "color": "#ffffff",
            },
            {
                # Make sea and sea glint transparent
                "title": "",
                "abstract": "",
                "flags": {"sea": True},
                "alpha": 0.0,
                "color": "#4f81bd",
            },
            {
                "title": "Cloudy Steep Terrain",
                "abstract": "",
                "flags": {
                    "and": {
                        "high_slope": True,
                        "cloud": True
                    }
                },
                "color": "#f2dcb4",
            },
            {
                "title": "Cloudy Water",
                "abstract": "",
                "flags": {
                    "and": {
                        "wet": True,
                        "cloud": True
                    }
                },
                "color": "#bad4f2",
            },
            {
                "title": "Shaded Water",
                "abstract": "",
                "flags": {
                    "and": {
                        "wet": True,
                        "cloud_shadow": True
                    }
                },
                "color": "#335277",
            },
            {
                "title": "Cloud",
                "abstract": "",
                "flags": {"cloud": True},
                "color": "#c2c1c0",
            },
            {
                "title": "Cloud Shadow",
                "abstract": "",
                "flags": {"cloud_shadow": True},
                "color": "#4b4b37",
            },
            {
                "title": "Terrain Shadow or Low Sun Angle",
                "abstract": "",
                "flags": {"terrain_or_low_angle": True},
                "color": "#2f2922",
            },
            {
                "title": "Steep Terrain",
                "abstract": "",
                "flags": {"high_slope": True},
                "color": "#776857",
            },
            {
                "title": "Water",
                "abstract": "",
                "flags": {
                    "and": {
                        "wet": True,
                        "sea": False
                    }
                },
                "color": "#4f81bd",
            },
            {
                "title": "Dry",
                "abstract": "",
                "flags": {"and": {"dry": True, "sea": False}},
                "color": "#96966e",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 2.1},
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
                "alpha": 0.0,
            },
            {
                # Possible Sea Glint, also mark as invalid
                "title": "",
                "abstract": "",
                "flags": {"dry": True, "sea": True},
                "color": "#707070",
                "alpha": 0.0,
            },
            {
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                    "sea": False,
                },
                "color": "#D99694",
                "alpha": 0.0,
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
    "title": "DEA Multi-Year Water Observations Source Data (C2)",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "DEA Multi-Year Wet Observation Statistics (Landsat, C2)",
            "name": "wofs_summary_wet",
            "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, Wet)
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products which help the understanding of surface water across Australia.  The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains Wet Count: how many times water was detected in observations that were clear. No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary.

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf
https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_summary",
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
                "default_style": "water_observations",
                "styles": [
                    style_wofs_count_wet,
                ],
            },
        },
        {
            "title": "DEA Multi-Year Clear Observation Statistics (Landsat, C2)",
            "name": "wofs_summary_clear",
            "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, Clear)
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products which help the understanding of surface water across Australia.  The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains Clear Count: how many times an area could be clearly seen (ie. not affected by clouds, shadows or other satellite observation problems). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary.

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf
https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_summary",
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
                "default_style": "clear_observations",
                "styles": [
                    style_wofs_count_clear,
                ],
            },
        },
        {
            "title": "DEA Multi-Year Water Observation Frequency Statistics (Landsat, C2)",
            "name": "Water Observations from Space Statistics",  # TODO: add underscore to link the name
            "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, Frequency)
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product which combines WOfS observations into summary products that help the understanding of surface water across Australia. WOfS Statistics is calculated from the full depth time series (1986 – 2018). The water detected for each location is summed through time and then compared to the number of clear observations of that location. The result is a percentage value of the number of times water was observed at the location. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time (water summary).

This layer contains the Water Summary: the percentage of clear observations which were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary.

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf
https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_summary",
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
                "default_style": "WOfS_frequency",
                "styles": [
                    style_wofs_frequency,
                    style_wofs_frequency_blue,
                ],
            },
        },
        {
            "title": "DEA Multi-Year Water Observation Confidence Filtered Statistics  (Landsat, C2)",
            "name": "wofs_filtered_summary_confidence",
            "abstract": """Water Observations from Space Filtered Statistics 25m 2.1.5 (Landsat, Confidence)
Water Observations from Space (WOfS) Filtered Statistics helps provide the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. WOfS Filtered Statistics consists of a Confidence layer that compares the WOfS Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the WOfS Statistics water summary where Confidence is low. This layer is Confidence: the degree of agreement between water shown in the Water Summary and other national datasets. Areas where there is less than 1% confidence appears black, areas with confidence for between 1% 10% confidence are styled between black and red, areas with 25% confidence are styled yellow, areas with 75% confidence and above correspond to green. The Confidence layer provides understanding of whether the water shown in the Water Summary agrees with where water should exist in the landscape, such as due to sloping land or whether water has been detected in a location by other means. For more information please see: https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/Product%20Description.pdf
https://cmi.ga.gov.au/data-products/dea/211/dea-water-observations-filtered-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_filtered_summary",
            "bands": bands_wofs_filt_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "wofs_confidence",
                "styles": [
                    style_wofs_confidence,
                ],
            },
        },
    ],
}

statistics_layer = {
    "title": "DEA Multi-Year Water Observation Frequency Filtered Statistics (Landsat, C2)",
    "name": "wofs_filtered_summary",
    "abstract": """Water Observations from Space Filtered Statistics 25m 2.1.5 (Landsat, Filtered)
Water Observations from Space (WOfS) Filtered Statistics helps provide the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. WOfS Filtered Statistics consists of a Confidence layer that compares the WOfS Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the WOfS Statistics water summary where Confidence is low. This layer is Filtered Water Summary: A simplified version of the Water Summary, showing the frequency of water observations where the Confidence is above a cutoff level. No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations. The Filtered Water Summary layer is a noise-reduced view of surface water across Australia. Even though confidence filtering is applied to the Filtered Water Summary, some cloud and shadow, and sensor noise does persist. For more information please see: https://data.dea.ga.gov.au/?prefix=WOfS/filtered_summary/v2.1.0/Product%20Description.pdf
https://cmi.ga.gov.au/data-products/dea/211/dea-water-observations-filtered-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "wofs_filtered_summary",
    "bands": bands_wofs_filt_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "WOfS_filtered_frequency",
        "styles": [
            style_wofs_filt_freq,
            style_wofs_filt_freq_blue,
        ],
    },
}

c3_wofs_layer = {
    "title": "DEA Multi-Year Water Observation Frequency (Landsat, C3)",
    "name": "ga_ls_wo_fq_myear_c3",
    "abstract": """Geoscience Australia Landsat Water Observations Frequency Multi Year Collection 3
For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_wo_fq_myear_3",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
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
        "default_style": "WOfS_frequency",
        "styles": [
            style_wofs_frequency,
            style_wofs_frequency_blue,
            style_wofs_count_wet,
            style_wofs_count_clear,
        ],
    },
}
