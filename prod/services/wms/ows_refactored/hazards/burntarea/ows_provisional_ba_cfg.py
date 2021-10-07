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
BSI (Rikimaru et. al 2002) is calculated as: BSI = ((SWIR2 + RED) - (NIR + BLUE)) / ((SWIR2 + RED) + (NIR + BLUE)).

Delta BSI (dBSI) shows a change in soil characteristics as the difference between a baseline (baseline-BSI) and post event (NRT-BSI). The change (delta) in BSI is calculated as: dBSI = (baseline-BSI - NRT-BSI) * -1.
dBSI is multiplied by negative 1 in order to reverse the scale so that dBSI values are presented the same way as the other delta indexes, which both have positive values for areas that show burnt characteristics.

This dBSI product is based on two input datasets:
    1) The baseline BSI is calculated on DEA Sentinel 2 Barest Earth (Roberts, et al. 2019).
    2) The post event (NRT-BSI) is calculated on the latest daily Sentinel-2 (A and B combined) Near Real-Time provisional data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.
The dBSI layer contains values between -1 and +1, with a positive value being more indicative that an area has increased exposure of bare soil, and therefore the characteristics a burn.
This metric should be used in combination with the other datasets to strengthen the agreement that the area has indeed been burnt.

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
        "url": "https://dea-public-data-dev.s3-ap-southeast-2.amazonaws.com/derivative/ga_s2_ba_provisional_3/dbsi_legend_edit.png",
    },
}

style_dndvi = {
    "name": "ga_s2_dndvi_provisional_3",
    "title": "Delta Normalized Difference Vegetation Index (dNDVI)",
    "abstract": """
Delta Normalized Difference Vegetation Index (dNDVI) based on Sentinel 2 Near Real-Time (Provisional) Surface Reflectance and Sentinel 2 Barest Earth Data.

Normalized Difference Vegetation Index (NDVI) is used to detect green vegetation characteristics by identifying the difference between red/visible and near infrared (NIR) spectral bands (Huete and Jackson 1987).

NDVI is calculated as: NDVI =  (NIR - RED)/(NIR + RED).
Delta NDVI (dNDVI) shows the change in vegetation characteristics as the difference between a reference baseline (baseline-NDVI) and post event (NRT-NDVI). The change (delta) in NDVI is calculated as: dNDVI = baseline-NDVI - NRT-NDVI.

This dNDVI product is based on two input datasets:
    1) The baseline NDVI is calculated on DEA Sentinel 2 Barest Earth (Roberts, et al. 2019).
    2) The post event NDVI is calculated on the latest daily Sentinel-2 (A and B combined) Near Real-Time provisional data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.
The dNDVI layer contains values between -1 and +1, with positive values being more indicative that the presence of green vegetation in an area has decreased, and therefore showing the characteristics of a burn.
This metric should be used in combination with the other datasets to strengthen the agreement that the area has indeed been burnt.

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
    "mpl_ramp": "PuOr_r",
    "legend": {
        "url": "https://dea-public-data-dev.s3-ap-southeast-2.amazonaws.com/derivative/ga_s2_ba_provisional_3/dndvi_legend_edit.png",
    },
}

style_dnbr = {
    "name": "ga_s2_dnbr_provisional_3",
    "title": "Delta Normalized Burn Ratio (dNBR)",
    "abstract": """
Delta Normalized Burn Ratio (dNBR) based on Sentinel 2 Near Real-Time (Provisional) Surface Reflectance and Sentinel 2 Barest Earth Data.

Normalized Burn Ratio (NBR) identifies areas that have the characteristics of being burnt. NBR looks at the relationship between near infrared (NIR) and short wave infrared (SWIR) spectral signatures. High SWIR reflectance values with low NIR reflectance values are indicative of an area that has been burnt by fire(s), while the opposite is seen in healthy vegetation (Wagtendonk et al. 2004).

NBR is calculated as: NBR = (NIR – SWIR2) / (NIR + SWIR2).
Delta NBR shows the change in burn characteristics as the difference between a baseline (baseline-NBR) and a post event (NRT-NBR). The change (delta) in NBR is calculated as: dNBR = baseline_NBR - NRT_NBR.

Normally dNBR analysis is run on data from a clear pre-fire and a post-fire satellite scene. However, in order to rapidly identify areas that are characteristic of burns for all of Australia, and on a near real-time basis, this dNBR product is based on two input datasets:
    1) The baseline NBR is calculated on DEA Sentinel 2 Barest Earth (Roberts, et al. 2019).
    2) The post event NBR (NRT-NBR) is calculated on the latest daily Sentinel-2 (A and B combined) Near Real-Time provisional data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

The dNBR data is a general screening tool to identify areas that are likely to have undergone burn. dNBR is a basic metric that can be used to identify areas that show characteristics of burn, but there is no guarantee that values are precise. For example, Landcover change, such as deforestation or changes to water bodies, can often be identified as false positives.

The delta NBR layer contains values between -1 and +1, with positive values being more indicative that an area has undergone a burn. This metric should be used in combination with the other datasets to strengthen the agreement that the area has indeed been burnt.

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
        "ticks": ["-1", "0", "1"],
        "tick_labels": {
            "-1": {"label": "-1"},
            "0": {"label": "0"},
            "1": {"label": "1"},
        },
        "decimal_places": 0,
        "title": "dNBR\n(larger positive values can be characteristic of burns)",
    },
}

style_dnbr_classes = {
    "name": "ga_s2_dnbrclasses_provisional_3",
    "title": "Delta Normalized Burn Ratio (dNBR) Classes",
    "abstract": """
Delta Normalized Burn Ratio (DNBR) based on Sentinel 2 Near Real-Time (Provisional) Surface Reflectance and Sentinel 2 Barest Earth Data.

Burn classes and thresholds are a simplified version of those proposed by USGS, as "Unburnt", "Low to Medium" and "High to Severe". Colour coding was established by UN-SPIDER.

Normalized Burn Ratio (NBR) identifies areas that have the characteristics of being burnt. NBR looks at the relationship between near infrared (NIR) and short wave infrared (SWIR) spectral signatures. High SWIR reflectance values with low NIR reflectance values are indicative of an area that has been burnt by fire(s), while the opposite is seen in healthy vegetation (Wagtendonk et al. 2004).

NBR is calculated as: NBR = (NIR – SWIR2) / (NIR + SWIR2).
Delta NBR (dNBR) shows the change in burn characteristics as the difference between a baseline (baseline-NBR) and post-event (NRT-NBR). The change (delta) in NBR is calculated as: dNBR = baseline-NBR - NRT-NBR.

Normally dNBR analysis is run on data from a clear pre-fire and a post-fire satellite scene. However, in order to rapidly identify areas that are characteristic of burns for all of Australia, and on a near real-time basis, this dNBR product is based on two input datasets:
    1) The baseline NBR is calculated on DEA Sentinel 2 Barest Earth (Roberts, et al. 2019).
    2) The post event NBR (NRT-NBR) is calculated on the latest daily Sentinel-2 (A and B combined) Near Real-Time provisional data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

This dNBR data is a general screening tool to identify areas that are likely to have undergone burn. dNBR is a basic metric that can be used to identify areas that show characteristics of burn, but there is no guarantee that values are precise. For example, Landcover change, such as deforestation or changes to water bodies, can often be identified as false positives.

The delta NBR layer contains values between -1 and +1, with positive values being more indicative that an area has undergone a burn. This metric should be used in combination with the other datasets to strengthen the agreement that the area has indeed been burnt.

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
        {"value": -1.0, "color": "#0be344"},
        {"value": 0.0999, "color": "#0be344"},
        {"value": 0.10, "color": "#f8fc11"},
        {"value": 0.4399, "color": "#f8fc11"},
        {"value": 0.44, "color": "#f8671a"},
        {"value": 1.0, "color": "#f8671a"},
    ],
    "legend": {
        "url": "https://dea-public-data-dev.s3.ap-southeast-2.amazonaws.com/derivative/ga_s2_ba_provisional_3/dnbr_class_legend_edit.png",
    },
}

layers = {
    "title": "DEA Burnt Area Characteristic Layers (Sentinel 2 Near Real-Time, Provisional)",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Burnt Area Characteristic Layers (Sentinel 2 Near Real-Time, Provisional)",
            "name": "ga_s2_ba_provisional_3",
            "abstract": """
Bushfires pose a serious and increasing threat to Australia. The detection and mapping of burns have many applications to support communities and ecosystems impacted by fire. However, the identification of bushfire burn using Earth Observation is often manual, can come with a significant time delay, and at a relatively small scale. Digital Earth Australia (DEA) offer a provisional and preliminary change detection data product, for all of Australia, which uses same day satellite data and cloud-based infrastructure to automatically and rapidly identify areas that show burn characteristics.

Commonly, burnt area analysis is run on data from manually selected, cloud-free, pre-fire and post-fire satellite scenes. Automating the rapid identification of pre- and post-fire scenes is problematic due to cloud cover, differing fire duration, and the difficulty in automatically identifying a suitable pre-fire scene. Therefore, Analysing the change between a pre-fire reference baseline and the latest near real-time satellite data enables rapid, automatic, screening of areas that have changed to show characteristics of undergoing a burn.

This Near Real-Time (NRT) change detection product is based on:

-	a pre-fire reference baseline (baseline-metric) dataset; DEA Sentinel 2 Barest Earth (Roberts, et al. 2019). The Barest Earth data shows the spectral data for an area at its least vegetated state based on the Sentinel 2 data archive. The Barest Earth product is produced by a novel high-dimensional statistical technique that extracts a noise-reduced, cloud-free, and robust estimate of the spectral response of the barest state.
-	the latest (NRT-metric) daily Sentinel-2 (A and B combined) Near Real-Time provisional satellite data. The NRT service provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

The following metrics were calculated to identify burnt area characteristics:
-	Bare Soil Index (BSI)
-	Normalized Difference Vegetation Index (NDVI)
-	Normalized Burn Ratio (NBR)

Change (delta) in each metric was calculated by differencing the baseline metric and the post event (NRT) metric. Each delta layer contains values between -1 and +1, with positive values being more characterisitc of a burn.

These layers have been produced as input data into a burnt area vectorisor tool (link will be provided when in production). This data is preliminary and provisional in nature and is still undergoing further development.

These metrics should be used as a preliminary screening tool, and not an accurate identification of fire extent. These metrics should be used in combination with each other and can be used with other datasets to strengthen the agreement that the area has indeed been burnt. No decisions on life or property should be made based on this data.


**Bare Soil**

Bare Soil Index (BSI) identifies soil or bare-land characteristics by combining blue, red, near infrared (NIR), and short wave infrared (SWIR) spectral bands. SWIR and red spectral bands can be used to identify basic soil mineralogy while blue and NIR spectral bands can help to detect vegetation.

BSI (Rikimaru et al. 2002) is calculated as: BSI = ((SWIR2 + RED) - (NIR + BLUE)) / ((SWIR2 + RED) + (NIR + BLUE)).

Delta BSI (dBSI) shows the change in soil characteristics as the difference between a baseline BSI and a post event BSI (NRT-BSI). The change (delta) in BSI is calculated as: dBSI = (baseline-BSI - NRT-BSI) * -1. Delta BSI is multiplied by negative 1 in order to reverse the scaling so that it can be presented the same way as the other delta indexes, which all have positive values for areas that shows characteristics of being burnt.


**Vegetation**

Normalized Difference Vegetation Index (NDVI) is used to detect green vegetation characteristics by identifying the difference between red/visible and near infrared (NIR) spectral bands (Huete and Jackson 1987).

NDVI is calculated as: NDVI = (NIR - RED)/(NIR + RED).

Delta NDVI (dNDVI) shows the change in vegetation characteristics as the difference between a baseline-NDVI and a post event NDVI (NRT-NDVI). The change (delta) in NDVI is calculated as: dNDVI = baseline-NDVI - NRT-NDVI.


**Burnt area**

Normalized Burn Ratio (NBR) identifies areas that have the characteristics of being burnt. NBR looks at the relationship between near infrared (NIR) and short wave infrared (SWIR) spectral signatures. High SWIR reflectance values with low NIR reflectance values are indicative of an area that has been burnt by fire(s), while the opposite is seen in healthy vegetation.

NBR is calculated as: NBR = (NIR – SWIR2) / (NIR + SWIR2).

Delta NBR shows the change in burn characteristics as the difference between a baseline-NBR and a post event NBR (NRT-NBR). The change (delta) in NBR is calculated as: dNBR = baseline-NBR - NRT-NBR.

Normally dNBR analysis is run on data from a clear pre-fire and a post-fire satellite scene. However, in order to automatically and rapidly identify areas that are characteristic of burns for all of Australia, and on a near real-time basis, the Sentinel 2 Barest Earth layer has been used as a conservative pre-fire reference image.
dNBR is styled in two layers, as a colour ramp between -1 and +1, and also as a thresholded class layer. Burn classes and thresholds values are a simplified version of those proposed by USGS, as "Unburnt", "Low to Medium" and "High to Severe". Colour coding was established by UN-SPIDER.

For service status information, see https://status.dea.ga.gov.au
            """,
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
