from ows_refactored.ows_reslim_cfg import reslim_standard

# bands definition
bands_stacking = {
    "uncertainty": []
}

style_stacking = {
    "name": "stacking_burnt_area",
    "title": "Stacking Burnt Area",
    "abstract": "burnt area as detected by the Stacking method",
    "needed_bands": ["uncertainty"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "uncertainty"}
    },
    "value_map": {
        "uncertainty": [
            {
                "title": "",
                "abstract": "",
                "values": [0.0],
                "color": "#ffffff",
                "alpha": 0.0,
            },
            {
                "title": "Any",
                "abstract": "",
                "values": [0.33],
                "color": "#ffd966",
            },
            {
                "title": "Majority",
                "abstract": "",
                "values": [0.66],
                "color": "#f09c43",
            },
            {
                "title": "All",
                "abstract": "",
                "values": [1],
                "color": "#d53a3a",
            },
        ]
    },
    "legend": {},
}

layers = {
    "title": "Stacking Burnt Area",
    "name": "ga_burn_mapping_stacking",
    "abstract": """Stacking Burnt Area, 2023-2024 Financial Year, 30m, 0.0.0 (Landsat, Collection 3)""",
    "product_name": "ga_ls8c_nbart_burn_mapping_fyear_3",
    "bands": bands_stacking,
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "time_resolution": "summary",
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
    },
    "styling": {
        "default_style": "stacking_burnt_area",
        "styles": [
            style_stacking
        ],
    },
}
