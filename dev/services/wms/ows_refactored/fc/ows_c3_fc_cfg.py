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
            "flags": {"dry": True},
        },
        {
            "flags": {
                "terrain_shadow": False,
                "low_solar_angle": False,
                "high_slope": False,
                "cloud_shadow": False,
                "cloud": False,
                # "sea": False,
            }
        },
    ],
}


layers =  {
        "title": "Collection 3 fc",
        "name": "ga_ls_fc_3",
        "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. This product contains Fractional Cover dervied from the Landsat 5, 7 and 8 satellites For service status information, see https://status.dea.ga.gov.au
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
        "flags": {
            "band": "water",
            "product":"ga_ls_wo_3",
            "ignore_time": False,
            "ignore_info_flags": [],
            "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
        },
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