legend_intertidal_percentage_by_20 = {
    "begin": "0.0",
    "end": "100",
    "decimal_places": 1,
    "ticks_every": "20",
    "units": "%",
    "tick_labels": {
        "0": {"label": "0"},
        "20": {"label": "20"},
        "40": {"label": "40"},
        "60": {"label": "60"},
        "80": {"label": "80"},
        "100": {"label": "100"},
    },
}

style_intertidal_elevation_meso = {
    "name": "intertidal_elevation_meso",
    "title": "Elevation (mesotidal)",
    "abstract": "Intertidal elevation in metres above Mean Sea Level",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["elevation"],
    "mpl_ramp": "viridis",
    "range": [-2.0, 1.0],
    "legend": {
        "begin": "-2.0",
        "end": "1.0",
        "ticks": ["-2.0", "-1.0", "0.0", "1.0"],
        "units": "metres above Mean Sea Level",
        "tick_labels": {
            "1.0": {"prefix": ">"},
            "-2.0": {"prefix": "<"},
        },
    },
}

style_intertidal_elevation_micro = {
    "name": "intertidal_elevation_micro",
    "title": "Elevation (microtidal)",
    "abstract": "Intertidal elevation in metres above Mean Sea Level",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["elevation"],
    "mpl_ramp": "viridis",
    "range": [-1.0, 0.5],
    "legend": {
        "begin": "-1.0",
        "end": "0.5",
        "ticks": ["-1.0", "-0.5", "0.0", "0.5"],
        "units": "metres above Mean Sea Level",
        "tick_labels": {
            "0.5": {"prefix": ">"},
            "-1.0": {"prefix": "<"},
        },
    },
}

style_intertidal_elevation_macro = {
    "name": "intertidal_elevation_macro",
    "title": "Elevation (macrotidal)",
    "abstract": "Intertidal elevation in metres above Mean Sea Level",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["elevation"],
    "mpl_ramp": "viridis",
    "range": [-4.0, 2.0],
    "legend": {
        "begin": "-4.0",
        "end": "2.0",
        "ticks": ["-4.0", "-2.0", "0.0", "2.0"],
        "units": "metres above Mean Sea Level",
        "tick_labels": {
            "2.0": {"prefix": ">"},
            "-4.0": {"prefix": "<"},
        },
    },
}

style_intertidal_elevation_uncertainty = {
    "name": "intertidal_elevation_uncertainty",
    "title": "Elevation uncertainty",
    "abstract": "Intertidal elevation uncertainty in metres",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation_uncertainty",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["elevation_uncertainty"],
    "mpl_ramp": "inferno",
    "range": [0.0, 1.0],
    "legend": {
        "begin": "0.0",
        "end": "1.0",
        "ticks": ["0.0", "0.5", "1.0"],
        "units": "metres",
        "tick_labels": {
            "1.0": {"prefix": ">"},
        },
    },
}

style_intertidal_exposure = {
    "name": "intertidal_exposure",
    "title": "Exposure",
    "abstract": "Intertidal exposure in percent of time exposed to air",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "exposure",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["exposure"],
    "color_ramp": [
        {"value": 0, "color": '#2f0f3d'},
        {'value': 10, 'color': '#4f1552'},
        {'value': 20, 'color': '#72195f'},
        {'value': 30, 'color': '#931f63'},
        {'value': 40, 'color': '#b32e5e'},
        {'value': 50, 'color': '#ce4356'},
        {'value': 60, 'color': '#e26152'},
        {'value': 70, 'color': '#ee845d'},
        {'value': 80, 'color': '#f5a672'},
        {'value': 90, 'color': '#faca8f'},
        {'value': 100, 'color': '#fdedb0'}
    ],
    "legend": legend_intertidal_percentage_by_20,
}

style_intertidal_elevation_adaptive = {
    "name": "intertidal_elevation_adaptive",
    "title": "Elevation",
    "abstract": "Intertidal elevation in metres above Mean Sea Level",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.elevation_adaptive",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
            "lot": "ta_lot",
            "hot": "ta_hot",
        },
    },
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "animate": False,
            "preserve_user_date_order": True,
            "pass_raw_data": True,
            "aggregator_function": {
                "function": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.multi_date_raw_elevation",
                "mapped_bands": True,
                "kwargs": {
                    "band": "elevation",
                }
            },
            "mpl_ramp": "RdBu",
            "range": [-0.5, 0.5],
            "legend": {
                "title": "Elevation change (metres)",
                "begin": "-0.5",
                "end": "0.5",
                "ticks": [
                    "-0.5",
                    "0.0",
                    "0.5",
                ]
            },
            "feature_info_label": "elevation_difference",
        },
    ],
    "include_in_feature_info": False,
    "needed_bands": ["elevation", "ta_lot", "ta_hot"],
    "mpl_ramp": "viridis",
    "range": [0.1, 0.7],
    "legend": {
        "begin": "0.1",
        "end": "0.7",
        "ticks": ["0.1", "0.7"],
        "units": "",
        "tick_labels": {
            "0.1": {"label": "Low"},
            "0.7": {"label": "High"},
        },
    },
}

style_intertidal_elevation_uncertainty_adaptive = {
    "name": "intertidal_elevation_uncertainty_adaptive",
    "title": "Elevation uncertainty",
    "abstract": "Intertidal elevation uncertainty",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.uncertainty_adaptive",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation_uncertainty",
            "lot": "ta_lot",
            "hot": "ta_hot",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["elevation_uncertainty", "ta_lot", "ta_hot"],
    "mpl_ramp": "inferno",
    "range": [0.0, 0.3],
    "legend": {
        "begin": "0.0",
        "end": "0.3",
        "ticks": ["0.0", "0.3"],
        "units": "",
        "tick_labels": {
            "0.0": {"label": "Low"},
            "0.3": {"label": "High"},
        },
    },
}

style_intertidal_extents = {
    "name": "intertidal_extents",
    "title": "Extents",
    "abstract": "Intertidal Extents classification",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.tide_graph_path",  # add custom metadata field
    },
    "needed_bands": ["extents"],
    "value_map": {
        "extents": [
            {
                "title": "Ocean and coastal waters",
                "abstract": "",
                "values": [1],
                "color": "#396dbf",
            },
            {
                "title": "Exposed intertidal (low confidence)",
                "abstract": "",
                "values": [2],
                "color": "#f5e167",
            },
            {
                "title": "Exposed intertidal (high confidence)",
                "abstract": "",
                "values": [3],
                "color": "#f5be3d",
            },
            {
                "title": "Inland waters",
                "abstract": "",
                "values": [4],
                "color": "#769bd6",
            },
            {
                "title": "Land",
                "abstract": "",
                "values": [5],
                "color": "#ffffff",
            },
        ]
    }
}

style_intertidal_corr = {
    "name": "intertidal_corr",
    "title": "NDWI tide correlation",
    "abstract": "Correlation between NDWI and tide height",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "qa_ndwi_corr",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["qa_ndwi_corr"],
    "mpl_ramp": "RdBu",
    "range": [-0.5, 0.5],
    "legend": {
        "begin": "-0.5",
        "end": "0.5",
        "ticks": ["-0.5", "0.0", "0.5"],
        "units": "correlation",
    },
}

style_intertidal_freq = {
    "name": "intertidal_freq",
    "title": "NDWI frequency",
    "abstract": "NDWI inundation frequency",
    "custom_includes": {
        "tide_graph_path": "ows_refactored.sea_ocean_coast.intertidal_c3.utils_intertidal.tide_graph_path",  # add custom metadata field
    },
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "qa_ndwi_freq",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["qa_ndwi_freq"],
    "mpl_ramp": "RdBu",
    "range": [0, 100],
    "legend": legend_intertidal_percentage_by_20,
}

style_count_clear = {
    "name": "count_clear",
    "title": "Clear observation count",
    "abstract": "Count of satellite observations included in DEA Intertidal",
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
    "range": [0, 400],
    "legend": {
        "begin": "0",
        "end": "400",
        "decimal_places": 0,
        "ticks_every": 50,
        "tick_labels": {
            "400": {"prefix": ">"},
        },
    },
}

# Create combined list that is imported and passed to the layer
styles_intertidal_list = [
    style_intertidal_elevation_adaptive,
    style_intertidal_elevation_uncertainty_adaptive,
    style_intertidal_exposure,
    style_intertidal_elevation_micro,
    style_intertidal_elevation_meso,
    style_intertidal_elevation_macro,
    style_intertidal_elevation_uncertainty,
    style_intertidal_extents,
    style_intertidal_corr,
    style_intertidal_freq,
    style_count_clear,
]
