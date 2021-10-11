from ows_refactored.baseline_satellite_data.sentinel2.band_s2_cfg import \
    bands_sentinel2_provisional
from ows_refactored.baseline_satellite_data.sentinel2.style_s2_cfg import \
    styles_s2_provisional_list
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

combined_layer = {
    "title": "DEA Surface Reflectance (Sentinel-2) Provisional - near real time",
    "name": "s2_nrt_provisional_granule_nbar_t",
    "abstract": """Geoscience Australia Sentinel-2 MSI Analysis Ready Data Provisional Collection 3

This product takes Sentinel-2 (MSI) imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains sub-products that provide corrections or attribution information:

DEA Surface Reflectance NBART (Sentinel-2 MSI)

DEA Surface Reflectance OA (Sentinel-2 MSI)

The resolution is a 10-20m grid based on the ESA Level1C archive.

For service status information, see https://status.dea.ga.gov.au
""",
    "multi_product": True,
    "product_names": ["ga_s2am_ard_provisional_3", "ga_s2bm_ard_provisional_3"],
    "bands": bands_sentinel2_provisional,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "oa_fmask",
            "products": ["ga_s2am_ard_provisional_3", "ga_s2bm_ard_provisional_3"],
            "ignore_time": False,
            "ignore_info_flags": [],
        },
        {
            "band": "land",
            "products": ["geodata_coast_100k", "geodata_coast_100k"],
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_provisional_list},
}

s2b_layer = {
    "name": "s2b_nrt_provisional_granule_nbar_t",
    "title": "DEA Surface Reflectance (Sentinel-2B MSI) Provisional - near real time",
    "abstract": """Geoscience Australia Sentinel-2B MSI Analysis Ready Data Provisional Collection 3

This product takes Sentinel-2 (MSI) imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains sub-products that provide corrections or attribution information:

DEA Surface Reflectance NBART (Sentinel-2A MSI)

DEA Surface Reflectance OA (Sentinel-2A MSI)

The resolution is a 10-20m grid based on the ESA Level1C archive.

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_s2bm_ard_provisional_3",
    "bands": bands_sentinel2_provisional,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "oa_fmask",
            "product": "ga_s2bm_ard_provisional_3",
            "ignore_time": False,
            "ignore_info_flags": []
        },
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_provisional_list},
}

s2a_layer = {
    "name": "s2a_nrt_provisional_granule_nbar_t",
    "title": "DEA Surface Reflectance (Sentinel-2A MSI) Provisional - near real time",
    "abstract": """Geoscience Australia Sentinel-2A MSI Analysis Ready Data Provisional Collection 3

This product takes Sentinel-2 (MSI) imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains sub-products that provide corrections or attribution information:

DEA Surface Reflectance NBART (Sentinel-2A MSI)

DEA Surface Reflectance OA (Sentinel-2A MSI)

The resolution is a 10-20m grid based on the ESA Level1C archive.

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "ga_s2am_ard_provisional_3",
    "bands": bands_sentinel2_provisional,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "oa_fmask",
            "product": "ga_s2am_ard_provisional_3",
            "ignore_time": False,
            "ignore_info_flags": []
        },
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_provisional_list},
}
