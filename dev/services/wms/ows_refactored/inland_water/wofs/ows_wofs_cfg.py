
layers = {
    "title": "DEA Water Observations",
    "abstract": "Digital Earth Australia (DEA) Water Observations from Space (WOfS)",
    "layers": [
        {
            "include": "ows_refactored.inland_water.wofs.individual.ows_c3_wo_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.multiyear.ows_c3_wo_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.annual.ows_wofs_apr_oct_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.seasonal.ows_wofs_nov_mar_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_annual_cfg.layers",
            "type": "python",
        }
    ],
}
