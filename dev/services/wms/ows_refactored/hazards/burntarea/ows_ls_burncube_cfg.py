from ows_refactored.ows_reslim_cfg import reslim_standard

# bands definition
bands_in_burncube = {
    "wofssevere": [],
    "wofsmoderate": [],
}

style_combined_burncube = {
    "name": "combined_burncube",
    "title": "Burncube Burnt Area",
    "abstract": "",
    "needed_bands": ["wofssevere", "wofsmoderate"],
    "index_expression": "2*wofssevere + wofsmoderate",
    "color_ramp": [
        {"value": 0.0, "color": "#FFFFFF", "alpha": 0.0},
        {"value": 1, "color": "#F79646"},
        {"value": 2, "color": "#C0504D"},
    ],
    "legend": {
        "url": "https://dea-public-data-dev.s3.ap-southeast-2.amazonaws.com/derivative/ga_s2_ba_provisional_3/dnbr_class_legend_edit.png",
    },
}

style_severe_burncube = {
    "name": "severe_burncube",
    "title": "Burncube Severe",
    "abstract": "burnt area",
    "needed_bands": ["wofssevere"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "wofssevere",
        },
    },
    "value_map": {
        "wofssevere": [
            {
                "title": "Severe",
                "abstract": "",
                "values": [1],
                "color": "#C0504D",
            },
        ]
    },
    "legend": {},
}

style_moderate_burncube = {
    "name": "moderate_burncube",
    "title": "Burncube Moderate",
    "abstract": "burnt area",
    "needed_bands": ["wofsmoderate"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "wofsmoderate",
        },
    },
    "value_map": {
        "wofsmoderate": [
            {
                "title": "Moderate",
                "abstract": "",
                "values": [1],
                "color": "#F79646",
            },
        ]
    },
    "legend": {},
}

layers = {
    "title": "DEA Burncube Burnt Area",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Burncube Burnt Area (Landsat)",
            "name": "ga_ls_nbart_bc_fyear_3_demo",
            "abstract": """Burncube Burnt Area 30m 0.0.0 (Landsat, Collection 3)
            ADD words about the product.
            ADD DOI and collaboration.
            ADD CMI https://cmi.ga.gov.au/data-products/dea/634/dea-mangrove-canopy-cover-landsat
            For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls_nbart_bc_fyear_3_demo",
            "bands": bands_in_burncube,
            "resource_limits": reslim_standard,
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "time_resolution": "year",
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
            },
            "styling": {
                "default_style": "combined_burncube",
                "styles": [
                    style_combined_burncube,
                    style_moderate_burncube,
                    style_severe_burncube,
                ],
            },
        },
    ],
}
