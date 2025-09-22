from ows_refactored.baseline_satellite_data.sentinel1.band_s1_nrb_cfg import \
    bands_sentinel1_nrb
from ows_refactored.baseline_satellite_data.sentinel1.style_s1_nrb_cfg import \
    styles_s1_nrb_vvvh_list
from ows_refactored.ows_reslim_cfg import reslim_for_sentinel1

iw_vv_vh_0_layer = {
    "name": "ga_s1_nrb_iw_vv_vh_0",
    "title": "DE Normalised Radar Backscatter (Sentinel-1 IW, VV+VH)",
    "abstract": "Experimental Sentinel-1 backscatter data (VV+VH)",
    "product_name": "ga_s1_nrb_iw_vv_vh_0",
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "bands": bands_sentinel1_nrb,
    "resource_limits": reslim_for_sentinel1,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "VV",
        "styles": styles_s1_nrb_vvvh_list,
    },
}
