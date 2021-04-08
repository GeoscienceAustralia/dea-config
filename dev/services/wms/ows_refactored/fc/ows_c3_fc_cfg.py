from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35

bands_fc_3 = {
    "bs": ["bare_soil"],
    "pv": ["photosynthetic_vegetation", "green_vegetation"],
    "npv": ["non_photosynthetic_vegetation", "brown_vegetation"],
    "ue": [],
}

style_fc_3_simple = {
    "name": "simple_fc",
    "title": "Fractional Cover",
    "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
    "components": {"red": {"bs": 1.0}, "green": {"pv": 1.0}, "blue": {"npv": 1.0}},
    "scale_range": [0.0, 100.0],
    "pq_masks": [
        {
            # pq_masks:band now takes the actual ODC band name, not the identifier.
            "band": "water",
            "flags": {"dry": True},
        },
        {
            "band": "water",
            "flags": {
                "terrain_shadow": False,
                "low_solar_angle": False,
                "high_slope": False,
                "cloud_shadow": False,
                "cloud": False,
            },
        },
        {
            "band": "land",
            "invert": True,
            "enum": 0,
        },
    ],
}


layers = {
    "title": "Geoscience Australia Landsat Fractional Cover Collection 3",
    "name": "ga_ls_fc_3",
    "abstract": """
Fractional cover data can be used to identify large scale patterns and trends and inform evidence based decision making and policy on topics including wind and water erosion risk, soil carbon dynamics, land management practices and rangeland condition.

This information is used by policy agencies, natural and agricultural land resource managers, and scientists to monitor land conditions over large areas over long time frames.
""",
    "product_name": "ga_ls_fc_3",
    "bands": bands_fc_3,
    "resource_limits": reslim_wms_min_zoom_35,
    "dynamic": True,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        # flags is now a list of flag band definitions - NOT a dictionary with identifiers
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": [],
        },
        {
            "band": "water",
            "product": "ga_ls_wo_3",
            "ignore_time": False,
            "ignore_info_flags": [],
            "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
        },
    ],
    "wcs": {
        "native_crs": "EPSG:3577",
        "default_bands": ["bs", "pv", "npv"],
        "native_resolution": [25, -25],
    },
    "styling": {
        "default_style": "simple_fc",
        "styles": [
            style_fc_3_simple,
        ],
    },
}
