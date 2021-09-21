color_ramp_aster = [
    {
        "value": 0.0,
        "color": "#8F3F20",
        "alpha": 0.0,
    },
    {"value": 1, "color": "#000000"},
    {"value": 10, "color": "#2d002b"},
    {"value": 25, "color": "#550071"},
    {"value": 60, "color": "#0400ff"},
    {"value": 90, "color": "#0098ff"},
    {"value": 110, "color": "#00ffff"},
    {"value": 130, "color": "#00ff94"},
    {"value": 150, "color": "#00ff2a"},
    {"value": 170, "color": "#3fff00"},
    {"value": 210, "color": "#ffee00"},
    {"value": 230, "color": "#ff8300"},
    {
        "value": 255.0,
        "color": "#ff0000",
    },
]

style_aster_false_colour = {
    "name": "false_colour",
    "title": "False Colour",
    "abstract": "Simple false-colour image using ASTER Bands 3 as red, 2 as green and 1 as blue",
    "components": {
        "red": {"Band_1": 1.0},
        "green": {"Band_2": 1.0},
        "blue": {"Band_3": 1.0},
    },
    "scale_range": [0.0, 255.0],
}

style_aster_b2_gray = {
    "name": "gray",
    "title": "B2 Grayscale",
    "abstract": "Simple grayscale image using ASTER Band 2",
    "components": {
        "red": {"Band_2": 1.0},
        "green": {"Band_2": 1.0},
        "blue": {"Band_2": 1.0},
    },
    "scale_range": [0.0, 255.0],
}

style_aster_simple_rgb = {
    "name": "simple_rgb",
    "title": "Simple RGB",
    "abstract": "Simple  true-colour image, using the red, green and blue bands",
    "components": {
        "red": {"Band_1": 1.0},
        "green": {"Band_2": 1.0},
        "blue": {"Band_3": 1.0},
    },
    "scale_range": [0.0, 255.0],
}

style_aster_aloh_comp_ramp = {
    "name": "ramp",
    "title": "B5/B7 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "0.9"},
            "255.0": {"label": "1.3"},
        },
        "units": "Blue is well ordered kaolinite,\nRed is Al-poor (Si-rich) muscovite (phengite)",
    },
}

style_aster_aloh_cont_ramp = {
    "name": "ramp",
    "title": "(B5+B7)/B6 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "2.0"},
            "255.0": {"label": "2.25"},
        },
        "units": "Blue is low content,\nRed is high content",
    },
}

style_aster_feoh_cont_ramp = {
    "name": "ramp",
    "title": "(B6+B8)/B7 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "2.03"},
            "255.0": {"label": "2.25"},
        },
        "units": "Blue is low content,\nRed is high content",
    },
}

style_aster_ferrox_comp_ramp = {
    "name": "ramp",
    "title": "B2/B1 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "0.5"},
            "255.0": {"label": "3.3"},
        },
        "units": "Blue-cyan is non-hematitie,\nRed-yellow is hematite-rich",
    },
}

style_aster_ferrox_cont_ramp = {
    "name": "ramp",
    "title": "B4/B3 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "1.1"},
            "255.0": {"label": "2.1"},
        },
        "units": "Blue is low abundance,\nRed is high abundance",
    },
}

style_aster_ferrous_mgoh_ramp = {
    "name": "ramp",
    "title": "B5/B4 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "0.1"},
            "255.0": {"label": "2.0"},
        },
        "units": "Blue is low ferrous iron content,\nRed is high ferrous iron content",
    },
}

style_aster_ferrous_idx_ramp = {
    "name": "ramp",
    "title": "B5/B4 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "0.75"},
            "255.0": {"label": "1.025"},
        },
        "units": "Blue is low abundance,\nRed is high abundance",
    },
}

style_aster_green_veg_ramp = {
    "name": "ramp",
    "title": "B3/B2 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "1.4"},
            "255.0": {"label": "4"},
        },
        "units": "Blue is low content,\nRed is high content",
    },
}

style_aster_gypsum_idx_ramp = {
    "name": "ramp",
    "title": "(B10+B12)/B11 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "0.47"},
            "255.0": {"label": "0.5"},
        },
        "units": "Blue is low content,\nRed is high content",
    },
}

style_aster_kaolin_idx_ramp = {
    "name": "ramp",
    "title": "B6/B5 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "1.0"},
            "255.0": {"label": "1.25"},
        },
        "units": "Blue is low content,\nRed is high content",
    },
}

style_aster_mgoh_comp_ramp = {
    "name": "ramp",
    "title": "B7/B8 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "0.6"},
            "255.0": {"label": "1.4"},
        },
        "units": "Blue-cyan is magnesite-dolomite, amphibole, \nRed is calcite, epidote, amphibole",
    },
}

style_aster_mgoh_cont_ramp = {
    "name": "ramp",
    "title": "(B6+B9/(B7+B8) ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "1.05"},
            "255.0": {"label": "1.2"},
        },
        "units": "Blue low content,\nRed is high content",
    },
}

style_aster_opaque_idx_ramp = {
    "name": "ramp",
    "title": "B1/B4 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "0.4"},
            "255.0": {"label": "0.9"},
        },
        "units": "Blue low content,\nRed is high content",
    },
}

style_aster_silica_idx_ramp = {
    "name": "ramp",
    "title": "B13/B10 ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "1.0"},
            "255.0": {"label": "1.35"},
        },
        "units": "Blue low silica content,\nRed is high silica content",
    },
}

style_aster_quartz_idx_ramp = {
    "name": "ramp",
    "title": "B11/(B10+B12) ",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "Band_1",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["Band_1"],
    "color_ramp": color_ramp_aster,
    "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "0.5"},
            "255.0": {"label": "0.52"},
        },
        "units": "Blue low quartz content,\nRed is high quartz content",
    },
}
