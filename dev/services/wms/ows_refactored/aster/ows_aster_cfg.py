from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35

bands_aster = {
    "Band_1": [],
    "Band_2": [],
    "Band_3": [],
}

bands_aster_single_band = {
    "Band_1": [],
}

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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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
    "color_ramp": [
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
    ],
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


layers = {
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
    "layers": [
        {
            "title": "ASTER Geoscience Map of Australia (False Colour Mosaic)",
            "name": "aster_false_colour",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


False colour RGB composite

- Red: B3
- Green: B2
- Blue: B1
(red = green vegetation)

Use this image to help understand non-geological differences within and between ASTER scenes caused by green vegetation (red), fire scars, thin and thick cloud and cloud shadows.

Use band 2 only for a gray-scale background to the content, composition and index colour products.

For 'False Colour Mosaic' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74348

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_false_colour",
            "bands": bands_aster,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1", "Band_2", "Band_3"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "false_colour",
                "styles": [
                    style_aster_false_colour,
                    style_aster_b2_gray,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Regolith Ratios)",
            "name": "aster_regolith_ratios",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


3 band RGB composite

- Red: B3/B2
- Green: B3/B7
- Blue: B4/B7
(white = green vegetation)

Use this image to help interpret:

(1) the amount of green vegetation cover (appears as white);

(2) basic spectral separation (colour) between different regolith and geological units and regions/provinces; and

(3) evidence for unmasked cloud (appears as green).

For 'Regolith Ratios' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74349

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_regolith_ratios",
            "bands": bands_aster,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1", "Band_2", "Band_3"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": [
                    style_aster_simple_rgb,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (AlOH Group Composition)",
            "name": "aster_aloh_group_composition",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: B5/B7

- Blue is well ordered kaolinite, Al-rich muscovite/illite, paragonite, pyrophyllite
- Red is Al-poor (Si-rich) muscovite (phengite)

Useful for mapping:

(1) exposed saprolite/saprock is often white mica or Al-smectite (warmer colours) whereas transported materials are often kaolin-rich (cooler colours);

(2) clays developed over carbonates, especially Al-smectite (montmorillonite, beidellite) will produce middle to warmers colours;

(3) stratigraphic mapping based on different clay-types; and

(4) lithology-overprinting hydrothermal alteration, e.g. Si-rich and K-rich phengitic mica (warmer colours).

Combine with Ferrous iron in MgOH and FeOH content products to look for evidence of overlapping/juxtaposed potassic metasomatism in ferromagnesian parents rocks (e.g. Archaean greenstone associated Au mineralisation) +/- associated distal propyllitic alteration (e.g. chlorite, amphibole)

For 'AlOH Group Composition' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74356

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_aloh_group_composition",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_aloh_comp_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (AlOH Group Content)",
            "name": "aster_aloh_group_content",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: (B5+B7)/B6

- Blue is low abundance
- Red is high abundance

(potentially includes: phengite, muscovite, paragonite, lepidolite, illite, brammalite, montmorillonite, beidellite, kaolinite, dickite)

Useful for mapping:

(1) exposed saprolite/saprock;

(2) clay-rich stratigraphic horizons;

(3) lithology-overprinting hydrothermal phyllic (e.g. white mica) alteration; and

(4) clay-rich diluents in ore systems (e.g. clay in iron ore).

Also combine with AlOH composition to help map:

(1) exposed in situ parent material persisting through “cover” which can be expressed as:

(a) more abundant AlOH content +

(b) long-wavelength (warmer colour) AlOH composition (e.g. muscovite/phengite)

For 'AlOH Group Content' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74355

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_aloh_group_content",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_aloh_cont_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (FeOH Group Content)",
            "name": "aster_feoh_group_content",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: (B6+B8)/B7

- Blue is low content,
- Red is high content

(potentially includes: chlorite, epidote, jarosite, nontronite, gibbsite, gypsum, opal-chalcedony

Useful for mapping:

(1) jarosite (acid conditions) – in combination with ferric oxide content (high);

(2) gypsum/gibbsite – in combination with ferric oxide content (low);

(3) magnesite - in combination with ferric oxide content (low) and MgOH content (moderate-high);

(4) chlorite (e.g. propyllitic alteration) – in combination with Ferrous in MgOH (high); and

(5) epidote (calc-silicate alteration) – in combination with Ferrous in MgOH (low).

For 'FeOH Group Content' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74358

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_feoh_group_content",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_feoh_cont_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Ferric Oxide Composition)",
            "name": "aster_ferric_oxide_composition",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: B2/B1

- Blue-cyan is goethite rich,
- Green is hematite-goethite,
- Red-yellow is hematite-rich

Useful For:

(1) Mapping transported materials (including palaeochannels) characterised by hematite (relative to geothite). Combine with AlOH composition to find co-located areas of hematite and poorly ordered kaolin to map transported materials; and

(2) hematite-rish areas in drier conditions (eg above the water table) whereas goethite-rich in wetter conditions (eg at/below the water or areas recently exposed). May also be climate driven.

For 'Ferric Oxide Composition' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74352

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_ferric_oxide_composition",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_ferrox_comp_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Ferric Oxide Content)",
            "name": "aster_ferric_oxide_content",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: B4/B3

- Blue is low abundance,
- Red is high abundance

Useful for:

(1) Exposed iron ore (hematite-goethite). Use in combination with the “Opaques index” to help separate/map dark:

   (a) surface lags (e.g. maghemite gravels) which can be misidentified in visible and false colour imagery; and

   (b) magnetite in BIF and/or bedded iron ore; and

(2) Acid conditions: combine with FeOH Group content to help map jarosite which will have high values in both products.

Mapping hematite versus goethite mapping is NOT easily achieved as ASTER’s spectral bands were not designed to capture diagnostic iron oxide spectral behaviour.

However, some information on visible colour relating in part to differences in hematite and/or goethite content can be obtained using a ratio of B2/B1 especially when this is masked using a B4/B3 to locate those pixels with sufficient iro oxide content.

For 'Ferric Oxide Content' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74351

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_ferric_oxide_content",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_ferrox_cont_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Ferrous Iron Content in MgOH/Carbonate)",
            "name": "aster_ferrous_iron_content_in_mgoh",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: B5/B4

- Blue is low ferrous iron content in carbonate and MgOH minerals like talc and tremolite.
- Red is high ferrous iron content in carbonate and MgOH minerals like chlorite and actinolite.

Useful for mapping:

(1) un-oxidised “parent rocks” – i.e. mapping exposed parent rock materials (warm colours) in transported cover;

(2) talc/tremolite (Mg-rich – cool colours) versus actinolite (Fe-rich – warm colours);

(3) ferrous-bearing carbonates (warm colours) potentially associated with metasomatic “alteration”;

(4) calcite/dolomite which are ferrous iron-poor (cool colours); and

(5) epidote, which is ferrous iron poor (cool colours) – in combination with FeOH content product (high).

For 'Ferrous Iron Content in MgOH/Carbonate' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74361

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_ferrous_iron_content_in_mgoh",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_ferrous_mgoh_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Ferrous Iron Index)",
            "name": "aster_ferrous_iron_index",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: B5/B4

- Blue is low abundance,
- Red is high abundance

This product can help map exposed “fresh” (un-oxidised) rocks (warm colours) especially mafic and ultramafic lithologies rich in ferrous silicates (e.g. actinolite, chlorite) and/or ferrous carbonates (e.g. ferroan dolomite, ankerite, siderite).

Applying an MgOH Group content mask to this product helps to isolate ferrous bearing non-OH bearing minerals like pyroxenes (e.g. jadeite) from OH-bearing or carbonate-bearing ferrous minerals like actinolite or ankerite, respectively.

Also combine with the FeOH Group content product to find evidence for ferrous-bearing chlorite (e.g. chamosite).

For 'Ferrous Iron Index' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74353

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_ferrous_iron_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_ferrous_idx_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Green Vegetation Content)",
            "name": "aster_green_vegetation",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: B3/B2

- Blue is low content,
- Red is high content

Use this image to help interpret the amount of “obscuring/complicating” green vegetation cover.

For 'Green Vegetation Content' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74350

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_green_vegetation",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_green_veg_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Gypsum Index)",
            "name": "aster_gypsum_index",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band Ratio: (B10+B12)/B11

- Blue is low gypsum content,
- Red is high gypsum content

Useful for mapping:

(1) evaporative environments (e.g. salt lakes) and associated arid aeolian systems (e.g. dunes);

(2) acid waters (e.g. from oxidising sulphides) invading carbonate rich materials including around mine environments; and

(3) hydrothermal (e.g. volcanic) systems.

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_gypsum_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_gypsum_idx_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Kaolin Group Index)",
            "name": "aster_kaolin_group_index",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band Ratio: B6/B5

- Blue is low content,
- Red is high content

(potentially includes: pyrophyllite, alunite, well-ordered kaolinite)

Useful for mapping:

(1) different clay-type stratigraphic horizons;

(2) lithology-overprinting hydrothermal alteration, e.g. high sulphidation, “advanced argillic” alteration comprising pyrophyllite, alunite, kaolinite/dickite; and

(3) well-ordered kaolinite (warmer colours) versus poorly-ordered kaolinite (cooler colours) which can be used for mapping in situ versus transported materials, respectively.

For 'Kaolin Group Index' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74357

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_kaolin_group_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_kaolin_idx_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (MgOH Group Composition)",
            "name": "aster_mgoh_group_composition",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: B7/B8

- Blue-cyan is magnesite-dolomite, amphibole, chlorite
- Red is calcite, epidote, amphibole

Useful for mapping:

(1) exposed parent material persisting through "cover";

(2) "dolomitization" alteration in carbonates - combine with Ferrous iron in MgOH product to help separate dolomite versus ankerite;

(3) lithology-cutting hydrothermal (e.g. propyllitic) alteration - combine with FeOH content product and ferrous iron in Mg-OH to isolate chlorite from actinolite versus talc versus epidote; and

(4) layering within mafic/ultramafic intrusives


For 'MgOH Group Composition' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74360

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_mgoh_group_composition",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_mgoh_comp_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (MgOH Group Content)",
            "name": "aster_mgoh_group_content",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: (B6+B9)/(B7+B8)

- Blue is low content,
- Red is high content

(potentially includes: calcite, dolomite, magnesite, chlorite, epidote, amphibole, talc, serpentine)

Useful for mapping:

(1) “hydrated” ferromagnesian rocks rich in OH-bearing tri-octahedral silicates like actinolite, serpentine, chlorite and talc;

(2) carbonate-rich rocks, including shelf (palaeo-reef) and valley carbonates(calcretes, dolocretes and magnecretes); and

(3) lithology-overprinting hydrothermal alteration, e.g. “propyllitic alteration” comprising chlorite, amphibole and carbonate.

The nature (composition) of the silicate or carbonate mineral can be further assessed using the MgOH composition product.

For 'MgOH Group Content' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74359

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_mgoh_group_content",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_mgoh_cont_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Opaque Index)",
            "name": "aster_opaque_index",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: B1/B4

- Blue is low abundance,
- Red is high abundance

(potentially includes carbon black (e.g. ash), magnetite, Mn oxides, and sulphides in unoxidised environments)

Useful for mapping:

(1) magnetite-bearing rocks (e.g. BIF);

(2) maghemite gravels;

(3) manganese oxides;

(4) graphitic shales.

Note: (1) and (4) above can be evidence for “reduced” rocks when interpreting REDOX gradients.

Combine with AlOH group Content (high values) and Composition (high values) products, to find evidence for any invading “oxidised” hydrothermal fluids which may have interacted with reduced rocks evident in the Opaques index product.

For 'Opaque Index' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74354

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_opaque_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_opaque_idx_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (TIR Silica index)",
            "name": "aster_silica_index",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: B13/B10

- Blue is low silica content,
- Red is high silica content

(potentially includes Si-rich minerals, such as quartz, feldspars, Al-clays)

Geoscience Applications:

Broadly equates to the silica content though the intensity (depth) of this reststrahlen feature is also affected by particle size &lt;250 micron.

Useful product for mapping:

(1) colluvial/alluvial materials;

(2) silica-rich (quartz) sediments (e.g. quartzites);

(3) silification and silcretes; and

(4) quartz veins.

Use in combination with quartz index, which is often correlated with the Silica index.

For 'TIR Silica index' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74362

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_silica_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_silica_idx_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (TIR Quartz Index)",
            "name": "aster_quartz_index",
            "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

ASTER calibration, processing and standardisation approaches have been produced as part of a large multi-agency project to facilitate uptake of these techniques and make them easily integrated with other datasets in a GIS.

Collaborative research, undertaken by Geoscience Australia, the Commonwealth Scientific Research Organisation (CSIRO) and state and industry partners, on the world-class Mt Isa mineral province in Queensland was completed in 2008 as a test-case for these new methods.

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347


Band ratio: B11/(B10+B12)

- Blue is low quartz content,
- Red is high quartz content

Geoscience Applications:

Use in combination with Silica index to more accurately map “crystalline” quartz rather than poorly ordered silica (e.g. opal), feldspars and compacted clays.

For 'TIR Quartz Index' dataset information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74363

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "aster_quartz_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["Band_1"],
                "native_resolution": [15.0, 15.0],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_quartz_idx_ramp,
                ],
            },
        },
    ],
}
