from ows_refactored.ows_legend_cfg import legend_idx_0_1_5ticks

style_s2_simple_rgb = {
    "name": "simple_rgb",
    "title": "Simple RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {"red": {"red": 1.0}, "green": {"green": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [0.0, 3000.0],
}
style_s2_irg = {
    "name": "infrared_green",
    "title": "False colour - Green, SWIR, NIR",
    "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {"nbart_swir_2": 1.0},
        "green": {"nbart_nir_1": 1.0},
        "blue": {"nbart_green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_ndvi = {
    "name": "ndvi",
    "title": "NDVI - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nir", "band2": "red"},
    },
    "needed_bands": ["red", "nir"],
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
            "band": "fmask",
            "enum": 0,
            "invert": True,
        },
        {
            "band": "fmask",
            "enum": 2,
            "invert": True,
        },
        {
            "band": "fmask",
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
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "pq_masks": [
                {
                    "band": "fmask",
                    "enum": 0,
                    "invert": True,
                },
                {
                    "band": "fmask",
                    "enum": 2,
                    "invert": True,
                },
                {
                    "band": "fmask",
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
            "feature_info_label": "ndvi_delta",
        }
    ],
}

style_s2_ndwi = {
    "name": "ndwi",
    "title": "NDWI - Green, NIR",
    "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "green", "band2": "nir"},
    },
    "needed_bands": ["green", "nir"],
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
            "band": "fmask",
            "enum": 0,
            "invert": True,
        },
        {
            "band": "fmask",
            "enum": 2,
            "invert": True,
        },
        {
            "band": "fmask",
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
        "begin": "0.0",
        "end": "0.5",
        "decimal_places": 1,
        "ticks": ["0.0", "0.2", "0.4", "0.5"],
        "tick_labels": {
            "0.0": {"prefix": "<"},
            "0.2": {"label": "0.2"},
            "0.4": {"label": "0.4"},
            "0.5": {"prefix": ">"},
        }
    },
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "pq_masks": [
                {
                    "band": "fmask",
                    "enum": 0,
                    "invert": True,
                },
                {
                    "band": "fmask",
                    "enum": 2,
                    "invert": True,
                },
                {
                    "band": "fmask",
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
            "feature_info_label": "ndwi_delta",
        }
    ],
}
style_s2_mndwi = {
    # Cannot reuse landsat as we need swir_2 to landsat's swir_1
    "name": "mndwi",
    "title": "MNDWI - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_green", "band2": "nbart_swir_2"},
    },
    "needed_bands": ["nbart_green", "nbart_swir_2"],
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
            "band": "fmask",
            "enum": 0,
            "invert": True,
        },
        {
            "band": "fmask",
            "enum": 2,
            "invert": True,
        },
        {
            "band": "fmask",
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
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "pq_masks": [
                {
                    "band": "fmask",
                    "enum": 0,
                    "invert": True,
                },
                {
                    "band": "fmask",
                    "enum": 2,
                    "invert": True,
                },
                {
                    "band": "fmask",
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
            "feature_info_label": "mndwi_delta",
        }
    ],
}

style_s2_ndci = {
    "name": "ndci",
    "title": "NDCI - Red Edge, Red",
    "abstract": "Normalised Difference Chlorophyll Index - a derived index that correlates well with the existence of chlorophyll",
    "index_function": {
        "function": "datacube_ows.band_utils.sentinel2_ndci",
        "mapped_bands": True,
        "kwargs": {
            "b_red_edge": "nbart_red_edge_1",
            "b_red": "nbart_red",
            "b_green": "nbart_green",
            "b_swir": "nbart_swir_2",
        },
    },
    "needed_bands": ["nbart_red_edge_1", "nbart_red", "nbart_green", "nbart_swir_2"],
    "color_ramp": [
        {
            "value": -0.1,
            "color": "#1696FF",
        },
        {"value": -0.1, "color": "#1696FF"},
        {
            "value": 0.0,
            "color": "#00FFDF",
        },
        {
            "value": 0.1,
            "color": "#FFF50E",
        },
        {
            "value": 0.2,
            "color": "#FFB50A",
        },
        {
            "value": 0.4,
            "color": "#FF530D",
        },
        {
            "value": 0.5,
            "color": "#FF0000",
        },
    ],
    "legend": {
        "begin": "-0.1",
        "end": "0.5",
        "ticks_every": "0.1",
        "units": "unitless",
        "tick_labels": {"-0.1": {"prefix": "<"}, "0.5": {"prefix": ">"}},
    },
}

style_s2_nbr = {
    "name": "nbr",
    "title": "Normalised Burn Ratio",
    "abstract": "Normalised Burn Ratio - a derived index that that uses the differences in the way health green vegetation and burned vegetation reflect light to find burned area",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nbart_nir_1", "band2": "nbart_swir_3"},
    },
    "needed_bands": ["nbart_nir_1", "nbart_swir_3"],
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
            "band": "fmask",
            "enum": 0,
            "invert": True,
        },
        {
            "band": "fmask",
            "enum": 2,
            "invert": True,
        },
        {
            "band": "fmask",
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
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "preserve_user_date_order": True,
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "color_ramp": [
                {"value": -0.5, "color": "#768642", "alpha": 0.0},
                {"value": -0.5, "color": "#768642", "legend": {"label": "<-0.50"}},
                {
                    "value": -0.25,
                    "color": "#768642",
                    "alpha": 1.0,
                    "legend": {"label": "-0.25"},
                },
                {"value": -0.25, "color": "#a4bd5f"},
                {"value": -0.1, "color": "#a4bd5f", "legend": {"label": "-0.1"}},
                {"value": -0.1, "color": "#00e05d"},
                {"value": 0.1, "color": "#00e05d"},
                {"value": 0.1, "color": "#fdf950", "legend": {"label": "0.1"}},
                {"value": 0.27, "color": "#fdf950", "legend": {"label": "0.27"}},
                {"value": 0.27, "color": "#ffae52"},
                {"value": 0.44, "color": "#ffae52", "legend": {"label": "0.44"}},
                {"value": 0.44, "color": "#ff662e"},
                {"value": 0.66, "color": "#ff662e", "legend": {"label": "0.66"}},
                {"value": 0.66, "color": "#ad28cc"},
                {"value": 0.88, "color": "#ad28cc", "legend": {"label": ">1.30"}},
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

style_s2_pure_aerosol = {
    "name": "aerosol",
    "title": "Narrow Blue - 440",
    "abstract": "Coastal Aerosol or Narrow Blue band, approximately 435nm to 450nm",
    "components": {
        "red": {"coastal_aerosol": 1.0},
        "green": {"coastal_aerosol": 1.0},
        "blue": {"coastal_aerosol": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_blue = {
    "name": "blue",
    "title": "Blue - 490",
    "abstract": "Blue band, approximately 453nm to 511nm",
    "components": {"red": {"blue": 1.0}, "green": {"blue": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_s2_pure_green = {
    "name": "green",
    "title": "Green - 560",
    "abstract": "Green band, approximately 534nm to 588nm",
    "components": {
        "red": {"green": 1.0},
        "green": {"green": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_red = {
    "name": "red",
    "title": "Red - 670",
    "abstract": "Red band, roughly 637nm to 672nm",
    "components": {"red": {"red": 1.0}, "green": {"red": 1.0}, "blue": {"red": 1.0}},
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_redge_1 = {
    "name": "red_edge_1",
    "title": "Vegetation Red Edge - 710",
    "abstract": "Near infra-red band, centred on 710nm",
    "components": {
        "red": {"red_edge_1": 1.0},
        "green": {"red_edge_1": 1.0},
        "blue": {"red_edge_1": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_redge_2 = {
    "name": "red_edge_2",
    "title": "Vegetation Red Edge - 740",
    "abstract": "Near infra-red band, centred on 740nm",
    "components": {
        "red": {"red_edge_2": 1.0},
        "green": {"red_edge_2": 1.0},
        "blue": {"red_edge_2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_redge_3 = {
    "name": "red_edge_3",
    "title": "Vegetation Red Edge - 780",
    "abstract": "Near infra-red band, centred on 780nm",
    "components": {
        "red": {"red_edge_3": 1.0},
        "green": {"red_edge_3": 1.0},
        "blue": {"red_edge_3": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_nir = {
    "name": "nir",
    "title": "Near Infrared (NIR) - 840",
    "abstract": "Near infra-red band, roughly 853nm to 876nm",
    "components": {"red": {"nir": 1.0}, "green": {"nir": 1.0}, "blue": {"nir": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_s2_pure_narrow_nir = {
    "name": "narrow_nir",
    "title": "Narrow Near Infrared - 870",
    "abstract": "Near infra-red band, centred on 865nm",
    "components": {"red": {"nir": 1.0}, "green": {"nir": 1.0}, "blue": {"nir": 1.0}},
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_swir1 = {
    "name": "swir1",
    "title": "Shortwave Infrared (SWIR) - 1610",
    "abstract": "Short wave infra-red band 1, roughly 1575nm to 1647nm",
    "components": {
        "red": {"swir_2": 1.0},
        "green": {"swir_2": 1.0},
        "blue": {"swir_2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_swir2 = {
    "name": "swir2",
    "title": "Shortwave Infrared (SWIR) - 2190",
    "abstract": "Short wave infra-red band 2, roughly 2117nm to 2285nm",
    "components": {
        "red": {"swir_3": 1.0},
        "green": {"swir_3": 1.0},
        "blue": {"swir_3": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

bands_sentinel2_ard_nbar = {
    "nbar_coastal_aerosol": [
        "nbar_coastal_aerosol",
        "coastal_aerosol",
        "nbart_coastal_aerosol",
        "nbart_narrow_blue",
        "nbar_narrow_blue" "narrow_blue",
    ],
    "nbar_blue": ["nbar_blue", "blue", "nbart_blue"],
    "nbar_green": ["nbar_green", "green", "nbart_green"],
    "nbar_red": ["nbar_red", "red", "nbart_red"],
    "nbar_red_edge_1": ["nbar_red_edge_1", "red_edge_1", "nbart_red_edge_1"],
    "nbar_red_edge_2": ["nbar_red_edge_2", "red_edge_2", "nbart_red_edge_2"],
    "nbar_red_edge_3": ["nbar_red_edge_3", "red_edge_3", "nbart_red_edge_3"],
    "nbar_nir_1": ["nbar_nir_1", "nir", "nir_1", "nbart_nir_1"],
    "nbar_nir_2": ["nbar_nir_2", "nir2", "nbart_nir_2"],
    "nbar_swir_2": ["nbar_swir_2", "swir_2", "nbart_swir_2"],
    "nbar_swir_3": ["nbar_swir_3", "swir_3", "nbart_swir_3"],
}

bands_sentinel2 = {
    "nbar_coastal_aerosol": ["nbar_coastal_aerosol", "nbar_narrow_blue"],
    "nbar_blue": ["nbar_blue"],
    "nbar_green": ["nbar_green"],
    "nbar_red": ["nbar_red"],
    "nbar_red_edge_1": ["nbar_red_edge_1"],
    "nbar_red_edge_2": ["nbar_red_edge_2"],
    "nbar_red_edge_3": ["nbar_red_edge_3"],
    "nbar_nir_1": ["nbar_nir_1", "nbar_near_infrared_1"],
    "nbar_nir_2": ["nbar_nir_2", "nbar_near_infrared_2"],
    "nbar_swir_2": ["nbar_swir_2", "nbar_shortwave_infrared_2"],
    "nbar_swir_3": ["nbar_swir_3", "nbar_shortwave_infrared_3"],
    "nbart_coastal_aerosol": [
        "nbart_coastal_aerosol",
        "coastal_aerosol",
        "nbart_narrow_blue",
        "narrow_blue",
    ],
    "nbart_blue": ["nbart_blue", "blue"],
    "nbart_green": ["nbart_green", "green"],
    "nbart_red": ["nbart_red", "red"],
    "nbart_red_edge_1": ["nbart_red_edge_1", "red_edge_1"],
    "nbart_red_edge_2": ["nbart_red_edge_2", "red_edge_2"],
    "nbart_red_edge_3": ["nbart_red_edge_3", "red_edge_3"],
    "nbart_nir_1": ["nbart_nir_1", "nir", "nir_1", "nbart_near_infrared_1"],
    "nbart_nir_2": ["nbart_nir_2", "nir_2", "nbart_near_infrared_2"],
    "nbart_swir_2": ["nbart_swir_2", "swir_2", "nbart_shortwave_infrared_2"],
    "nbart_swir_3": ["nbart_swir_3", "swir_3", "nbart_shortwave_infrared_3"],
}


styles_s2_list = [
    style_s2_simple_rgb,
    style_s2_irg,
    style_s2_ndvi,
    style_s2_ndwi,
    style_s2_mndwi,
    style_s2_ndci,
    style_s2_pure_aerosol,
    style_s2_pure_blue,
    style_s2_pure_green,
    style_s2_pure_red,
    style_s2_pure_redge_1,
    style_s2_pure_redge_2,
    style_s2_pure_redge_3,
    style_s2_pure_nir,
    style_s2_pure_narrow_nir,
    style_s2_pure_swir1,
    style_s2_pure_swir2,
]

style_s2_nbr_list = styles_s2_list + [style_s2_nbr]
