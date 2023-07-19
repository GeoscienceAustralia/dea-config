from ows_refactored.ows_reslim_cfg import reslim_standard

# bands definition
bands_in_burncube = {
    "wofssevere": [],
    "wofsmoderate": [],
}

style_combined_burncube = {
    "name": "combined_burncube",
    "title": "BurnCube: Burnt Area",
    "abstract": "",
    "needed_bands": ["wofssevere", "wofsmoderate"],
    "index_expression": "2*wofssevere + wofsmoderate",
    "color_ramp": [
        {"value": 0.0, "color": "#FFFFFF", "alpha": 0.0},
        {"value": 1, "color": "#F79646"},
        {"value": 2, "color": "#C0504D"},
    ],
    "legend": {
        "url": "https://dea-public-data-dev.s3-ap-southeast-2.amazonaws.com/projects/burn_cube/legend_combined.png",
    },
}

style_severe_burncube = {
    "name": "severe_burncube",
    "title": "BurnCube: Severe",
    "abstract": "burnt area",
    "needed_bands": ["wofssevere"],
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
    "title": "BurnCube: Moderate",
    "abstract": "burnt area",
    "needed_bands": ["wofsmoderate"],
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
    "title": "DEA BurnCube Historic Burnt Area",
    "abstract": "",
    "layers": [
        {
            "title": "DEA BurnCube Historic Burnt Area Financial Year (Landsat)",
            "name": "ga_ls8c_nbart_bc_fyear_3",
            "abstract": """BurnCube Historic Burnt Area, Financial Year, 30m, 0.0.0 (Landsat, Collection 3)

Bushfires pose a serious and increasing threat to Australia. The detection and mapping of burns have many applications to support communities and ecosystems impacted by fire. Digital Earth Australia (DEA) offer a preliminary data product which was developed in collaboration with the Australian National University (ANU) to map historic burns with Landsat 8 data within continental Australia.

The BurnCube burnt area method is presented in (Renzullo et al. 2019) and analyses spectral anomalies. The method starts by using four years’ worth of satellite data to generate a Geomedian (Roberts, et al. 2017) which represents the average landscape over that time period. Next, the BurnCube burnt area method takes the following years’ worth of satellite data and detects deviations from the normal spectrum of each pixel (i.e. the difference of an area of land to the normal landscape over the last four years).

BurnCube Historic Burnt Area is styled in three layers; “Moderate Burn”, “Severe Burn”, and “Combined Burn: Moderate and Severe”. Each layer contains identifies area that have shown the characteristic being burnt during that financial year.

This data is preliminary and provisional in nature and is still undergoing further development. These metrics should be used as a preliminary screening tool, and not an accurate identification of fire extent. These metrics should be used in combination with each other and can be used with other datasets to strengthen the agreement that the area has indeed been burnt. No decisions on life or property should be made based on this data.

Renzullo, L & Tian, Siyuan & van Dijk, Albert & Rozas Larraondo, Pablo & Yebra, Marta & Yuan, F & Mueller, N. (2019). Burn extent and severity mapping by spectral anomaly detection in the Landsat data cube.

Roberts, Dale & Mueller, Norman & McIntyre, Alexis. (2017). High-Dimensional Pixel Composites From Earth Observation Time Series. IEEE Transactions on Geoscience and Remote Sensing. PP. 1-11. 10.1109/TGRS.2017.2723896.

Draft CMI https://cmi.ga.gov.au/data-products/dea/841/draft...-burncube-historic-burnt-area

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls8c_nbart_bc_fyear_3",
            "bands": bands_in_burncube,
            "resource_limits": reslim_standard,
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "time_resolution": "summary",
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
