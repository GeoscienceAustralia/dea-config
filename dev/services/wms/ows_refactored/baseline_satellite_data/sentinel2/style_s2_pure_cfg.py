style_s2_pure_aerosol = {
    "name": "aerosol",
    "title": "Narrow Blue - 440",
    "abstract": "Coastal Aerosol or Narrow Blue band, approximately 435nm to 450nm",
    "components": {
        "red": {"coastal_aerosol": 1.0},
        "green": {"coastal_aerosol": 1.0},
        "blue": {"coastal_aerosol": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_blue = {
    "name": "blue",
    "title": "Blue - 490",
    "abstract": "Blue band, approximately 453nm to 511nm",
    "components": {"red": {"blue": 1.0}, "green": {"blue": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_s2_pure_green = {
    "name": "green",
    "title": "Green - 560",
    "abstract": "Green band, approximately 534nm to 588nm",
    "components": {
        "red": {"green": 1.0},
        "green": {"green": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_red = {
    "name": "red",
    "title": "Red - 670",
    "abstract": "Red band, roughly 637nm to 672nm",
    "components": {"red": {"red": 1.0}, "green": {"red": 1.0}, "blue": {"red": 1.0}},
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_redge_1 = {
    "name": "red_edge_1",
    "title": "Vegetation Red Edge - 710",
    "abstract": "Near infra-red band, centred on 710nm",
    "components": {
        "red": {"red_edge_1": 1.0},
        "green": {"red_edge_1": 1.0},
        "blue": {"red_edge_1": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_redge_2 = {
    "name": "red_edge_2",
    "title": "Vegetation Red Edge - 740",
    "abstract": "Near infra-red band, centred on 740nm",
    "components": {
        "red": {"red_edge_2": 1.0},
        "green": {"red_edge_2": 1.0},
        "blue": {"red_edge_2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_redge_3 = {
    "name": "red_edge_3",
    "title": "Vegetation Red Edge - 780",
    "abstract": "Near infra-red band, centred on 780nm",
    "components": {
        "red": {"red_edge_3": 1.0},
        "green": {"red_edge_3": 1.0},
        "blue": {"red_edge_3": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_nir = {
    "name": "nir",
    "title": "Near Infrared (NIR) - 840",
    "abstract": "Near infra-red band, roughly 853nm to 876nm",
    "components": {"red": {"nir": 1.0}, "green": {"nir": 1.0}, "blue": {"nir": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_s2_pure_narrow_nir = {
    "name": "narrow_nir",
    "title": "Narrow Near Infrared - 870",
    "abstract": "Near infra-red band, centred on 865nm",
    "components": {"red": {"nir": 1.0}, "green": {"nir": 1.0}, "blue": {"nir": 1.0}},
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_swir1 = {
    "name": "swir1",
    "title": "Shortwave Infrared (SWIR) - 1610",
    "abstract": "Short wave infra-red band 1, roughly 1575nm to 1647nm",
    "components": {
        "red": {"swir_2": 1.0},
        "green": {"swir_2": 1.0},
        "blue": {"swir_2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_swir2 = {
    "name": "swir2",
    "title": "Shortwave Infrared (SWIR) - 2190",
    "abstract": "Short wave infra-red band 2, roughly 2117nm to 2285nm",
    "components": {
        "red": {"swir_3": 1.0},
        "green": {"swir_3": 1.0},
        "blue": {"swir_3": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}
