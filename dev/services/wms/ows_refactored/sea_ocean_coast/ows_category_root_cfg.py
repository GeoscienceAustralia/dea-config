category_layers = {
    "title": "Sea, Occean and Coast",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Intertidal (ITEM, NIDEM)",
            "abstract": "",
            "layers": [
                {
                    "include": "ows_refactored.sea_ocean_coast.intertidal.ows_extents_cfg.item_v2_00_layer",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.sea_ocean_coast.intertidal.ows_extents_cfg.item_v2_00_conf_layer",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.sea_ocean_coast.intertidal.ows_national_cfg.layer",
                    "type": "python",
                },
            ]
        },
        {
            "include": "ows_refactored.sea_ocean_coast.ows_tide_cfg.layers",
            "type": "python",
        },
    ]
}
