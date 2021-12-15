from ows_refactored.land_and_vegetation.fc.flag_fc_cfg import fc_pq_mask
from ows_refactored.ows_legend_cfg import (
    legend_idx_0_100_pixel_fc_25ticks, legend_idx_0_100_pixel_fc_bs_25ticks,
    legend_idx_0_100_pixel_fc_ngv_25ticks)

c3_fc_pq_mask = [
    {
        # pq_masks:band now takes the actual ODC band name, not the identifier.
        "band": "water",
        "flags": {"dry": True},
    },
    {
        "band": "water",
        "flags": {
            "terrain_shadow": False,
            "low_solar_angle": False,
            "high_slope": False,
            "cloud_shadow": False,
            "cloud": False,
        },
    },
    {
        "band": "land",
        "invert": True,
        "values": [0],
    },
]

style_fc_c3_rgb = {
    "name": "fc_rgb",
    "title": "Three-band Fractional Cover",
    "abstract": "Fractional cover medians - red is bare soil, green is green vegetation and blue is non-green vegetation",
    "components": {
        "red": {"bs": 1.0},
        "green": {"pv": 1.0},
        "blue": {"npv": 1.0},
    },
    "scale_range": [0.0, 100.0],
    "pq_masks": c3_fc_pq_mask,
    "legend": {
        "show_legend": True,
        "url": "https://data.dea.ga.gov.au/fractional-cover/FC_legend.png",
    },
}

style_fc_gv_c3 = {
    "name": "green_veg_c3",
    "title": "Green Vegetation",
    "abstract": "Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "pv",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["pv"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffcc",
        },
        {
            "value": 25,
            "color": "#c2e699",
        },
        {
            "value": 50,
            "color": "#78c679",
        },
        {
            "value": 75,
            "color": "#31a354",
        },
        {
            "value": 100,
            "color": "#006837",
        },
    ],
    "pq_masks": c3_fc_pq_mask,
    "legend": legend_idx_0_100_pixel_fc_25ticks,
}

style_fc_bs_c3 = {
    "name": "bare_ground_c3",
    "title": "Bare Ground",
    "abstract": "Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bs",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["bs"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#feebe2",
        },
        {
            "value": 25,
            "color": "#fbb4b9",
        },
        {
            "value": 50,
            "color": "#f768a1",
        },
        {
            "value": 75,
            "color": "#c51b8a",
        },
        {
            "value": 100,
            "color": "#7a0177",
        },
    ],
    "pq_masks": c3_fc_pq_mask,
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
}

style_fc_ngv_c3 = {
    "name": "non_green_veg_c3",
    "title": "Non-Green vegetation",
    "abstract": "Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "npv",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["npv"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffd4",
        },
        {"value": 25, "color": "#fed98e", "legend": {}},
        {
            "value": 50,
            "color": "#fe9929",
        },
        {
            "value": 75,
            "color": "#d95f0e",
        },
        {
            "value": 100,
            "color": "#993404",
        },
    ],
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    "pq_masks": c3_fc_pq_mask,
}

style_fc_simple_rgb = {
    "name": "simple_rgb",
    "title": "Simple RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {
        "red": {"BS_PC_50": 1.0},
        "green": {"PV_PC_50": 1.0},
        "blue": {"NPV_PC_50": 1.0},
    },
    "scale_range": [0.0, 100.0],
    "pq_masks": fc_pq_mask,
}

style_fc_simple = {
    "name": "simple_fc",
    "title": "Fractional Cover",
    "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
    "components": {"red": {"BS": 1.0}, "green": {"PV": 1.0}, "blue": {"NPV": 1.0}},
    "scale_range": [0.0, 100.0],
    "pq_masks": [
        {
            "band": "water",
            "flags": {"dry": True},
        },
        {
            "band": "water",
            "flags": {
                "terrain_or_low_angle": False,
                "high_slope": False,
                "cloud_shadow": False,
                "cloud": False,
                "sea": False,
            }
        },
    ],
}

style_fc_gv_10 = {
    "name": "green_veg_10",
    "title": "10th Percentile",
    "abstract": "10th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "PV_PC_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["PV_PC_10"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffcc",
        },
        {
            "value": 25,
            "color": "#c2e699",
        },
        {
            "value": 50,
            "color": "#78c679",
        },
        {
            "value": 75,
            "color": "#31a354",
        },
        {
            "value": 100,
            "color": "#006837",
        },
    ],
    "pq_masks": fc_pq_mask,
    "legend": legend_idx_0_100_pixel_fc_25ticks,
}

style_fc_gv_50 = {
    "name": "green_veg_50",
    "title": "50th Percentile",
    "abstract": "50th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "PV_PC_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["PV_PC_50"],
    "color_ramp": [
        {"value": 0, "color": "#ffffcc"},
        {"value": 25, "color": "#c2e699"},
        {"value": 50, "color": "#78c679"},
        {"value": 75, "color": "#31a354"},
        {"value": 100, "color": "#006837"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_25ticks,
    "pq_masks": fc_pq_mask,
}

style_fc_gv_90 = {
    "name": "green_veg_90",
    "title": "90th Percentile",
    "abstract": "90th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "PV_PC_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["PV_PC_90"],
    "color_ramp": [
        {"value": 0, "color": "#ffffcc"},
        {"value": 25, "color": "#c2e699"},
        {"value": 50, "color": "#78c679"},
        {"value": 75, "color": "#31a354"},
        {"value": 100, "color": "#006837"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_25ticks,
    "pq_masks": fc_pq_mask,
}

style_fc_ngv_10 = {
    "name": "non_green_veg_10",
    "title": "10th Percentile",
    "abstract": "10th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "NPV_PC_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["NPV_PC_10"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffd4",
        },
        {"value": 25, "color": "#fed98e", "legend": {}},
        {
            "value": 50,
            "color": "#fe9929",
        },
        {
            "value": 75,
            "color": "#d95f0e",
        },
        {
            "value": 100,
            "color": "#993404",
        },
    ],
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    "pq_masks": fc_pq_mask,
}

style_fc_ngv_50 = {
    "name": "non_green_veg_50",
    "title": "50th Percentile",
    "abstract": "50th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "NPV_PC_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["NPV_PC_50"],
    "color_ramp": [
        {"value": 0, "color": "#ffffd4"},
        {"value": 25, "color": "#fed98e"},
        {"value": 50, "color": "#fe9929"},
        {"value": 75, "color": "#d95f0e"},
        {"value": 100, "color": "#993404"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    "pq_masks": fc_pq_mask,
}

style_fc_ngv_90 = {
    "name": "non_green_veg_90",
    "title": "90th Percentile",
    "abstract": "90th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "NPV_PC_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["NPV_PC_90"],
    "color_ramp": [
        {"value": 0, "color": "#ffffd4"},
        {"value": 25, "color": "#fed98e"},
        {"value": 50, "color": "#fe9929"},
        {"value": 75, "color": "#d95f0e"},
        {"value": 100, "color": "#993404"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    "pq_masks": fc_pq_mask,
}

style_fc_bs_10 = {
    "name": "bare_ground_10",
    "title": "10th Percentile",
    "abstract": "10th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "BS_PC_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["BS_PC_10"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#feebe2",
        },
        {
            "value": 25,
            "color": "#fbb4b9",
        },
        {
            "value": 50,
            "color": "#f768a1",
        },
        {
            "value": 75,
            "color": "#c51b8a",
        },
        {
            "value": 100,
            "color": "#7a0177",
        },
    ],
    "pq_masks": fc_pq_mask,
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
}

style_fc_bs_50 = {
    "name": "bare_ground_50",
    "title": "50th Percentile",
    "abstract": "50th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "BS_PC_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["BS_PC_50"],
    "color_ramp": [
        {"value": 0, "color": "#feebe2"},
        {"value": 25, "color": "#fbb4b9"},
        {"value": 50, "color": "#f768a1"},
        {"value": 75, "color": "#c51b8a"},
        {"value": 100, "color": "#7a0177"},
    ],
    # Old behaviour was wrong - this is what Leo and Emma have requested.
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
    "pq_masks": fc_pq_mask,
}

style_fc_bs_90 = {
    "name": "bare_ground_90",
    "title": "90th Percentile",
    "abstract": "90th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "BS_PC_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["BS_PC_90"],
    "color_ramp": [
        {"value": 0, "color": "#feebe2"},
        {"value": 25, "color": "#fbb4b9"},
        {"value": 50, "color": "#f768a1"},
        {"value": 75, "color": "#c51b8a"},
        {"value": 100, "color": "#7a0177"},
    ],
    # Old behaviour was wrong - this is what Leo and Emma have requested.
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
    "pq_masks": fc_pq_mask,
}

style_fc_rgb = {
    "name": "fc_rgb",
    "title": "Three-band fractional cover",
    "abstract": "Fractional cover medians - red is bare soil, green is green vegetation and blue is non-green vegetation",
    "components": {
        "red": {"BS_PC_50": 1.0},
        "green": {"PV_PC_50": 1.0},
        "blue": {"NPV_PC_50": 1.0},
    },
    "scale_range": [0.0, 100.0],
    "pq_masks": fc_pq_mask,
    "legend": {
        "show_legend": True,
        "url": "https://data.dea.ga.gov.au/fractional-cover/FC_legend.png",
    },
}

styles_fc_gv_list = [
    style_fc_gv_10,
    style_fc_gv_50,
    style_fc_gv_90,
]

styles_fc_ngv_list = [
    style_fc_ngv_10,
    style_fc_ngv_50,
    style_fc_ngv_90,
]

styles_fc_bare_list = [
    style_fc_bs_10,
    style_fc_bs_50,
    style_fc_bs_90,
]
