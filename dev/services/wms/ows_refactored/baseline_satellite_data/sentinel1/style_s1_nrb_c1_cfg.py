style_s1_nrb_hh = {
    "name": "hh_linear",
    "title": "Backscatter HH",
    "abstract": "Backscatter HH",
    "index_expression": "hh_gamma0",
    "mpl_ramp": "bone",
    "scale_range": [0.001, 2.3],  # 2% - 99.9%
}

style_s1_nrb_hv = {
    "name": "hv_linear",
    "title": "Backscatter HV",
    "abstract": "Backscatter HV",
    "index_expression": "hv_gamma0",
    "mpl_ramp": "bone",
    "scale_range": [0.0001, 0.78],  # 2% - 99.9%
}

style_s1_nrb_hh_db = {
    "name": "hh_db",
    "title": "Backscatter HH (dB)",
    "abstract": "Backscatter HH (dB)",
    "index_function": {
        "function": "s1_style_functions.db",
        "kwargs": {
            "band": "hh_gamma0",
            "scale_from": (-27.21538734, 3.62868977),  # 2% - 99.9%
            "scale_to": (0, 255),
        },
    },
    "mpl_ramp": "bone",
    "range": [0, 255],
    "needed_bands": ["hh_gamma0"],
}

style_s1_nrb_hv_db = {
    "name": "hv_db",
    "title": "Backscatter HV (dB)",
    "abstract": "Backscatter HV (dB)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
        "kwargs": {
            "band": "hv_gamma0",
            "scale_from": (-38.688, -1.09818748),  # 2% - 99.9%
            "scale_to": (0, 255),
        },
    },
    "mpl_ramp": "gray",
    "range": [0, 255],
    "needed_bands": ["hv_gamma0"],
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
            "scale_range": [0.00189175, 2.30599523],  # 2% - 99.9%
        },
        "green": {
            "hv_gamma0": 1.0,
            "scale_range": [0.00013038, 0.77636848],  # 2% - 99.9%
        },
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {
                "band1": "hh_gamma0",
                "band2": "hv_gamma0",
                "scale_from": [0.0425341308, 10773.0266],  # 2% - 99.9%
            },
        },
    },
}

# TODO: Get scale range is p5 and p99 of samples across Antarctica/Australia.
style_s1_nrb_hh_hv_false_colour_db = {
    "name": "hh_hv_false_colour_db",
    "title": "HH+HV False Colour (dB)",
    "abstract": "HH+HV False Colour (dB)",
    "additional_bands": ["hh_gamma0", "hv_gamma0"],
    "components": {
        "red": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hh_gamma0",
                "scale_from": ( -27.21538734, 3.62868977),  # 2% - 99.9%
            },
        },
        "green": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
            "kwargs": {
                "band": "hv_gamma0",
                "scale_from": (-38.688, -1.09818748),  # 2% - 99.9%
            },
        },
        "blue": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db_difference",
            "kwargs": {
                "band1": "hh_gamma0",
                "band2": "hv_gamma0",
                "scale_from": (-13.70164358, 40.32355998),  # 2% - 99.9%
            },
        },
    },
}

style_s1_nrb_hh_hv_sar_ice = {
    "name": "hh_hv_sar_ice",
    "title": "HH+HV SAR-Ice",
    "abstract": "HH+HV Sea Ice Composite",
    "additional_bands": ["hh_gamma0", "hv_gamma0"],
    "components": {
        "red": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sar_ice_square_root_stretch",
            "kwargs": {
                "band": "hv_gamma0",
                "min_val": 0.02,
                "max_val": 0.1,
                "gamma": 1.0
            }
        },
        "green": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sar_ice_overlay",
            "kwargs": {
                "band1": "hh_gamma0",
                "band2": "hv_gamma0",
                "min_val": 0.0,
                "max_val": 0.06,
                "gamma": 1.0
            },
        },
        "blue": {
            "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sar_ice_square_root_stretch",
            "kwargs": {
                "band": "hh_gamma0",
                "min_val": 0.0,
                "max_val": 0.32,
                "gamma": 1.0
            }
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
    "pq_masks": [
        {
            "band": "mask",
            "values": [255],
            "invert": True,
        }
    ],
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
    style_s1_nrb_hh_hv_false_colour_db,
    style_s1_nrb_hh_hv_sar_ice,
    style_s1_nrb_mask,
]

styles_s1_nrb_hh_list = [
    style_s1_nrb_hh,
    style_s1_nrb_hh_db,
    style_s1_nrb_mask,
]
