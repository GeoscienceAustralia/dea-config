style_s1_nrb_HH = {
    "name": "HH",
    "title": "Backscatter HH",
    "abstract": "Backscatter HH",
    "components": {
        "red": {"HH": 1},
        "green": {"HH": 1},
        "blue": {"HH": 1},
    },
    "scale_range": [0.02, 0.4],
}

style_s1_nrb_VV = {
    "name": "VV",
    "title": "Backscatter VV",
    "abstract": "Backscatter VV",
    "components": {
        "red": {"VV_gamma0": 1},
        "green": {"VV_gamma0": 1},
        "blue": {"VV_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
}

# Scale range is p5 and p90 of samples across Australia, calculated in s1_stats.py.
# The scale range is set to these values to enhance the contrast of the images and make it easier to distinguish different features in the data.
# The scale range can be adjusted based on the specific use case and the desired level of detail in the images.
style_s1_nrb_false_colour_linear = {
    "name": "vv_vh_false_colour_linear",
    "title": "VV+VH False Colour",
    "abstract": "VV+VH False Colour",
    "additional_bands": ["VV_gamma0", "VH_gamma0"],
    "components": {
        "red": {
            "VV_gamma0": 1.0,
            "scale_range": [0.00978187, 0.12744568],
        },
        "green": {
            "VH_gamma0": 1.0,
            "scale_range": [0.00096179, 0.03024042],
        },
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {
                "band1": "VH_gamma0",
                "band2": "VV_gamma0",
                "scale_from": [0.01472214, 1.10262954],
            },
        },
    },
}

# scale range is p5 and p90 of samples across Australia.
style_s1_nrb_false_colour_db = {
    "name": "vv_vh_false_colour_db",
    "title": "VV+VH False Colour (dB)",
    "abstract": "VV+VH False Colour (dB)",
    "additional_bands": ["VV_gamma0", "VH_gamma0"],
    "components": {
        "red": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "VV_gamma0",
                "scale_from": (-20.09524918, -8.94672203),
            },
        },
        "green": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "VH_gamma0",
                "scale_from": (-30.15318871, -15.19352818),
            },
        },
        "blue": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db_difference",
            "kwargs": {
                "band1": "VH_gamma0",
                "band2": "VV_gamma0",
                "scale_from": (-18.30269623, 0.42520905),
            },
        },
    },
}

style_s1_nrb_mask = {
    "name": "mask",
    "title": "Shadow Layover Mask",
    "abstract": "Shadow Layover Mask",
    "components": {
        "red": {"mask": 1},
        "green": {"mask": 1},
        "blue": {"mask": 1},
    },
    "scale_range": [0, 3],
}


styles_s1_nrb_vvvh_list = [
    style_s1_nrb_VV,
    style_s1_nrb_mask,
    style_s1_nrb_false_colour_linear,
    style_s1_nrb_false_colour_db,
]
