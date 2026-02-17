category_layers = {
    "title": "Other",
    "abstract": "Other nonDEA services",
    "layers": [
        {
            "include": "ows_refactored.others.insar.ows_insar_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.others.aster.ows_aster_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.others.dev_only.ows_hap_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.others.ows_mstp_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.others.srtm.ows_srtm_cfg.dea_srtm_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.others.ows_weather_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.others.s2cloudless_prob_pc.ows_s2cloudless_prob_pc_cfg.s2cloudless_prob_pc_layer",
            "type": "python",
        },
    ]
}
