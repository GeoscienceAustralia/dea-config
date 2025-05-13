from ows_refactored.ows_reslim_cfg import reslim_standard

bands_nidem = {"nidem": []}

style_nidem_macro = {
    "name": "nidem_macro",
    "title": "Intertidal elevation (macrotidal)",
    "abstract": "Intertidal elevation visualised for macrotidal coastal environments",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "nidem",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["nidem"],
    "mpl_ramp": "viridis",
    "range": [-4.0, 2.0],
    "legend": {
        "begin": "-4.0",
        "end": "2.0",
        "ticks": ["-4.0", "0.0", "2.0"],
        "units": "metres",
        "tick_labels": {
            "2.0": {"prefix": ">"},
            "-4.0": {"prefix": "<"},
        },
    },
}


style_nidem_micro = {
    "name": "nidem_micro",
    "title": "Elevation (microtidal)",
    "abstract": "Intertidal elevation visualised for microtidal coastal environments",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "nidem",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["nidem"],
    "mpl_ramp": "viridis",
    "range": [-1.0, 0.5],
    "legend": {
        "begin": "-1.0",
        "end": "0.5",
        "ticks": ["-1.0", "0.0", "0.5"],
        "units": "metres",
        "tick_labels": {
            "0.5": {"prefix": ">"},
            "-1.0": {"prefix": "<"},
        },
    },
}


layer = {
    "title": "National Intertidal Digital Elevation Model (NIDEM)",
    "name": "NIDEM",
    "abstract": """National Intertidal Digital Elevation Model 25m 1.0.0

This product is deprecated; users are advised to transition to using DEA Intertidal instead: https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "nidem",
    "bands": bands_nidem,
    "time_resolution": "summary",
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "flags": [
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": [],
        },
    ],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "nidem_macro",
        "styles": [
            style_nidem_macro,
            style_nidem_micro,
        ],
    },
}
