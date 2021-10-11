category_layers = {
    "title": "DEA Surface Reflectance (Sentinel-2)",
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
            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_provisional_cfg.combined_layer",
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
