from datacube_ows.band_utils import scalable


@scalable
def elevation_adaptive(data, band, lot, hot, band_mapper=None):
    """
    Experimental adaptive elevation function, using pixel-level
    tide metadata to calculate relative elevation for any
    given location.

    This implementation should be free of any tile-based
    discontinuities in the resulting visualisation.

    # TODO: Add hillshading
    """

    # Calculate observed tide range (max - min)
    otr = data[hot] - data[lot]

    # Calculate distance between elevation and minumum
    # observed tide height
    distance_to_min = data[band] - data[lot]

    # Calculate proportion along observed tide range
    proportion_array = distance_to_min / otr

    return proportion_array


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

style_intertidal_elevation = {
    "name": "intertidal_elevation",
    "title": "Elevation",
    "abstract": "Intertidal elevation in metres above Mean Sea Level",
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

style_intertidal_elevation_macro = {
    "name": "intertidal_elevation_macro",
    "title": "Elevation (macrotidal style)",
    "abstract": "Intertidal elevation in metres above Mean Sea Level",
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

style_intertidal_extents = {
    "name": "intertidal_extents",
    "title": "Extents",
    "abstract": "Intertidal Extents classification",
    "needed_bands": ["extents"],
    "value_map": {
        "extents": [
            {
                "title": "Dry",
                "abstract": "",
                "values": [0],
                "color": "#dddddd",
            },
            {
                "title": "Inland intermittent wet",
                "abstract": "",
                "values": [1],
                "color": "#00a7c8",
            },
            {
                "title": "Inland persistent wet",
                "abstract": "",
                "values": [2],
                "color": "#00667a",
            },
            {
                "title": "Tidally influenced wet",
                "abstract": "",
                "values": [3],
                "color": "#2a5fa1",
            },
            {
                "title": "Intertidal (low confidence)",
                "abstract": "",
                "values": [4],
                "color": "#ffe8a1",
            },
            {
                "title": "Intertidal (high confidence)",
                "abstract": "",
                "values": [5],
                "color": "#ffc001",
            },
        ]
    }
}

style_intertidal_elevation_adaptive = {
    "name": "intertidal_elevation_adaptive",
    "title": "Elevation",
    "abstract": "Intertidal elevation in metres above Mean Sea Level",
    "index_function": {
        "function": elevation_adaptive,
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
            "lot": "ta_lot",
            "hot": "ta_hot",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["elevation"],
    "mpl_ramp": "viridis",
    "range": [0.05, 0.7],
    "legend": {
        "begin": "0.0",
        "end": "1.0",
        "ticks": ["0.0", "0.5", "1.0"],
        "units": "",
        "tick_labels": {
            "0.0": {"label": "Low"},
            "0.5": {"label": ""},
            "1.0": {"label": "High"},
        },
    },
}

# Create combined list that is imported and passed to the layer
styles_intertidal_list = [
    style_intertidal_elevation,
    style_intertidal_elevation_macro,
    style_intertidal_elevation_adaptive,
    style_intertidal_elevation_uncertainty,
    style_intertidal_exposure,
    style_intertidal_extents,
]
