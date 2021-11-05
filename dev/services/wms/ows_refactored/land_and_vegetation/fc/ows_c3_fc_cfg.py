from ows_refactored.land_and_vegetation.fc.band_fc_cfg import bands_fc_3
from ows_refactored.land_and_vegetation.fc.style_fc_cfg import (
    style_fc_bs_c3, style_fc_c3_rgb, style_fc_gv_c3, style_fc_ngv_c3)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35

layer = {
    "title": "DEA Fractional Cover (Landsat)",
    "name": "ga_ls_fc_3",
    "abstract": """Geoscience Australia Landsat Fractional Cover Collection 3
Fractional Cover (FC), developed by the Joint Remote Sensing Research Program, is a measurement that splits the landscape into three parts, or fractions:

green (leaves, grass, and growing crops)

brown (branches, dry grass or hay, and dead leaf litter)

bare ground (soil or rock)

DEA uses Fractional Cover to characterise every 30 m square of Australia for any point in time from 1987 to today.

https://cmi.ga.gov.au/data-products/dea/629/dea-fractional-cover-landsat-c3

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_fc_3",
    "bands": bands_fc_3,
    "resource_limits": reslim_wms_min_zoom_35,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
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
    "styling": {
        "default_style": "fc_rgb",
        "styles": [
            style_fc_c3_rgb,
            style_fc_bs_c3,
            style_fc_gv_c3,
            style_fc_ngv_c3,
        ],
    },
}

layer_c2 = {
    "title": "DEA Fractional Cover USGS C2 Test (Landsat)",
    "name": "ga_ls_fc_c2_3",
    "abstract": """Geoscience Australia Landsat Fractional Cover Collection 3
Fractional Cover (FC), developed by the Joint Remote Sensing Research Program, is a measurement that splits the landscape into three parts, or fractions:

green (leaves, grass, and growing crops)

brown (branches, dry grass or hay, and dead leaf litter)

bare ground (soil or rock)

DEA uses Fractional Cover to characterise every 30 m square of Australia for any point in time from 1987 to today.

https://cmi.ga.gov.au/data-products/dea/629/dea-fractional-cover-landsat-c3

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_fc_c2_3",
    "bands": bands_fc_3,
    "resource_limits": reslim_wms_min_zoom_35,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
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
            "product": "ga_ls_wo_c2_3",
            "ignore_time": False,
            "ignore_info_flags": [],
            "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
        },
    ],
    "styling": {
        "default_style": "fc_rgb",
        "styles": [
            style_fc_c3_rgb,
            style_fc_bs_c3,
            style_fc_gv_c3,
            style_fc_ngv_c3,
        ],
    },
}
