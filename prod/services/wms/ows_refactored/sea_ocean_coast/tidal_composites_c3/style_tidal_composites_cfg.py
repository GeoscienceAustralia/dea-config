style_low_true = {
    "name": "low_true",
    "title": "True colour – Low tide",
    "abstract": "Low tide true colour image, using the Red, Green and Blue bands",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.tide_graph_path",  # add custom metadata field
    },
    "components": {
        "red": {"low_red": 1.0},
        "green": {"low_green": 1.0},
        "blue": {"low_blue": 1.0},
    },
    "scale_range": [20.0, 2000.0],
}

style_high_true = {
    "name": "high_true",
    "title": "True colour – High tide",
    "abstract": "High tide true colour image, using the Red, Green and Blue bands",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.tide_graph_path",  # add custom metadata field
    },
    "components": {
        "red": {"high_red": 1.0},
        "green": {"high_green": 1.0},
        "blue": {"high_blue": 1.0},
    },
    "scale_range": [20.0, 2000.0],
}

style_low_false = {
    "name": "low_false",
    "title": "False colour – Low tide",
    "abstract": "Low tide false colour image, using the SWIR2, Green and Blue bands",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.tide_graph_path",  # add custom metadata field
    },
    "components": {
        "red": {"low_swir_2": 1.0},
        "green": {"low_nir_1": 1.0},
        "blue": {"low_green": 1.0},
    },
    "scale_range": [20.0, 3000.0],
}

style_high_false = {
    "name": "high_false",
    "title": "False colour – High tide",
    "abstract": "High tide false colour image, using the SWIR2, Green and Blue bands",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.tide_graph_path",  # add custom metadata field
    },
    "components": {
        "red": {"high_swir_2": 1.0},
        "green": {"high_nir_1": 1.0},
        "blue": {"high_green": 1.0},
    },
    "scale_range": [20.0, 3000.0],
}

style_low_mndwi = {
    "name": "low_mndwi",
    "title": "MNDWI – Low tide",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "low_green", "band2": "low_swir_2"},
    },
    "needed_bands": ["low_green", "low_swir_2"],
    "mpl_ramp": "RdBu",
    "range": [-0.75, 0.75],
    "legend": {
        "begin": "-1.0",
        "end": "1.0",
        "ticks_every": 0.5,
        "tick_labels": {
            "-1.0": {"label": "-1.0\n(dry)"},
            "1.0": {"label": "1.0\n(wet)"},
        },
    },
}

style_high_mndwi = {
    "name": "high_mndwi",
    "title": "MNDWI – High tide",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "high_green", "band2": "high_swir_2"},
    },
    "needed_bands": ["high_green", "high_swir_2"],
    "mpl_ramp": "RdBu",
    "range": [-0.75, 0.75],
    "legend": {
        "begin": "-1.0",
        "end": "1.0",
        "ticks_every": 0.5,
        "tick_labels": {
            "-1.0": {"label": "-1.0\n(dry)"},
            "1.0": {"label": "1.0\n(wet)"},
        },
    },
}

style_count_clear = {
    "name": "count_clear",
    "title": "Clear observation count",
    "abstract": "Count of satellite observations included in tidal composites",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "qa_count_clear",
        },
    },
    "needed_bands": ["qa_count_clear"],
    "include_in_feature_info": True,
    "mpl_ramp": "YlOrRd_r",
    "range": [0, 30],
    "legend": {
        "begin": "0",
        "end": "30",
        "decimal_places": 0,
        "ticks_every": 5,
        "tick_labels": {
            "30": {"prefix": ">"},
        },
    },
}

style_low_true_log = {
    "name": "low_true_log",
    "title": "True colour – Low tide (experimental)",
    "abstract": "Low tide true colour image, using the red, green and blue bands",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.tide_graph_path",  # add custom metadata field
    },
    "additional_bands": ["low_red", "low_green", "low_blue"],
    "components": {
        "red": {
            "function": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.log_scaling",
            "kwargs": {
                "band": "low_red",
                "scale_from": (5.5, 7.8),
                "scale_to": (0, 255)
            }
        },
        "green": {
            "function": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.log_scaling",
            "kwargs": {
                "band": "low_green",
                "scale_from": (5.5, 7.8),
                "scale_to": (0, 255)
            }
        },
        "blue": {
            "function": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.log_scaling",
            "kwargs": {
                "band": "low_blue",
                "scale_from": (5.5, 7.8),
                "scale_to": (0, 255)
            }
        },
    },
}

style_high_true_log = {
    "name": "high_true_log",
    "title": "True colour – High tide (experimental)",
    "abstract": "High tide true colour image, using the red, green and blue bands",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.tide_graph_path",  # add custom metadata field
    },
    "additional_bands": ["high_red", "high_green", "high_blue"],
    "components": {
        "red": {
            "function": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.log_scaling",
            "kwargs": {
                "band": "high_red",
                "scale_from": (5.5, 7.8),
                "scale_to": (0, 255)
            }
        },
        "green": {
            "function": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.log_scaling",
            "kwargs": {
                "band": "high_green",
                "scale_from": (5.5, 7.8),
                "scale_to": (0, 255)
            }
        },
        "blue": {
            "function": "ows_refactored.sea_ocean_coast.tidal_composites_c3.utils_tidal_composites.log_scaling",
            "kwargs": {
                "band": "high_blue",
                "scale_from": (5.5, 7.8),
                "scale_to": (0, 255)
            }
        },
    },
}

# Create combined list that is imported and passed to the layer
styles_tidal_composites_list = [
    style_low_true,
    style_high_true,
    style_low_false,
    style_high_false,
    style_low_mndwi,
    style_high_mndwi,
    style_count_clear,
]
