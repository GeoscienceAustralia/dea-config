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
            # {
            #     "title": "Invalid",
            #     "abstract": "Slope or Cloud",
            #     "flags": {
            #         "or": {
            #             "terrain_or_low_angle": True,
            #             "cloud_shadow": True,
            #             "cloud": True,
            #             "high_slope": True,
            #             "noncontiguous": True,
            #         }
            #     },
            #     "color": "#707070",
            #     "mask": True,
            # },
            # {
            #     # Possible Sea Glint, also mark as invalid
            #     "title": "",
            #     "abstract": "",
            #     "flags": {"dry": True, "sea": True},
            #     "color": "#707070",
            #     "mask": True,
            # },
            # {
            #     "title": "Dry",
            #     "abstract": "Dry",
            #     "flags": {
            #         "dry": True,
            #         "sea": False,
            #     },
            #     "color": "#D99694",
            #     "mask": True,
            # },
            {
                "title": "Wet",
                "abstract": "Wet or Sea",
                "flags": {"or": {"wet": True, "sea": True}},
                "color": "#4F81BD",
            },
        ]
    },
    "pq_masks": [
        {
            "band": "water",
            "flags": {
                    "or": {
                        "terrain_or_low_angle": True,
                        "cloud_shadow": True,
                        "cloud": True,
                        "high_slope": True,
                        "noncontiguous": True,
                    }
                },
        },
        {
            "band": "water",
            "flags": {"dry": True, "sea": True},

        },
        {
            "band": "water",
            "flags": {
                    "dry": True,
                    "sea": False,
                },
        }
    ]
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
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
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
            "title": "Water Observations from Space 25m Confidence (WOfS Filtered Statistics)",
            "name": "wofs_filtered_summary_confidence",
            "abstract": """
Water Observations from Space (WOfS) Filtered Statistics helps provide the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. WOfS Filtered Statistics consists of a Confidence layer that compares the WOfS Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the WOfS Statistics water summary where Confidence is low. This layer is Confidence: the degree of agreement between water shown in the Water Summary and other national datasets. Areas where there is less than 1% confidence appears black, areas with confidence for between 1% 10% confidence are styled between black and red, areas with 25% confidence are styled yellow, areas with 75% confidence and above correspond to green. The Confidence layer provides understanding of whether the water shown in the Water Summary agrees with where water should exist in the landscape, such as due to sloping land or whether water has been detected in a location by other means. For more information please see: https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/Product%20Description.pdf For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_filtered_summary",
            "bands": bands_wofs_filt_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
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
            "include": "ows_refactored.wofs.ows_wofs_summary_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.wofs.ows_wofs_annual_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.wofs.ows_wofs_seasonal_cfg.layers",
            "type": "python",
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
            "flags": [
                {
                    "band": "water",
                    "product": "wofs_albers",
                    "ignore_time": False,
                    "ignore_info_flags": [],
                    "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
                }
            ],
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
