from ows_refactored.ows_reslim_cfg import reslim_standard

# bands definition
bands_bc = {
    "bc": []
}

style_bc = {
    "name": "bc_burnt_area",
    "title": "BurnCube Burnt Area",
    "abstract": "burnt area as detected by the BurnCube method",
    "needed_bands": ["bc"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bc",
        },
    },
    "value_map": {
        "bc": [
            {
                "title": "Burnt Area",
                "abstract": "",
                "values": [1],
                "color": "#674ea7",
            },
        ]
    },
    "legend": {},
}

layers = {
    "title": "BurnCube Burnt Area",
    "name": "ga_burn_mapping_bc",
    "abstract": """BurnCube Burnt Area, 2023-2024 Financial Year, 30m, 0.0.0 (Landsat, Collection 3)""",
    "product_name": "ga_ls8c_nbart_burn_mapping_fyear_3",
    "bands": bands_bc,
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "time_resolution": "summary",
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
    },
    "flags": [{
        "band": "land",
        "product": "geodata_coast_100k",
        "ignore_time": True,
        "ignore_info_flags": []
    }],
    "styling": {
        "default_style": "bc_burnt_area",
        "styles": [
            style_bc
        ],
    },
}
