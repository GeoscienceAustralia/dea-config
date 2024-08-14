from ows_refactored.ows_legend_cfg import legend_idx_0_1_5ticks

# 1. PQ mask common

pq_mask_fmask_land = [
    {
        "band": "oa_fmask",
        "values": [0, 2, 3],
        "invert": True,
    },
    {
        "band": "land",
        "invert": True,
        "values": [0],
    }
]

pq_mask_fmask_only = [
    {
        "band": "oa_fmask",
        "values": [0, 2, 3],
        "invert": True,
    }
]

# 2. Style Definitions
# 2a. Standard true and false colour component styles
style_combined_true_colour = {
    "name": "true_colour",
    "title": "True Colour",
    "abstract": "True-colour image, using the red, green and blue bands",
    "components": {
        "red": {"nbart_red": 1.0},
        "green": {"nbart_green": 1.0},
        "blue": {"nbart_blue": 1.0},
    },
    "scale_range": [0.0, 3000.0],
    "pq_masks": [
        {
            "band": "oa_fmask",
            "values": [0],
            "invert": True,
        }
    ],
}

style_combined_false_colour = {
    "name": "false_colour",
    "title": "False colour - Green, SWIR, NIR",
    "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {"nbart_common_swir_1": 1.0},
        "green": {"nbart_common_nir": 1.0},
        "blue": {"nbart_green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
    "pq_masks": [
        {
            "band": "oa_fmask",
            "values": [0],
            "invert": True,
        }
    ],
}

# 2b. Index colour-ramp styles

style_combined_ndvi = {
    "name": "ndvi",
    "title": "Normalised Difference Vegetation Index - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_common_nir", "band2": "nbart_red"},
    },
    "needed_bands": ["nbart_red", "nbart_common_nir"],
    "color_ramp": [
        {"value": -0.0, "color": "#8F3F20", "alpha": 0.0},
        {"value": 0.0, "color": "#8F3F20", "alpha": 1.0},
        {"value": 0.1, "color": "#A35F18"},
        {"value": 0.2, "color": "#B88512"},
        {"value": 0.3, "color": "#CEAC0E"},
        {"value": 0.4, "color": "#E5D609"},
        {"value": 0.5, "color": "#FFFF0C"},
        {"value": 0.6, "color": "#C3DE09"},
        {"value": 0.7, "color": "#88B808"},
        {"value": 0.8, "color": "#529400"},
        {"value": 0.9, "color": "#237100"},
        {"value": 1.0, "color": "#114D04"},
    ],
    "pq_masks": pq_mask_fmask_land,
    "legend": legend_idx_0_1_5ticks,
    # Define behaviour(s) for multi-date requests. If not declared, style only supports single-date requests.
    "multi_date": [
        # A multi-date handler.  Different handlers can be declared for different numbers of dates in a request.
        {
            # The count range for which this handler is to be used - a tuple of two ints, the smallest and
            # largest date counts for which this handler will be used.  Required.
            "allowed_count_range": [2, 2],
            # Preserve user date order
            "preserve_user_date_order": True,
            # A function, expressed in the standard format as described elsewhere in this example file.
            # The function is assumed to take one arguments, an xarray Dataset.
            # The function returns an xarray Dataset with a single band, which is the input to the
            # colour ramp defined below.
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "pq_masks": pq_mask_fmask_land,
            "legend": {
                "begin": "-1.0",
                "end": "1.0",
                "ticks": [
                    "-1.0",
                    "0.0",
                    "1.0",
                ],
            },
            # The feature info label for the multi-date index value.
            "feature_info_label": "ndvi_delta",
        }
    ],
}

style_combined_ndwi = {
    "name": "ndwi",
    "title": "Normalised Difference Water Index - Green, NIR",
    "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_green", "band2": "nbart_common_nir"},
    },
    "needed_bands": ["nbart_green", "nbart_common_nir"],
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {
            "value": 0.0,
            "color": "#d8e7f5",
        },
        {"value": 0.1, "color": "#b0d2e8"},
        {
            "value": 0.2,
            "color": "#73b3d8",
        },
        {"value": 0.3, "color": "#3e8ec4"},
        {
            "value": 0.4,
            "color": "#1563aa",
        },
        {
            "value": 0.5,
            "color": "#08306b",
        },
    ],
    "pq_masks": pq_mask_fmask_only,
    "legend": {
        "begin": "0.0",
        "end": "0.5",
        "decimal_places": 1,
        "ticks": ["0.0", "0.2", "0.4", "0.5"],
        "tick_labels": {
            "0.0": {"prefix": "<"},
            "0.2": {"label": "0.2"},
            "0.4": {"label": "0.4"},
            "0.5": {"prefix": ">"},
        },
    },
    # Define behaviour(s) for multi-date requests. If not declared, style only supports single-date requests.
    "multi_date": [
        # A multi-date handler.  Different handlers can be declared for different numbers of dates in a request.
        {
            # The count range for which this handler is to be used - a tuple of two ints, the smallest and
            # largest date counts for which this handler will be used.  Required.
            "allowed_count_range": [2, 2],
            # Preserve user date order
            "preserve_user_date_order": True,
            # A function, expressed in the standard format as described elsewhere in this example file.
            # The function is assumed to take one arguments, an xarray Dataset.
            # The function returns an xarray Dataset with a single band, which is the input to the
            # colour ramp defined below.
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "pq_masks": pq_mask_fmask_land,
            "legend": {
                "begin": "-1.0",
                "end": "1.0",
                "ticks": [
                    "-1.0",
                    "-0.0",
                    "1.0",
                ],
            },
            # The feature info label for the multi-date index value.
            "feature_info_label": "ndwi_delta",
        }
    ],
}

style_combined_mndwi = {
    "name": "mndwi",
    "title": "Modified Normalised Difference Water Index - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_green", "band2": "nbart_common_swir_1"},
    },
    "needed_bands": ["nbart_green", "nbart_common_swir_1"],
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5"},
        {"value": 0.2, "color": "#b0d2e8"},
        {"value": 0.4, "color": "#73b3d8"},
        {"value": 0.6, "color": "#3e8ec4"},
        {"value": 0.8, "color": "#1563aa"},
        {"value": 1.0, "color": "#08306b"},
    ],
    "pq_masks": pq_mask_fmask_only,
    "legend": legend_idx_0_1_5ticks,
    # Define behaviour(s) for multi-date requests. If not declared, style only supports single-date requests.
    "multi_date": [
        # A multi-date handler.  Different handlers can be declared for different numbers of dates in a request.
        {
            # The count range for which this handler is to be used - a tuple of two ints, the smallest and
            # largest date counts for which this handler will be used.  Required.
            "allowed_count_range": [2, 2],
            # Preserve user date order
            "preserve_user_date_order": True,
            # A function, expressed in the standard format as described elsewhere in this example file.
            # The function is assumed to take one arguments, an xarray Dataset.
            # The function returns an xarray Dataset with a single band, which is the input to the
            # colour ramp defined below.
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "pq_masks": pq_mask_fmask_land,
            "legend": {
                "begin": "-1.0",
                "end": "1.0",
                "ticks": [
                    "-1.0",
                    "0.0",
                    "1.0",
                ],
            },
            # The feature info label for the multi-date index value.
            "feature_info_label": "mndwi_delta",
        }
    ],
}

style_combined_nbr = {
    "name": "nbr",
    "title": "Normalised Burn Ratio - NIR, SWIR",
    "abstract": "Normalised Burn Ratio - a derived index that that uses the differences in the way health green vegetation and burned vegetation reflect light to find burned area",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_common_nir", "band2": "nbart_common_swir_2"},
    },
    "needed_bands": ["nbart_common_nir", "nbart_common_swir_2"],
    "color_ramp": [
        {
            "value": -1.0,
            "color": "#67001F",
            "alpha": 0.0,
        },
        {
            "value": -1.0,
            "color": "#67001F",
        },
        {
            "value": -0.8,
            "color": "#B2182B",
        },
        {"value": -0.4, "color": "#D6604D"},
        {"value": -0.2, "color": "#F4A582"},
        {"value": -0.1, "color": "#FDDBC7"},
        {
            "value": 0,
            "color": "#F7F7F7",
        },
        {"value": 0.2, "color": "#D1E5F0"},
        {"value": 0.4, "color": "#92C5DE"},
        {"value": 0.6, "color": "#4393C3"},
        {"value": 0.9, "color": "#2166AC"},
        {
            "value": 1.0,
            "color": "#053061",
        },
    ],
    "pq_masks": pq_mask_fmask_land,
    "legend": {
        "show_legend": True,
        "begin": "-1.0",
        "end": "1.0",
        "ticks_every": "1.0",
        "decimal_places": 0,
        "tick_labels": {"-1.0": {"prefix": "<"}, "1.0": {"suffix": ">"}},
    },
    # Define behaviour(s) for multi-date requests. If not declared, style only supports single-date requests.
    "multi_date": [
        # A multi-date handler.  Different handlers can be declared for different numbers of dates in a request.
        {
            # The count range for which this handler is to be used - a tuple of two ints, the smallest and
            # largest date counts for which this handler will be used.  Required.
            "allowed_count_range": [2, 2],
            # Preserve user date order
            "preserve_user_date_order": True,
            # A function, expressed in the standard format as described elsewhere in this example file.
            # The function is assumed to take one arguments, an xarray Dataset.
            # The function returns an xarray Dataset with a single band, which is the input to the
            # colour ramp defined below.
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "color_ramp": [
                {"value": -0.5, "color": "#768642", "alpha": 0.0},
                {"value": -0.5, "color": "#768642"},
                {"value": -0.25, "color": "#768642", "alpha": 1.0},
                {"value": -0.25, "color": "#a4bd5f"},
                {"value": -0.1, "color": "#a4bd5f"},
                {"value": -0.1, "color": "#00e05d"},
                {"value": 0.1, "color": "#00e05d"},
                {"value": 0.1, "color": "#fdf950"},
                {"value": 0.27, "color": "#fdf950"},
                {"value": 0.27, "color": "#ffae52"},
                {"value": 0.44, "color": "#ffae52"},
                {"value": 0.44, "color": "#ff662e"},
                {"value": 0.66, "color": "#ff662e"},
                {"value": 0.66, "color": "#ad28cc"},
                {"value": 0.88, "color": "#ad28cc"},
            ],
            "pq_masks": pq_mask_fmask_land,
            "legend": {
                "begin": "-0.5",
                "end": "0.88",
                "ticks": [
                    "-0.5",
                    "-0.25",
                    "-0.1",
                    "0.1",
                    "0.27",
                    "0.44",
                    "0.66",
                    "0.88",
                ],
                "tick_labels": {
                    "-0.5": {"label": "<-0.5"},
                    "-0.25": {"label": "-0.25"},
                    "-0.1": {"label": "-0.1"},
                    "0.1": {"label": "0.1"},
                    "0.27": {"label": "0.27"},
                    "0.44": {"label": "0.44"},
                    "0.66": {"label": "0.66"},
                    "0.88": {"label": ">1.30"},
                },
            },
            # The multi-date color ramp.  May be defined as an explicit colour ramp, as shown above for the single
            # date case; or may be defined with a range and unscaled color ramp as shown here.
            #
            # The range specifies the min and max values for the color ramp.  Required if an explicit color
            # ramp is not defined.
            # "range": [-1.0, 1.0],
            # The name of a named matplotlib color ramp.
            # Reference here: https://matplotlib.org/examples/color/colormaps_reference.html
            # Only used if an explicit colour ramp is not defined.  Optional - defaults to a simple (but
            # kind of ugly) blue-to-red rainbow ramp.
            # "mpl_ramp": "RdBu",
            # The feature info label for the multi-date index value.
            "feature_info_label": "nbr_delta",
        }
    ],
}

# 2c. Categorical (value map) styles
style_combined_fmask = {
    "name": "fmask",
    "title": "Fmask Classification",
    "abstract": "Fmask (Function of mask) is used for automated clouds, cloud shadows, snow, and water masking for Landsats 4-8 and Sentinel 2 images.",
    "include_in_feature_info": False,
    "needed_bands": ["oa_fmask"],
    "value_map": {
        "oa_fmask": [
            {
                "title": "No Data",
                "abstract": "",
                "values": [
                    0,    # nodata
                ],
                "alpha": 0.0,
                "color": "#FFFFFF",
            },
            {
                "title": "Clear",
                "abstract": "",
                "values": [
                    1,    # clear/valid
                ],
                "color": "#84A278",
            },
            {
                "title": "Cloud",
                "abstract": "",
                "values": [
                    2,    # cloud
                ],
                "color": "#D0CFCE",
            },
            {
                "title": "Shadow",
                "abstract": "",
                "values": [
                    3    # shadow
                ],
                "color": "#464633",
            },
            {
                "title": "Snow",
                "abstract": "",
                "values": [
                    4    # snow
                ],
                "color": "#E0EDFF",
            },
            {
                "title": "Water",
                "abstract": "",
                "values": [
                    5    # water
                ],
                "color": "#475B74",
            },
        ]
    }
}

# 2d. Pure single-band styles
style_combined_pure_blue = {
    "name": "blue",
    "title": "Blue",
    "abstract": "Visible blue band (approx 480nm)",
    "components": {
        "red": {"nbart_blue": 1.0},
        "green": {"nbart_blue": 1.0},
        "blue": {"nbart_blue": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_combined_pure_green = {
    "name": "green",
    "title": "Green",
    "abstract": "Visible green band (approx 550nm)",
    "components": {
        "red": {"nbart_green": 1.0},
        "green": {"nbart_green": 1.0},
        "blue": {"nbart_green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_combined_pure_red = {
    "name": "red",
    "title": "Red",
    "abstract": "Visible red band (approx 650nm)",
    "components": {
        "red": {"nbart_red": 1.0},
        "green": {"nbart_red": 1.0},
        "blue": {"nbart_red": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_combined_pure_nir = {
    "name": "nir",
    "title": "Near infrared",
    "abstract": "Broad near-infrared band (approx 850nm)",
    "components": {
        "red": {"nbart_common_nir": 1.0},
        "green": {"nbart_common_nir": 1.0},
        "blue": {"nbart_common_nir": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_combined_pure_swir1 = {
    "name": "swir1",
    "title": "Shortwave infrared band 1",
    "abstract": "Shortwave near-infrared band 1 (approx 1600nm)",
    "components": {
        "red": {"nbart_common_swir_1": 1.0},
        "green": {"nbart_common_swir_1": 1.0},
        "blue": {"nbart_common_swir_1": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_combined_pure_swir2 = {
    "name": "swir2",
    "title": "Shortwave infrared band 2",
    "abstract": "Shortwave near-infrared band 2 (approx 2200nm)",
    "components": {
        "red": {"nbart_common_swir_2": 1.0},
        "green": {"nbart_common_swir_2": 1.0},
        "blue": {"nbart_common_swir_2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


# Styles grouping
styles_combined = [
    style_combined_true_colour,
    style_combined_false_colour,
    style_combined_ndvi,
    style_combined_ndwi,
    style_combined_mndwi,
    style_combined_nbr,
    style_combined_pure_blue,
    style_combined_pure_green,
    style_combined_pure_red,
    style_combined_pure_nir,
    style_combined_pure_swir1,
    style_combined_pure_swir2,
    style_combined_fmask
]
