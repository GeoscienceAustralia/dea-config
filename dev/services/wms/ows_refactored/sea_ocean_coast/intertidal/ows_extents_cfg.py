from ows_refactored.ows_reslim_cfg import reslim_standard

bands_item = {
    "relative": [],
}

bands_item_conf = {
    "stddev": [],
}

style_item_relative = {
    "name": "relative_layer",
    "title": "relative layer",
    "abstract": "The Relative Extents Model (item_v2) 25m v2.0.0",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "relative",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["relative"],
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 1.0, "color": "#d7191c", "alpha": 1.0},
        {
            "value": 2.0,
            "color": "#ec6e43",
        },
        {
            "value": 3.0,
            "color": "#fdb96e",
        },
        {
            "value": 4.0,
            "color": "#fee7a4",
        },
        {
            "value": 5.0,
            "color": "#e7f5b7",
        },
        {
            "value": 6.0,
            "color": "#b7e1a7",
        },
        {
            "value": 7.0,
            "color": "#74b6ad",
        },
        {"value": 8.0, "color": "#2b83ba"},
        {"value": 9.0, "color": "#000000", "alpha": 0.0},
    ],
    "legend": {
        "begin": "0.0",
        "end": "9.0",
        "ticks_every": "1.0",
        "units": "%",
        "decimal_places": 0,
        "tick_labels": {
            "0.0": {"label": "0"},
            "0.1": {"label": "10"},
            "0.2": {"label": "20"},
            "0.3": {"label": "30"},
            "0.4": {"label": "40"},
            "0.5": {"label": "50"},
            "0.6": {"label": "60"},
            "0.7": {"label": "70"},
            "0.8": {"label": "80"},
            "0.9": {"label": "90"},
        },
    },
}

style_item_confidence = {
    "name": "confidence_layer",
    "title": "confidence layer",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev",
        },
    },
    "include_in_feature_info": False,
    "abstract": "The Confidence layer (item_v2_conf) 25m v2.0.0",
    "needed_bands": ["stddev"],
    "color_ramp": [
        {"value": 0.0, "color": "#2b83ba", "alpha": 0.0},
        {"value": 0.01, "color": "#2b83ba"},
        {
            "value": 0.055,
            "color": "#55a1b2",
        },
        {
            "value": 0.1,
            "color": "#80bfab",
        },
        {
            "value": 0.145,
            "color": "#abdda4",
        },
        {
            "value": 0.19,
            "color": "#c7e8ad",
        },
        {
            "value": 0.235,
            "color": "#e3f3b6",
        },
        {
            "value": 0.28,
            "color": "#fdbf6f",
        },
        {
            "value": 0.325,
            "color": "#e37d1c",
        },
        {
            "value": 0.37,
            "color": "#e35e1c",
        },
        {
            "value": 0.415,
            "color": "#e31a1c",
        },
        {
            "value": 0.46,
            "color": "#e31a1c",
        },
        {
            "value": 0.505,
            "color": "#e31a1c",
        },
        {"value": 0.55, "color": "#e31a1c"},
    ],
    "legend": {
        "begin": "0.01",
        "end": "0.55",
        "ticks": ["0.01", "0.55"],
        "tick_labels": {
            "0.01": {"prefix": "<"},
            "0.55": {"prefix": ">"},
        },
        "decimal_places": 2,
        "strip_location": [0.1, 0.5, 0.8, 0.15],
        "units": "NDWI standard deviations",
    },
}

item_v2_00_layer = {
    "title": "Intertidal Extents Model (ITEM)",
    "name": "ITEM_V2.0.0",
    "abstract": """Intertidal Extents Model 25m 2.0.0 (Extents)

This product is deprecated; users are advised to transition to using DEA Intertidal instead: https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "item_v2",
    "time_resolution": "summary",
    "bands": bands_item,
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "relative_layer",
        "styles": [
            style_item_relative,
        ],
    },
}

item_v2_00_conf_layer = {
    "title": "Intertidal Extents Model (ITEM) confidence",
    "name": "ITEM_V2.0.0_Conf",
    "abstract": """Intertidal Extents Model 25m 2.0.0 (Confidence)

This product is deprecated; users are advised to transition to using DEA Intertidal instead: https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "item_v2_conf",
    "bands": bands_item_conf,
    "resource_limits": reslim_standard,
    "time_resolution": "summary",
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val2",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "confidence_layer",
        "styles": [
            style_item_confidence,
        ],
    },
}
