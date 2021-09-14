from ows_refactored.land_and_vegetation.fc.style_fc_cfg import style_fc_simple
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_10

bands_fc = {
    "BS": ["bare_soil"],
    "PV": ["photosynthetic_vegetation", "green_vegetation"],
    "NPV": ["non_photosynthetic_vegetation", "brown_vegetation"],
}

fc_albers_flags = [
    {
        "band": "water",
        "product": "wofs_albers",
        "ignore_time": False,
        "ignore_info_flags": [],
        "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
    },
]

layers = {
    "title": "DEA Fractional Cover (Landsat, Collection 2)",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Fractional Cover (Landsat 5, Collection 2)",
            "name": "ls5_fc_albers",
            "abstract": """Fractional Cover 25m 2.2.1 (Landsat 5, Collection 2)
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 5 satellite
https://cmi.ga.gov.au/data-products/dea/119/dea-fractional-cover-landsat
For service status information, see https://status.dea.ga.gov.au
        """,
            "product_name": "ls5_fc_albers",
            "bands": bands_fc,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": fc_albers_flags,
            "wcs": {
                "default_bands": ["BS", "PV", "NPV"],
            },
            "styling": {
                "default_style": "simple_fc",
                "styles": [
                    style_fc_simple,
                ],
            },
        },
        {
            "title": "DEA Fractional Cover (Landsat 7, Collection 2)",
            "name": "ls7_fc_albers",
            "abstract": """Fractional Cover 25m 2.2.1 (Landsat 7, Collection 2)
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 7 satellite
https://cmi.ga.gov.au/data-products/dea/119/dea-fractional-cover-landsat
For service status information, see https://status.dea.ga.gov.au
        """,
            "product_name": "ls7_fc_albers",
            "bands": bands_fc,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "dynamic": True,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": fc_albers_flags,
            "wcs": {
                "default_bands": ["BS", "PV", "NPV"],
            },
            "styling": {
                "default_style": "simple_fc",
                "styles": [
                    style_fc_simple,
                ],
            },
        },
        {
            "title": "DEA Fractional Cover (Landsat 8, Collection 2)",
            "name": "ls8_fc_albers",
            "abstract": """Fractional Cover 25m 2.2.1 (Landsat 8, Collection 2)
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 8 satellite
https://cmi.ga.gov.au/data-products/dea/119/dea-fractional-cover-landsat
For service status information, see https://status.dea.ga.gov.au
        """,
            "product_name": "ls8_fc_albers",
            "bands": bands_fc,
            "resource_limits": reslim_wms_min_zoom_10,
            "dynamic": True,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": fc_albers_flags,
            "wcs": {
                "default_bands": ["BS", "PV", "NPV"],
            },
            "styling": {
                "default_style": "simple_fc",
                "styles": [
                    style_fc_simple,
                ],
            },
        },
        {
            "title": "DEA Fractional Cover (Landsat, Collection 2)",
            "name": "fc_albers_combined",
            "abstract": """Fractional Cover 25m 2.2.1 (Landsat, Collection 2)
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. This product contains Fractional Cover dervied from the Landsat 5, 7 and 8 satellites.
https://cmi.ga.gov.au/data-products/dea/119/dea-fractional-cover-landsat
For service status information, see https://status.dea.ga.gov.au
        """,
            "multi_product": True,
            "product_names": [
                "ls5_fc_albers",
                "ls7_fc_albers",
                "ls8_fc_albers",
            ],
            "bands": bands_fc,
            "resource_limits": reslim_wms_min_zoom_10,
            "dynamic": True,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": [
                {
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
            ],
            "wcs": {
                "default_bands": ["BS", "PV", "NPV"],
            },
            "styling": {
                "default_style": "simple_fc",
                "styles": [
                    style_fc_simple,
                ],
            },
        }
    ]
}
