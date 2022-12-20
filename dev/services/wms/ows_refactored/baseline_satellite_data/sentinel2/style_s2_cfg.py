import copy

from ows_refactored.baseline_satellite_data.sentinel2.style_s2_pure_cfg import (
    style_s2_pure_aerosol, style_s2_pure_blue, style_s2_pure_green,
    style_s2_pure_narrow_nir, style_s2_pure_nir, style_s2_pure_red,
    style_s2_pure_redge_1, style_s2_pure_redge_2, style_s2_pure_redge_3,
    style_s2_pure_swir1, style_s2_pure_swir2)
from ows_refactored.ows_legend_cfg import legend_idx_0_1_5ticks

s2_cloudless_mask = [
    {
        "band": "oa_s2cloudless_mask",
        "values": [0, 2, 3],
        "invert": True,
    },
    {
        "band": "land",
        "invert": True,
        "values": [1],
    }
]

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
    "title": "Normalised Difference Vegetation Index - Red, NIR",
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
    "pq_masks": s2_cloudless_mask,
    "legend": legend_idx_0_1_5ticks,
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "preserve_user_date_order": True,
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "pq_masks": s2_cloudless_mask,
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
    "title": "Normalised Difference Water Index - Green, NIR",
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
    "pq_masks": s2_cloudless_mask,
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
            "preserve_user_date_order": True,
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "pq_masks": s2_cloudless_mask,
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
    "title": "Modified Normalised Difference Water Index - Green, SWIR",
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
    "pq_masks": s2_cloudless_mask,
    "legend": legend_idx_0_1_5ticks,
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "preserve_user_date_order": True,
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta"
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "pq_masks": s2_cloudless_mask,
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
    "title": "Normalised Difference Chlorophyll Index - Red Edge, Red",
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
    "title": "Normalised Burn Ratio - NIR, SWIR",
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
    "pq_masks": s2_cloudless_mask,
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
                {"value": -0.5, "color": "#768642"},
                {
                    "value": -0.25,
                    "color": "#768642",
                    "alpha": 1.0,
                },
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

fmask_bits = [
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

s2cloudless_mask_bits = [
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
]

style_s2_fmask = {
    "name": "fmask",
    "title": "Fmask Classification",
    "abstract": "Fmask (Function of mask) is used for automated clouds, cloud shadows, snow, and water masking for Landsats 4-8 and Sentinel 2 images.",
    "include_in_feature_info": False,
    "needed_bands": ["fmask"],
    "value_map": {
        "fmask": fmask_bits
    }
}

style_s2_cloudless_mask = {
    "name": "s2cloudless_mask",
    "title": "S2 Cloudless Mask Classification",
    "abstract": "S2 Cloudless Mask is used for automated cloud masking Sentinel 2 images.",
    "include_in_feature_info": False,
    "needed_bands": ["s2cloudless_mask"],
    "value_map": {
        "s2cloudless_mask": s2cloudless_mask_bits
    }
}

style_s2_cloudless_prob = {
    "name": "s2cloudless_prob",
    "title": "S2 Cloudless Mask Probability",
    "abstract": "S2 Cloudless Probabilities given for s2cloudless_mask classification",
    "include_in_feature_info": False,
    "needed_bands": ["s2cloudless_prob"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "s2cloudless_prob"},
    },
    "mpl_ramp": "inferno",
    "range": [0.0, 1.0]
}

styles_s2_list = [
    style_s2_simple_rgb,
    style_s2_irg,
    style_s2_ndvi,
    style_s2_ndwi,
    style_s2_mndwi,
    style_s2_ndci,
    style_s2_nbr,
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
    style_s2_fmask,
    style_s2_cloudless_mask,
    style_s2_cloudless_prob,
]