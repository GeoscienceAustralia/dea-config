from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_500_max_datasets

bands_hap = {
    "Band_1": [],
}


style_hap_simple_gray = {
    "name": "simple_gray",
    "title": "Simple gray",
    "abstract": "Simple grayscale image",
    "components": {
        "red": {"Band_1": 1.0},
        "green": {"Band_1": 1.0},
        "blue": {"Band_1": 1.0},
    },
    "scale_range": [0.0, 255],
}


layer = {
    "title": "Historical Airborne Photography",
    "abstract": "",
    "layers": [
        {
            "title": "Historical Airborne Photography (HAP)",
            "name": "historical_airborne_photography",
            "abstract": "Historical Airborne Photography",
            "product_name": "historical_airborne_photography",
            "bands": bands_hap,
            "resource_limits": reslim_wms_min_zoom_500_max_datasets,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [1.0, 1.0],
            },
            "styling": {
                "default_style": "simple_gray",
                "styles": [
                    style_hap_simple_gray,
                ],
            },
        }
    ],
}
