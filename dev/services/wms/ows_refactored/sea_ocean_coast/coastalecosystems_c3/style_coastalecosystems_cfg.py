legend_coastalecosystems_percentage_by_20 = {
    "begin": "20",
    "end": "100",
    "decimal_places": 1,
    "ticks_every": "20",
    "units": "%",
    "tick_labels": {
        "20": {"label": "20"},
        "40": {"label": "40"},
        "60": {"label": "60"},
        "80": {"label": "80"},
        "100": {"label": "100"},
    },
}

style_coastalecosystems_mangrove_prob = {
    "name": "coastalecosystems_mangrove_prob",
    "title": "Mangrove Probability",
    "abstract": "Coastal Ecosystems Mangrove Probability as a percentage",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mangrove_prob",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["mangrove_prob"],
    "mpl_ramp": "inferno",
    "range": [20.0, 100],
    "legend": legend_coastalecosystems_percentage_by_20,
}

style_coastalecosystems_saltmarsh_prob = {
    "name": "coastalecosystems_saltmarsh_prob",
    "title": "Saltmarsh Probability",
    "abstract": "Coastal Ecosystems Saltmarsh Probability as a percentage",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "saltmarsh_prob",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["saltmarsh_prob"],
    "mpl_ramp": "inferno",
    "range": [20.0, 100],
    "legend": legend_coastalecosystems_percentage_by_20,
}

style_coastalecosystems_seagrass_prob = {
    "name": "coastalecosystems_seagrass_prob",
    "title": "Seagrass Probability",
    "abstract": "Coastal Ecosystems Seagrass Probability as a percentage",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "seagrass_prob",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["seagrass_prob"],
    "mpl_ramp": "inferno",
    "range": [0.0, 100],
    "legend": legend_coastalecosystems_percentage_by_20,
}

style_coastalecosystems_saltflat_prob = {
    "name": "coastalecosystems_saltflat_prob",
    "title": "Saltflat Probability",
    "abstract": "Coastal Ecosystems Saltflat Probability as a percentage",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "saltflat_prob",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["saltflat_prob"],
    "mpl_ramp": "inferno",
    "range": [20.0, 100],
    "legend": legend_coastalecosystems_percentage_by_20,
}

style_coastalecosystems_classification = {
    "name": "coastalecosystems_classification",
    "title": "Classification",
    "abstract": "Coastal Ecosystems classification",
    "needed_bands": ["classification"],
    "value_map": {
        "classification": [
            {
                "title": "Intertidal",
                "abstract": "",
                "values": [2],
                "color": "#823f4b",
            },
            {
                "title": "Mangroves",
                "abstract": "",
                "values": [3],
                "color": "#268f52",
            },
            {
                "title": "Saltmarsh",
                "abstract": "",
                "values": [4],
                "color": "#74bcfb",
            },
            {
                "title": "Intertidal Seagrass",
                "abstract": "",
                "values": [5],
                "color": "#3d4ca5",
            },
        ]
    }
}

style_coastalecosystems_count_clear = {
    "name": "coastalecosystems_count_clear",
    "title": "Clear observation count",
    "abstract": "Count of satellite observations included in DEA Coastal Ecosystems",
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
    "range": [0, 150],
    "legend": {
        "begin": "0",
        "end": "150",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "150": {"prefix": ">"},
        },
    },
}

# Create combined list that is imported and passed to the layer
styles_coastalecosystems_list = [
    style_coastalecosystems_classification,
    style_coastalecosystems_mangrove_prob,
    style_coastalecosystems_saltmarsh_prob,
    style_coastalecosystems_seagrass_prob,
    style_coastalecosystems_saltflat_prob,
    style_coastalecosystems_count_clear,
]
