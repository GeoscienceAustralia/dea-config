bands_sentinel1_nrb_vv_vh = {
    "vv_gamma0": ["VV_gamma0", "vv_gamma0"],
    "vh_gamma0": ["VH_gamma0", "vh_gamma0"],
    "oa_layover_shadow_mask": ["mask"],
    "oa_number_of_looks": ["number_of_looks", "n_looks", "nlooks"],
    "oa_gamma0_to_beta0_ratio": ["gamma0_to_beta0_ratio"],
    "oa_gamma0_to_sigma0_ratio": ["gamma0_to_sigma0_ratio"],
    "oa_local_incidence_angle": ["local_incidence_angle", "lia", "LIA"],
    "oa_incidence_angle": ["incidence_angle", "ia", "IA"],
}

bands_sentinel1_nrb_vv = bands_sentinel1_nrb_vv_vh.copy()
bands_sentinel1_nrb_vv.pop("vh_gamma0")

bands_sentinel1_nrb_hh_hv = {
    "hh_gamma0": ["HH_gamma0", "hh_gamma0"],
    "hv_gamma0": ["HV_gamma0", "hv_gamma0"],
    "oa_layover_shadow_mask": ["mask"],
    "oa_number_of_looks": ["number_of_looks", "n_looks", "nlooks"],
    "oa_gamma0_to_beta0_ratio": ["gamma0_to_beta0_ratio"],
    "oa_gamma0_to_sigma0_ratio": ["gamma0_to_sigma0_ratio"],
    "oa_local_incidence_angle": ["local_incidence_angle", "lia", "LIA"],
    "oa_incidence_angle": ["incidence_angle", "ia", "IA"],
}

bands_sentinel1_nrb_hh = bands_sentinel1_nrb_hh_hv.copy()
bands_sentinel1_nrb_hh.pop("hv_gamma0")
