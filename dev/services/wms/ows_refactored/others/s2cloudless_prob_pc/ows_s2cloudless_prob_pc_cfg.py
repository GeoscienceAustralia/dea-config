from ows_refactored.others.s2cloudless_prob_pc.style_s2cloudless_prob_pc_cfg import \
    styles_s2cloudless_prob_pc_list
from ows_refactored.ows_reslim_cfg import reslim_standard

bands_s2cloudless_prob_pc = {
    "oa_s2cloudless_prob_pc_5": [],
    "oa_s2cloudless_prob_pc_10": [],
    "oa_s2cloudless_prob_pc_25": [],
}

abstract_s2cloudless_prob_pc = """Geoscience Australia S2Cloudless Probability Percentiles Calendar Year, Collection 3"""

s2cloudless_prob_pc_layer = {
    "title": "Geoscience Australia S2Cloudless Probability Percentiles Calendar Year, Collection 3",
    "name": "ga_s2cloudless_percentiles_cyear_3_v1",
    "abstract": abstract_s2cloudless_prob_pc,
    "product_name": "ga_s2cloudless_percentiles_cyear_3_v1",
    "bands": bands_s2cloudless_prob_pc,
    "time_resolution": "summary",
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [10, -10],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "s2cloudless_prob_pc_10",
        "styles": styles_s2cloudless_prob_pc_list,
    },
}
