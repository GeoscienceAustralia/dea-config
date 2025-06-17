from ows_refactored.ows_reslim_cfg import reslim_standard

bands_nidem = {"nidem": []}

style_nidem = {
    "name": "NIDEM",
    "title": "National Intertidal Digital Elevation Model",
    "abstract": "National Intertidal Digital Elevation Model 25 m v1.0.0",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "nidem",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["nidem"],
    "color_ramp": [
        {"value": -2.51, "color": "#440154"},
        {
            "value": -2.5,
            "color": "#440154",
        },
        {
            "value": -2.34,
            "color": "#460e61",
        },
        {
            "value": -2.18,
            "color": "#471b6e",
        },
        {"value": -2.02, "color": "#472877"},
        {"value": -1.86, "color": "#45347f"},
        {"value": -1.7, "color": "#413f85"},
        {"value": -1.58, "color": "#3b4d8a"},
        {"value": -1.42, "color": "#37578b"},
        {"value": -1.26, "color": "#32618c"},
        {
            "value": -1.1,
            "color": "#2e6b8d",
        },
        {"value": -0.94, "color": "#2a748e"},
        {"value": -0.78, "color": "#267d8e"},
        {"value": -0.62, "color": "#23868d"},
        {"value": -0.46, "color": "#208f8c"},
        {"value": -0.3, "color": "#1e9889"},
        {"value": -0.14, "color": "#1fa186"},
        {
            "value": 0.0,
            "color": "#26ac7f",
        },
        {"value": 0.14, "color": "#32b579"},
        {"value": 0.3, "color": "#41bd70"},
        {"value": 0.46, "color": "#54c566"},
        {"value": 0.62, "color": "#69cc59"},
        {"value": 0.78, "color": "#80d24b"},
        {"value": 0.94, "color": "#99d83c"},
        {
            "value": 1.1,
            "color": "#b2dc2c",
        },
        {"value": 1.26, "color": "#cce01e"},
        {"value": 1.42, "color": "#e5e31a"},
        {
            "value": 1.5,
            "color": "#fde724",
        },
    ],
    "legend": {
        "begin": "-2.5",
        "end": "1.5",
        "ticks": ["-2.5", "-1.1", "0.0", "1.5"],
        "units": "metres",
        "tick_labels": {
            "1.5": {"prefix": ">"},
            "-2.5": {"prefix": "<"},
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
        "default_style": "NIDEM",
        "styles": [
            style_nidem,
        ],
    },
}
