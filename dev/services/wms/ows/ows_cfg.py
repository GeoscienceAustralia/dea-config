# Migration of wms_cfg.py.  As at commit  c44c5e61c7fb9

# Reusable Chunks 1. Resource limit configurations

reslim_landsat = {
    "wms": {
        "zoomed_out_fill_colour": [150,180,200,160],
        "min_zoom_factor": 35.0,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    }
}

reslim_mangrove = {
    "wms": {
        "zoomed_out_fill_colour": [150,180,200,160],
        "min_zoom_factor": 15.0,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    }
}

reslim_wofs = reslim_mangrove

reslim_wofs_obs = reslim_landsat

reslim_s2 = reslim_mangrove

reslim_s2_ard = reslim_landsat

reslim_multi_topog = reslim_landsat

reslim_weathering = reslim_mangrove

# Reusable Chunks 2. Band lists.

bands_ls8 = {
    "red": [],
    "green": [],
    "blue": [ ],
    "nir": [ "near_infrared" ],
    "swir1": [ "shortwave_infrared_1", "near_shortwave_infrared" ],
    "swir2": [ "shortwave_infrared_2", "far_shortwave_infrared" ],
    "coastal_aerosol": [ ],
}

bands_ls = {
    "red": [],
    "green": [],
    "blue": [ ],
    "nir": [ "near_infrared" ],
    "swir1": [ "shortwave_infrared_1", "near_shortwave_infrared" ],
    "swir2": [ "shortwave_infrared_2", "far_shortwave_infrared" ],
}

bands_mangrove = {
    "canopy_cover_class": [],
    "extent": [],
}

bands_wofs_filt_sum = {
    "confidence": []
}

bands_wofs_sum = {
    "count_wet": [],
    "count_clear": [],
    "frequency": [],
}

bands_wofs_obs = {
    "water": [],
}

bands_sentinel2 = {
    "nbar_coastal_aerosol": [ 'nbar_narrow_blue' ],
    "nbar_blue": [],
    "nbar_green": [],
    "nbar_red": [],
    "nbar_red_edge_1": [],
    "nbar_red_edge_2": [],
    "nbar_red_edge_3": [],
    "nbar_nir_1":  [ "nbar_near_infrared_1" ],
    "nbar_nir_2":  [ "nbar_near_infrared_2" ],
    "nbar_swir_2": [ "nbar_shortwave_infrared_2" ],
    "nbar_swir_3": [ "nbar_shortwave_infrared_3" ],
    "nbart_coastal_aerosol": [ 'coastal_aerosol', 'nbart_narrow_blue', 'narrow_blue'],
    "nbart_blue": [ 'blue' ],
    "nbart_green": [ 'green' ],
    "nbart_red": [ 'red' ],
    "nbart_red_edge_1": [ 'red_edge_1' ],
    "nbart_red_edge_2": [ 'red_edge_2' ],
    "nbart_red_edge_3": [ 'red_edge_3' ],
    "nbart_nir_1":  [ "nir", "nir_1", "nbart_near_infrared_1" ],
    "nbart_nir_2":  [ "nir_2", "nbart_near_infrared_2" ],
    "nbart_swir_2": [ "swir_2", "nbart_shortwave_infrared_2" ],
    "nbart_swir_3": [ "swir_3", "nbart_shortwave_infrared_3" ],

    "quality": [],
}

bands_multi_topog = {
    "regional": [], 
    "intermediate": [], 
    "local": [], 

bands_weathering = {
    "intensity": [], 
}

# Reusable Chunks 3. Styles

style_ls_simple_rgb = {
        "name": "simple_rgb",
        "title": "Simple RGB",
        "abstract": "Simple true-colour image, using the red, green and blue bands",
        "components": {
            "red": {
                "red": 1.0
            },
            "green": {
                "green": 1.0
            },
            "blue": {
                "blue": 1.0
            }
        },
        "scale_range": [0.0, 3000.0]
}

style_ls_irg = {
    "name": "infrared_green",
    "title": "False colour - Green, SWIR, NIR",
    "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {
            "swir1": 1.0
        },
        "green": {
            "nir": 1.0
        },
        "blue": {
            "green": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_ls_ndvi = {
    "name": "ndvi",
    "title": "NDVI - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "pass_product_cfg": True,
        "kwargs": {
            "band1": "nir",
            "band2": "red"
        }
    },
    "needed_bands": ["red", "nir"],
    "color_ramp": [
        {
            "value": -0.0,
            "color": "#8F3F20",
            "alpha": 0.0
        },
        {
            "value": 0.0,
            "color": "#8F3F20",
            "alpha": 1.0
        },
        {
            "value": 0.1,
            "color": "#A35F18"
        },
        {
            "value": 0.2,
            "color": "#B88512"
        },
        {
            "value": 0.3,
            "color": "#CEAC0E"
        },
        {
            "value": 0.4,
            "color": "#E5D609"
        },
        {
            "value": 0.5,
            "color": "#FFFF0C"
        },
        {
            "value": 0.6,
            "color": "#C3DE09"
        },
        {
            "value": 0.7,
            "color": "#88B808"
        },
        {
            "value": 0.8,
            "color": "#529400"
        },
        {
            "value": 0.9,
            "color": "#237100"
        },
        {
            "value": 1.0,
            "color": "#114D04"
        }
    ]
}

style_ls_ndwi = {
    "name": "ndwi",
    "title": "NDWI - Green, NIR",
    "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "pass_product_cfg": True,
        "kwargs": {
            "band1": "green",
            "band2": "nir"
        }
    },
    "needed_bands": ["green", "nir"],
    "color_ramp": [
        {
            "value": -0.1,
            "color": "#f7fbff",
            "alpha": 0.0
        },
        {
            "value": 0.0,
            "color": "#d8e7f5",
            "legend": {
                "prefix": "<"
            }
        },
        {
            "value": 0.1,
            "color": "#b0d2e8"
        },
        {
            "value": 0.2,
            "color": "#73b3d8",
            "legend": { }
        },
        {
            "value": 0.3,
            "color": "#3e8ec4"
        },
        {
            "value": 0.4,
            "color": "#1563aa",
            "legend": { }
        },
        {
            "value": 0.5,
            "color": "#08306b",
            "legend": {
                "prefix": ">"
            }
        }
    ]
}

style_ls_mndwi = {
    "name": "mndwi",
    "title": "MNDWI - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "pass_product_cfg": True,
        "kwargs": {
            "band1": "green",
            "band2": "swir1"
        }
    },
    "needed_bands": ["green", "swir1"],
    "color_ramp": [
        {
            "value": -0.1,
            "color": "#f7fbff",
            "alpha": 0.0
        },
        {
            "value": 0.0,
            "color": "#d8e7f5"
        },
        {
            "value": 0.2,
            "color": "#b0d2e8"
        },
        {
            "value": 0.4,
            "color": "#73b3d8"
        },
        {
            "value": 0.6,
            "color": "#3e8ec4"
        },
        {
            "value": 0.8,
            "color": "#1563aa"
        },
        {
            "value": 1.0,
            "color": "#08306b"
        }
    ]
}

style_ls_pure_blue = {
    "name": "blue",
    "title": "Blue - 480",
    "abstract": "Blue band, centered on 480nm",
    "components": {
        "red": {
            "blue": 1.0
        },
        "green": {
            "blue": 1.0
        },
        "blue": {
            "blue": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_ls_pure_blue = {
    "name": "green",
    "title": "Green - 560",
    "abstract": "Green band, centered on 560nm",
    "components": {
        "red": {
            "green": 1.0
        },
        "green": {
            "green": 1.0
        },
        "blue": {
            "green": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_ls_pure_red = {
    "name": "red",
    "title": "Red - 660",
    "abstract": "Red band, centered on 660nm",
    "components": {
        "red": {
            "red": 1.0
        },
        "green": {
            "red": 1.0
        },
        "blue": {
            "red": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_ls_pure_nir = {
    "name": "nir",
    "title": "Near Infrared (NIR) - 870",
    "abstract": "Near infra-red band, centered on 870nm",
    "components": {
        "red": {
            "nir": 1.0
        },
        "green": {
            "nir": 1.0
        },
        "blue": {
            "nir": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_ls_pure_swir1 = {
    "name": "swir1",
    "title": "Shortwave Infrared (SWIR) - 1610",
    "abstract": "Short wave infra-red band 1, centered on 1610nm",
    "components": {
        "red": {
            "swir1": 1.0
        },
        "green": {
            "swir1": 1.0
        },
        "blue": {
            "swir1": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_ls_pure_swir2 = {
    "name": "swir2",
    "title": "Shortwave Infrared (SWIR) - 2200",
    "abstract": "Short wave infra-red band 2, centered on 2200nm",
    "components": {
        "red": {
            "swir2": 1.0
        },
        "green": {
            "swir2": 1.0
        },
        "blue": {
            "swir2": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_mangrove_cover_v1 = {
    "name": "mangrove",
    "title": "Mangrove Cover",
    "abstract": "",
    "value_map": {
        "canopy_cover_class": [
            {
                "title": "Woodland",
                "abstract": "(20% - 50% cover)",
                "flags": {
                    "woodland": True
                },
                "color": "#9FFF4C"
            },
            {
                "title": "Open Forest",
                "abstract": "(50% - 80% cover)",
                "flags": {
                    "open_forest": True
                },
                "color": "#5ECC00"
            },
            {
                "title": "Closed Forest",
                "abstract": "(>80% cover)",
                "flags": {
                    "closed_forest": True
                },
                "color": "#3B7F00"
            },
        ]
    }
}

style_mangrove_cover_v2 = {
    "name": "mangrove",
    "title": "Mangrove Cover",
    "abstract": "",
    "value_map": {
        "canopy_cover_class": [
            {
                "title": "Not Observed",
                "abstract": "(Clear Obs < 3)",
                "flags": {
                    "notobserved": True
                },
                "color": "#BDBDBD"
            },
            {
                "title": "Woodland",
                "abstract": "(20% - 50% cover)",
                "flags": {
                    "woodland": True
                },
                "color": "#9FFF4C"
            },
            {
                "title": "Open Forest",
                "abstract": "(50% - 80% cover)",
                "flags": {
                    "open_forest": True
                },
                "color": "#5ECC00"
            },
            {
                "title": "Closed Forest",
                "abstract": "(>80% cover)",
                "flags": {
                    "closed_forest": True
                },
                "color": "#3B7F00"
            },
        ]
    }
}

style_wofs_filt_freq = {
    "name": "WOfS_filtered_frequency",
    "title": "Filtered Water Summary",
    "abstract": "WOfS filtered summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "wofs_filtered_summary",
        }
    },
    "include_in_feature_info": False,
    "needed_bands": ["wofs_filtered_summary"],
    "color_ramp": [
        {
            "value": 0.0,
            "color": "#000000",
            "alpha": 0.0
        },
        {
            "value": 0.002,
            "color": "#000000",
            "alpha": 0.0
        },
        {
            "value": 0.005,
            "color": "#8e0101",
            "alpha": 0.25
        },
        {
            "value": 0.01,
            "color": "#cf2200",
            "alpha": 0.75
        },
        {
            "value": 0.02,
            "color": "#e38400"
        },
        {
            "value": 0.05,
            "color": "#e3df00"
        },
        {
            "value": 0.1,
            "color": "#a6e300"
        },
        {
            "value": 0.2,
            "color": "#62e300"
        },
        {
            "value": 0.3,
            "color": "#00e32d"
        },
        {
            "value": 0.4,
            "color": "#00e384"
        },
        {
            "value": 0.5,
            "color": "#00e3c8"
        },
        {
            "value": 0.6,
            "color": "#00c5e3"
        },
        {
            "value": 0.7,
            "color": "#0097e3"
        },
        {
            "value": 0.8,
            "color": "#005fe3"
        },
        {
            "value": 0.9,
            "color": "#000fe3"
        },
        {
            "value": 1.0,
            "color": "#5700e3"
        }
    ],
    "legend": {
        "url": "https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/wofs_full_summary_legend.png",
    }
}

style_wofs_filt_freq_blue = {
    "name": "WOfS_filtered_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS filtered summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "wofs_filtered_summary",
        }
    },
    "include_in_feature_info": False,
    "needed_bands": ["wofs_filtered_summary"],
    "color_ramp": [
        {
            "value": 0.0,
            "color": "#ffffff",
            "alpha": 0.0,
        },
        {
            "value": 0.001,
            "color": "#d5fef9",
            "alpha": 0.0,
        },
        {
            "value": 0.02,
            "color": "#d5fef9",
        },
        {
            "value": 0.2,
            "color": "#71e3ff"
        },
        {
            "value": 0.4,
            "color": "#01ccff"
        },
        {
            "value": 0.6,
            "color": "#0178ff"
        },
        {
            "value": 0.8,
            "color": "#2701ff"
        },
        {
            "value": 1.0,
            "color": "#5700e3"
        }
    ],
    "legend": {
        "units": "%",
        "radix_point": 0,
        "scale_by": 100.0,
        "major_ticks": 0.1
    }
}

style_wofs_count_wet = {
    "name": "water_observations",
    "title": "Wet Count",
    "abstract": "WOfS summary showing the count of water observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "count_wet",
        }
    },
    "needed_bands": ["count_wet"],
    "include_in_feature_info": False,
    "color_ramp": [
        {
            "value": 0,
            "color": "#666666",
            "alpha": 0
        },
        {
            "value": 2,
            "color": "#890000"
        },
        {
            "value": 5,
            "color": "#990000"
        },
        {
            "value": 10,
            "color": "#E38400"
        },
        {
            "value": 25,
            "color": "#E3DF00"
        },
        {
            "value": 50,
            "color": "#A6E300"
        },
        {
            "value": 100,
            "color": "#00E32D"
        },
        {
            "value": 150,
            "color": "#00E3C8"
        },
        {
            "value": 200,
            "color": "#0097E3"
        },
        {
            "value": 250,
            "color": "#005FE3"
        },
        {
            "value": 300,
            "color": "#000FE3"
        },
        {
            "value": 350,
            "color": "#000EA9"
        },
        {
            "value": 400,
            "color": "#5700E3",
            "legend": {
                "prefix": ">"
            }
        }
    ],
    "legend": {
        "radix_point": 0,
        "scale_by": 1,
        "major_ticks": 100
    }
}

style_wofs_count_clear = {
    "name": "clear_observations",
    "title": "Clear Count",
    "abstract": "WOfS summary showing the count of clear observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "count_clear",
        }
    },
    "needed_bands": ["count_clear"],
    "include_in_feature_info": False,
    "color_ramp": [
        {
            "value": 0,
            "color": "#FFFFFF",
            "alpha": 0
        },
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 10,
            "color": "#b21800",
            "alpha": 1
        },
        {
            "value": 100,
            "color": "#ef8500"
        },
        {
            "value": 200,
            "color": "#ffb800"
        },
        {
            "value": 300,
            "color": "#ffd300"
        },
        {
            "value": 400,
            "color": "#ffe300"
        },
        {
            "value": 500,
            "color": "#fff300"
        },
        {
            "value": 600,
            "color": "#d0f800"
        },
        {
            "value": 700,
            "color": "#a0fd00"
        },
        {
            "value": 800,
            "color": "#6ee100"
        },
        {
            "value": 901,
            "color": "#39a500"
        },
        {
            "value": 1000,
            "color": "#026900",
            "legend": {
                "prefix": ">"
            }
        }
    ],
    "legend": {
        "radix_point": 0,
        "scale_by": 1,
        "major_ticks": 100,
        "axes_position": [0.05, 0.5, 0.89, 0.15]
    }
}


style_wofs_frequency = {
    "name": "WOfS_frequency",
    "title": " Water Summary",
    "abstract": "WOfS summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "frequency",
        }
    },
    "needed_bands": ["frequency"],
    "include_in_feature_info": False,
    "color_ramp": [
        {
            "value": 0.0,
            "color": "#000000",
            "alpha": 0.0
        },
        {
            "value": 0.002,
            "color": "#000000",
            "alpha": 0.0
        },
        {
            "value": 0.005,
            "color": "#8e0101",
            "alpha": 0.25
        },
        {
            "value": 0.01,
            "color": "#cf2200",
            "alpha": 0.75
        },
        {
            "value": 0.02,
            "color": "#e38400"
        },
        {
            "value": 0.05,
            "color": "#e3df00"
        },
        {
            "value": 0.1,
            "color": "#a6e300"
        },
        {
            "value": 0.2,
            "color": "#62e300"
        },
        {
            "value": 0.3,
            "color": "#00e32d"
        },
        {
            "value": 0.4,
            "color": "#00e384"
        },
        {
            "value": 0.5,
            "color": "#00e3c8"
        },
        {
            "value": 0.6,
            "color": "#00c5e3"
        },
        {
            "value": 0.7,
            "color": "#0097e3"
        },
        {
            "value": 0.8,
            "color": "#005fe3"
        },
        {
            "value": 0.9,
            "color": "#000fe3"
        },
        {
            "value": 1.0,
            "color": "#5700e3"
        }
    ],
    "legend": {
        "url": "https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/wofs_full_summary_legend.png",
    }
}

style_wofs_frequency_blue = {
    "name": "WOfS_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "frequency",
        }
    },
    "include_in_feature_info": False,
    "needed_bands": ["frequency"],
    "color_ramp": [
        {
            "value": 0.0,
            "color": "#ffffff",
            "alpha": 0.0,
        },
        {
            "value": 0.001,
            "color": "#d5fef9",
            "alpha": 0.0,
        },
        {
            "value": 0.02,
            "color": "#d5fef9",
        },
        {
            "value": 0.2,
            "color": "#71e3ff"
        },
        {
            "value": 0.4,
            "color": "#01ccff"
        },
        {
            "value": 0.6,
            "color": "#0178ff"
        },
        {
            "value": 0.8,
            "color": "#2701ff"
        },
        {
            "value": 1.0,
            "color": "#5700e3"
        }
    ],
    "legend": {
        "units": "%",
        "radix_point": 0,
        "scale_by": 100.0,
        "major_ticks": 0.1
    }

}

style_wofs_confidence = {
    "name": "wofs_confidence",
    "title": "Confidence",
    "abstract": "WOfS Confidence",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "confidence",
        }
    "include_in_feature_info": False,
    "needed_bands": ["confidence"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#000000",
        },
        {
            "value": 0.01,
            "color": "#000000"
        },
        {
            "value": 0.02,
            "color": "#990000"
        },
        {
            "value": 0.05,
            "color": "#CF2200"
        },
        {
            "value": 0.1,
            "color": "#E38400"
        },
        {
            "value": 0.25,
            "color": "#E3DF00"
        },
        {
            "value": 0.5,
            "color": "#A6E300"
        },
        {
            "value": 0.75,
            "color": "#62E300"
        },
        {
            "value": 1.0,
            "color": "#00E32D"
        }
    ],
    "legend": {
        "units": "%",
        "radix_point": 0,
        "scale_by": 100.0,
        "major_ticks": 0.25
    }
}

style_wofs_summary_wet = {
    "name": "wet_count",
    "title": "Wet Count",
    "abstract": "WOfS annual summary showing the count of water observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "count_wet",
        }
    },
    "include_in_feature_info": False,
    "needed_bands": ["count_wet"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#666666",
            "alpha": 0
        },
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#990000",
            "alpha": 1
        },
        {
            "value": 2,
            "color": "#990000"
        },
        {
            "value": 4,
            "color": "#E38400"
        },
        {
            "value": 6,
            "color": "#E3DF00"
        },
        {
            "value": 8,
            "color": "#00E32D"
        },
        {
            "value": 10,
            "color": "#00E3C8"
        },
        {
            "value": 12,
            "color": "#0097E3"
        },
        {
            "value": 14,
            "color": "#005FE3"
        },
        {
            "value": 16,
            "color": "#000FE3"
        },
        {
            "value": 18,
            "color": "#000EA9"
        },
        {
            "value": 20,
            "color": "#5700E3",
            "legend": {
                "prefix": ">"
            }
        }
    ],
    "legend": {
        "radix_point": 0,
        "scale_by": 1,
        "major_ticks": 10
    }
}

style_wofs_summary_clear = {
    "name": "clear_count",
    "title": "Clear Count",
    "abstract": "WOfS annual summary showing the count of clear observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "count_clear",
        }
    },
    "include_in_feature_info": False,
    "needed_bands": ["count_clear"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#FFFFFF",
            "alpha": 0
        },
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#B21800",
            "alpha": 1
        },
        {
            "value": 1,
            "color": "#B21800"
        },
        {
            "value": 4,
            "color": "#ef8500"
        },
        {
            "value": 8,
            "color": "#ffb800"
        },
        {
            "value": 10,
            "color": "#ffd000"
        },
        {
            "value": 13,
            "color": "#fff300"
        },
        {
            "value": 16,
            "color": "#fff300"
        },
        {
            "value": 20,
            "color": "#c1ec00"
        },
        {
            "value": 24,
            "color": "#6ee100"
        },
        {
            "value": 28,
            "color": "#39a500"
        },
        {
            "value": 30,
            "color": "#026900",
            "legend": {
                "prefix": ">"
            }
        }
    ],
    "legend": {
        "radix_point": 0,
        "scale_by": 1,
        "major_ticks": 10,
        "axes_position": [0.05, 0.5, 0.89, 0.15]
    }
}

style_wofs_summary_frequency = {
    "name": "WOfS_frequency",
    "title": "Water Summary",
    "abstract": "WOfS annual summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "frequency",
        }
    },
    "include_in_feature_info": False,
    "needed_bands": ["frequency"],
    "color_ramp": [
        {
            "value": 0.0,
            "color": "#000000",
            "alpha": 0.0
        },
        {
            "value": 0.02,
            "color": "#000000",
            "alpha": 0.0
        },
        {
            "value": 0.05,
            "color": "#8e0101",
            "alpha": 0.25
        },
        {
            "value": 0.1,
            "color": "#cf2200",
            "alpha": 0.75
        },
        {
            "value": 0.2,
            "color": "#e38400"
        },
        {
            "value": 0.3,
            "color": "#e3df00"
        },
        {
            "value": 0.4,
            "color": "#62e300"
        },
        {
            "value": 0.5,
            "color": "#00e32d"
        },
        {
            "value": 0.6,
            "color": "#00e3c8"
        },
        {
            "value": 0.7,
            "color": "#0097e3"
        },
        {
            "value": 0.8,
            "color": "#005fe3"
        },
        {
            "value": 0.9,
            "color": "#000fe3"
        },
        {
            "value": 1.0,
            "color": "#5700e3"
        }
    ],
    "legend": {
        "units": "%",
        "radix_point": 0,
        "scale_by": 100.0,
        "major_ticks": 0.1
    }
}

style_wofs_summary_frequency_blue = {
    "name": "WOfS_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS annual summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "frequency",
        }
    },
    "include_in_feature_info": False,
    "needed_bands": ["frequency"],
    "color_ramp": [
        {
            "value": 0.0,
            "color": "#ffffff",
            "alpha": 0.0,
        },
        {
            "value": 0.001,
            "color": "#d5fef9",
            "alpha": 0.0,
        },
        {
            "value": 0.02,
            "color": "#d5fef9",
        },
        {
            "value": 0.2,
            "color": "#71e3ff"
        },
        {
            "value": 0.4,
            "color": "#01ccff"
        },
        {
            "value": 0.6,
            "color": "#0178ff"
        },
        {
            "value": 0.8,
            "color": "#2701ff"
        },
        {
            "value": 1.0,
            "color": "#5700e3"
        }
    ],
    "legend": {
        "units": "%",
        "radix_point": 0,
        "scale_by": 100.0,
        "major_ticks": 0.1
    }
}

style_wofs_obs = {
    "name": "observations",
    "title": "Observations",
    "abstract": "Observations",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {
                    "or": {
                      "terrain_or_low_angle": True,
                      "cloud_shadow": True,
                      "cloud": True,
                      "high_slope": True,
                      "noncontiguous": True
                    }
                },
                "color": "#707070"
            },
            {
                # Possible Sea Glint, also mark as invalid
                "title": "",
                "abstract": "",
                "flags": {
                    "dry": True,
                    "sea": True
                },
                "color": "#707070"
            },
            {
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                    "sea": False,
                },
                "color": "#D99694"
            },
            {
                "title": "Wet",
                "abstract": "Wet or Sea",
                "flags": {
                  "or": {
                    "wet": True,
                    "sea": True
                  }
                },
                "color": "#4F81BD"
            }
        ]
    }
}

style_wofs_obs_wet_only = {
    "name": "wet",
    "title": "Wet Only",
    "abstract": "Wet Only",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {
                    "or": {
                      "terrain_or_low_angle": True,
                      "cloud_shadow": True,
                      "cloud": True,
                      "high_slope": True,
                      "noncontiguous": True
                    }
                },
                "color": "#707070",
                "mask": True
            },
            {
                # Possible Sea Glint, also mark as invalid
                "title": "",
                "abstract": "",
                "flags": {
                    "dry": True,
                    "sea": True
                },
                "color": "#707070",
                "mask": True
            },
            {
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                    "sea": False,
                },
                "color": "#D99694",
                "mask": True
            },
            {
                "title": "Wet",
                "abstract": "Wet or Sea",
                "flags": {
                  "or": {
                    "wet": True,
                    "sea": True
                  }
                },
                "color": "#4F81BD"
            }
        ]
    }
}

style_s2_simple_rgb = style_ls_simple_rgb
style_s2_irg = style_ls_irg
style_s2_ndvi = style_ls_ndvi
style_s2_ndwi = style_ls_ndwi
style_s2_mndwi = {
    # Cannot reuse landsat as we need swir_2 to landsat's swir_1
    "name": "mndwi",
    "title": "MNDWI - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "pass_product_cfg": True,
        "kwargs": {
            "band1": "nbart_green",
            "band2": "nbart_swir_2"
        }
    },
    "needed_bands": ["nbart_green", "nbart_swir_2"],
    "color_ramp": [
        {
            "value": -0.1,
            "color": "#f7fbff",
            "alpha": 0.0
        },
        {
            "value": 0.0,
            "color": "#d8e7f5"
        },
        {
            "value": 0.2,
            "color": "#b0d2e8"
        },
        {
            "value": 0.4,
            "color": "#73b3d8"
        },
        {
            "value": 0.6,
            "color": "#3e8ec4"
        },
        {
            "value": 0.8,
            "color": "#1563aa"
        },
        {
            "value": 1.0,
            "color": "#08306b"
        }
    ]
}
style_s2_ndci = {
    "name": "ndci",
    "title": "NDCI - Red Edge, Red",
    "abstract": "Normalised Difference Chlorophyll Index - a derived index that correlates well with the existence of chlorophyll",
    "index_function": {
        "function": "datacube_ows.band_utils.sentinel2_ndci",
        "pass_product_cfg": True,
        "kwargs": {
            "b_red_edge": "nbart_red_edge_1",
            "b_red": "nbart_red",
            "b_green": "nbart_green",
            "b_swir": "nbart_swir_2",
        }
    },
    "needed_bands": ["nbart_red_edge_1", "nbart_red", "nbart_green", "nbart_swir_2"],
    "color_ramp": [
        {
            "value": -0.1,
            "color": "#1696FF",
            "legend": {
                "prefix" : "<"
            }
        },
        {
            "value": -0.1,
            "color": "#1696FF"
        },
        {
            "value": 0.0,
            "color": "#00FFDF",
            "legend": { }
        },
        {
            "value": 0.1,
            "color": "#FFF50E",
        },
        {
            "value": 0.2,
            "color": "#FFB50A",
            "legend": { }
        },
        {
            "value": 0.4,
            "color": "#FF530D",
        },
        {
            "value": 0.5,
            "color": "#FF0000",
            "legend": {
                "prefix": ">"
            }
        }
    ]
}

style_s2_pure_aerosol = {
    "name": "aerosol",
    "title": "Narrow Blue - 440",
    "abstract": "Coastal Aerosol or Narrow Blue band, approximately 435nm to 450nm",
    "components": {
        "red": {
            "coastal_aerosol": 1.0
        },
        "green": {
            "coastal_aerosol": 1.0
        },
        "blue": {
            "coastal_aerosol": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}


style_s2_pure_blue = {
    "name": "blue",
    "title": "Narrow Blue - 490",
    "abstract": "Blue band, approximately 453nm to 511nm",
    "components": {
        "red": {
            "blue": 1.0
        },
        "green": {
            "blue": 1.0
        },
        "blue": {
            "blue": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}


style_s2_pure_green = {
    "name": "green",
    "title": "Green - 560",
    "abstract": "Coastal Aerosol or Narrow Blue band, approximately 534nm to 588nm",
    "components": {
        "red": {
            "green": 1.0
        },
        "green": {
            "green": 1.0
        },
        "blue": {
            "green": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}


style_s2_pure_red = {
    "name": "red",
    "title": "Red - 670",
    "abstract": "Red band, roughly 637nm to 672nm",
    "components": {
        "red": {
            "red": 1.0
        },
        "green": {
            "red": 1.0
        },
        "blue": {
            "red": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}


style_s2_pure_redge_1 = {
    "name": "red_edge_1",
    "title": "Vegetation Red Edge - 710",
    "abstract": "Near infra-red band, centred on 710nm",

    "components": {
        "red": {
            "red_edge_1": 1.0
        },
        "green": {
            "red_edge_1": 1.0
        },
        "blue": {
            "red_edge_1": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}


style_s2_pure_redge_2 = {
    "name": "red_edge_2",
    "title": "Vegetation Red Edge - 740",
    "abstract": "Near infra-red band, centred on 740nm",

    "components": {
        "red": {
            "red_edge_2": 1.0
        },
        "green": {
            "red_edge_2": 1.0
        },
        "blue": {
            "red_edge_2": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}


style_s2_pure_redge_3 = {
    "name": "red_edge_3",
    "title": "Vegetation Red Edge - 780",
    "abstract": "Near infra-red band, centred on 780nm",

    "components": {
        "red": {
            "red_edge_3": 1.0
        },
        "green": {
            "red_edge_3": 1.0
        },
        "blue": {
            "red_edge_3": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}


style_s2_pure_nir = {
    "name": "nir",
    "title": "Near Infrared (NIR) - 840",
    "abstract": "Near infra-red band, roughly 853nm to 876nm",
    "components": {
        "red": {
            "nir": 1.0
        },
        "green": {
            "nir": 1.0
        },
        "blue": {
            "nir": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_s2_pure_narrow_nir = {
    "name": "narrow_nir",
    "title": "Narrow Near Infrared - 870",
    "abstract": "Near infra-red band, centred on 865nm",
    "components": {
        "red": {
            "nir": 1.0
        },
        "green": {
            "nir": 1.0
        },
        "blue": {
            "nir": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}


style_s2_pure_swir1 = {
    "name": "swir1",
    "title": "Shortwave Infrared (SWIR) - 1610",
    "abstract": "Short wave infra-red band 1, roughly 1575nm to 1647nm",
    "components": {
        "red": {
            "swir_2": 1.0
        },
        "green": {
            "swir_2": 1.0
        },
        "blue": {
            "swir_2": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}


style_s2_pure_swir2 = {
    "name": "swir2",
    "title": "Shortwave Infrared (SWIR) - 2190",
    "abstract": "Short wave infra-red band 2, roughly 2117nm to 2285nm",
    "components": {
        "red": {
            "swir_3": 1.0
        },
        "green": {
            "swir_3": 1.0
        },
        "blue": {
            "swir_3": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_s2_water_classifier = {
    "name": "water_classifier",
    "title": " Water Summary",
    "abstract": "WOfS NRT",
    "needed_bands": ["water"],
    "value_map": {
        "water": [
            {
                "title": "Wet",
                "abstract": "(100%)",
                "color": "#5700E3"
            },

        ]
    }
}

style_mstp_rgb = {
    "name": "mstp_rgb",
    "title": "Multi-scale Topographic Position",
    "abstract": "red regional, green intermediate and blue local",
    "components": {
        "red": {
            "regional": 1.0
        },
        "green": {
            "intermediate": 1.0
        },
        "blue": {
            "local": 1.0
        }
    },
    "scale_range": [0.0, 255.0]
}

style_wii = {
    "name": "wii",
    "title": "Weathering Intensity",
    "abstract": "Weather Intensity Index (0-6)",
    "needed_bands": ["intensity"],
    "color_ramp": [
        {
            'value': 0,
            'color': '#ffffff',
            'alpha': 0
        },
        {
            'value': 1,
            'color': '#2972a8',
            'legend': {
                'label': 'Low\nClass 1'
            }
        },
        {
            'value': 3.5,
            'color': '#fcf24b'
        },
        {
            'value': 6,
            'color': '#a02406',
            'legend': {
                'label': 'High\nClass 6'
            }
        }
    ],
    "legend": {
        "axes_position": [0.1, 0.5, 0.8, 0.15]
    }
}

# Actual Configuration

ows_cfg = {
    "global": {
        # Master config for all services and products.
        "resonse_headers": {
            "Access-Control-Allow-Origin": "*",  # CORS header
        },
        "services": {
            "wms": True,
            "wcs": True,
            "wmts": True,
        },
        "published_CRSs": {
            "EPSG:3857": {  # Web Mercator
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:4326": {  # WGS-84
                "geographic": True,
                "vertical_coord_first": True
            },
            "EPSG:3577": {  # GDA-94, internal representation
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:3111": {  # VicGrid94 for delwp.vic.gov.au
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
        },
        "allowed_urls": [
                "https://ows.services.dea.ga.gov.au",
                "https://ows.services.dev.dea.ga.gov.au",
                "https://ows.dev.dea.ga.gov.au",
                "https://ows.dea.ga.gov.au",
                "https://ows.services.devkube.dea.ga.gov.au",
                "https://nrt.services.dea.ga.gov.au",
                "https://geomedian.services.dea.ga.gov.au",
                "https://geomedianau.dea.ga.gov.au",
                "https://geomedian.dea.ga.gov.au",
                "https://nrt.dea.ga.gov.au",
                "https://nrt-au.dea.ga.gov.au"],

        # Metadata to go straight into GetCapabilities documents
        "title": "Digital Earth Australia - OGC Web Services",
        "abstract": "Digital Earth Australia OGC Web Services",
        "info_url": "https://dea.ga.gov.au/",
        "keywords": [
            "geomedian",
            "WOfS",
            "mangrove",
            "bare-earth",
            "NIDEM",
            "HLTC",
            "landsat",
            "australia",
            "time-series",
            "fractional-cover"
        ],
        "contact_info": {
            "person": "Digital Earth Australia",
            "organisation": "Geoscience Australia",
            "position": "",
            "address": {
                "type": "postal",
                "address": "GPO Box 378",
                "city": "Canberra",
                "state": "ACT",
                "postcode": "2609",
                "country": "Australia",
            },
            "telephone": "+61 2 6249 9111",
            "fax": "",
            "email": "earth.observation@ga.gov.au",
        },
        "fees": "",
        "access_constraints": "© Commonwealth of Australia (Geoscience Australia) 2018. " 
                              "This product is released under the Creative Commons Attribution 4.0 International Licence. "
                              "http://creativecommons.org/licenses/by/4.0/legalcode",
    }, # END OF global SECTION
    "wms": {
        # Config for WMS service, for all products/layers
        "s3_url": "https://data.dea.ga.gov.au",
        "s3_bucket": "dea-public-data",
        "s3_aws_zone": "ap-southeast-2",

        "max_width": 512,
        "max_height": 512,
    }, # END OF wms SECTION
    "wcs": {
        # Config for WCS service, for all products/coverages
        "default_geographic_CRS": "EPSG:4326",
        "formats": {
            "GeoTIFF": {
                "renderer": "datacube_ows.wcs_utils.get_tiff",
                "mime": "image/geotiff",
                "extension": "tif",
                "multi-time": False
            },
            "netCDF": {
                "renderer": "datacube_ows.wcs_utils.get_netcdf",
                "mime": "application/x-netcdf",
                "extension": "nc",
                "multi-time": True,
            },
        },
        "native_format": "GeoTIFF",
    }, # END OF wcs SECTION
    "layers": [
        # Hierarchical list of layers.  May be a combination of unnamed/unmappable folder-layers or named mappable layers.
        {
            "title": "Landsat Series Geomedian Surface Reflectance",
            "abstract": "",
            "layers": [
                {
                    "title": "Landsat 8 Annual Geomedian",
                    "name": "ls8_nbart_geomedian_annual",
                    "abstract": """
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 8: 2013 to 2017;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374

For service status information, see https://status.dea.ga.gov.au
                    """,
                    "product_name": "ls8_nbart_geomedian_annual",
                    "bands": bands_ls,
                    "resource_limits": reslim_landsat,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [],
                        "manual_merge": True,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["red", "green", "blue"]
                    },
                    "styling": {
                        "default_style": "simple_rgb",
                        "styles": [
                            style_ls_simple_rgb,
                            style_ls_irg, style_ls_ndvi, style_ls_ndwi, style_ls_mndwi,
                            style_ls_pure_blue, style_ls_pure_green, style_ls_pure_red,
                            style_ls_pure_nir, style_ls_pure_swir1, style_ls_pure_swir2,
                        ]
                    }
                },
                {
                    "title": "Landsat 7 Annual Geomedian",
                    "name": "ls7_nbart_geomedian_annual",
                    "abstract": """
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 7: 2000 to 2017;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374

For service status information, see https://status.dea.ga.gov.au
                    """,
                    "product_name": "ls7_nbart_geomedian_annual",
                    "bands": bands_ls,
                    "resource_limits": reslim_landsat,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [],
                        "manual_merge": True,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["red", "green", "blue"]
                    },
                    "styling": {
                        "default_style": "simple_rgb",
                        "styles": [
                            style_ls_simple_rgb,
                            style_ls_irg, style_ls_ndvi, style_ls_ndwi, style_ls_mndwi,
                            style_ls_pure_blue, style_ls_pure_green, style_ls_pure_red,
                            style_ls_pure_nir, style_ls_pure_swir1, style_ls_pure_swir2,
                        ]
                    }
                },
                {
                    "title": "Landsat 5 Annual Geomedian",
                    "name": "ls5_nbart_geomedian_annual",
                    "abstract": """
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 5: 1988 to 1999, 2004 to 2007, 2009 to 2011;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374

For service status information, see https://status.dea.ga.gov.au
                    """,
                    "product_name": "ls5_nbart_geomedian_annual",
                    "bands": bands_ls,
                    "resource_limits": reslim_landsat,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [],
                        "manual_merge": True,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["red", "green", "blue"]
                    },
                    "styling": {
                        "default_style": "simple_rgb",
                        "styles": [
                            style_ls_simple_rgb,
                            style_ls_irg, style_ls_ndvi, style_ls_ndwi, style_ls_mndwi,
                            style_ls_pure_blue, style_ls_pure_green, style_ls_pure_red,
                            style_ls_pure_nir, style_ls_pure_swir1, style_ls_pure_swir2,
                        ]
                    }
                },
            ]
        },
        {
            "title": "Barest Earth",
            "abstract": """
A `weighted geometric median’ approach has been used to estimate the median surface reflectance of the barest state (i.e., least vegetation) observed through Landsat-8 OLI observations from 2013 to September 2018 to generate a six-band Landsat-8 Barest Earth pixel composite mosaic over the Australian continent.

The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The weighted median approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.

Reference: Dale Roberts, John Wilford, and Omar Ghattas (2018). Revealing the Australian Continent at its Barest, submitted.

Mosaics are available for the following years:
    Landsat 8: 2013 to 2017;

For service status information, see https://status.dea.ga.gov.au
            """,
            "layers": [
                {
                    "title": "Landsat 8 Barest Earth",
                    "name": "ls8_barest_earth_mosaic",
                    "abstract": """
A `weighted geometric median’ approach has been used to estimate the median surface reflectance of the barest state (i.e., least vegetation) observed through Landsat-8 OLI observations from 2013 to September 2018 to generate a six-band Landsat-8 Barest Earth pixel composite mosaic over the Australian continent.

The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The weighted median approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.

Reference: Dale Roberts, John Wilford, and Omar Ghattas (2018). Revealing the Australian Continent at its Barest, submitted.

Mosaics are available for the following years:
    Landsat 8: 2013 to 2017;

For service status information, see https://status.dea.ga.gov.au
                    """,
                    "product_name": "ls8_barest_earth_albers",
                    "bands": bands_ls,
                    "resource_limits": reslim_landsat,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [],
                        "manual_merge": True,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["red", "green", "blue"]
                    },
                    "styling": {
                        "default_style": "simple_rgb",
                        "styles": [
                            style_ls_simple_rgb,
                            style_ls_irg, style_ls_ndvi,
                            style_ls_pure_blue, style_ls_pure_green, style_ls_pure_red,
                            style_ls_pure_nir, style_ls_pure_swir1, style_ls_pure_swir2,
                        ]
                    }

                }
            ]
        },
        {
            "title": "Barest Earth 30 Years",
            "abstract": """
A `weighted geometric median` approach has been used to estimate the median surface reflectance of the barest state (i.e., least vegetation) observed through Landsat-5 TM / Landsat-7 ETM+ / Landsat-8 OLI observations from 1980 to 2018 to generate a six-band Landsat Barest Earth pixel composite mosaic over the Australian continent.

The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The weighted median approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.

Reference: Dale Roberts, John Wilford, and Omar Ghattas (2018). Revealing the Australian Continent at its Barest, submitted.

Mosaics are available for the following years:
    Landsat 5 / Landsat 7 / Landsat 8 - 1980 to 2018;

            """,
            "layers": [
                {
                    "title": "Combined Landsat Barest Earth",
                    "name": "landsat_barest_earth",
                    "abstract": """
A `weighted geometric median` approach has been used to estimate the median surface reflectance of the barest state (i.e., least vegetation) observed through Landsat-5 TM / Landsat-7 ETM+ / Landsat-8 OLI observations from 1980 to 2018 to generate a six-band Landsat Barest Earth pixel composite mosaic over the Australian continent.

The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The weighted median approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.

Reference: Dale Roberts, John Wilford, and Omar Ghattas (2018). Revealing the Australian Continent at its Barest, submitted.

Mosaics are available for the following years:
    Landsat 5 / Landsat 7 / Landsat 8 - 1980 to 2018;

For service status information, see https://status.dea.ga.gov.au
                    """,
                    "product_name": "landsat_barest_earth",
                    "bands": bands_ls,
                    "resource_limits": reslim_landsat,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [],
                        "manual_merge": True,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["red", "green", "blue"]
                    },
                    "styling": {
                        "default_style": "simple_rgb",
                        "styles": [
                            style_ls_simple_rgb,
                            style_ls_irg, style_ls_ndvi, style_ls_ndwi,
                            style_ls_pure_blue, style_ls_pure_green, style_ls_pure_red,
                            style_ls_pure_nir, style_ls_pure_swir1, style_ls_pure_swir2,
                        ]
                    }

                }
            ]
        },
        {
            "title": "Mangrove Canopy Cover",
            "abstract": "",
            "layers": [
                {
                    "title": "Mangrove Canopy Cover",
                    "name": "mangrove_cover",
                    "abstract": """
Mangrove canopy cover version 1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.

The mangrove canopy cover product provides valuable information about the extent and canopy density of mangroves for each year between 1987 and 2016 for the entire Australian coastline.
The canopy cover classes are:
20-50% (pale green), 50-80% (mid green), 80-100% (dark green).

The product consists of  a sequence (one per year) of 25 meter resolution maps that are generated by analysing the Landsat fractional cover (https://doi.org/10.6084/m9.figshare.94250.v1) developed by the Joint Remote Sensing Research Program and the Global Mangrove Watch layers (https://doi.org/10.1071/MF13177) developed by the Japanese Aerospace Exploration Agency.

The mangrove canopy cover version 1 product has the following caveats:
it underestimates the overall extent of mangroves.
it doesn’t detect small mangrove communities i.e. smaller estuaries in NSW and Victoria
that there is localised confusion between mangroves and wooded freshwater wetlands i.e. Melaleuca swamps, and
in some locations dense dwarf/shrub mangroves that are less than 2 metres tall may be mis-labelled as woodland/open forest/closed forest.

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "mangrove_cover",
                    "bands": bands_mangrove,
                    "resource_limits": reslim_mangrove,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_extent_flag",
                        "always_fetch_bands": [ "extent" ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["canopy_cover_class", "extent"]
                    },
                    "styling": {
                        "default_style": "mangrove",
                        "styles": [
                            style_mangrove_cover_v1,
                        ]
                    }
                },
                {
                    "title": "Mangrove Canopy Cover v2.0.2",
                    "name": "mangrove_cover_v2_0_2",
                    "abstract": """
Mangrove canopy cover version 2.0.2, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.

The mangrove canopy cover product provides valuable information about the extent and canopy density of mangroves for each year between 1987 and 2016 for the entire Australian coastline.
The canopy cover classes are:
20-50% (pale green), 50-80% (mid green), 80-100% (dark green).

The product consists of  a sequence (one per year) of 25 meter resolution maps that are generated by analysing the Landsat fractional cover (https://doi.org/10.6084/m9.figshare.94250.v1) developed by the Joint Remote Sensing Research Program and the Global Mangrove Watch layers (https://doi.org/10.1071/MF13177) developed by the Japanese Aerospace Exploration Agency.

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "mangrove_cover_test",
                    "bands": bands_mangrove,
                    "resource_limits": reslim_mangrove,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_extent_val",
                        "always_fetch_bands": [ "extent" ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["canopy_cover_class", "extent"]
                    },
                    "styling": {
                        "default_style": "mangrove",
                        "styles": [
                            style_mangrove_cover_v2,
                        ]
                    }
                },
            ]
        },
        {
            "title": "Water Observations from Space",
            "abstract": "WOfS",
            "layers": [
                {
                    "title": "WOfS Filtered Statistics",
                    "name": "wofs_filtered_summary",
                    "abstract": """
Water Observations from Space (WOfS) Filtered Statistics helps provide the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. WOfS Filtered Statistics consists of a Confidence layer that compares the WOfS Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the WOfS Statistics water summary where Confidence is low. 

This layer is Filtered Water Summary: A simplified version of the Water Summary, showing the frequency of water observations where the Confidence is above a cutoff level.  No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

The Filtered Water Summary layer is a noise-reduced view of surface water across Australia. Even though confidence filtering is applied to the Filtered Water Summary, some cloud and shadow, and sensor noise does persist. 

For more information please see: https://data.dea.ga.gov.au/?prefix=WOfS/filtered_summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_filtered_summary",
                    "bands": bands_wofs_filt_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["wofs_filtered_summary"]
                    },
                    "styling": {
                        "default_style": "WOfS_filtered_frequency",
                        "styles": [
                            style_wofs_filt_freq,
                            style_wofs_filt_freq_blue
                        ]
                    }
                },
                {
                    "title": "WOfS Statistics - Wet Count",
                    "name": "wofs_summary_wet",
                    "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products which help the understanding of surface water across Australia.  The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. 

This layer contains Wet Count: how many times water was detected in observations that were clear. No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary. 

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["count_wet"]
                    },
                    "styling": {
                        "default_style": "water_observations",
                        "styles": [
                            style_wofs_count_wet,
                        ]
                    }
                },
                {
                    "title": "WOfS Statistics - Clear Count",
                    "name": "wofs_summary_clear",
                    "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products which help the understanding of surface water across Australia.  The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. 

This layer contains Clear Count: how many times an area could be clearly seen (ie. not affected by clouds, shadows or other satellite observation problems). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary. 

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["count_clear"]
                    },
                    "styling": {
                        "default_style": "clear_observations",
                        "styles": [
                            style_wofs_count_clear,
                        ]
                    }
                },
                {
                    "title": "WOfS Statistics - Water Summary",
                    "name": "wofs_summary",
                    "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product which combines WOfS observations into summary products that help the understanding of surface water across Australia. WOfS Statistics is calculated from the full depth time series (1986 – 2018). The water detected for each location is summed through time and then compared to the number of clear observations of that location. The result is a percentage value of the number of times water was observed at the location. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time (water summary). 

This layer contains the Water Summary: the percentage of clear observations which were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary. 

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["frequency"]
                    },
                    "styling": {
                        "default_style": "WOfS_frequency",
                        "styles": [
                            style_wofs_frequency,
                            style_wofs_frequency_blue
                        ]
                    }
                },
                {
                    "title": "WOfS Filtered Statistics - Confidence",
                    "name": "wofs_filtered_summary_confidence",
                    "abstract": """
Water Observations from Space (WOfS) Filtered Statistics helps provide the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. WOfS Filtered Statistics consists of a Confidence layer that compares the WOfS Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the WOfS Statistics water summary where Confidence is low.
 
This layer is Confidence: the degree of agreement between water shown in the Water Summary and other national datasets. Areas where there is less than 1% confidence appears black, areas with confidence for between 1% 10% confidence are styled between black and red, areas with 25% confidence are styled yellow, areas with 75% confidence and above correspond to green.

The Confidence layer provides understanding of whether the water shown in the Water Summary agrees with where water should exist in the landscape, such as due to sloping land or whether water has been detected in a location by other means. 

For more information please see: https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_filtered_summary_confidence",
                    "bands": bands_wofs_filt_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["confidence"]
                    },
                    "styling": {
                        "default_style": "wofs_confidence",
                        "styles": [
                            style_wofs_confidence,
                        ]
                    }
                },
                {
                    "title": "WOfS Annual Statistics - Wet Count",
                    "name": "wofs_annual_summary_wet",
                    "abstract": """
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.
For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_annual_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["count_wet"]
                    },
                    "styling": {
                        "default_style": "wet_count",
                        "styles": [
                            style_wofs_summary_wet,
                        ]
                    }
                },
                {
                    "title": "WOfS Annual Statistics - Clear Count",
                    "name": "wofs_annual_summary_clear",
                    "abstract": """
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.
For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_annual_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["count_clear"]
                    },
                    "styling": {
                        "default_style": "clear_count",
                        "styles": [
                            style_wofs_summary_clear,
                        ]
                    }
                },
                {
                    "title": "WOfS Annual Statistics - Water Summary",
                    "name": "wofs_annual_summary_statistics",
                    "abstract": """
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.
For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_annual_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["frequency"]
                    },
                    "styling": {
                        "default_style": "WOfS_frequency", 
                        "styles": [
                            style_wofs_summary_frequency,
                            style_wofs_summary_frequency_blue,
                        ]
                    }
                },
                {
                    "title": "WOfS April-October Statistics - Wet Count",
                    "name": "wofs_apr_oct_summary_wet",
                    "abstract": """
Water Observations from Space - April to October Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_apr_oct_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["count_wet"]
                    },
                    "styling": {
                        "default_style": "wet_count",
                        "styles": [
                            style_wofs_summary_wet,
                        ]
                    }
                },
                {
                    "title": "WOfS April-October Statistics - Clear Count",
                    "name": "wofs_apr_oct_summary_clear",
                    "abstract": """
Water Observations from Space - April to October Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_apr_oct_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["count_clear"]
                    },
                    "styling": {
                        "default_style": "clear_count",
                        "styles": [
                            style_wofs_summary_clear,
                        ]
                    }
                },
                {
                    "title": "WOfS April-October Statistics - Water Summary",
                    "name": "wofs_apr_oct_summary_statistics",
                    "abstract": """
Water Observations from Space - April to October Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_apr_oct_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["frequency"]
                    },
                    "styling": {
                        "default_style": "WOfS_frequency",
                        "styles": [
                            style_wofs_summary_frequency,
                            style_wofs_summary_frequency_blue,
                        ]
                    }
                },
                {
                    "title": "WOfS November-March Statistics - Wet Count",
                    "name": "wofs_nov_mar_summary_wet",
                    "abstract": """
Water Observations from Space - November to March Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_nov_mar_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["count_wet"]
                    },
                    "styling": {
                        "default_style": "wet_count",
                        "styles": [
                            style_wofs_summary_wet,
                        ]
                    }
                },
                {
                    "title": "WOfS November-March Statistics - Clear Count",
                    "name": "wofs_nov_mar_summary_clear",
                    "abstract": """
Water Observations from Space - November to March Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_nov_mar_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["count_clear"]
                    },
                    "styling": {
                        "default_style": "clear_count",
                        "styles": [
                            style_wofs_summary_clear,
                        ]
                    }
                },
                {
                    "title": "WOfS November-March Statistics - Water Summary",
                    "name": "wofs_nov_mar_summary_statistics",
                    "abstract": """
Water Observations from Space - November to March Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_nov_mar_summary",
                    "bands": bands_wofs_sum,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["frequency"]
                    },
                    "styling": {
                        "default_style": "WOfS_frequency",
                        "styles": [
                            style_wofs_summary_frequency,
                            style_wofs_summary_frequency_blue,
                        ]
                    }
                },
                {
                    "title": "WOfS Daily Observations",
                    "name": "wofs_albers",
                    "abstract": """
Water Observations from Space (WOfS) provides surface water observations derived from satellite imagery for all of Australia. The current product (Version 2.1.5) includes observations taken from 1986 to the present, from the Landsat 5, 7 and 8 satellites. WOfS covers all of mainland Australia and Tasmania but excludes off-shore Territories.

The WOfS product allows users to get a better understanding of where water is normally present in a landscape, where water is seldom observed, and where inundation has occurred occasionally.

Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water. The details of the WOfS algorithm and derived statistics are available at http://dx.doi.org/10.1016/j.rse.2015.11.003.

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "wofs_albers",
                    "bands": bands_wofs_obs,
                    "resource_limits": reslim_wofs_obs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_bitflag",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                        "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
                    },
                    "wcs": {
                        "native_crs": "EPSG:3577",
                        "native_resolution": [25.0, 25.0],
                        "default_bands": ["water"]
                    },
                    "styling": {
                        "default_style": "observations",
                        "styles": [
                            style_wofs_obs,
                            style_wofs_obs_wet_only
                        ]
                    }
                }
            ]
        },
        {
            "title": "Sentinel-2 Near Real-Time",
            "abstract": """ 
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data.

The Near Real-Time capability provides analysis-ready data that is processed on receipt using 
the best-available ancillary information at the time to provide atmospheric corrections. 

For more information see http://pid.geoscience.gov.au/dataset/ga/122229
""",
            "layers": [
                {
                    "name": "s2_nrt_granule_nbar_t",
                    "title": "Sentinel 2 (A and B combined) Surface Reflectance, Near Real-Time",
                    "abstract": """
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For more information see http://pid.geoscience.gov.au/dataset/ga/122229

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For service status information, see https://status.dea.ga.gov.au
""",
                    "multi_product": True,
                    "product_names": [ "s2a_nrt_granule", "s2b_nrt_granule" ],
                    "bands": bands_sentinel2,
                    "resource_limits": reslim_s2,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_wcs_crs": "EPSG:3577",
                        "native_resolution": [ 10.0, 10.0 ],
                        "default_bands": [ "nbart_red", "nbart_green", "nbart_blue" ]
                    },
                    "styling": {
                        default_style: "simple_rgb",
                        styles: [
                            style_s2_simple_rgb,
                            style_s2_irg,
                            style_s2_ndvi, style_s2_ndwi, style_s2_mndwi, style_s2_ndci,
                            style_s2_pure_aerosol,
                            style_s2_pure_blue, style_s2_pure_green, style_s2_pure_red,
                            style_s2_pure_redge_1, style_s2_pure_redge_2, style_s2_pure_redge_3,
                            style_s2_pure_nir, style_s2_pure_narrow_nir,
                            style_s2_pure_swir1, style_s2_pure_swir2,
                        ]
                    }
                }, 
                {
                    "name": "s2a_nrt_granule_nbar_t",
                    "title": "Sentinel 2A Surface Reflectance, Near Real-Time",
                    "abstract": """
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For more information see http://pid.geoscience.gov.au/dataset/ga/122229

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "s2a_nrt_granule",
                    "bands": bands_sentinel2,
                    "resource_limits": reslim_s2,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_wcs_crs": "EPSG:3577",
                        "native_resolution": [ 10.0, 10.0 ],
                        "default_bands": [ "nbart_red", "nbart_green", "nbart_blue" ]
                    },
                    "styling": {
                        default_style: "simple_rgb",
                        styles: [
                            style_s2_simple_rgb,
                            style_s2_irg,
                            style_s2_ndvi, style_s2_ndwi, style_s2_mndwi, style_s2_ndci,
                            style_s2_pure_aerosol,
                            style_s2_pure_blue, style_s2_pure_green, style_s2_pure_red,
                            style_s2_pure_redge_1, style_s2_pure_redge_2, style_s2_pure_redge_3,
                            style_s2_pure_nir, style_s2_pure_narrow_nir,
                            style_s2_pure_swir1, style_s2_pure_swir2,
                        ]
                    }
                }, 
                {
                    "name": "s2b_nrt_granule_nbar_t",
                    "title": "Sentinel 2B Surface Reflectance, Near Real-Time",
                    "abstract": """
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For more information see http://pid.geoscience.gov.au/dataset/ga/122229

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "s2b_nrt_granule",
                    "bands": bands_sentinel2,
                    "resource_limits": reslim_s2,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_wcs_crs": "EPSG:3577",
                        "native_resolution": [ 10.0, 10.0 ],
                        "default_bands": [ "nbart_red", "nbart_green", "nbart_blue" ]
                    },
                    "styling": {
                        default_style: "simple_rgb",
                        styles: [
                            style_s2_simple_rgb,
                            style_s2_irg,
                            style_s2_ndvi, style_s2_ndwi, style_s2_mndwi, style_s2_ndci,
                            style_s2_pure_aerosol,
                            style_s2_pure_blue, style_s2_pure_green, style_s2_pure_red,
                            style_s2_pure_redge_1, style_s2_pure_redge_2, style_s2_pure_redge_3,
                            style_s2_pure_nir, style_s2_pure_narrow_nir,
                            style_s2_pure_swir1, style_s2_pure_swir2,
                        ]
                    }
                }, 
                {
                    "name": "s2_nrt_wofs",
                    "title": "Sentinel 2 Water Observations from Space (WOfS), Near Real-Time",
                    "abstract": """Sentinel 2 NRT Water Classifier

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "sentinel2_wofs_nrt",
                    "bands": bands_wofs_obs,
                    "resource_limits": reslim_wofs,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_wcs_crs": "EPSG:3577",
                        "native_resolution": [ 10.0, 10.0 ],
                        "default_bands": [ "water" ]
                    },
                    "styling": {
                        default_style: "water_classifer",
                        styles: [ style_s2_water_classifier ],
                    }
                } 
            ]
        },
        {
            "title": "Sentinel-2 Definitive",
            "abstract": """ 
This is a definitive archive of daily Sentinel-2 data.

The Surface Reflectance product has been corrected to account for variations caused by atmospheric 
properties, sun position and sensor view angle at time of image capture.

These corrections have been applied to all satellite imagery in the Sentinel-2 archive.
For more information see http://pid.geoscience.gov.au/dataset/ga/129684
""",
            "layers": [
                {
                    "name": "s2_ard_granule_nbar_t",
                    "title": "Sentinel 2 (A and B combined) Surface Reflectance",
                    "abstract": """
This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time.
The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive.

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For more information see http://pid.geoscience.gov.au/dataset/ga/129684

For service status information, see https://status.dea.ga.gov.au
""",
                    "multi_product": True,
                    "product_names": [ "s2a_ard_granule", "s2b_ard_granule" ],
                    "bands": bands_sentinel2,
                    "resource_limits": reslim_s2_ard,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_wcs_crs": "EPSG:3577",
                        "native_resolution": [ 10.0, 10.0 ],
                        "default_bands": [ "nbart_red", "nbart_green", "nbart_blue" ]
                    },
                    "styling": {
                        default_style: "simple_rgb",
                        styles: [
                            style_s2_simple_rgb,
                            style_s2_irg,
                            style_s2_ndvi, style_s2_ndwi, style_s2_mndwi, style_s2_ndci,
                            style_s2_pure_aerosol,
                            style_s2_pure_blue, style_s2_pure_green, style_s2_pure_red,
                            style_s2_pure_redge_1, style_s2_pure_redge_2, style_s2_pure_redge_3,
                            style_s2_pure_nir, style_s2_pure_narrow_nir,
                            style_s2_pure_swir1, style_s2_pure_swir2,
                        ]
                    }
                }, 
                {
                    "name": "s2a_ard_granule_nbar_t",
                    "title": "Sentinel 2A Surface Reflectance",
                    "abstract": """
This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time.
The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive.

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For more information see http://pid.geoscience.gov.au/dataset/ga/129684

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "s2a_ard_granule",
                    "bands": bands_sentinel2,
                    "resource_limits": reslim_s2_ard,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_wcs_crs": "EPSG:3577",
                        "native_resolution": [ 10.0, 10.0 ],
                        "default_bands": [ "nbart_red", "nbart_green", "nbart_blue" ]
                    },
                    "styling": {
                        default_style: "simple_rgb",
                        styles: [
                            style_s2_simple_rgb,
                            style_s2_irg,
                            style_s2_ndvi, style_s2_ndwi, style_s2_mndwi, style_s2_ndci,
                            style_s2_pure_aerosol,
                            style_s2_pure_blue, style_s2_pure_green, style_s2_pure_red,
                            style_s2_pure_redge_1, style_s2_pure_redge_2, style_s2_pure_redge_3,
                            style_s2_pure_nir, style_s2_pure_narrow_nir,
                            style_s2_pure_swir1, style_s2_pure_swir2,
                        ]
                    }
                }, 
                {
                    "name": "s2b_ard_granule_nbar_t",
                    "title": "Sentinel 2B Surface Reflectance",
                    "abstract": """
This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time.
The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive.

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For more information see http://pid.geoscience.gov.au/dataset/ga/129684

For service status information, see https://status.dea.ga.gov.au
""",
                    "product_name": "s2b_ard_granule",
                    "bands": bands_sentinel2,
                    "resource_limits": reslim_s2_ard,
                    "image_processing": {
                        "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                        "always_fetch_bands": [ ],
                        "manual_merge": False,
                    },
                    "wcs": {
                        "native_wcs_crs": "EPSG:3577",
                        "native_resolution": [ 10.0, 10.0 ],
                        "default_bands": [ "nbart_red", "nbart_green", "nbart_blue" ]
                    },
                    "styling": {
                        default_style: "simple_rgb",
                        styles: [
                            style_s2_simple_rgb,
                            style_s2_irg,
                            style_s2_ndvi, style_s2_ndwi, style_s2_mndwi, style_s2_ndci,
                            style_s2_pure_aerosol,
                            style_s2_pure_blue, style_s2_pure_green, style_s2_pure_red,
                            style_s2_pure_redge_1, style_s2_pure_redge_2, style_s2_pure_redge_3,
                            style_s2_pure_nir, style_s2_pure_narrow_nir,
                            style_s2_pure_swir1, style_s2_pure_swir2,
                        ]
                    }
                } 
            ]
        },
        {
            "title": "Multi-Scale Topographic Position",
            "abstract": "",
            "layers": [
                {
                    {
                        "title": "Multi-Scale Topographic Position",
                        "name": "multi_scale_topographic_position",
                        "abstract": """
A Multi-scale topographic position image of Australia has been generated by combining 
a topographic position index and topographic ruggedness. Topographic Position Index (TPI) measures 
the topographic slope position of landforms. Ruggedness informs on the roughness of the surface and 
is calculated as the standard deviation of elevations. Both these terrain attributes are therefore 
scale dependent and will vary according to the size of the analysis window. Based on an algorithm 
developed by Lindsay et al. (2015) we have generated multi-scale topographic position model over the 
Australian continent using 3 second resolution (~90m) DEM derived from the Shuttle Radar Topography 
Mission (SRTM). The algorithm calculates topographic position scaled by the corresponding ruggedness 
across three spatial scales (window sizes) of 0.2-8.1 Km; 8.2-65.2 Km and 65.6-147.6 Km. The derived 
ternary image captures variations in topographic position across these spatial scales (blue local, 
green intermediate and red regional) and gives a rich representation of nested landform features that 
have broad application in understanding geomorphological and hydrological processes and in mapping 
regolith and soils over the Australian continent. Lindsay, J, B., Cockburn, J.M.H. and Russell, 
H.A.J. 2015. An integral image approach to performing multi-scale topographic position analysis, 
Geomorphology 245, 51–61.

For service status information, see https://status.dea.ga.gov.au""",
                        "product_name": "multi_scale_topographic_position",
                        "bands": bands_weathering,
                        "resource_limits": reslim_weathering,
                        "image_processing": {
                            "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                            "always_fetch_bands": [ ],
                            "manual_merge": False,
                        },
                        "wcs": {
                            "native_wcs_crs": "EPSG:3577",
                            "native_resolution": [ 90.0, 90.0 ],
                            "default_bands": [ "regional", "intermediate", "local" ]
                        },
                        "styling": {
                            default_style: "mstp_rgb",
                            styles: [
                                style_mstp_rgb,
                            ]
                        }
                    },
                },
            ]
        },
        {
            "title": "Weathering Intensity",
            "abstract": "",
            "layers": [
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
                "bands": bands_multi_topog,
                "resource_limits": reslim_multi_topog,
                "image_processing": {
                    "extent_mask_function": "datacube_ows.ogc_utils.mask_by_val",
                    "always_fetch_bands": [ ],
                    "manual_merge": False,
                },
                "wcs": {
                    "native_wcs_crs": "EPSG:3577",
                    "native_resolution": [ 60.0, 60.0 ],
                    "default_bands": [ "intensity" ]
                },
                "styling": {
                    default_style: "wii",
                    styles: [
                        style_wii,
                    ]
                }
            ]
        },
        {
            "title": "Fractional Cover Percentiles - Green Vegetation",
            "abstract": "",
            "layers": [
            ]
        },
        {
            "title": "Fractional Cover Percentiles - Non Green Vegetation",
            "abstract": "",
            "layers": []
        },
        {
            "title": "Fractional Cover Percentiles - Bare Soil",
            "abstract": "",
            "layers": []
        },
        {
            "title": "Fractional Cover Percentiles - Median",
            "abstract": "",
            "layers": []
        },
        {
            "title": "Fractional Cover Percentiles Seasonal",
            "abstract": "",
            "layers": []
        },
        {
            "title": "National Intertidal Digital Elevation Model",
            "abstract": "",
            "layers": []
        },
        {
            "title": "High Tide Low Tide Composite",
            "abstract": """ 
The High and Low Tide Composites product is composed of two surface reflectance composite mosaics 
of Landsat TM and ETM+ (Landsat 5 and Landsat 7 respectively) and OLI (Landsat 8) 
surface reflectance data (Li et al., 2012). These products have been produced using 
Digital Earth Australia (DEA). The two mosaics allow cloud free and noise reduced visualisation 
of the shallow water and inter-tidal coastal regions of Australia, as observed at 
high and low tide respectively.The composites are generated utilising the geomedian approach of 
Roberts et al (2017) to ensure a valid surface reflectance spectra suitable for uses such as 
habitat mapping. The time range used for composite generation in each polygon of the mosaic is 
tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud 
free composite to be generated. The concepts of the Observed Tidal Range (OTR), 
and Highest and Lowest Observed Tide (HOT, LOT) are discussed and described fully in Sagar et al. 
(2017) and the product description for the ITEM v 1.0 product (Geoscience Australia, 2016).
            """,
            "layers": []
        },
        {
            "title": "Intertidal Extents Model (ITEM)",
            "abstract": """
The Intertidal Extents Model (ITEM) product is a national dataset of the exposed intertidal zone;
the land between the observed highest and lowest tide. ITEM provides the extent and topography of 
the intertidal zone of Australia's coastline (excluding off-shore Territories). 
This information was collated using observations in the Landsat archive since 1986. 
ITEM can be a valuable complimentary dataset to both onshore LiDAR survey data and coarser offshore 
bathymetry data, enabling a more realistic representation of the land and ocean interface.
""",
        "layers": []
        },
        {
            "title": "Projects",
            "abstract": "Projects",
            "layers": []
        },
        {
            "title": "ASTER Geoscience Map of Australia",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

The individual geoscience products are a combination of bands and band ratios to highlight different mineral groups and parameters including:
- False Colour Mosaic
- CSIRO Landsat TM
- Regolith Ratios
- AlOH Group Composition
- AlOH Group Content
- FeOH Group Content
- Ferric Oxide Composition
- Ferric Oxide Content
- Ferrous Iron Content in MgOH/Carbonate
- Ferrous Iron Index
- Green Vegetation Content
- Gypsum Index
- Kaolin Group Index
- MgOH Group Composition
- MgOH Group Content
- Opaque Index
- TIR Silica index
- TIR Quartz Index
- Surface mineral group distribution (relative abundance and composition)

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347
""",
            "layers": []
        },
        {
            "title": "Fractional Cover",
            "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au
""",
            "layers": []
        },
    ] # End of Layers List
} # End of ows_cfg object
