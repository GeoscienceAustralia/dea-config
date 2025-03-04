from ows_refactored.ows_reslim_cfg import reslim_standard

bands_fmc = {
    "fmc": [],
}

style_fmc = {
    "name": "style_fmc",
    "title": "Fuel Moisture Content",
    "abstract": "the percentage of water in vegetation by weight",
    "needed_bands": ["fmc"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "fmc",
        },
    },
    "range": [0, 300],
    "mpl_ramp": "PuOr_r",
    "legend": {
        "url": "https://data.dea.ga.gov.au/derivative/ga_ls_tcw_percentiles_2/tcw_percentiles_legend.png",
    },
}

layers = {
    "title": "DEA Fuel Moisture Content (Sentinel 2)",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Fuel Moisture Content (Sentinel 2)",
            "name": "ga_s2am_fmc",
            "abstract": """DEA Fuel Moisture Content (Sentinel 2)""",
            "product_name": "ga_s2am_fmc",
            "bands": bands_fmc,
            "resource_limits": reslim_standard,
            "native_crs": "EPSG:3577",
            "native_resolution": [20, -20],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "style_fmc",
                "styles": [style_fmc],
            },
        },
    ],
}
