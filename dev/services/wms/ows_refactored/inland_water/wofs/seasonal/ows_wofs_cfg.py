
layers = {
    "title": "Seasonal Observations",
    "abstract": "Digital Earth Australia (DEA) Water Observations from Space (WOfS)",
    "layers": [
        {
            "include": "ows_refactored.inland_water.wofs.seasonal.ows_wofs_apr_oct_cfg.c3_statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.seasonal.ows_wofs_nov_mar_cfg.c3_statistics_layer",
            "type": "python",
        }
    ],
}
