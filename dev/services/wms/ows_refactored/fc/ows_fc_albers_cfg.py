from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35

bands_fc = {
    "BS": ["bare_soil"],
    "PV": ["photosynthetic_vegetation", "green_vegetation"],
    "NPV": ["non_photosynthetic_vegetation", "brown_vegetation"],
}

style_fc_simple_rgb = {
    "name": "simple_rgb",
    "title": "Simple RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {
        "red": {"BS_PC_50": 1.0},
        "green": {"PV_PC_50": 1.0},
        "blue": {"NPV_PC_50": 1.0},
    },
    "scale_range": [0.0, 100.0],
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
}

style_fc_simple = {
    "name": "simple_fc",
    "title": "Fractional Cover",
    "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
    "components": {"red": {"BS": 1.0}, "green": {"PV": 1.0}, "blue": {"NPV": 1.0}},
    "scale_range": [0.0, 100.0],
    "pq_masks": [
        {
            "flags": {"dry": True},
        },
        {
            "flags": {
                "terrain_or_low_angle": False,
                "high_slope": False,
                "cloud_shadow": False,
                "cloud": False,
                "sea": False,
            }
        },
    ],
}
layers = {
    "title": "Fractional Cover",
    "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au
""",
    "layers": [
        {
            "title": "Fractional Cover 25m 100km tile (Fractional Cover Landsat 5)",
            "name": "ls5_fc_albers",
            "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 5 satellite

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ls5_fc_albers",
            "bands": bands_fc,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": {
                "band": "water",
                "product": "wofs_albers",
                "ignore_time": False,
                "ignore_info_flags": [],
                "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["BS", "PV", "NPV"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "simple_fc",
                "styles": [
                    style_fc_simple,
                ],
            },
        },
        {
            "title": "Fractional Cover 25m 100km tile (Fractional Cover Landsat 7)",
            "name": "ls7_fc_albers",
            "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 7 satellite

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ls7_fc_albers",
            "bands": bands_fc,
            "resource_limits": reslim_wms_min_zoom_35,
            "dynamic": True,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": {
                "band": "water",
                "product": "wofs_albers",
                "ignore_time": False,
                "ignore_info_flags": [],
                "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["BS", "PV", "NPV"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "simple_fc",
                "styles": [
                    style_fc_simple,
                ],
            },
        },
        {
            "title": "Fractional Cover 25m 100km tile (Fractional Cover Landsat 8)",
            "name": "ls8_fc_albers",
            "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 8 satellite

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ls8_fc_albers",
            "bands": bands_fc,
            "resource_limits": reslim_wms_min_zoom_35,
            "dynamic": True,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": {
                "band": "water",
                "product": "wofs_albers",
                "ignore_time": False,
                "ignore_info_flags": [],
                "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["BS", "PV", "NPV"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "simple_fc",
                "styles": [
                    style_fc_simple,
                ],
            },
        },
        {
            "title": "Fractional Cover 25m 100km tile (Fractional Cover Combined)",
            "name": "fc_albers_combined",
            "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. This product contains Fractional Cover dervied from the Landsat 5, 7 and 8 satellites For service status information, see https://status.dea.ga.gov.au
""",
            "multi_product": True,
            "product_names": [
                "ls5_fc_albers",
                "ls7_fc_albers",
                "ls8_fc_albers",
            ],
            "bands": bands_fc,
            "resource_limits": reslim_wms_min_zoom_35,
            "dynamic": True,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": {
                "band": "water",
                "products": [
                    "wofs_albers",
                    "wofs_albers",
                    "wofs_albers",
                ],
                "ignore_time": False,
                "ignore_info_flags": [],
                "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["BS", "PV", "NPV"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "simple_fc",
                "styles": [
                    style_fc_simple,
                ],
            },
        },
    ],
}
