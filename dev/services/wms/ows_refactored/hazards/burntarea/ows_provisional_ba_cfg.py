from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

bands_ba_rasters = {
    "delta_bsi": [],
    "delta_ndvi": [],
    "delta_nbr": [],
}

style_dbsi = {
    "name": "ga_s2_dbsi_provisional_3",
    "title": "Delta Bare Soil Index (dBSI)",
    "abstract": """
        Delta Bare Soil Index (dBSI) based on Sentinel 2 Near Real-Time (Provisional) Surface Reflectance and Sentinel 2 Barest Earth Data.

        Bare Soil Index (BSI) identifies soil or bare-land characteristics by combining blue, red, near infrared (NIR), and short wave infrared (SWIR) spectral bands. SWIR and red spectral bands can be used to identify basic soil mineralogy while blue and NIR spectral bands can help to detect vegetation.
        BSI (Rikimaru and Miyatake 2002) is calculated as: BSI = ((SWIR2 + RED) - (NIR + BLUE)) / ((SWIR2 + RED) + (NIR + BLUE)).

        Delta BSI (dBSI) shows the change in soil characteristics between two events, the difference between a baseline (pre-BSI) and a latter time (post-BSI). The change (delta) in BSI is calculated as: dBSI = pre-BSI - post-BSI.

        This dBSI product is based on two input datasets:
         1) The baseline (pre) BSI is calculated on DEA Sentinel 2 Barest Earth (Roberts, et al. 2019).
         2) The latter (post) BSI is calculated on the latest daily Sentinel-2 (A and B combined) Near Real-Time provisional data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.
        The larger the positive dBSI value, the more the area shows characteristics of being burnt. This metric should be used in combination with the other datasets to strengthen the agreement that the area has indeed been burnt.

        For service status information, see https://status.dea.ga.gov.au
        """,
    "needed_bands": ["delta_bsi"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "delta_bsi",
        },
    },
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "enum": 0,
        }
    ],
    "range": [-1, 1],
    "mpl_ramp": "PuOr_r",
    "legend": {
        "begin": "-1",
        "end": "1",
        "tick_labels": {
            "-1.0": {"label": "<-1"},
            "0": {"label": "0"},
            "1.0": {"label": ">1"},
        },
        "decimal_places": 0,
        "title": "dBSI\n(larger values can be characteristic of burnt areas)",
    },
}

style_dndvi = {
    "name": "ga_s2_ndvi_provisional_3",
    "title": "Delta Normalized Difference Vegetation Index (dNDVI)",
    "abstract": """
        Delta Normalized Difference Vegetation Index (dNDVI) based on Sentinel 2 Near Real-Time (Provisional) Surface Reflectance and Sentinel 2 Barest Earth Data.

        Normalized Difference Vegetation Index (NDVI) Normalized Difference Vegetation Index (NDVI) is used to detect green vegetation characteristics by identifying the difference between red/visible and near infrared (NIR) spectral bands.
        NDVI is calculated as: NDVI =  (NIR - RED)/(NIR + RED).

        Delta NDVI (dNDVI) shows the change in vegetation characteristics between two events, the difference between a baseline (pre-NDVI) and a latter time (post-NDVI). The change (delta) in NDVI is calculated as: dNDVI = pre-ndvi - post-NDVI.

        This dNDVI product is based on two input datasets:
         1) The baseline (pre) NDVI is calculated on DEA Sentinel 2 Barest Earth (Roberts, et al. 2019).
         2) The latter (post) NDVI is calculated on the latest daily Sentinel-2 (A and B combined) Near Real-Time provisional data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

        The larger the positive dNDVI value, the more the area shows characteristics of being burnt. This metric should be used in combination with the other datasets to strengthen the agreement that the area has indeed been burnt.

        For service status information, see https://status.dea.ga.gov.au
        """,
    "needed_bands": ["delta_ndvi"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "delta_ndvi",
        },
    },
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "enum": 0,
        }
    ],
    "range": [-1, 1],
    "mpl_ramp": "PuOr",
    # "mpl_ramp": "RdYlGn_r",
    "legend": {
        "begin": "-1",
        "end": "1",
        "tick_labels": {
            "-1.0": {"label": "<-1"},
            "0": {"label": "0"},
            "1.0": {"label": ">1"},
        },
        "decimal_places": 0,
        "title": "dNDVI\n(smaller values can be characteristic of burnt areas)",
    },
}

style_dnbr = {
    "name": "ga_s2_dnbr_provisional_3",
    "title": "Delta Normalized Burn Ratio (dNBR)",
    "abstract": """
        Delta Normalized Burn Ratio (DNBR) based on Sentinel 2 Near Real-Time (Provisional) Surface Reflectance and Sentinel 2 Barest Earth Data.

        Normalized Burn Ratio (NBR) identifies areas that have the characteristics of being burnt. NBR looks at the relationship between near infrared (NIR) and short wave infrared (SWIR) spectral signatures. High SWIR reflectance values with low NIR reflectance values are indicative of an area that has been burnt by fire(s), while the opposite is seen in healthy vegetation.
        NBR is calculated as: NBR = (NIR – SWIR2) / (NIR + SWIR2).

        Delta NBR shows the change in burn characteristics between two events, the difference between a baseline (pre-NBR) and a latter time (post-NBR). The change (delta) in NBR is calculated as: dNBR = pre-NBR - post-NBR.

        Normally dNBR analysis is run on data from a clear pre-fire and a post-fire satellite scene. However, in order to rapidly identify areas that are characteristic of burns for all of Australia, and on a near real-time basis, this dNBR product is based on two input datasets:
         1) The baseline (pre) NBR is calculated on DEA Sentinel 2 Barest Earth (Roberts, et al. 2019).
         2) The latter (post) NBR is calculated on the latest daily Sentinel-2 (A and B combined) Near Real-Time provisional data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.
        Therefore, this dNBR data is a general screening tool to identify areas that are likely to have undergone burn. dNBR is a basic metric that can be used to identify areas that show characteristics of burn, but there is no guarantee that values are precise. For example, Land-use change, such as deforestation or changes to water bodies, can often be identified as false positives.

        The larger the positive dNBR value, the more the area shows characteristics of being burnt. This metric should be used in combination with the other datasets to strengthen the agreement that the area has indeed been burnt.

        For service status information, see https://status.dea.ga.gov.au

        """,
    "needed_bands": ["delta_nbr"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "delta_nbr",
        },
    },
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "enum": 0,
        }
    ],
    "range": [-1, 1],
    "mpl_ramp": "PuOr_r",
    "legend": {
        "begin": "-1",
        "end": "1",
        "tick_labels": {
            "-1.0": {"label": "<-1"},
            "0": {"label": "0"},
            "1.0": {"label": ">1"},
        },
        "decimal_places": 0,
        "title": "dNBR\n(larger values can be characteristic of burnt areas)",
    },
}

style_dnbr_classes = {
    "name": "ga_s2_dnbrclasses_provisional_3",
    "title": "Delta Normalized Burn Ratio (dNBR) Classes",
    "abstract": """
        Delta Normalized Burn Ratio (DNBR) based on Sentinel 2 Near Real-Time (Provisional) Surface Reflectance and Sentinel 2 Barest Earth Data.

        Burn classes and thresholds are a simplified version of those proposed by USGS. Color coding established by UN-SPIDER.

        Normalized Burn Ratio (NBR) identifies areas that have the characteristics of being burnt. NBR looks at the relationship between near infrared (NIR) and short wave infrared (SWIR) spectral signatures. High SWIR reflectance values with low NIR reflectance values are indicative of an area that has been burnt by fire(s), while the opposite is seen in healthy vegetation.
        NBR is calculated as: NBR = (NIR – SWIR2) / (NIR + SWIR2).

        Delta NBR (dNBR) shows the change in burn characteristics between two events, the difference between a baseline (pre-NBR) and a latter time (post-NBR). The change (delta) in NBR is calculated as: dNBR = pre-NBR - post-NBR.

        Normally dNBR analysis is run on data from a clear pre-fire and a post-fire satellite scene. However, in order to rapidly identify areas that are characteristic of burns for all of Australia, and on a near real-time basis, this dNBR product is based on two input datasets:
         1) The baseline (pre) NBR is calculated on DEA Sentinel 2 Barest Earth (Roberts, et al. 2019).
         2) The latter (post) NBR is calculated on the latest daily Sentinel-2 (A and B combined) Near Real-Time provisional data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.
        Therefore, this dNBR data is a general screening tool to identify areas that are likely to have undergone burn. dNBR is a basic metric that can be used to identify areas that show characteristics of burn, but there is no guarantee that values are precise. For example, Land-use change, such as deforestation or changes to water bodies, can often be identified as false positives.

        The larger the positive dNBR value, the more the area shows characteristics of being burnt. This metric should be used in combination with the other datasets to strengthen the agreement that the area has indeed been burnt.

        For service status information, see https://status.dea.ga.gov.au
        """,
    "needed_bands": ["delta_nbr"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "delta_nbr",
        },
    },
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "enum": 0,
        }
    ],
    "range": [-1, 1],
    "color_ramp": [
        {"value": -1.0, "color": "#0be344", },
        {"value": 0.1, "color": "#0be344", },
        {"value": 0.10001, "color": "#f8fc11", },
        {"value": 0.44, "color": "#f8671a", },
        {"value": 1.0, "color": "#f8671a", },
    ],
    "legend": {
        "title": "dNBR classes",
        "begin": "-1.0",
        "end": "1.0",
        "ticks": ["-1.0", "-0.45", "0.1", "0.27", "0.44", "0.72", "1.0"],
        "tick_labels": {
            "-1.0": "-1.0",
            "-0.45": "Unburnt",
            "0.1": "0.1",
            "0.27": "Low to\nModerate",
            "0.44": "0.44",
            "0.72": "Moderate to\nSevere",
            "1.0": "1.0",
        },
    },
}

layers = {
    "title": "DEA Burnt Area Input Datasets (Provisional, NRT Sentinel 2) ",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Burnt Area Characteristic Layers (Provisional, NRT Sentinel 2)",
            "name": "ga_s2_ba_provisional_3",
            "abstract": """ text here, currently working on it""",
            "product_name": "ga_s2_ba_provisional_3",
            "bands": bands_ba_rasters,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "dynamic": True,
            "native_crs": "EPSG:3577",
            "native_resolution": [10.0, 10.0],
            "flags": [
                {
                    "band": "land",
                    "product": "geodata_coast_100k",
                    "ignore_time": True,
                    "ignore_info_flags": [],
                },
            ],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },

            "wcs": {
                "default_bands": [
                    "delta_nbr",
                    "delta_bsi",
                    "delta_ndvi",
                ],
            },
            "styling": {
                "default_style": "ga_s2_dnbr_provisional_3",
                "styles": [style_dnbr, style_dnbr_classes, style_dbsi, style_dndvi],
            },
        },
    ],
}