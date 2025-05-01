style_dem_greyscale = {
    "name": "dem_greyscale",
    "title": "Elevation",
    "abstract": "Elevation above sea level (m)",
    "needed_bands": ["dem"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "dem",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#383838", "alpha": 0.0},
        {"value": 0.1, "color": "#383838"},
        {"value": 125, "color": "#5e5e5e"},
        {"value": 250, "color": "#858585"},
        {"value": 500, "color": "#adadad"},
        {"value": 1000, "color": "#d4d4d4"},
        {"value": 2000, "color": "#fafafa"},
    ],
    "legend": {
        "title": "Elevation ",
        "begin": "0",
        "end": "2000",
        "ticks_every": 500,
        "units": "m",
        "tick_labels": {
            "2000": {"prefix": ">"},
        },
    },
}


# Create combined list that is imported and passed to the layer
styles_srtm_list = [
    style_dem_greyscale,
]