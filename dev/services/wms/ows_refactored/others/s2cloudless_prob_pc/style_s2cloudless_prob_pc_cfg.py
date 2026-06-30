style_s2cloudless_prob_pc_5 = {
    "name": "s2cloudless_prob_pc_5",
    "title": "s2cloudless_prob_pc_5",
    "abstract": "5th percentile of oa_s2cloudless_prob values",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "oa_s2cloudless_prob_pc_5",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["oa_s2cloudless_prob_pc_5"],
    "mpl_ramp": "inferno",
    "range": [0, 0.4],
}

style_s2cloudless_prob_pc_10 = {
    "name": "s2cloudless_prob_pc_10",
    "title": "s2cloudless_prob_pc_10",
    "abstract": "10th percentile of oa_s2cloudless_prob values",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "oa_s2cloudless_prob_pc_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["oa_s2cloudless_prob_pc_10"],
    "mpl_ramp": "inferno",
    "range": [0, 0.4],
}

style_s2cloudless_prob_pc_25 = {
    "name": "s2cloudless_prob_pc_25",
    "title": "s2cloudless_prob_pc_25",
    "abstract": "25th percentile of oa_s2cloudless_prob values",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "oa_s2cloudless_prob_pc_25",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["oa_s2cloudless_prob_pc_25"],
    "mpl_ramp": "inferno",
    "range": [0, 0.4],
}


# Create combined list that is imported and passed to the layer
styles_s2cloudless_prob_pc_list = [
    style_s2cloudless_prob_pc_5,
    style_s2cloudless_prob_pc_10,
    style_s2cloudless_prob_pc_25,
]
