category_layers = [
    {
        "title": "Land and Vegetation",
        "abstract": "",
        "layers": [
            {
                "include": "ows_refactored.land_and_vegetation.landcover.ows_c2_lc_cyear_cfg.layers",
                "type": "python",
            },
            {
                "include": "ows_refactored.land_and_vegetation.fc.ows_fc_percentiles_cfg.fcp_g_layers",
                "type": "python",
            },
            {
                "include": "ows_refactored.land_and_vegetation.fc.ows_fc_percentiles_cfg.fcp_ngv_layers",
                "type": "python",
            },
            {
                "include": "ows_refactored.land_and_vegetation.fc.ows_fc_percentiles_cfg.fcp_bs_layers",
                "type": "python",
            },
            {
                "include": "ows_refactored.land_and_vegetation.fc.ows_fc_percentiles_cfg.fcp_median_layers",
                "type": "python",
            },
            {
                "include": "ows_refactored.land_and_vegetation.fc.ows_fc_percentiles_cfg.fcp_seasonal_layers",
                "type": "python",
            },
            {
                "include": "ows_refactored.land_and_vegetation.fc.ows_fc_albers_cfg.layers",
                "type": "python",
            },
            {
                "include": "ows_refactored.land_and_vegetation.fc.ows_c3_fc_cfg.layers",
                "type": "python",
            },
        ]
    }
]