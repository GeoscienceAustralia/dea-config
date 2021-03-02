from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35
from ows_refactored.wofs.bands_wo_cfg import bands_wofs_obs

style_c3_wofs_obs = {
    "name": "observations",
    "title": "Observations",
    "abstract": "Observations",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {
                    "or": {
                        "terrain_shadow": True,
                        "low_solar_angle": True,
                        "cloud_shadow": True,
                        "cloud": True,
                        "high_slope": True,
                        "noncontiguous": True,
                    }
                },
                "color": "#707070",
            },
            {
                # Possible Sea Glint, also mark as invalid
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                },
                "color": "#D99694",
            },
            {
                "title": "Wet",
                "abstract": "Wet",
                "flags": {"wet": True},
                "color": "#4F81BD",
            },
        ],
    },
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "enum": 0,
        }
    ],
}

style_c3_wofs_obs_wet_only = {
    "name": "wet",
    "title": "Wet Only",
    "abstract": "Wet Only",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {
                    "or": {
                        "terrain_shadow": True,
                        "low_solar_angle": True,
                        "cloud_shadow": True,
                        "cloud": True,
                        "high_slope": True,
                        "noncontiguous": True,
                    }
                },
                "color": "#707070",
                "mask": True,
            },
            {
                # Possible Sea Glint, also mark as invalid
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                },
                "color": "#D99694",
                "mask": True,
            },
            {
                "title": "Wet",
                "abstract": "Wet",
                "flags": {"wet": True},
                "color": "#4F81BD",
            },
        ],
    },
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "enum": 1,
        },
    ],
}


layers = {
    "title": "Collection 3 Water",
    "name": "ga_ls_wo_3",
    "abstract": """
Water Observations from Space (WOfS) provides surface water observations derived from satellite imagery for all of Australia. The current product (Version 2.1.5) includes observations taken from 1986 to the present, from the Landsat 5, 7 and 8 satellites. WOfS covers all of mainland Australia and Tasmania but excludes off-shore Territories.
The WOfS product allows users to get a better understanding of where water is normally present in a landscape, where water is seldom observed, and where inundation has occurred occasionally.
Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water. The details of the WOfS algorithm and derived statistics are available at http://dx.doi.org/10.1016/j.rse.2015.11.003.
For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_wo_3",
    "bands": bands_wofs_obs,
    "resource_limits": reslim_wms_min_zoom_35,
    "dynamic": True,
    "flags": [
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
        }
    ],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_bitflag",
        "always_fetch_bands": [],
        "manual_merge": False,
        "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
    },
    "wcs": {
        "native_crs": "EPSG:3577",
        "native_resolution": [25, -25],
        "default_bands": ["water"],
    },
    "styling": {
        "default_style": "observations",
        "styles": [style_c3_wofs_obs, style_c3_wofs_obs_wet_only],
    },
}
