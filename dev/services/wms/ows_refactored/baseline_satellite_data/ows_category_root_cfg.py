category_layers = {
    "title": "Baseline satellite data",
    "abstract": "",
    "layers": [
        {
            "include": "ows_refactored.baseline_satellite_data.landsat_s2_combined.ows_c3_cfg.combined_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.landsat_s2_combined.ows_c3_cfg.combined_mosaic_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.landsat.ows_c3_cfg.combined_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_ard_cfg.combined_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.landsat_annual.ows_landsat_annual_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.landsat.ows_c3_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_s2_cfg.category_layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.sentinel1.ows_s1_cfg.category_layers",
            "type": "python",
        },
    ],
}
