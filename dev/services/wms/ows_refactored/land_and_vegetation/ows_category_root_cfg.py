category_layers = {
    "title": "Land and vegetation",
    "abstract": "",
    "layers": [
        {
            "include": "ows_refactored.land_and_vegetation.landcover.ows_c2_lc_cyear_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.land_and_vegetation.fc.ows_fc_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.land_and_vegetation.ows_mangrove_cfg.layer",
            "type": "python",
        },
        {
            "title": "GA Barest Earth",
            "abstract": "",
            "layers": [
                {
                    "include": "ows_refactored.land_and_vegetation.ows_barest_earth_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.land_and_vegetation.ows_nd_cfg.ls8_be_layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.land_and_vegetation.ows_nd_cfg.ls30_be_layers",
                    "type": "python",
                },
            ],
        },
    ]
}
