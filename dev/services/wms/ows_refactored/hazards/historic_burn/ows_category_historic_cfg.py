category_layers = {
    "title": "DEA BurnCube Historic Burnt Area",
    "abstract": "",
    "layers": [
        {
            "include": "ows_refactored.hazards.ows_ls_burncube_cyear_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.ows_ls_burncube_fyear_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.ows_s2_burncube_cyear_cfg.layers",
            "type": "python",
        },
    ]
}
