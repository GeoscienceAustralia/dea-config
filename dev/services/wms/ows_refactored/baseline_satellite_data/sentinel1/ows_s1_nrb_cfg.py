from ows_refactored.baseline_satellite_data.sentinel1.band_s1_nrb_cfg import (
    bands_sentinel1_nrb,
)
from ows_refactored.baseline_satellite_data.sentinel1.style_s1_nrb_cfg import (
    styles_s1_nrb_list,
)

s1_nrb_layer = {
    "name": "ga_s1_nrb_iw_vv_vh_c0",
    "product_name": "ga_s1_nrb_iw_vv_vh_c0",
    "bands": bands_sentinel1_nrb,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_nan",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "vv_gamma0",
        "styles": styles_s1_nrb_list,
    },
}
