from ows_refactored.ows_reslim_cfg import reslim_standard

# bands definition
bands_rbr = {
    "rbr": []
}

style_rbr = {
    "name": "rbr_burnt_area",
    "title": "RBR Burnt Area",
    "abstract": "burnt area as detected by the RBR method",
    "needed_bands": ["rbr"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "rbr",
        },
    },
    "value_map": {
        "rbr": [
            {
                "title": "",
                "abstract": "",
                "values": [1],
                "color": "#a64d79",
            },
        ]
    },
    "legend": {},
}

layers = {
    "title": "Relativised Burn Ratio (RBR) Burnt Area",
    "name": "ga_ls8c_nbart_burn_mapping_fyear_3",
    "abstract": """Relativised Burn Ratio (RBR) Burnt Area, 2023-2024 Financial Year, 30m, 0.0.0 (Landsat, Collection 3)""",
    "product_name": "ga_ls8c_nbart_bc_cyear_3",
    "bands": bands_rbr,
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "time_resolution": "summary",
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
    },
    "styling": {
        "default_style": "rbr_burnt_area",
        "styles": [
            style_rbr
        ],
    },
}