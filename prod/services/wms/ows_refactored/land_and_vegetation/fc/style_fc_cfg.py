from ows_refactored.land_and_vegetation.fc.flag_fc_cfg import \
    fc_percentile_pq_mask
from ows_refactored.ows_legend_cfg import (
    legend_idx_0_100_pixel_fc_25ticks, legend_idx_0_100_pixel_fc_bs_25ticks,
    legend_idx_0_100_pixel_fc_ngv_25ticks)

c3_fc_pq_mask = [
    {
        # pq_masks:band now takes the actual ODC band name, not the identifier.
        "band": "water",
        "flags": {
            "water_observed": False,
            "terrain_shadow": False,
            "low_solar_angle": False,
            "high_slope": False,
            "cloud_shadow": False,
            "cloud": False,
            "nodata": False,
        },
    },
    {
        "band": "land",
        "invert": True,
        "values": [0],
    },
]

style_fc_c3_rgb_unmasked = {
    "name": "fc_rgb_unmasked",
    "title": "Three-band Fractional Cover Unmasked (Warning: includes invalid data)",
    "abstract": "Fractional cover medians - red is bare soil, green is green vegetation and blue is non-green vegetation",
    "components": {
        "red": {"bs": 1.0},
        "green": {"pv": 1.0},
        "blue": {"npv": 1.0},
    },
    "scale_range": [0.0, 100.0],
    "legend": {
        "show_legend": True,
        "url": "https://data.dea.ga.gov.au/fractional-cover/FC_legend.png",
    },
}

style_fc_c3_rgb = {
    "inherits": style_fc_c3_rgb_unmasked,
    "name": "fc_rgb",
    "title": "Three-band Fractional Cover",
    "pq_masks": c3_fc_pq_mask,
}

style_fc_gv_c3_unmasked = {
    "name": "green_veg_c3_unmasked",
    "title": "Green Vegetation Unmasked (Warning: includes invalid data)",
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
    "legend": legend_idx_0_100_pixel_fc_25ticks,
}

style_fc_gv_c3 = {
    "inherits": style_fc_gv_c3_unmasked,
    "name": "green_veg_c3",
    "title": "Green Vegetation",
    "pq_masks": c3_fc_pq_mask,
}

style_fc_bs_c3_unmasked = {
    "name": "bare_ground_c3_unmasked",
    "title": "Bare Ground Unmasked (Warning: includes invalid data)",
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
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
}

style_fc_bs_c3 = {
    "inherits": style_fc_bs_c3_unmasked,
    "name": "bare_ground_c3",
    "title": "Bare Ground",
    "pq_masks": c3_fc_pq_mask,
}

style_fc_ngv_c3_unmasked = {
    "name": "non_green_veg_c3_unmasked",
    "title": "Non-Green Vegetation Unmasked (Warning: includes invalid data)",
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
        {
            "value": 25,
            "color": "#fed98e",
        },
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
}

style_fc_ngv_c3 = {
    "inherits": style_fc_ngv_c3_unmasked,
    "name": "non_green_veg_c3",
    "title": "Non-Green vegetation",
    "pq_masks": c3_fc_pq_mask,
}


styles_fc_c3_masked = [
    style_fc_c3_rgb,
    style_fc_bs_c3, style_fc_gv_c3, style_fc_ngv_c3
]
styles_fc_c3_unmasked = [
    style_fc_c3_rgb_unmasked,
    style_fc_bs_c3_unmasked, style_fc_gv_c3_unmasked, style_fc_ngv_c3_unmasked
]

style_fc_gv_10 = {
    "name": "green_veg_10",
    "title": "Green Vegetation 10th Percentile",
    "abstract": "10th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "pv_pc_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["pv_pc_10"],
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
    "pq_masks": fc_percentile_pq_mask,
    "legend": legend_idx_0_100_pixel_fc_25ticks,
}

style_fc_gv_50 = {
    "name": "green_veg_50",
    "title": "Green Vegetation 50th Percentile",
    "abstract": "50th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "pv_pc_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["pv_pc_50"],
    "color_ramp": [
        {"value": 0, "color": "#ffffcc"},
        {"value": 25, "color": "#c2e699"},
        {"value": 50, "color": "#78c679"},
        {"value": 75, "color": "#31a354"},
        {"value": 100, "color": "#006837"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_25ticks,
    "pq_masks": fc_percentile_pq_mask,
}

style_fc_gv_90 = {
    "name": "green_veg_90",
    "title": "Green Vegetation 90th Percentile",
    "abstract": "90th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "pv_pc_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["pv_pc_90"],
    "color_ramp": [
        {"value": 0, "color": "#ffffcc"},
        {"value": 25, "color": "#c2e699"},
        {"value": 50, "color": "#78c679"},
        {"value": 75, "color": "#31a354"},
        {"value": 100, "color": "#006837"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_25ticks,
    "pq_masks": fc_percentile_pq_mask,
}

style_fc_ngv_10 = {
    "name": "non_green_veg_10",
    "title": "Non-green Vegetation 10th Percentile",
    "abstract": "10th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "npv_pc_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["npv_pc_10"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffd4",
        },
        {"value": 25, "color": "#fed98e"},
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
    "pq_masks": fc_percentile_pq_mask,
}

style_fc_ngv_50 = {
    "name": "non_green_veg_50",
    "title": "Non-green Vegetation 50th Percentile",
    "abstract": "50th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "npv_pc_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["npv_pc_50"],
    "color_ramp": [
        {"value": 0, "color": "#ffffd4"},
        {"value": 25, "color": "#fed98e"},
        {"value": 50, "color": "#fe9929"},
        {"value": 75, "color": "#d95f0e"},
        {"value": 100, "color": "#993404"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    "pq_masks": fc_percentile_pq_mask,
}

style_fc_ngv_90 = {
    "name": "non_green_veg_90",
    "title": "Non-green Vegetation 90th Percentile",
    "abstract": "90th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "npv_pc_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["npv_pc_90"],
    "color_ramp": [
        {"value": 0, "color": "#ffffd4"},
        {"value": 25, "color": "#fed98e"},
        {"value": 50, "color": "#fe9929"},
        {"value": 75, "color": "#d95f0e"},
        {"value": 100, "color": "#993404"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    "pq_masks": fc_percentile_pq_mask,
}

style_fc_bs_10 = {
    "name": "bare_ground_10",
    "title": "Bare soil 10th Percentile",
    "abstract": "10th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bs_pc_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["bs_pc_10"],
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
    "pq_masks": fc_percentile_pq_mask,
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
}

style_fc_bs_50 = {
    "name": "bare_ground_50",
    "title": "Bare soil 50th Percentile",
    "abstract": "50th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bs_pc_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["bs_pc_50"],
    "color_ramp": [
        {"value": 0, "color": "#feebe2"},
        {"value": 25, "color": "#fbb4b9"},
        {"value": 50, "color": "#f768a1"},
        {"value": 75, "color": "#c51b8a"},
        {"value": 100, "color": "#7a0177"},
    ],
    # Old behaviour was wrong - this is what Leo and Emma have requested.
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
    "pq_masks": fc_percentile_pq_mask,
}

style_fc_bs_90 = {
    "name": "bare_ground_90",
    "title": "Bare soil 90th Percentile",
    "abstract": "90th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bs_pc_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["bs_pc_90"],
    "color_ramp": [
        {"value": 0, "color": "#feebe2"},
        {"value": 25, "color": "#fbb4b9"},
        {"value": 50, "color": "#f768a1"},
        {"value": 75, "color": "#c51b8a"},
        {"value": 100, "color": "#7a0177"},
    ],
    # Old behaviour was wrong - this is what Leo and Emma have requested.
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
    "pq_masks": fc_percentile_pq_mask,
}

style_fc_pc_qa = {
    "name": "qa",
    "title": "Quality Assurance",
    "abstract": "Quality Assurance",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "qa",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["qa"],
    "value_map": {
        "qa": [
            {
                "title": "Insufficient observations wet",
                "abstract": "",
                "values": [
                    0,
                ],
                "color": "#7884A2",
            },
            {
                "title": "Insufficient observations dry",
                "abstract": "",
                "values": [
                    1,
                ],
                "color": "#A29678",
            },
            {
                "title": "Sufficient observations",
                "abstract": "",
                "values": [
                    2,
                ],
                "color": "#84A278",
            },

        ],
    },
    "pq_masks": fc_percentile_pq_mask,
}

style_fc_rgb = {
    "name": "fc_rgb",
    "title": "Three-band fractional cover",
    "abstract": "Fractional cover medians - red is bare soil, green is green vegetation and blue is non-green vegetation",
    "components": {
        "red": {"bs_pc_50": 1.0},
        "green": {"pv_pc_50": 1.0},
        "blue": {"npv_pc_50": 1.0},
    },
    "scale_range": [0.0, 100.0],
    "pq_masks": fc_percentile_pq_mask,
    "legend": {
        "show_legend": True,
        "url": "https://data.dea.ga.gov.au/fractional-cover/FC_legend.png",
    },
}

styles_fc_pc_list = [
    style_fc_rgb,
    style_fc_gv_10,
    style_fc_gv_50,
    style_fc_gv_90,
    style_fc_ngv_10,
    style_fc_ngv_50,
    style_fc_ngv_90,
    style_fc_bs_10,
    style_fc_bs_50,
    style_fc_bs_90,
    style_fc_pc_qa,
]
