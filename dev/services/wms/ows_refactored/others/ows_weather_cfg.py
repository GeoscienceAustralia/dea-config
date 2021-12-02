from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35

bands_weathering = {
    "intensity": [],
}


style_wii = {
    "name": "wii",
    "title": "Weathering Intensity",
    "abstract": "Weather Intensity Index (0-6)",
    "needed_bands": ["intensity"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "intensity",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#ffffff", "alpha": 0},
        {"value": 1, "color": "#2972a8", "legend": {"label": "Low\nClass 1"}},
        {"value": 3.5, "color": "#fcf24b"},
        {"value": 6, "color": "#a02406", "legend": {"label": "High\nClass 6"}},
    ],
    "legend": {
        "begin": 1,
        "end": 6,
        "decimal_places": 0,
        "tick_labels": {
            "1": {"label": "Low\nClass 1"},
            "6": {"label": "High\nClass 6"},
        },
        "strip_location": [0.1, 0.5, 0.8, 0.15],
    },
}

layer = {
    "title": "Weathering Intensity",
    "abstract": "",
    "layers": [
        {
            "title": "Weathering Intensity",
            "name": "weathering_intensity",
            "abstract": """
Weathering intensity or the degree of weathering is an important characteristic of the
earth’s surface that has a significant influence on the chemical and physical properties
of surface materials. Weathering intensity largely controls the degree to which primary
minerals are altered to secondary components including clay minerals and oxides. The
degree of surface weathering is particularly important in Australia where variations in
weathering intensity correspond to the nature and distribution of regolith (weathered
bedrock and sediments) which mantles approximately 90% of the Australian continent. The
weathering intensity prediction has been generated using the Random Forest decision tree
machine learning algorithm. The algorithm is used to establish predictive relationships
between field estimates of the degree of weathering and a comprehensive suite of
covariate or predictive datasets. The covariates used to generate the model include
satellite imagery, terrain attributes, airborne radiometric imagery and mapped geology.
Correlations between the training dataset and the covariates were explored through the
generation of 300 random tree models. An r-squared correlation of 0.85 is reported using
5 K-fold cross-validation. The mean of the 300 models is used for predicting the
weathering intensity and the uncertainty in the weathering intensity is estimated at
each location via the standard deviation in the 300 model values. The predictive
weathering intensity model is an estimate of the degree of surface weathering only. The
interpretation of the weathering intensity is different for in-situ or residual
landscapes compared with transported materials within depositional landscapes. In
residual landscapes, weathering process are operating locally whereas in depositional
landscapes the model is reflecting the degree of weathering either prior to erosion and
subsequent deposition, or weathering of sediments after being deposited. The weathering
intensity model has broad utility in assisting mineral exploration in variably weathered
geochemical landscapes across the Australian continent, mapping chemical and physical
attributes of soils in agricultural landscapes and in understanding the nature and
distribution of weathering processes occurring within the upper regolith.

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "weathering_intensity",
            "bands": bands_weathering,
            "resource_limits": reslim_wms_min_zoom_35,
            "native_crs": "EPSG:4326",
            "native_resolution": [
                0.000833333333347,
                -0.000833333333347,
            ],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "wii",
                "styles": [
                    style_wii,
                ],
            },
        }
    ],
}
