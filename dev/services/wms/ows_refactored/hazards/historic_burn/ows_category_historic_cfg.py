category_layers = {
    "title": "Historic Burnt Area",
    "abstract": "",
    "layers": [
        {
            "include": "ows_refactored.hazards.burntarea.ows_ls_burncube_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.burntarea.ows_ls_burncube_fy_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.hazards.burntarea.ows_s2_burncube_cyear_cfg.layers",
            "type": "python",
        },
    ]
}
