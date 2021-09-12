category_layers = {
    "title": "Inland Water",
    "abstract": "",
    "layers": [
        {
            "include": "ows_refactored.inland_water.tcw.ows_tcw_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_c3_wo_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_cfg.layers",
            "type": "python",
        },
    ]
}
