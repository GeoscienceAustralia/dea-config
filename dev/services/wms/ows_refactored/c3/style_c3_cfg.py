from ows_refactored.ows_legend_cfg import legend_idx_0_1_5ticks

# Style definition
style_c3_pure_aerosol = {
    "name": "aerosol",
    "title": "Narrow Blue - 440",
    "abstract": "Coastal Aerosol or Narrow Blue band, approximately 435nm to 450nm",
    "components": {
        "red": {"nbart_coastal_aerosol": 1.0},
        "green": {"nbart_coastal_aerosol": 1.0},
        "blue": {"nbart_coastal_aerosol": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_c3_ls7_pure_panchromatic = {
    "name": "panchromatic",
    "title": "Panchromatic - 710",
    "abstract": "Panchromatic, centered on 710nm",
    "components": {
        "red": {"nbart_panchromatic": 1.0},
        "green": {"nbart_panchromatic": 1.0},
        "blue": {"nbart_panchromatic": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_c3_ls8_pure_panchromatic = {
    "name": "panchromatic",
    "title": "Panchromatic - 590",
    "abstract": "Panchromatic, centered on 590nm",
    "components": {
        "red": {"nbart_panchromatic": 1.0},
        "green": {"nbart_panchromatic": 1.0},
        "blue": {"nbart_panchromatic": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_c3_true_colour = {
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
            "enum": 0,
            "invert": True,
        }
    ],
}

style_c3_false_colour = {
    "name": "false_colour",
    "title": "False colour - Green, SWIR, NIR",
    "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {"nbart_swir_1": 1.0},
        "green": {"nbart_nir": 1.0},
        "blue": {"nbart_green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
    "pq_masks": [
        {
            "band": "oa_fmask",
            "enum": 0,
            "invert": True,
        }
    ],
}

style_c3_ndvi = {
    "name": "ndvi",
    "title": "Normalised Difference Vegetation Index - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_nir", "band2": "nbart_red"},
    },
    "needed_bands": ["nbart_red", "nbart_nir"],
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
    "pq_masks": [
        {
            "band": "oa_fmask",
            "enum": 0,
            "invert": True,
        },
        {
            "band": "oa_fmask",
            "enum": 2,
            "invert": True,
        },
        {
            "band": "oa_fmask",
            "enum": 3,
            "invert": True,
        },
        {
            "band": "land",
            "invert": True,
            "enum": 1,
        },
    ],
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
            "pq_masks": [
                {
                    "band": "oa_fmask",
                    "enum": 0,
                    "invert": True,
                },
                {
                    "band": "oa_fmask",
                    "enum": 2,
                    "invert": True,
                },
                {
                    "band": "oa_fmask",
                    "enum": 3,
                    "invert": True,
                },
                {
                    "band": "land",
                    "invert": True,
                    "enum": 1,
                },
            ],
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

style_c3_ndvi_anim = {
    "name": "ndvi_animated",
    "title": "Normalised Difference Vegetation Index (Animated) - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_nir", "band2": "nbart_red"},
    },
    "needed_bands": ["nbart_red", "nbart_nir"],
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
    "pq_masks": [
        {
            "band": "oa_fmask",
            "enum": 0,
            "invert": True,
        },
        {
            "band": "oa_fmask",
            "enum": 2,
            "invert": True,
        },
        {
            "band": "oa_fmask",
            "enum": 3,
            "invert": True,
        },
        {
            "band": "land",
            "invert": True,
            "enum": 1,
        },
    ],
    "legend": legend_idx_0_1_5ticks,
    # Define behaviour(s) for multi-date requests. If not declared, style only supports single-date requests.
    "multi_date": [
        # A multi-date handler.  Different handlers can be declared for different numbers of dates in a request.
        {
            # The count range for which this handler is to be used - a tuple of two ints, the smallest and
            # largest date counts for which this handler will be used.  Required.
            "allowed_count_range": [2, 10],
            # Preserve user date order
            "preserve_user_date_order": True,
            # A function, expressed in the standard format as described elsewhere in this example file.
            # The function is assumed to take one arguments, an xarray Dataset.
            # The function returns an xarray Dataset with a single band, which is the input to the
            # colour ramp defined below.
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_pass"
            },
            "animate": True,
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
            "pq_masks": [
                {
                    "band": "oa_fmask",
                    "enum": 0,
                    "invert": True,
                },
                {
                    "band": "oa_fmask",
                    "enum": 2,
                    "invert": True,
                },
                {
                    "band": "oa_fmask",
                    "enum": 3,
                    "invert": True,
                },
                {
                    "band": "land",
                    "invert": True,
                    "enum": 1,
                },
            ],
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
            "feature_info_label": "ndvi_animate",
        }
    ],
}

style_c3_ndwi = {
    "name": "ndwi",
    "title": "Normalised Difference Water Index - Green, NIR",
    "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_green", "band2": "nbart_nir"},
    },
    "needed_bands": ["nbart_green", "nbart_nir"],
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
    "pq_masks": [
        {
            "band": "oa_fmask",
            "enum": 0,
            "invert": True,
        },
        {
            "band": "oa_fmask",
            "enum": 2,
            "invert": True,
        },
        {
            "band": "oa_fmask",
            "enum": 3,
            "invert": True,
        },
    ],
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
            "pq_masks": [
                {
                    "band": "oa_fmask",
                    "enum": 0,
                    "invert": True,
                },
                {
                    "band": "oa_fmask",
                    "enum": 2,
                    "invert": True,
                },
                {
                    "band": "oa_fmask",
                    "enum": 3,
                    "invert": True,
                },
                {
                    "band": "land",
                    "invert": True,
                    "enum": 1,
                },
            ],
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

style_c3_mndwi = {
    "name": "mndwi",
    "title": "Modified Normalised Difference Water Index - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_green", "band2": "nbart_swir_1"},
    },
    "needed_bands": ["nbart_green", "nbart_swir_1"],
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5"},
        {"value": 0.2, "color": "#b0d2e8"},
        {"value": 0.4, "color": "#73b3d8"},
        {"value": 0.6, "color": "#3e8ec4"},
        {"value": 0.8, "color": "#1563aa"},
        {"value": 1.0, "color": "#08306b"},
    ],
    "pq_masks": [
        {
            "band": "oa_fmask",
            "enum": 0,
            "invert": True,
        },
        {
            "band": "oa_fmask",
            "enum": 2,
            "invert": True,
        },
        {
            "band": "oa_fmask",
            "enum": 3,
            "invert": True,
        },
    ],
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
            "pq_masks": [
                {
                    "band": "oa_fmask",
                    "enum": 0,
                    "invert": True,
                },
                {
                    "band": "oa_fmask",
                    "enum": 2,
                    "invert": True,
                },
                {
                    "band": "oa_fmask",
                    "enum": 3,
                    "invert": True,
                },
                {
                    "band": "land",
                    "invert": True,
                    "enum": 1,
                },
            ],
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

style_c3_pure_blue = {
    "name": "blue",
    "title": "Blue - 480",
    "abstract": "Blue band, centered on 480nm",
    "components": {
        "red": {"nbart_blue": 1.0},
        "green": {"nbart_blue": 1.0},
        "blue": {"nbart_blue": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_c3_pure_green = {
    "name": "green",
    "title": "Green - 560",
    "abstract": "Green band, centered on 560nm",
    "components": {
        "red": {"nbart_green": 1.0},
        "green": {"nbart_green": 1.0},
        "blue": {"nbart_green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_c3_pure_red = {
    "name": "red",
    "title": "Red - 660",
    "abstract": "Red band, centered on 660nm",
    "components": {
        "red": {"nbart_red": 1.0},
        "green": {"nbart_red": 1.0},
        "blue": {"nbart_red": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_c3_pure_nir = {
    "name": "nir",
    "title": "Near Infrared (NIR) - 840",
    "abstract": "Near infra-red band, centered on 840nm",
    "components": {
        "red": {"nbart_nir": 1.0},
        "green": {"nbart_nir": 1.0},
        "blue": {"nbart_nir": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_c3_pure_swir1 = {
    "name": "swir1",
    "title": "Shortwave Infrared (SWIR) - 1650",
    "abstract": "Short wave infra-red band 1, centered on 1650nm",
    "components": {
        "red": {"nbart_swir_1": 1.0},
        "green": {"nbart_swir_1": 1.0},
        "blue": {"nbart_swir_1": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_c3_pure_swir2 = {
    "name": "swir2",
    "title": "Shortwave Infrared (SWIR) - 2220",
    "abstract": "Short wave infra-red band 2, centered on 2220nm",
    "components": {
        "red": {"nbart_swir_2": 1.0},
        "green": {"nbart_swir_2": 1.0},
        "blue": {"nbart_swir_2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_c3_nbr = {
    "name": "nbr",
    "title": "Normalised Burn Ratio - NIR, SWIR",
    "abstract": "Normalised Burn Ratio - a derived index that that uses the differences in the way health green vegetation and burned vegetation reflect light to find burned area",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_nir", "band2": "nbart_swir_2"},
    },
    "needed_bands": ["nbart_nir", "nbart_swir_2"],
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
    "pq_masks": [
        {
            "band": "oa_fmask",
            "enum": 0,
            "invert": True,
        },
        {
            "band": "oa_fmask",
            "enum": 2,
            "invert": True,
        },
        {
            "band": "oa_fmask",
            "enum": 3,
            "invert": True,
        },
        {
            "band": "land",
            "invert": True,
            "enum": 1,
        },
    ],
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
            "pq_masks": [
                {
                    "band": "oa_fmask",
                    "enum": 0,
                    "invert": True,
                },
                {
                    "band": "oa_fmask",
                    "enum": 2,
                    "invert": True,
                },
                {
                    "band": "oa_fmask",
                    "enum": 3,
                    "invert": True,
                },
                {
                    "band": "land",
                    "invert": True,
                    "enum": 1,
                },
            ],
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

style_c3_fmask = {
    "name": "fmask",
    "title": "Fmask Classification",
    "abstract": "Fmask (Function of mask) is used for automated clouds, cloud shadows, snow, and water masking for Landsats 4-8 and Sentinel 2 images.",
    "include_in_feature_info": False,
    "needed_bands": ["oa_fmask"],
    "value_map": {
        "fmask": [
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

# Styles grouping
styles_c3_ls_common = [
    style_c3_true_colour,
    style_c3_false_colour,
    style_c3_ndvi,
    style_c3_ndvi_anim,
    style_c3_ndwi,
    style_c3_mndwi,
    style_c3_nbr,
    style_c3_pure_blue,
    style_c3_pure_green,
    style_c3_pure_red,
    style_c3_pure_nir,
    style_c3_pure_swir1,
    style_c3_pure_swir2,
    style_c3_fmask,
]


styles_c3_ls_7 = styles_c3_ls_common.copy()
styles_c3_ls_7.append(style_c3_ls7_pure_panchromatic)

styles_c3_ls_8 = styles_c3_ls_common.copy()
styles_c3_ls_8.append(style_c3_ls8_pure_panchromatic)
styles_c3_ls_8.append(style_c3_pure_aerosol)
