from ows_refactored.baseline_satellite_data.landsat_annual.style_ls_cfg import (
    style_ls_irg, style_ls_ndvi, style_ls_pure_blue, style_ls_pure_green,
    style_ls_pure_red, style_ls_simple_rgb, style_sentinel_pure_nir,
    style_sentinel_pure_swir1, style_sentinel_pure_swir2)
from ows_refactored.ows_legend_cfg import legend_idx_0_1_5ticks

style_barest_earth_simple_rgb = style_ls_simple_rgb
style_barest_earth_pure_blue = style_ls_pure_blue
style_barest_earth_pure_green = style_ls_pure_green
style_barest_earth_pure_red = style_ls_pure_red


style_barest_earth_pure_red_edge_1 = {
    "name": "red_edge_1",
    "title": "Vegetation Red Edge 1 - 705",
    "abstract": "Vegetation Red Edge, centered on 705nm",
    "components": {"red": {"red_edge_1": 1.0}, "green": {"red_edge_1": 1.0}, "blue": {"red_edge_1": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_barest_earth_pure_red_edge_2 = {
    "name": "red_edge_2",
    "title": "Vegetation Red Edge 2 - 740",
    "abstract": "Vegetation Red Edge, centered on 740nm",
    "components": {"red": {"red_edge_2": 1.0}, "green": {"red_edge_2": 1.0}, "blue": {"red_edge_2": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_barest_earth_pure_red_edge_3 = {
    "name": "red_edge_3",
    "title": "Vegetation Red Edge 3 - 783",
    "abstract": "Vegetation Red Edge, centered on 783nm",
    "components": {"red": {"red_edge_3": 1.0}, "green": {"red_edge_3": 1.0}, "blue": {"red_edge_3": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_barest_earth_pure_nir_1 = {
    "name": "nir_1",
    "title": "Near Infrared (NIR) - 840",
    "abstract": "Near infra-red band, centered on 840nm",
    "components": {"red": {"nir_1": 1.0}, "green": {"nir_1": 1.0}, "blue": {"nir_1": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_barest_earth_pure_nir_2 = {
    "name": "nir_2",
    "title": "Near Infrared (NIR) - 840",
    "abstract": "Near infra-red band, centered on 840nm",
    "components": {"red": {"nir_2": 1.0}, "green": {"nir_2": 1.0}, "blue": {"nir_2": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_barest_earth_pure_swir_2 = {
    "name": "swir_2",
    "title": "Shortwave Infrared (SWIR) - 2220",
    "abstract": "Short wave infra-red band 2, centered on 2220nm",
    "components": {
        "red": {"swir_2": 1.0},
        "green": {"swir_2": 1.0},
        "blue": {"swir_2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_barest_earth_pure_swir_3 = {
    "name": "swir_3",
    "title": "Shortwave Infrared (SWIR) - 2220",
    "abstract": "Short wave infra-red band 3, centered on 2220nm",
    "components": {
        "red": {"swir_3": 1.0},
        "green": {"swir_3": 1.0},
        "blue": {"swir_3": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_nd_ferric_iron = {
    "name": "nd_ferric_iron",
    "title": "Ferric Iron",
    "abstract": "Normalised Difference Ferric Iron Index - a derived index that correlates well with the existence of Ferric Iron Content",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "red", "band2": "blue"},
    },
    "needed_bands": ["red", "blue"],
    "color_ramp": [
        {"value": -0.1, "color": "#3B97C3", "alpha": 0.0},
        {"value": 0.0, "color": "#6EA9B0", "alpha": 1.0},
        {"value": 0.1, "color": "#83B3A9"},
        {"value": 0.2, "color": "#9FC29D"},
        {"value": 0.3, "color": "#F3F56C"},
        {"value": 0.4, "color": "#FCDE56"},
        {"value": 0.5, "color": "#FCC54C"},
        {"value": 0.6, "color": "#F77F2F"},
        {"value": 0.7, "color": "#F55F25"},
        {"value": 0.8, "color": "#F25622"},
        {"value": 0.9, "color": "#EB1E15"},
        {"value": 1.0, "color": "#E81515"},
    ],
    "legend": legend_idx_0_1_5ticks,
}

style_nd_soil = {
    "name": "nd_soil",
    "title": "Normalised Difference Soil Index",
    "abstract": "Normalised Difference Soil Index - a derived index that correlates well with the existence of bare Soil/Rock",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "swir1", "band2": "nir"},
    },
    "needed_bands": ["nir", "swir1"],
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

style_nd_clay_mica = {
    "name": "nd_clay_mica",
    "title": "Clay and Mica Minerals",
    "abstract": "Normalised Difference Clay and Mica Minerals Index - a derived index that correlates well with the existence of hydroxyl bearing minerals (clay and mica minerals)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "swir1", "band2": "swir2"},
    },
    "needed_bands": ["swir1", "swir2"],
    "color_ramp": [
        {"value": -0.1, "color": "#ffffb2", "alpha": 0.0},
        {"value": 0.0, "color": "#ffef97", "alpha": 1.0},
        {"value": 0.1, "color": "#ffe07d"},
        {"value": 0.2, "color": "#fecc5c"},
        {"value": 0.3, "color": "#feb450"},
        {"value": 0.4, "color": "#fd8d3c"},
        {"value": 0.5, "color": "#f86b30"},
        {"value": 0.6, "color": "#f44f26"},
        {"value": 0.7, "color": "#f03b20"},
        {"value": 0.8, "color": "#de2522"},
        {"value": 0.9, "color": "#cc1024"},
        {"value": 1.0, "color": "#bd0026"},
    ],
    "legend": legend_idx_0_1_5ticks,
}

styles_barest_earth_mosaic_list = [
    style_ls_simple_rgb,
    style_ls_irg,
    style_ls_ndvi,
    style_ls_pure_blue,
    style_ls_pure_green,
    style_ls_pure_red,
    style_sentinel_pure_nir,
    style_sentinel_pure_swir1,
    style_sentinel_pure_swir2,
]

styles_barest_earth_list = styles_barest_earth_mosaic_list + [
    style_nd_ferric_iron,
    style_nd_soil,
    style_nd_clay_mica,
]

styles_s2_barest_earth_list = [
    style_barest_earth_simple_rgb,
    style_ls_irg,
    style_ls_ndvi,
    style_barest_earth_pure_blue,
    style_barest_earth_pure_green,
    style_barest_earth_pure_red,
    style_barest_earth_pure_red_edge_1,
    style_barest_earth_pure_red_edge_2,
    style_barest_earth_pure_red_edge_3,
    style_barest_earth_pure_nir_1,
    style_barest_earth_pure_nir_2,
    style_barest_earth_pure_swir_2,
    style_barest_earth_pure_swir_3,
]
