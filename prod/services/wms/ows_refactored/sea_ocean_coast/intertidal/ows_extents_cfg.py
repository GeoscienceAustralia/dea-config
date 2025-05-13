from ows_refactored.ows_reslim_cfg import reslim_standard

bands_item = {
    "relative": [],
}

bands_item_conf = {
    "stddev": [],
}

style_item_relative = {
    "name": "relative_layer",
    "title": "relative layer",
    "abstract": "The Relative Extents Model (item_v2) 25m v2.0.0",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "relative",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["relative"],
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 1.0, "color": "#d7191c", "alpha": 1.0},
        {
            "value": 2.0,
            "color": "#ec6e43",
        },
        {
            "value": 3.0,
            "color": "#fdb96e",
        },
        {
            "value": 4.0,
            "color": "#fee7a4",
        },
        {
            "value": 5.0,
            "color": "#e7f5b7",
        },
        {
            "value": 6.0,
            "color": "#b7e1a7",
        },
        {
            "value": 7.0,
            "color": "#74b6ad",
        },
        {"value": 8.0, "color": "#2b83ba"},
        {"value": 9.0, "color": "#000000", "alpha": 0.0},
    ],
    "legend": {
        "begin": "0.0",
        "end": "9.0",
        "ticks_every": "1.0",
        "units": "%",
        "decimal_places": 0,
        "tick_labels": {
            "0.0": {"label": "0"},
            "0.1": {"label": "10"},
            "0.2": {"label": "20"},
            "0.3": {"label": "30"},
            "0.4": {"label": "40"},
            "0.5": {"label": "50"},
            "0.6": {"label": "60"},
            "0.7": {"label": "70"},
            "0.8": {"label": "80"},
            "0.9": {"label": "90"},
        },
    },
}

style_item_confidence = {
    "name": "confidence_layer",
    "title": "confidence layer",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev",
        },
    },
    "include_in_feature_info": False,
    "abstract": "The Confidence layer (item_v2_conf) 25m v2.0.0",
    "needed_bands": ["stddev"],
    "color_ramp": [
        {"value": 0.0, "color": "#2b83ba", "alpha": 0.0},
        {"value": 0.01, "color": "#2b83ba"},
        {
            "value": 0.055,
            "color": "#55a1b2",
        },
        {
            "value": 0.1,
            "color": "#80bfab",
        },
        {
            "value": 0.145,
            "color": "#abdda4",
        },
        {
            "value": 0.19,
            "color": "#c7e8ad",
        },
        {
            "value": 0.235,
            "color": "#e3f3b6",
        },
        {
            "value": 0.28,
            "color": "#fdbf6f",
        },
        {
            "value": 0.325,
            "color": "#e37d1c",
        },
        {
            "value": 0.37,
            "color": "#e35e1c",
        },
        {
            "value": 0.415,
            "color": "#e31a1c",
        },
        {
            "value": 0.46,
            "color": "#e31a1c",
        },
        {
            "value": 0.505,
            "color": "#e31a1c",
        },
        {"value": 0.55, "color": "#e31a1c"},
    ],
    "legend": {
        "begin": "0.01",
        "end": "0.55",
        "ticks": ["0.01", "0.55"],
        "tick_labels": {
            "0.01": {"prefix": "<"},
            "0.55": {"prefix": ">"},
        },
        "decimal_places": 2,
        # Why "NDWI"???
        "strip_location": [0.1, 0.5, 0.8, 0.15],
        "units": "NDWI standard deviation",
    },
}

item_v2_00_layer = {
    "title": "Intertidal Extents Model (ITEM)",
    "name": "ITEM_V2.0.0",
    "abstract": """Intertidal Extents Model 25m 2.0.0 (Extents)

The Intertidal Extents Model (ITEM v2.0) product analyses GA’s historic archive of satellite imagery to derive a model of the spatial extents of the intertidal zone throughout the tidal cycle. The model can assist in understanding the relative elevation profile of the intertidal zone,
delineating exposed areas at differing tidal heights and stages.

The product differs from previous methods used to map the intertidal zone which have been predominately focused on analysing a small number of individual satellite images per location (e.g Ryu et al., 2002; Murray et al., 2012).
By utilising a full 30 year time series of observations and a global tidal model (Egbert and Erofeeva, 2002), the methodology enables us to overcome the requirement for clear, high quality observations acquired concurrent to the time of high and low tide.

*Accuracy and limitations*

Due the sun-synchronous nature of the various Landsat sensor observations; it is unlikely that the full physical extents of the tidal range in any cell will be observed. Hence, terminology has been adopted for the product to reflect the highest modelled tide observed in a given cell (HOT) and the lowest modelled tide observed (LOT) (see Sagar et al. 2017). These measures are relative to Mean Sea Level, and have no consistent relationship to Lowest (LAT) and Highest Astronomical Tide (HAT).

The inclusion of the lowest (LMT) and highest (HMT) modelled tide values for each tidal polygon indicates the highest and lowest tides modelled for that location across the full time series by the OTPS model. The relative difference between the LOT and LMT (and HOT and HMT) heights gives an indication of the extent of the tidal range represented in the Relative Extents Model.

As in ITEM v1.0, v2.0 contains some false positive land detection in open ocean regions. These are a function of the lack of data at the extremes of the observed tidal range, and features like glint and undetected cloud in these data poor regions/intervals. Methods to isolate and remove these features are in development for future versions. Issues in the DEA archive and data noise in the Esperance, WA region off Cape Le Grande and Cape Arid (Polygons 236,201,301) has resulted in significant artefacts in the model, and use of the model in this area is not recommended.

The Confidence layer is designed to assess the reliability of the Relative Extent Model. Within each tidal range percentile interval, the pixel-based standard deviation of the NDWI values for all observations in the interval subset is calculated. The average standard deviation across all tidal range intervals is then calculated and retained as a quality indicator in this product layer.

The Confidence Layer reflects the pixel based consistency of the NDWI values within each subset of observations, based on the tidal range. Higher standard deviation values indicate water classification changes not based on the tidal cycle, and hence lower confidence in the extent model.

Possible drivers of these changes include:

Inadequacies of the tidal model, due perhaps to complex coastal bathymetry or estuarine structures not captured in the model. These effects have been reduced in ITEM v2.0 compared to previous versions, through the use of an improved tidal modelling frameworkChange in the structure and exposure of water/non-water features NOT driven by tidal variation.
For example, movement of sand banks in estuaries, construction of man-made features (ports etc.).Terrestrial/Inland water features not influenced by the tidal cycle.
File naming:
THE RELATIVE EXTENTS MODEL v2.0
ITEM_REL_<TIDAL POLYGON NUMBER>_<LONGITUDE>_<LATITUDE>
TIDAL POLYGON NUMBER relates to the id of the tidal polygon referenced by the file
LONGITUDE is the longitude of the centroid of the tidal polygon
LATITUDE is the latitude of the centroid of the tidal polygon

THE CONFIDENCE LAYER v2.0
ITEM_STD_<TIDAL POLYGON NUMBER>_<LONGITUDE>_<LATITUDE>
TIDAL POLYGON NUMBER relates to the id of the tidal polygon referenced by the file
LONGITUDE is the longitude of the centroid of the tidal polygon
LATITUDE is the latitude of the centroid of the tidal polygon

*Overview*

The Intertidal Extents Model product is a national scale gridded dataset characterising the spatial extents of the exposed intertidal zone, at intervals of the observed tidal range (Sagar et al. 2017).The current version (2.0) utilises all Landsat observations (5, 7, and 8) for Australian coastal regions (excluding off-shore Territories) between 1986 and 2016 (inclusive).

ITEM v2.0 has implemented an improved tidal modelling framework (see Sagar et al. 2018) over that utilised in ITEM v1.0. The expanded Landsat archive within the Digital Earth Australia (DEA) has also enabled the model extent to be increased to cover a number of offshore reefs, including the full Great Barrier Reef and southern sections of the Torres Strait Islands.
The DEA archive and new tidal modelling framework has improved the coverage and quality of the ITEM v2.0 relative extents model, particularly in regions where AGDC cell boundaries in ITEM v1.0 produced discontinuities or the imposed v1.0 cell structure resulted in poor quality tidal modelling (see Sagar et al. 2017).

https://knowledge.dea.ga.gov.au/data/product/dea-intertidal-extents-landsat/

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "item_v2",
    "time_resolution": "summary",
    "bands": bands_item,
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "relative_layer",
        "styles": [
            style_item_relative,
        ],
    },
}

item_v2_00_conf_layer = {
    "title": "Intertidal Extents Model (ITEM) confidence",
    "name": "ITEM_V2.0.0_Conf",
    "abstract": """Intertidal Extents Model 25m 2.0.0 (Confidence)

The Intertidal Extents Model (ITEM v2.0) product analyses GA’s historic archive of satellite imagery to derive a model of the spatial extents of the intertidal zone throughout the tidal cycle. The model can assist in understanding the relative elevation profile of the intertidal zone,
delineating exposed areas at differing tidal heights and stages.

The product differs from previous methods used to map the intertidal zone which have been predominately focused on analysing a small number of individual satellite images per location (e.g Ryu et al., 2002; Murray et al., 2012).
By utilising a full 30 year time series of observations and a global tidal model (Egbert and Erofeeva, 2002), the methodology enables us to overcome the requirement for clear, high quality observations acquired concurrent to the time of high and low tide.

*Accuracy and limitations*

Due the sun-synchronous nature of the various Landsat sensor observations; it is unlikely that the full physical extents of the tidal range in any cell will be observed. Hence, terminology has been adopted for the product to reflect the highest modelled tide observed in a given cell (HOT) and the lowest modelled tide observed (LOT) (see Sagar et al. 2017). These measures are relative to Mean Sea Level, and have no consistent relationship to Lowest (LAT) and Highest Astronomical Tide (HAT).

The inclusion of the lowest (LMT) and highest (HMT) modelled tide values for each tidal polygon indicates the highest and lowest tides modelled for that location across the full time series by the OTPS model. The relative difference between the LOT and LMT (and HOT and HMT) heights gives an indication of the extent of the tidal range represented in the Relative Extents Model.

As in ITEM v1.0, v2.0 contains some false positive land detection in open ocean regions. These are a function of the lack of data at the extremes of the observed tidal range, and features like glint and undetected cloud in these data poor regions/intervals. Methods to isolate and remove these features are in development for future versions. Issues in the DEA archive and data noise in the Esperance, WA region off Cape Le Grande and Cape Arid (Polygons 236,201,301) has resulted in significant artefacts in the model, and use of the model in this area is not recommended.

The Confidence layer is designed to assess the reliability of the Relative Extent Model. Within each tidal range percentile interval, the pixel-based standard deviation of the NDWI values for all observations in the interval subset is calculated. The average standard deviation across all tidal range intervals is then calculated and retained as a quality indicator in this product layer.

The Confidence Layer reflects the pixel based consistency of the NDWI values within each subset of observations, based on the tidal range. Higher standard deviation values indicate water classification changes not based on the tidal cycle, and hence lower confidence in the extent model.

Possible drivers of these changes include:

Inadequacies of the tidal model, due perhaps to complex coastal bathymetry or estuarine structures not captured in the model. These effects have been reduced in ITEM v2.0 compared to previous versions, through the use of an improved tidal modelling frameworkChange in the structure and exposure of water/non-water features NOT driven by tidal variation.
For example, movement of sand banks in estuaries, construction of man-made features (ports etc.).Terrestrial/Inland water features not influenced by the tidal cycle.
File naming:
THE RELATIVE EXTENTS MODEL v2.0
ITEM_REL_<TIDAL POLYGON NUMBER>_<LONGITUDE>_<LATITUDE>
TIDAL POLYGON NUMBER relates to the id of the tidal polygon referenced by the file
LONGITUDE is the longitude of the centroid of the tidal polygon
LATITUDE is the latitude of the centroid of the tidal polygon

THE CONFIDENCE LAYER v2.0
ITEM_STD_<TIDAL POLYGON NUMBER>_<LONGITUDE>_<LATITUDE>
TIDAL POLYGON NUMBER relates to the id of the tidal polygon referenced by the file
LONGITUDE is the longitude of the centroid of the tidal polygon
LATITUDE is the latitude of the centroid of the tidal polygon

*Overview*

The Intertidal Extents Model product is a national scale gridded dataset characterising the spatial extents of the exposed intertidal zone, at intervals of the observed tidal range (Sagar et al. 2017).The current version (2.0) utilises all Landsat observations (5, 7, and 8) for Australian coastal regions (excluding off-shore Territories) between 1986 and 2016 (inclusive).

ITEM v2.0 has implemented an improved tidal modelling framework (see Sagar et al. 2018) over that utilised in ITEM v1.0. The expanded Landsat archive within the Digital Earth Australia (DEA) has also enabled the model extent to be increased to cover a number of offshore reefs, including the full Great Barrier Reef and southern sections of the Torres Strait Islands.
The DEA archive and new tidal modelling framework has improved the coverage and quality of the ITEM v2.0 relative extents model, particularly in regions where AGDC cell boundaries in ITEM v1.0 produced discontinuities or the imposed v1.0 cell structure resulted in poor quality tidal modelling (see Sagar et al. 2017).

https://knowledge.dea.ga.gov.au/data/product/dea-intertidal-extents-landsat/

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "item_v2_conf",
    "bands": bands_item_conf,
    "resource_limits": reslim_standard,
    "time_resolution": "summary",
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val2",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "confidence_layer",
        "styles": [
            style_item_confidence,
        ],
    },
}
