from ows_refactored.ows_reslim_cfg import reslim_standard

# bands definition
bands_in_burncube = {
    "wofssevere": [],
    "wofsmoderate": [],
}

style_burncube = {
    "name": "burncube",
    "title": "TEST area",
    "abstract": "words here",
    "needed_bands": ["wofssevere"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "wofssevere",
        },
    },
    # "pq_masks": pq_ba,
    "value_map": {
        "Burnt area": [
            {
                "title": "Burncube",
                "abstract": "burnt area",
                "color": "#833d08",
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
                "default_style": "burncube",
                "styles": [
                    style_burncube,
                ],
            },
        },
    ],
}
