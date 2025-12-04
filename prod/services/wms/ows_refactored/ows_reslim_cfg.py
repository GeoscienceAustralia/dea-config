# dataset cache rules - enable caching hints to optimise effectiveness of
#                       external caches (e.g Cloudfront)

dataset_cache_rules = [
    {
        "min_datasets": 1,
        "max_age": 60 * 60,
    },
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

reslim_standard = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 6.9,
        "dataset_cache_rules": dataset_cache_rules,
        "max_datasets": 24,
    },
    "wcs": common_wcs_limits,
}

reslim_for_sentinel2 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 5.9,
        "dataset_cache_rules": dataset_cache_rules,
        "max_datasets": 24,
    },
    "wcs": common_wcs_limits,
}

reslim_for_lccs = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 7.8,
        "dataset_cache_rules": dataset_cache_rules,
        "max_datasets": 24,
    },
    "wcs": common_wcs_limits,
}

reslim_for_mstp = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 8.1,
        "dataset_cache_rules": dataset_cache_rules,
        "max_datasets": 24,
    },
    "wcs": common_wcs_limits,
}

reslim_wms_unlimited = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 1.0,
        "max_datasets": 24,
    },
    "wcs": common_wcs_limits,
}

