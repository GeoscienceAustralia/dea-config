
layers = {
    "title": "DEA Water Observations (WOfS)",
    "abstract": "WOfS",
    "layers": [
        {
            "include": "ows_refactored.inland_water.wofs.ows_c3_wo_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_c3_wo_cfg.layer_c2",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_apr_oct_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_nov_mar_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_annual_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_summary_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_annual_cfg.c3_statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_summary_cfg.c3_wofs_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_apr_oct_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_nov_mar_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_annual_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_summary_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_alber_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_s2_wo_cfg.layer",
            "type": "python",
        },
    ],
}
