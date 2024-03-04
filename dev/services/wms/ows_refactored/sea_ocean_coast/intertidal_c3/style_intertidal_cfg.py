from ows_refactored.ows_legend_cfg import legend_idx_percentage_by_20


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
        "ticks": ["-2.0", "0.0", "1.0"],
        "units": "metres",
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
        "ticks": ["-4.0", "0.0", "2.0"],
        "units": "metres",
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
    "mpl_ramp": "magma",
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
    "mpl_ramp": "viridis",
    "range": [0, 100],
    "legend": legend_idx_percentage_by_20,
}


# Create combined list that is imported and passed to the layer
styles_intertidal_list = [
    style_intertidal_elevation,
    style_intertidal_elevation_macro,
    style_intertidal_elevation_uncertainty,
    style_intertidal_exposure,
]
