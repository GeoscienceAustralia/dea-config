from ows_refactored.inland_water.wofs.bands_wo_cfg import bands_wofs_obs
from ows_refactored.ows_reslim_cfg import reslim_standard

style_c3_wofs_obs = {
    "name": "observations",
    "title": "Water Observations",
    "abstract": "Observations",
    "value_map": {
        "water": [
            {
                "title": "",
                "abstract": "",
                "flags": {
                    "and": {
                        "noncontiguous": True,
                        "low_solar_angle": True
                    }
                },
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Cloudy Steep Terrain",
                "abstract": "",
                "flags": {
                    "and": {
                        "cloud": True,
                        "high_slope": True
                    }
                },
                "color": "#f2dcb4",
            },
            {
                "title": "Cloudy Water",
                "abstract": "",
                "flags": {
                    "and": {
                        "wet": True,
                        "cloud": True
                    }
                },
                "color": "#bad4f2",
            },
            {
                "title": "Shaded Water",
                "abstract": "",
                "flags": {
                    "and": {
                        "wet": True,
                        "cloud_shadow": True
                    }
                },
                "color": "#335277",
            },
            {
                "title": "Cloud",
                "abstract": "",
                "flags": {"cloud": True},
                "color": "#c2c1c0",
            },
            {
                "title": "Cloud Shadow",
                "abstract": "",
                "flags": {"cloud_shadow": True},
                "color": "#4b4b37",
            },
            {
                "title": "Terrain Shadow",
                "abstract": "",
                "flags": {"terrain_shadow": True},
                "color": "#2f2922",
            },
            {
                "title": "Steep Terrain",
                "abstract": "",
                "flags": {"high_slope": True},
                "color": "#776857",
            },
            {
                "title": "Water",
                "abstract": "",
                "flags": {"wet": True},
                "color": "#4F81BD",
            },
            {
                "title": "Dry",
                "abstract": "",
                "flags": {
                    "dry": True,
                },
                "color": "#96966e",
            },
        ],
    },
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "values": [0],
        }
    ],
    "legend": {"width": 3.0, "height": 2.1},
}

style_s2_wofs_obs_wet_only = {
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
                "alpha": 0.0,
            },
            {
                # Possible Sea Glint, also mark as invalid
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                },
                "color": "#D99694",
                "alpha": 0.0,
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
            "values": [0],
        },
    ],
}


layer = {
    "title": "DEA Water Observations Provisional (Sentinel-2 NRT)",
    "name": "ga_s2_wo_provisional_3",
    "abstract": """**Prototype Geoscience Australia Sentinel 2 Near Real Time Water Observations Provisional Collection 3.**


This product is the implementation of the DEA Water Observations (DEA WO) product (previously known as Water Observations from Space, or WOfS) on the Geoscience Australia Sentinel-2 Near Real Time surface reflectance product. This is a rapid, provisional, product. It has not been validated and is of unknown accuracy.

The Provisional Digital Earth Australia Water Observations (Sentinel-2) product shows where surface water was observed by the Sentinel 2A and Sentinel 2B satellites on any particular day over the most recent 3 months. The surface water observations are derived from Geoscience Australia Sentinel-2 Near Real Time surface reflectance imagery for all of Australia. The provisional, Near Real Time product is available for a rolling window of the most recent three months of data, and is produced within 24 hours of the satellite passing over an area.

For more information, see https://cmi.ga.gov.au/data-products/dea/639/dea-water-observations-provisional-sentinel-2-nrt""",
    "product_name": "ga_s2_wo_provisional_3",
    "bands": bands_wofs_obs,
    "resource_limits": reslim_standard,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10, -10],
    "flags": [
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": [],
        },
        {
            "band": "water",
            "product": "ga_s2_wo_provisional_3",
            "ignore_time": False,
            "ignore_info_flags": [],
            "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
        },
    ],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_bitflag",
        "always_fetch_bands": [],
        "manual_merge": False,
        "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
    },
    "styling": {
        "default_style": "observations",
        "styles": [style_c3_wofs_obs, style_s2_wofs_obs_wet_only],
    },
}
