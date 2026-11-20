style_s1_nrb_hh = {
    "name": "hh_linear",
    "title": "HH Gamma0 (Linear)",
    "abstract": "Backscatter HH Gamma0 (Linear)",
    "index_expression": "hh_gamma0",
    "mpl_ramp": "bone",
    "range": [0.001, 2.3],  # 2% - 99.9%
}

style_s1_nrb_hv = {
    "name": "hv_linear",
    "title": "HV Gamma0 (Linear)",
    "abstract": "Backscatter HV Gamma0 (Linear)",
    "index_expression": "hv_gamma0",
    "mpl_ramp": "bone",
    "range": [0.0001, 0.78],  # 2% - 99.9%
}

style_s1_nrb_hh_db = {
    "name": "hh_db",
    "title": "HH Gamma0 (dB)",
    "abstract": "Backscatter HH Gamma0 (dB)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
        "kwargs": {
            "band": "hh_gamma0",
        },
    },
    "mpl_ramp": "bone",
    "range": [-27.21538734, 3.62868977],  # 2% - 99.9%
    "needed_bands": ["hh_gamma0"],
}

style_s1_nrb_hv_db = {
    "name": "hv_db",
    "title": "HV Gamma0 (dB)",
    "abstract": "Backscatter HV Gamma0 (dB)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
        "kwargs": {
            "band": "hv_gamma0",
        },
    },
    "mpl_ramp": "bone",
    "range": [-38.688, -1.09818748],  # 2% - 99.9%
    "needed_bands": ["hv_gamma0"],
}

style_s1_nrb_hh_sigma = {
    "name": "hh_sigma",
    "title": "HH Sigma0-ellipsoid (Linear)",
    "abstract": "Backscatter HH Sigma0-ellipsoid (Linear)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sigma0_ellipsoid",
        "kwargs": {
            "gamma": "hh_gamma0",
            "gamma_to_beta": "gamma0_to_beta0_ratio",
            "incidence_angle": "incidence_angle",
        },
    },
    "mpl_ramp": "bone",
    "range": [-27.21538734, 3.62868977],  # 2% - 99.9%
    "needed_bands": ["hh_gamma0", "gamma0_to_beta0_ratio", "incidence_angle"],
}

style_s1_nrb_hv_sigma = {
    "name": "hv_sigma",
    "title": "HV Sigma0-ellipsoid (Linear)",
    "abstract": "Backscatter HV Sigma0-ellipsoid (Linear)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sigma0_ellipsoid",
        "kwargs": {
            "gamma": "hv_gamma0",
            "gamma_to_beta": "gamma0_to_beta0_ratio",
            "incidence_angle": "incidence_angle",
        },
    },
    "mpl_ramp": "bone",
    "range": [-38.688, -1.09818748],  # 2% - 99.9%
    "needed_bands": ["hv_gamma0", "gamma0_to_beta0_ratio", "incidence_angle"],
}

style_s1_nrb_hh_sigma_db = {
    "name": "hh_sigma_db",
    "title": "HH Sigma0-ellipsoid (dB)",
    "abstract": "Backscatter HH Sigma0-ellipsoid (dB)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sigma0_ellipsoid_db",
        "kwargs": {
            "gamma": "hh_gamma0",
            "gamma_to_beta": "gamma0_to_beta0_ratio",
            "incidence_angle": "incidence_angle",
        },
    },
    "mpl_ramp": "bone",
    "range": [-27.21538734, 3.62868977],  # 2% - 99.9%
    "needed_bands": ["hh_gamma0", "gamma0_to_beta0_ratio", "incidence_angle"],
}

style_s1_nrb_hv_sigma_db = {
    "name": "hv_sigma_db",
    "title": "HV Sigma0-ellipsoid (dB)",
    "abstract": "Backscatter HV Sigma0-ellipsoid (dB)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sigma0_ellipsoid_db",
        "kwargs": {
            "gamma": "hv_gamma0",
            "gamma_to_beta": "gamma0_to_beta0_ratio",
            "incidence_angle": "incidence_angle",
        },
    },
    "mpl_ramp": "bone",
    "range": [-38.688, -1.09818748],  # 2% - 99.9%
    "needed_bands": ["hv_gamma0", "gamma0_to_beta0_ratio", "incidence_angle"],
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_hh_hv_false_colour_linear = {
    "name": "hh_hv_false_colour_linear",
    "title": "HH+HV False Colour (Linear)",
    "abstract": "HH+HV False Colour (Linear)",
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
                "scale_from": (-27.21538734, 3.62868977),  # 2% - 99.9%
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
    "title": "Backscatter VV (Linear)",
    "abstract": "Backscatter VV (Linear)",
    "index_expression": "vv_gamma0",
    "mpl_ramp": "viridis",
    "range": [0.00978187, 0.16764995],
}

# Scale range is p5 and p90 of samples across Australia.
style_s1_nrb_vh = {
    "name": "vh_linear",
    "title": "Backscatter VH (Linear)",
    "abstract": "Backscatter VH (Linear)",
    "index_expression": "vh_gamma0",
    "mpl_ramp": "viridis",
    "range": [0.00096179, 0.03024042],
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_vv_db = {
    "name": "vv_db",
    "title": "Backscatter VV (dB)",
    "abstract": "Backscatter VV (dB)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
        "kwargs": {
            "band": "vv_gamma0",
        },
    },
    "mpl_ramp": "viridis",
    "range": [-20.09524918, -5.6233408],  # 5% - 99%
    "needed_bands": ["vv_gamma0"],
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_vh_db = {
    "name": "vh_db",
    "title": "Backscatter VH (dB)",
    "abstract": "Backscatter VH (dB)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.db",
        "kwargs": {
            "band": "vh_gamma0",
        },
    },
    "mpl_ramp": "viridis",
    "range": [-30.15318871, -11.6874733],  # 5% - 99%
    "needed_bands": ["vh_gamma0"],
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_vv_sigma = {
    "name": "vv_sigma",
    "title": "VV Sigma0-ellipsoid (Linear)",
    "abstract": "Backscatter VV Sigma0-ellipsoid (Linear)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sigma0_ellipsoid",
        "kwargs": {
            "gamma": "vv_gamma0",
            "gamma_to_beta": "gamma0_to_beta0_ratio",
            "incidence_angle": "incidence_angle",
        },
    },
    "mpl_ramp": "viridis",
    "range": [-20.09524918, -5.6233408],  # 5% - 99%
    "needed_bands": ["vv_gamma0", "gamma0_to_beta0_ratio", "incidence_angle"],
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_vh_sigma = {
    "name": "vh_sigma",
    "title": "VH Sigma0-ellipsoid (Linear)",
    "abstract": "Backscatter VH Sigma0-ellipsoid (Linear)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sigma0_ellipsoid",
        "kwargs": {
            "gamma": "vh_gamma0",
            "gamma_to_beta": "gamma0_to_beta0_ratio",
            "incidence_angle": "incidence_angle",
        },
    },
    "mpl_ramp": "viridis",
    "range": [-30.15318871, -11.6874733],  # 5% - 99%
    "needed_bands": ["vh_gamma0", "gamma0_to_beta0_ratio", "incidence_angle"],
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_vv_sigma_db = {
    "name": "vv_sigma_db",
    "title": "VV Sigma0-ellipsoid (dB)",
    "abstract": "Backscatter VV Sigma0-ellipsoid (dB)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sigma0_ellipsoid_db",
        "kwargs": {
            "gamma": "vv_gamma0",
            "gamma_to_beta": "gamma0_to_beta0_ratio",
            "incidence_angle": "incidence_angle",
        },
    },
    "mpl_ramp": "viridis",
    "range": [-20.09524918, -5.6233408],  # 5% - 99%
    "needed_bands": ["vv_gamma0", "gamma0_to_beta0_ratio", "incidence_angle"],
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_vh_sigma_db = {
    "name": "vh_sigma_db",
    "title": "VH Sigma0-ellipsoid (dB)",
    "abstract": "Backscatter VH Sigma0-ellipsoid (dB)",
    "index_function": {
        "function": "ows_refactored.baseline_satellite_data.sentinel1.style_s1_functions.sigma0_ellipsoid_db",
        "kwargs": {
            "gamma": "vh_gamma0",
            "gamma_to_beta": "gamma0_to_beta0_ratio",
            "incidence_angle": "incidence_angle",
        },
    },
    "mpl_ramp": "viridis",
    "range": [-30.15318871, -11.6874733],  # 5% - 99%
    "needed_bands": ["vh_gamma0", "gamma0_to_beta0_ratio", "incidence_angle"],
}

# Scale range is p5 and p99 of samples across Australia.
style_s1_nrb_false_colour_linear = {
    "name": "vv_vh_false_colour_linear",
    "title": "VV+VH False Colour (Linear)",
    "abstract": "VV+VH False Colour (Linear)",
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
        "red": {"oa_layover_shadow_mask": 1},
        "green": {"oa_layover_shadow_mask": 1},
        "blue": {"oa_layover_shadow_mask": 1},
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
    style_s1_nrb_vv_sigma,
    style_s1_nrb_vh_sigma,
    style_s1_nrb_vv_sigma_db,
    style_s1_nrb_vh_sigma_db,
    style_s1_nrb_false_colour_linear,
    style_s1_nrb_false_colour_db,
    style_s1_nrb_mask,
]


styles_s1_nrb_vv_list = [
    style_s1_nrb_vv,
    style_s1_nrb_vv_db,
    style_s1_nrb_vv_sigma,
    style_s1_nrb_vv_sigma_db,
    style_s1_nrb_mask,
]

styles_s1_nrb_hh_hv_list = [
    style_s1_nrb_hh,
    style_s1_nrb_hv,
    style_s1_nrb_hh_db,
    style_s1_nrb_hv_db,
    style_s1_nrb_hh_sigma,
    style_s1_nrb_hv_sigma,
    style_s1_nrb_hh_sigma_db,
    style_s1_nrb_hv_sigma_db,
    style_s1_nrb_hh_hv_false_colour_linear,
    style_s1_nrb_hh_hv_false_colour_db,
    style_s1_nrb_hh_hv_sar_ice,
    style_s1_nrb_mask,
]

styles_s1_nrb_hh_list = [
    style_s1_nrb_hh,
    style_s1_nrb_hh_db,
    style_s1_nrb_hh_sigma,
    style_s1_nrb_hh_sigma_db,
    style_s1_nrb_mask,
]
