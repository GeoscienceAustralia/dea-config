
layers = {
    "title": "DEA Water Observations",
    "abstract": "Digital Earth Australia (DEA) Water Observations from Space (WOfS)",
    "layers": [
        {
            "include": "ows_refactored.inland_water.wofs.individual.ows_c3_wo_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.individual.ows_c3_wo_cfg.layer_usgsc2",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.individual.ows_s2_wo_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.multiyear.ows_wofs_summary_cfg.c3_wofs_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.annual.ows_wofs_annual_cfg.c3_statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.seasonal.ows_wofs_apr_oct_cfg.c3_statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.seasonal.ows_wofs_nov_mar_cfg.c3_statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_alber_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_annual_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_annual_cfg.clear_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_annual_cfg.wet_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_summary_cfg.statistics_layer",
            "type": "python",
        },
                {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_summary_cfg.clear_layer",
            "type": "python",
        },
                {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_summary_cfg.wet_layer",
            "type": "python",
        },
                {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_summary_cfg.freq_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_summary_cfg.filtered_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_apr_oct_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_apr_oct_cfg.clear_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_apr_oct_cfg.wet_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_nov_mar_cfg.statistics_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_nov_mar_cfg.clear_layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.c2.ows_wofs_nov_mar_cfg.wet_layer",
            "type": "python",
        }
    ],
}
