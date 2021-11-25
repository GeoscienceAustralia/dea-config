
layers = {
    "title": "Individual Observations",
    "abstract": "Digital Earth Australia (DEA) Water Observations from Space (WOfS)",
    "layers": [
        {
            "include": "ows_refactored.inland_water.wofs.individual.ows_wofs_cfg.ows_c3_wo_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.individual.ows_wofs_cfg.ows_c3_wo_cfg.layer_usgsc2",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.individual.ows_wofs_cfg.ows_s2_wo_cfg.layer",
            "type": "python",
        }
    ],
}
