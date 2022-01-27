# dataset cache rules - enable caching hints to optimise effectiveness of
#                       external caches (e.g Cloudfront)

dataset_cache_rules = [
    {
        "min_datasets": 5,
        "max_age": 60 * 60 * 24,
    },
    {
        "min_datasets": 9,
        "max_age": 60 * 60 * 24 * 14,
    },
]

common_wcs_limits = {
    # Maximum size in bytes of uncompressed image that can be
    # returned.
    "max_image_size": 800_000_000,
    # Maximum number of datasets that can be accessed in a
    # single query
    "max_datasets": 24,   # defaults to no limit
}

reslim_wms_min_zoom_35 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 6.9,
        # "min_zoom_factor": 35.0,
        # "max_datasets": 16, # Defaults to no dataset limit
        "dataset_cache_rules": dataset_cache_rules
    },
    "wcs": common_wcs_limits,
}

reslim_wms_min_zoom_15 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 6.9,
        # "min_zoom_factor": 15.0,
        # "max_datasets": 16, # Defaults to no dataset limit
        "dataset_cache_rules": dataset_cache_rules,
    },
    "wcs": common_wcs_limits,
}
reslim_wms_min_zoom_15_cache_rules = reslim_wms_min_zoom_15

reslim_wms_min_zoom_10 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 6.9,
        # "min_zoom_factor": 10.0,
        # "max_datasets": 16, # Defaults to no dataset limit
        "dataset_cache_rules": dataset_cache_rules,
    },
    "wcs": common_wcs_limits,
}

reslim_wms_min_zoom_lvl_7 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 6.9,
        # "max_datasets": 16, # Defaults to no dataset limit
        "dataset_cache_rules": dataset_cache_rules
    },
    "wcs": common_wcs_limits,
}

reslim_wms_min_zoom_500_max_datasets = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 500.0,
        "max_datasets": 6,
    },
    "wcs": common_wcs_limits,
}
