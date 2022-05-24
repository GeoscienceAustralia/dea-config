category_layers = {
    "title": "Inland water",
    "abstract": "",
    "layers": [
        {
            "include": "ows_refactored.inland_water.tcw.ows_tcw_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.tcw.ows_c3_tcp_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.inland_water.wofs.ows_wofs_cfg.layers",
            "type": "python",
        },
    ]
}
