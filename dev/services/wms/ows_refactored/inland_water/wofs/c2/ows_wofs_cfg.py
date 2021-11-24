
layers = {
    "title": "DEA Water Observations (C2)",
    "abstract": "Digital Earth Australia (DEA) Water Observations from Space (WOfS)",
    "layers": [
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_alber_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_annual_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_annual_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_summary_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_summary_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_apr_oct_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_apr_oct_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_nov_mar_cfg.statistics_layer",
            "type": "python",
        },
                {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_nov_mar_cfg.layer",
            "type": "python",
        }
    ],
}
