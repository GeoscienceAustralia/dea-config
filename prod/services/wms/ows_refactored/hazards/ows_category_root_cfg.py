category_layers = {
    "title": "Hazards",
    "abstract": "",
    "layers": [
        {
            "include": "ows_refactored.hazards.burntarea.ows_provisional_ba_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.dea_fmc.ows_fmc_combined_cfg.ga_s2_fmc_layer",
            "type": "python",
        },
                {
            "include": "ows_refactored.hazards.dea_fmc.ows_fmc_combined_cfg.ga_s2m_fmc_mosaic_layer",
            "type": "python",
        },
    ]
}
