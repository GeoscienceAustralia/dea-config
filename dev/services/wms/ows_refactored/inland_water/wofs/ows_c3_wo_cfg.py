from ows_refactored.inland_water.wofs.bands_wo_cfg import bands_wofs_obs
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35

style_c3_wofs_obs = {
    "name": "observations",
    "title": "Observations",
    "abstract": "Observations",
    "value_map": {
        "water": [
            {
                "title": "",
                "abstract": "",
                "flags": {
                    "nodata": True,
                },
                "alpha": 0.0,
                "color": "#707070",
            },
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
                        "water_observed": True,
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
                        "water_observed": True,
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
                "flags": {"water_observed": True},
                "color": "#4F81BD",
            },
            {
                "title": "Dry",
                "abstract": "",
                "flags": {
                    "water_observed": False,
                },
                "color": "#96966e",
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
    "legend": {"width": 3.0, "height": 2.1},
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
                "abstract": "",
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


layer = {
    "title": "DEA Water Observations (Landsat)",
    "name": "ga_ls_wo_3",
    "abstract": """ DEA Water Observations (Landsat)
DEA Water Observations provides surface water observations derived from Landsat satellite imagery for all of Australia from 1986 to present.

The Water Observations show the extent of water in a corresponding Landsat scene, along with the degree to which the scene was obscured by clouds, shadows or where sensor problems cause parts of a scene to not be observable.

https://cmi.ga.gov.au/data-products/dea/613/dea-water-observations-landsat

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "ga_ls_wo_3",
    "bands": bands_wofs_obs,
    "resource_limits": reslim_wms_min_zoom_35,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
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
        "styles": [style_c3_wofs_obs, style_c3_wofs_obs_wet_only],
    },
}

layer_c2 = {
    "title": "DEA Water Observations USGS C2 Test (Landsat)",
    "name": "ga_ls_wo_c2_3",
    "abstract": """ DEA Water Observations (Landsat)
DEA Water Observations provides surface water observations derived from Landsat satellite imagery for all of Australia from 1986 to present.

The Water Observations show the extent of water in a corresponding Landsat scene, along with the degree to which the scene was obscured by clouds, shadows or where sensor problems cause parts of a scene to not be observable.

https://cmi.ga.gov.au/data-products/dea/613/dea-water-observations-landsat

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "ga_ls_wo_c2_3",
    "bands": bands_wofs_obs,
    "resource_limits": reslim_wms_min_zoom_35,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "flags": [
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
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_bitflag",
        "always_fetch_bands": [],
        "manual_merge": False,
        "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
    },
    "styling": {
        "default_style": "observations",
        "styles": [style_c3_wofs_obs, style_c3_wofs_obs_wet_only],
    },
}
