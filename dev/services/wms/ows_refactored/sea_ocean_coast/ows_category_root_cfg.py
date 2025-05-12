category_layers = {
    "title": "Sea, ocean and coast",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Intertidal",
            "abstract": "",
            "layers": [
                {
                    # DEA Intertidal Collection 3
                    "include": "ows_refactored.sea_ocean_coast.intertidal_c3.ows_intertidal_cfg.dea_intertidal_layer",
                    "type": "python",
                },
            ]
        },
        {
            "title": "DEA Tidal Composites",
            "abstract": "",
            "layers": [
                {
                    # DEA Tidal Composites Collection 3
                    "include": "ows_refactored.sea_ocean_coast.tidal_composites_c3.ows_tidal_composites_cfg.dea_tidal_composites_layer",
                    "type": "python",
                },
            ]
        },
        {
            "title": "Other",
            "abstract": "",
            "layers": [
                {
                    # ITEM 2.0 Collection 2
                    "include": "ows_refactored.sea_ocean_coast.intertidal.ows_extents_cfg.item_v2_00_layer",
                    "type": "python",
                },
                {
                    # ITEM 2.0 Confidence Collection 2
                    "include": "ows_refactored.sea_ocean_coast.intertidal.ows_extents_cfg.item_v2_00_conf_layer",
                    "type": "python",
                },
                {
                    # NIDEM Colllection 2
                    "include": "ows_refactored.sea_ocean_coast.intertidal.ows_national_cfg.layer",
                    "type": "python",
                },
                {
                    # HLTC Collection 2 (nested folder structure is defined below)
                    "include": "ows_refactored.sea_ocean_coast.ows_tide_cfg.layers",
                    "type": "python",
                },
            ]
        },
    ]
}
