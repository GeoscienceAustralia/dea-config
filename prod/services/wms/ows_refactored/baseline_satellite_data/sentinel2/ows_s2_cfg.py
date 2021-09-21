category_layers = {
    "title": "Sentinel-2 satellite images",
    "abstract": "",
    "layers": [
        {
            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_cfg.s2b_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_cfg.s2a_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_provisional_cfg.s2b_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_provisional_cfg.s2a_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_ard_cfg.s2a_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_ard_cfg.s2b_layer",
            "type": "python",
        },
    ]
}
