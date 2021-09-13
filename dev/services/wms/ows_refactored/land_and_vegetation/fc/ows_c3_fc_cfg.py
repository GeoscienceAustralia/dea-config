from ows_refactored.ows_legend_cfg import (
    legend_idx_0_100_pixel_fc_25ticks, legend_idx_0_100_pixel_fc_bs_25ticks,
    legend_idx_0_100_pixel_fc_ngv_25ticks)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35

bands_fc_3 = {
    "bs": ["bare_soil"],
    "pv": ["photosynthetic_vegetation", "green_vegetation"],
    "npv": ["non_photosynthetic_vegetation", "brown_vegetation"],
    "ue": [],
}

c3_fc_pq_mask = [
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
]

style_fc_c3_rgb = {
    "name": "fc_rgb",
    "title": "Three-band Fractional Cover",
    "abstract": "Fractional cover medians - red is bare soil, green is green vegetation and blue is non-green vegetation",
    "components": {
        "red": {"bs": 1.0},
        "green": {"pv": 1.0},
        "blue": {"npv": 1.0},
    },
    "scale_range": [0.0, 100.0],
    "pq_masks": c3_fc_pq_mask,
    "legend": {
        "show_legend": True,
        "url": "https://data.dea.ga.gov.au/fractional-cover/FC_legend.png",
    },
}

style_fc_gv_c3 = {
    "name": "green_veg_c3",
    "title": "Green Vegetation",
    "abstract": "Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "pv",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["pv"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffcc",
        },
        {
            "value": 25,
            "color": "#c2e699",
        },
        {
            "value": 50,
            "color": "#78c679",
        },
        {
            "value": 75,
            "color": "#31a354",
        },
        {
            "value": 100,
            "color": "#006837",
        },
    ],
    "pq_masks": c3_fc_pq_mask,
    "legend": legend_idx_0_100_pixel_fc_25ticks,
}

style_fc_bs_c3 = {
    "name": "bare_ground_c3",
    "title": "Bare Ground",
    "abstract": "Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bs",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["bs"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#feebe2",
        },
        {
            "value": 25,
            "color": "#fbb4b9",
        },
        {
            "value": 50,
            "color": "#f768a1",
        },
        {
            "value": 75,
            "color": "#c51b8a",
        },
        {
            "value": 100,
            "color": "#7a0177",
        },
    ],
    "pq_masks": c3_fc_pq_mask,
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
}

style_fc_ngv_c3 = {
    "name": "non_green_veg_c3",
    "title": "Non-Green vegetation",
    "abstract": "Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "npv",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["npv"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffd4",
        },
        {"value": 25, "color": "#fed98e", "legend": {}},
        {
            "value": 50,
            "color": "#fe9929",
        },
        {
            "value": 75,
            "color": "#d95f0e",
        },
        {
            "value": 100,
            "color": "#993404",
        },
    ],
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    "pq_masks": c3_fc_pq_mask,
}

layer = {
    "title": "DEA Fractional Cover (Landsat)",
    "name": "ga_ls_fc_3",
    "abstract": """
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
    "wcs": {
        "default_bands": ["bs", "pv", "npv"],
    },
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
