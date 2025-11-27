category_layers = {
    "title": "Hazards",
    "abstract": "",
    "layers": [
        {
            "include": "ows_refactored.hazards.historic_burn.ows_category_historic_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.nrt_burn.ows_category_nrt_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.dea_fmc.ows_fmc_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.burn_mapping_uplift.ows_rbr_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.burn_mapping_uplift.ows_burncube_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.burn_mapping_uplift.ows_dea_gbdt_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.burn_mapping_uplift.ows_stacking_uncertainty_cfg.layers",
            "type": "python",
        },
    ]
}
