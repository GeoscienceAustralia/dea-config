from ows_refactored.ows_reslim_cfg import reslim_standard

# bands definition
bands_dea_gbdt = {
    "rf": []
}

style_dea_gbdt = {
    "name": "rf_burnt_area",
    "title": "DEA GBDT Burnt Area",
    "abstract": "burnt area as detected by the DEA GBDT method",
    "needed_bands": ["rf"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "rf",
        },
    },
    "value_map": {
        "rf": [
            {
                "title": "DEA GBDT Burnt Area",
                "abstract": "",
                "values": [1],
                "color": "#3d85c6",
            },
        ]
    },
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "values": [0],
        }
    ],
    "legend": {},
}

layers = {
    "title": "DEA Gradient Boosted Decision Tree (GBDT) Burnt Area",
    "name": "ga_burn_mapping_dea_gbdt",
    "abstract": """DEA Gradient Boosted Decision Tree (GBDT) Burnt Area, 2023-2024 Financial Year, 30m, 0.0.0 (Landsat, Collection 3)""",
    "product_name": "ga_ls8c_nbart_burn_mapping_fyear_3",
    "bands": bands_dea_gbdt,
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
        "default_style": "rf_burnt_area",
        "styles": [
            style_dea_gbdt
        ],
    },
}
