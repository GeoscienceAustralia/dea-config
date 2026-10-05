from ows_refactored.baseline_satellite_data.sentinel1.band_s1_nrb_c1_cfg import (
    bands_sentinel1_nrb_hh, bands_sentinel1_nrb_hh_hv, bands_sentinel1_nrb_vv,
    bands_sentinel1_nrb_vv_vh)
from ows_refactored.baseline_satellite_data.sentinel1.style_s1_nrb_c1_cfg import (
    styles_s1_nrb_hh_hv_list, styles_s1_nrb_hh_list, styles_s1_nrb_vv_list,
    styles_s1_nrb_vv_vh_list)
from ows_refactored.ows_reslim_cfg import reslim_for_sentinel1

iw_vv_vh_1_layer = {
    "name": "ga_s1_nrb_iw_vv_vh_1",
    "title": "DE Normalised Radar Backscatter C1 (Sentinel-1 IW, VV+VH)",
    "abstract": "Experimental Sentinel-1 backscatter data (VV+VH)",
    "product_name": "ga_s1_nrb_iw_vv_vh_1",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": bands_sentinel1_nrb_vv_vh,
    "resource_limits": reslim_for_sentinel1,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "vv_vh_false_colour_db",
        "styles": styles_s1_nrb_vv_vh_list,
    },
}

iw_vv_1_layer = {
    "name": "ga_s1_nrb_iw_vv_1",
    "title": "DE Normalised Radar Backscatter C1 (Sentinel-1 IW, VV)",
    "abstract": "Sentinel-1 backscatter data (VV)",
    "product_name": "ga_s1_nrb_iw_vv_1",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": bands_sentinel1_nrb_vv,
    "resource_limits": reslim_for_sentinel1,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "VV_DB",
        "styles": styles_s1_nrb_vv_list,
    },
}

iw_hh_hv_1_layer = {
    "name": "ga_s1_nrb_iw_hh_hv_1",
    "title": "DE Normalised Radar Backscatter C1 (Sentinel-1 IW, HH+HV)",
    "abstract": "Experimental Sentinel-1 backscatter data (HH+HV)",
    "product_name": "ga_s1_nrb_iw_hh_hv_1",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": bands_sentinel1_nrb_hh_hv,
    "resource_limits": reslim_for_sentinel1,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "vv_vh_false_colour_db",
        "styles": styles_s1_nrb_hh_hv_list,
    },
}

iw_hh_1_layer = {
    "name": "ga_s1_nrb_iw_hh_1",
    "title": "DE Normalised Radar Backscatter C1 (Sentinel-1 IW, HH)",
    "abstract": "Sentinel-1 backscatter data (HH)",
    "product_name": "ga_s1_nrb_iw_hh_1",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": bands_sentinel1_nrb_hh,
    "resource_limits": reslim_for_sentinel1,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "HH_DB",
        "styles": styles_s1_nrb_hh_list,
    },
}
