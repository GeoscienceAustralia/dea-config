from ows_refactored.ows_legend_cfg import legend_idx_0_1_5ticks

style_ls_simple_rgb = {
    "name": "simple_rgb",
    "title": "Simple RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {"red": {"red": 1.0}, "green": {"green": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_ls_irg = {
    "name": "infrared_green",
    "title": "False colour - Green, SWIR, NIR",
    "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {"swir1": 1.0},
        "green": {"nir": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_ls_ndvi = {
    "name": "ndvi",
    "title": "NDVI - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nir", "band2": "red"},
    },
    "needed_bands": ["red", "nir"],
    "color_ramp": [
        {"value": -0.0, "color": "#8F3F20", "alpha": 0.0},
        {"value": 0.0, "color": "#8F3F20", "alpha": 1.0},
        {"value": 0.1, "color": "#A35F18"},
        {"value": 0.2, "color": "#B88512"},
        {"value": 0.3, "color": "#CEAC0E"},
        {"value": 0.4, "color": "#E5D609"},
        {"value": 0.5, "color": "#FFFF0C"},
        {"value": 0.6, "color": "#C3DE09"},
        {"value": 0.7, "color": "#88B808"},
        {"value": 0.8, "color": "#529400"},
        {"value": 0.9, "color": "#237100"},
        {"value": 1.0, "color": "#114D04"},
    ],
    "legend": legend_idx_0_1_5ticks,
}


style_ls_ndwi = {
    "name": "ndwi",
    "title": "NDWI - Green, NIR",
    "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "green", "band2": "nir"},
    },
    "needed_bands": ["green", "nir"],
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {
            "value": 0.0,
            "color": "#d8e7f5",
        },
        {"value": 0.1, "color": "#b0d2e8"},
        {
            "value": 0.2,
            "color": "#73b3d8",
        },
        {"value": 0.3, "color": "#3e8ec4"},
        {
            "value": 0.4,
            "color": "#1563aa",
        },
        {
            "value": 0.5,
            "color": "#08306b",
        },
    ],
    "legend": {
        "begin": "0.0",
        "end": "0.5",
        "decimal_places": 1,
        "ticks": ["0.0", "0.2", "0.4", "0.5"],
        "tick_labels": {
            "0.0": {"prefix": "<"},
            "0.2": {"label": "0.2"},
            "0.4": {"label": "0.4"},
            "0.5": {"prefix": ">"},
        },
    },
}

style_ls_mndwi = {
    "name": "mndwi",
    "title": "MNDWI - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "green", "band2": "swir1"},
    },
    "needed_bands": ["green", "swir1"],
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5"},
        {"value": 0.2, "color": "#b0d2e8"},
        {"value": 0.4, "color": "#73b3d8"},
        {"value": 0.6, "color": "#3e8ec4"},
        {"value": 0.8, "color": "#1563aa"},
        {"value": 1.0, "color": "#08306b"},
    ],
    "legend": legend_idx_0_1_5ticks,
}

style_ls_pure_blue = {
    "name": "blue",
    "title": "Blue - 480",
    "abstract": "Blue band, centered on 480nm",
    "components": {"red": {"blue": 1.0}, "green": {"blue": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [0.0, 3000.0],
}


style_ls_pure_green = {
    "name": "green",
    "title": "Green - 560",
    "abstract": "Green band, centered on 560nm",
    "components": {
        "red": {"green": 1.0},
        "green": {"green": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_ls_pure_red = {
    "name": "red",
    "title": "Red - 660",
    "abstract": "Red band, centered on 660nm",
    "components": {"red": {"red": 1.0}, "green": {"red": 1.0}, "blue": {"red": 1.0}},
    "scale_range": [0.0, 3000.0],
}


style_ls_pure_nir = {
    "name": "nir",
    "title": "Near Infrared (NIR) - 840",
    "abstract": "Near infra-red band, centered on 840nm",
    "components": {"red": {"nir": 1.0}, "green": {"nir": 1.0}, "blue": {"nir": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_ls_pure_swir1 = {
    "name": "swir1",
    "title": "Shortwave Infrared (SWIR) - 1650",
    "abstract": "Short wave infra-red band 1, centered on 1650nm",
    "components": {
        "red": {"swir1": 1.0},
        "green": {"swir1": 1.0},
        "blue": {"swir1": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}
style_ls_pure_swir2 = {
    "name": "swir2",
    "title": "Shortwave Infrared (SWIR) - 2220",
    "abstract": "Short wave infra-red band 2, centered on 2220nm",
    "components": {
        "red": {"swir2": 1.0},
        "green": {"swir2": 1.0},
        "blue": {"swir2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

# styles tmad
sdev_scaling = [0.020, 0.18]
edev_scaling = [6.2, 7.3]
bcdev_scaling = [0.025, 0.13]

style_tmad_sdev_std = {
    "name": "arcsec_sdev",
    "title": "Spectral MAD (SMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_arcsec",
        "mapped_bands": True,
        "kwargs": {"band": "sdev", "scale_from": sdev_scaling, "scale_to": [0.0, 4.0]},
    },
    "needed_bands": ["sdev"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nSMAD"},
            "4.0": {"label": "High\nSMAD"},
        },
    },
}

style_tmad_edev_std = {
    "name": "log_edev",
    "title": "Euclidean MAD (EMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {"band": "edev", "scale_from": edev_scaling, "scale_to": [0.0, 4.0]},
    },
    "needed_bands": ["edev"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nEMAD"},
            "4.0": {"label": "High\nEMAD"},
        },
    },
}


style_tmad_bcdev_std = {
    "name": "log_bcdev",
    "title": "Bray-Curtis MAD (BCMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {
            "band": "bcdev",
            "scale_from": bcdev_scaling,
            "scale_to": [0.0, 4.0],
        },
    },
    "needed_bands": ["bcdev"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nBCMAD"},
            "4.0": {"label": "High\nBCMAD"},
        },
    },
}

style_tmad_rgb_std = {
    "name": "tmad_rgb_std",
    "title": "MADs - SMAD, EMAD, BCMAD",
    "abstract": "Good for cropland and forest",
    "components": {
        "red": {
            "function": "datacube_ows.band_utils.single_band_arcsec",
            "mapped_bands": True,
            "kwargs": {
                "band": "sdev",
                "scale_from": sdev_scaling,
            },
        },
        "green": {
            "function": "datacube_ows.band_utils.single_band_offset_log",
            "mapped_bands": True,
            "kwargs": {
                "band": "edev",
                "scale_from": edev_scaling,
            },
        },
        "blue": {
            "function": "datacube_ows.band_utils.single_band_offset_log",
            "mapped_bands": True,
            "kwargs": {
                "band": "bcdev",
                "scale_from": bcdev_scaling,
            },
        },
    },
    "additional_bands": ["sdev", "bcdev", "edev"],
    "legend": {
        "show_legend": True,
        "url": "https://data.dea.ga.gov.au/tmad-annual/geomad.png",
    },
}

style_tmad_rgb_sens = {
    "inherits": style_tmad_rgb_std,
    "name": "tmad_rgb_sens",
    "title": "MADs (desert) - SMAD, EMAD, BCMAD",
    "abstract": "Good for arid land and desert",
    "components": {
        "red": {
            "kwargs": {
                "scale_from": [0.0005, 0.11],
            }
        },
        "green": {
            "kwargs": {
                "scale_from": [5.9, 6.9],
            }
        },
        "blue": {
            "kwargs": {
                "scale_from": [0.008, 0.07],
            }
        },
    },
    "legend": {
        "show_legend": True,
        "url": "https://data.dea.ga.gov.au/tmad-annual/geomad.png",
    },
}


style_gm_count = {
    "name": "count",
    "title": "Clear observation count",
    "abstract": "Count of observations included in geomedian/MAD calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count",
        },
    },
    "needed_bands": ["count"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#890000",
            "alpha": 1,
        },
        {"value": 5, "color": "#990000"},
        {"value": 10, "color": "#E38400"},
        {"value": 15, "color": "#E3DF00"},
        {"value": 20, "color": "#A6E300"},
        {"value": 25, "color": "#00E32D"},
        {"value": 30, "color": "#00E3C8"},
        {"value": 35, "color": "#0097E3"},
        {"value": 40, "color": "#005FE3"},
        {"value": 45, "color": "#000FE3"},
        {"value": 50, "color": "#000EA9"},
        {"value": 55, "color": "#5700E3"},
    ],
    "legend": {
        "begin": "0",
        "end": "50",
        "decimal_places": 0,
        "ticks_every": 10,
        "tick_labels": {
            "50": {"prefix": ">"},
        },
    },
}


styles_c3_ls_list = [
    style_ls_simple_rgb,
    style_ls_irg,
    style_ls_ndvi,
    style_ls_ndwi,
    style_ls_mndwi,
    style_ls_pure_blue,
    style_ls_pure_green,
    style_ls_pure_red,
    style_ls_pure_nir,
    style_ls_pure_swir1,
    style_ls_pure_swir2,
    style_tmad_sdev_std,
    style_tmad_edev_std,
    style_tmad_bcdev_std,
    style_tmad_rgb_std,
    style_tmad_rgb_sens,
    style_gm_count,
]
