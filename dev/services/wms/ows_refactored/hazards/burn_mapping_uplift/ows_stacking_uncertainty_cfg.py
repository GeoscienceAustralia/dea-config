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
        "kwargs": {"band": "uncertainty"}},
    "color_ramp": [{"value": 0.0, "color": "#000000", "alpha": 0.0},
                   {"value": 0.33, "color": "#ffd966"},
                   {"value": 0.66, "color": "#f09c43"},
                   {"value": 1, "color": "#d53a3a"}],
    "legend": {
        "url": "https://dea-public-data-dev.s3.ap-southeast-2.amazonaws.com/projects/burn_cube/derivative/terria_accessory_files/burnt_area_stack_legend.png",
    },
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
    "flags": [{
        "band": "land",
        "product": "geodata_coast_100k",
        "ignore_time": True,
        "ignore_info_flags": []
    }],
    "styling": {
        "default_style": "stacking_burnt_area",
        "styles": [
            style_stacking
        ],
    },
}
