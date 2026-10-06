style_s1_nrb_hh = {
    "name": "hh_linear",
    "title": "Backscatter HH",
    "abstract": "Backscatter HH",
    "components": {
        "red": {"hh_gamma0": 1},
        "green": {"hh_gamma0": 1},
        "blue": {"hh_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
}

style_s1_nrb_hv = {
    "name": "hv_linear",
    "title": "Backscatter HV",
    "abstract": "Backscatter HV",
    "components": {
        "red": {"hv_gamma0": 1},
        "green": {"hv_gamma0": 1},
        "blue": {"hv_gamma0": 1},
    },
    "scale_range": [0.02, 0.4],
}

# TODO: Get scale range is p5 and p99 of samples across Antarctica/Australia.
style_s1_nrb_hh_db = {
    "name": "hh_db",
    "title": "Backscatter HH (dB)",
    "abstract": "Backscatter HH (dB)",
    "additional_bands": ["hh_gamma0"],
    "components": {
        "red": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hh_gamma0",
                "scale_from": (-20.09524918, -5.6233408),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hh_gamma0",
                "scale_from": (-20.09524918, -5.6233408),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hh_gamma0",
                "scale_from": (-20.09524918, -5.6233408),
                "scale_to": (0, 255),
            },
        },
    },
}

# TODO: Get scale range is p5 and p99 of samples across Antarctica/Australia.
style_s1_nrb_hv_db = {
    "name": "hv_db",
    "title": "Backscatter HV (dB)",
    "abstract": "Backscatter HV (dB)",
    "additional_bands": ["hv_gamma0"],
    "components": {
        "red": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hv_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hv_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hv_gamma0",
                "scale_from": (-17, 6),
                "scale_to": (0, 255),
            },
        },
    },
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_hh_hv_false_colour_linear = {
    "name": "hh_hv_false_colour_linear",
    "title": "HH+HV False Colour",
    "abstract": "HH+HV False Colour",
    "additional_bands": ["hh_gamma0", "hv_gamma0"],
    "components": {
        "red": {
            "hh_gamma0": 1.0,
            "scale_range": [0.0, 0.28],
        },
        "green": {
            "hv_gamma0": 1.0,
            "scale_range": [0.0, 0.06],
        },
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {
                "band1": "hh_gamma0",
                "band2": "hv_gamma0",
                "scale_from": [0.0, 0.49],
            },
        },
    },
}

# TODO: Get scale range is p5 and p99 of samples across Antarctica/Australia.
style_s1_nrb_hh_hv_false_colour_blue_db = {
    "name": "hh_hv_false_colour_blue_db",
    "title": "HH+HV False Colour (dB) [blue=ratio]",
    "abstract": "HH+HV False Colour (dB)",
    "additional_bands": ["hh_gamma0", "hv_gamma0"],
    "components": {
        "red": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hh_gamma0",
                "scale_from": (-25, 5),
            },
        },
        "green": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hv_gamma0",
                "scale_from": (-35, -5),
            },
        },
        "blue": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db_difference",
            "kwargs": {
                "band1": "hh_gamma0",
                "band2": "hv_gamma0",
                "scale_from": (0.0, 15),
            },
        },
    },
}

# TODO: Get scale range is p5 and p99 of samples across Antarctica/Australia.
style_s1_nrb_hh_hv_false_colour_red_db = {
    "name": "hh_hv_false_colour_red_db",
    "title": "HH+HV False Colour (dB) [red=ratio]",
    "abstract": "HH+HV False Colour (dB)",
    "additional_bands": ["hh_gamma0", "hv_gamma0"],
    "components": {
        "red": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db_difference",
            "kwargs": {
                "band1": "hh_gamma0",
                "band2": "hv_gamma0",
                "scale_from": (0.0, 15),
            },
        },
        "green": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hv_gamma0",
                "scale_from": (-25, 5),
            },
        },
        "blue": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hh_gamma0",
                "scale_from": (-35, -5),
            },
        },
    },
}

# Scale range is p5 and p95 of samples across Australia.
# The scale range is set to these values to enhance the contrast of the images and make it easier to distinguish different features in the data.
# The scale range can be adjusted based on the specific use case and the desired level of detail in the images.
style_s1_nrb_vv = {
    "name": "vv_linear",
    "title": "Backscatter VV",
    "abstract": "Backscatter VV",
    "components": {
        "red": {"vv_gamma0": 1},
        "green": {"vv_gamma0": 1},
        "blue": {"vv_gamma0": 1},
    },
    "scale_range": [0.00978187, 0.16764995],
}

# Scale range is p5 and p90 of samples across Australia.
style_s1_nrb_vh = {
    "name": "vh_linear",
    "title": "Backscatter VH",
    "abstract": "Backscatter VH",
    "components": {
        "red": {"vh_gamma0": 1},
        "green": {"vh_gamma0": 1},
        "blue": {"vh_gamma0": 1},
    },
    "scale_range": [0.00096179, 0.03024042],
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_vv_db = {
    "name": "vv_db",
    "title": "Backscatter VV (dB)",
    "abstract": "Backscatter VV (dB)",
    "additional_bands": ["vv_gamma0"],
    "components": {
        "red": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "vv_gamma0",
                "scale_from": (-20.09524918, -5.6233408),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "vv_gamma0",
                "scale_from": (-20.09524918, -5.6233408),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "vv_gamma0",
                "scale_from": (-20.09524918, -5.6233408),
                "scale_to": (0, 255),
            },
        },
    },
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_vh_db = {
    "name": "vh_db",
    "title": "Backscatter VH (dB)",
    "abstract": "Backscatter VH (dB)",
    "additional_bands": ["vh_gamma0"],
    "components": {
        "red": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "vh_gamma0",
                "scale_from": (-30.15318871, -11.6874733),
                "scale_to": (0, 255),
            },
        },
        "blue": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "vh_gamma0",
                "scale_from": (-30.15318871, -11.6874733),
                "scale_to": (0, 255),
            },
        },
        "green": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "vh_gamma0",
                "scale_from": (-30.15318871, -11.6874733),
                "scale_to": (0, 255),
            },
        },
    },
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_false_colour_linear = {
    "name": "vv_vh_false_colour_linear",
    "title": "VV+VH False Colour",
    "abstract": "VV+VH False Colour",
    "additional_bands": ["vv_gamma0", "vh_gamma0"],
    "components": {
        "red": {
            "vv_gamma0": 1.0,
            "scale_range": [0.00978187, 0.2739456],
        },
        "green": {
            "vh_gamma0": 1.0,
            "scale_range": [0.00096179, 0.06779868],
        },
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {
                "band1": "vh_gamma0",
                "band2": "vv_gamma0",
                "scale_from": [0.01472214, 4.3769968],
            },
        },
    },
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_false_colour_db = {
    "name": "vv_vh_false_colour_db",
    "title": "VV+VH False Colour (dB)",
    "abstract": "VV+VH False Colour (dB)",
    "additional_bands": ["vv_gamma0", "vh_gamma0"],
    "components": {
        "red": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "vv_gamma0",
                "scale_from": (-20.09524918, -5.6233408),
            },
        },
        "green": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "vh_gamma0",
                "scale_from": (-30.15318871, -11.6874733),
            },
        },
        "blue": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db_difference",
            "kwargs": {
                "band1": "vh_gamma0",
                "band2": "vv_gamma0",
                "scale_from": (-18.30269623, 6.41235924),
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


styles_s1_nrb_vv_vh_list = [
    style_s1_nrb_vv,
    style_s1_nrb_vh,
    style_s1_nrb_vv_db,
    style_s1_nrb_vh_db,
    style_s1_nrb_false_colour_linear,
    style_s1_nrb_false_colour_db,
    style_s1_nrb_mask,
]


styles_s1_nrb_vv_list = [
    style_s1_nrb_vv,
    style_s1_nrb_vv_db,
    style_s1_nrb_mask,
]

styles_s1_nrb_hh_hv_list = [
    style_s1_nrb_hh,
    style_s1_nrb_hv,
    style_s1_nrb_hh_db,
    style_s1_nrb_hv_db,
    style_s1_nrb_hh_hv_false_colour_linear,
    style_s1_nrb_hh_hv_false_colour_blue_db,
    style_s1_nrb_hh_hv_false_colour_red_db,
    style_s1_nrb_mask,
]

styles_s1_nrb_hh_list = [
    style_s1_nrb_hh,
    style_s1_nrb_hh_db,
    style_s1_nrb_mask,
]
