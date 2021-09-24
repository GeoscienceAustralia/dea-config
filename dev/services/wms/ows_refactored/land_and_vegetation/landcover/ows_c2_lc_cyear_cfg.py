from ows_refactored.land_and_vegetation.landcover.lc_class_desc import \
    class_description
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

bands_landcover = {
    "level3": [],
    "level4": [],
}

bands_eds = {
    "lifeform_veg_cat_l4a": ["lifeform"],
    "canopyco_veg_cat_l4d": ["canopy_cover"],
    "watersea_veg_cat_l4a_au": ["water_seasonality"],
    "waterper_wat_cat_l4d_au": ["water_persistence"],
    "baregrad_phy_cat_l4d_au": ["bare_gradation"],
}

style_c2_level3 = {
    "name": "level3",
    "title": "Basic - 6 classes",
    "abstract": "Standardised colouring of Level 3 land cover classes",
    "value_map": {
        "level3": [
            {'title': "", 'abstract': "", 'values': [0], 'color': '#FFFFFF', 'alpha': 0, },
            {'title': "Cultivated Terrestrial Vegetation", 'abstract': "", 'values': [111], 'color': '#ACBC2D', 'alpha': 1},
            {'title': "Natural Terrestrial Vegetation", 'abstract': "", 'values': [112], 'color': '#0E7912', 'alpha': 1},
            # {'title': "Cultivated Aquatic Vegetation", 'abstract': "", 'values': [123], 'color': '#56ECE7', 'alpha': 1},
            {'title': "Natural Aquatic Vegetation", 'abstract': "", 'values': [124], 'color': '#1EBF79', 'alpha': 1},
            {'title': "Artificial Surface", 'abstract': "", 'values': [215], 'color': '#DA5C69', 'alpha': 1},
            {'title': "Natural Bare Surface", 'abstract': "", 'values': [216], 'color': '#F3AB69', 'alpha': 1},
            {'title': "Water", 'abstract': "", 'values': [220], 'color': '#4D9FDC', 'alpha': 1}
        ]
    },
    # "pq_masks": [
    #     {
    #         "band": "land",
    #         "invert": True,
    #         "enum": 0,
    #     }
    # ],
    "legend": {"width": 3.0, "height": 1.5},
}


style_c2_level4_lifeform = {
    "name": "lifeform",
    "title": "Lifeform",
    "abstract": "Lifeform (L4): woody / herbaceous",
    "value_map": {
        "lifeform_veg_cat_l4a": [
            {'title': "", 'abstract': "", 'values': [0], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "Woody", 'abstract': "", 'values': [1], 'color': '#0E7912', 'alpha': 1},
            {'title': "Herbaceous", 'abstract': "", 'values': [2], 'color': '#77A71E', 'alpha': 1}
        ]
    },
    # "pq_masks": [
    #     {
    #         "band": "land",
    #         "invert": True,
    #         "enum": 0,
    #     }
    # ],
}


style_c2_level4_canopyco = {
    "name": "canopyco",
    "title": "Canopy Cover",
    "abstract": "Canopy Cover (L4)",
    "value_map": {
        'canopyco_veg_cat_l4d': [
            {'title': "", 'abstract': "", 'values': [0], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "Closed Vegetation", 'abstract': "(> 65 %)", 'values': [10], 'color': '#0E7912', 'alpha': 1},
            {'title': "Open Vegetation", 'abstract': "(40 to 65 %)", 'values': [12], 'color': '#2D8D2F', 'alpha': 1},
            {'title': "Open Vegetation", 'abstract': "(15 to 40 %)", 'values': [13], 'color': '#50A052', 'alpha': 1},
            {'title': "Sparse Vegetation", 'abstract': "(4 to 15 %)", 'values': [15], 'color': '#75B476', 'alpha': 1},
            {'title': "Scattered Vegetation", 'abstract': "(1 to 4 %)", 'values': [16], 'color': '#9AC79C', 'alpha': 1}
        ]
    },
    # "pq_masks": [
    #     {
    #         "band": "land",
    #         "invert": True,
    #         "enum": 0,
    #     }
    # ],
}


style_c2_level4_watersea = {
    "name": "watersea",
    "title": "Water Seasonality",
    "abstract": "Water Seasonality (L4) in vegetated areas",
    "value_map": {
        "watersea_veg_cat_l4a_au": [
            {'title': "", 'abstract': "", 'values': [0], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "> 3 months", 'abstract': "(semi) permanent", 'values': [1], 'color': '#19AD6D', 'alpha': 1},
            {'title': "< 3 months", 'abstract': "temporary or seasonal", 'values': [2], 'color': '#B0DAC9', 'alpha': 1}
        ]
    },
}


style_c2_level4_waterper = {
    "name": "waterper",
    "title": "Water Persistence",
    "abstract": "Water persistence in non-vegetated areas",
    "value_map": {
        "waterper_wat_cat_l4d_au": [
            {'title': "", 'abstract': "", 'values': [0], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "Perennial", 'abstract': "(> 9 months)", 'values': [1], 'color': '#1b55ba', 'alpha': 1},
            {'title': "Non-perennial", 'abstract': "(7 to 9 months)", 'values': [7], 'color': '#3479C9', 'alpha': 1},
            {'title': "Non-perennial", 'abstract': "(4 to 6 months)", 'values': [8], 'color': '#4F9DD9', 'alpha': 1},
            {'title': "Non-perennial", 'abstract': "(1 to 3 months)", 'values': [9], 'color': '#71CAFD', 'alpha': 1}
        ]
    }
}


style_c2_level4_baregrad = {
    "name": "baregrad",
    "title": "Bare Gradation",
    "abstract": "Level of vegetation in predominantly bare areas",
    "value_map": {
        "baregrad_phy_cat_l4d_au": [
            {'title': "", 'abstract': "", 'values': [0], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "Sparsely Vegetated", 'abstract': "", 'values': [10], 'color': '#FFE68C', 'alpha': 1},
            {'title': "Very Sparsely Vegetated", 'abstract': "", 'values': [12], 'color': '#FAD26E', 'alpha': 1},
            {'title': "Bare Areas, Unvegetated", 'abstract': "", 'values': [15], 'color': '#F3AB69', 'alpha': 1}
        ]
    },
    # "pq_masks": [
    #     {
    #         "band": "land",
    #         "invert": True,
    #         "enum": 0,
    #     }
    # ],
}


style_c2_level4 = {
    "name": "level4",
    "title": "Detailed - 80 classes",
    "abstract": "Standardised colouring of Level 4 land cover classes",
    "value_map": {
        "level4": [
            {'title': '', 'abstract': '', 'values': [1], 'color': '#97bb1a', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Woody', 'abstract': '', 'values': [2], 'color': '#97bb1a', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Herbaceous', 'abstract': '', 'values': [3], 'color': '#d1e033', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Closed (> 65 %)', 'abstract': '', 'values': [4], 'color': '#c5a847', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Open (40 to 65 %)', 'abstract': '', 'values': [5], 'color': '#cdb54b', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Open (15 to 40 %)', 'abstract': '', 'values': [6], 'color': '#d5c14f', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Sparse (4 to 15 %)', 'abstract': '', 'values': [7], 'color': '#e4d26c', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Scattered (1 to 4 %)', 'abstract': '', 'values': [8], 'color': '#f2e38a', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Woody Closed (> 65 %)', 'abstract': '', 'values': [9], 'color': '#c5a847', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Woody Open (40 to 65 %)', 'abstract': '', 'values': [10], 'color': '#cdb54b', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Woody Open (15 to 40 %)', 'abstract': '', 'values': [11], 'color': '#d5c14f', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Woody Sparse (4 to 15 %)', 'abstract': '', 'values': [12], 'color': '#e4d26c', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Woody Scattered (1 to 4 %)', 'abstract': '', 'values': [13], 'color': '#f2e38a', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Herbaceous Closed (> 65 %)', 'abstract': '', 'values': [14], 'color': '#e4e034', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Herbaceous Open (40 to 65 %)', 'abstract': '', 'values': [15], 'color': '#ebe854', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Herbaceous Open (15 to 40 %)', 'abstract': '', 'values': [16], 'color': '#f2f07f', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Herbaceous Sparse (4 to 15 %)', 'abstract': '', 'values': [17], 'color': '#f9f7ae', 'alpha': 1},
            {'title': 'Cultivated Terrestrial Vegetated: Herbaceous Scattered (1 to 4 %)', 'abstract': '', 'values': [18], 'color': '#fffede', 'alpha': 1},
            {'title': '', 'abstract': '', 'values': [19], 'color': '#0e7912', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Woody', 'abstract': '', 'values': [20], 'color': '#1ab157', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Herbaceous', 'abstract': '', 'values': [21], 'color': '#5eb31f', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Closed (> 65 %)', 'abstract': '', 'values': [22], 'color': '#0e7912', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Open (40 to 65 %)', 'abstract': '', 'values': [23], 'color': '#2d8d2f', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Open (15 to 40 %)', 'abstract': '', 'values': [24], 'color': '#50a052', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Sparse (4 to 15 %)', 'abstract': '', 'values': [25], 'color': '#75b476', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Scattered (1 to 4 %)', 'abstract': '', 'values': [26], 'color': '#9ac79c', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Woody Closed (> 65 %)', 'abstract': '', 'values': [27], 'color': '#0e7912', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Woody Open (40 to 65 %)', 'abstract': '', 'values': [28], 'color': '#2d8d2f', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Woody Open (15 to 40 %)', 'abstract': '', 'values': [29], 'color': '#50a052', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Woody Sparse (4 to 15 %)', 'abstract': '', 'values': [30], 'color': '#75b476', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Woody Scattered (1 to 4 %)', 'abstract': '', 'values': [31], 'color': '#9ac79c', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Herbaceous Closed (> 65 %)', 'abstract': '', 'values': [32], 'color': '#77a71e', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Herbaceous Open (40 to 65 %)', 'abstract': '', 'values': [33], 'color': '#88b633', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Herbaceous Open (15 to 40 %)', 'abstract': '', 'values': [34], 'color': '#99c450', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Herbaceous Sparse (4 to 15 %)', 'abstract': '', 'values': [35], 'color': '#aad471', 'alpha': 1},
            {'title': 'Natural Terrestrial Vegetated: Herbaceous Scattered (1 to 4 %)', 'abstract': '', 'values': [36], 'color': '#bae292', 'alpha': 1},
            {'title': '', 'abstract': '', 'values': [37], 'color': '#56ece7', 'alpha': 1},
            # {'title': 'Cultivated Aquatic Vegetated: Woody', 'abstract': '', 'values': [38], 'color': '#3daa8c', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Herbaceous', 'abstract': '', 'values': [39], 'color': '#52e7ac', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Closed (> 65 %)', 'abstract': '', 'values': [40], 'color': '#2bd2cb', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Open (40 to 65 %)', 'abstract': '', 'values': [41], 'color': '#49ded8', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Open (15 to 40 %)', 'abstract': '', 'values': [42], 'color': '#6ee9e4', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Sparse (4 to 15 %)', 'abstract': '', 'values': [43], 'color': '#95f4f0', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Scattered (1 to 4 %)', 'abstract': '', 'values': [44], 'color': '#bbfffc', 'alpha': 1},
            # {'title': 'Cultivated Aquatic Vegetated: Woody Closed (> 65 %)', 'abstract': '', 'values': [45], 'color': '#2bd2cb', 'alpha': 1},
            # {'title': 'Cultivated Aquatic Vegetated: Woody Open (40 to 65 %)', 'abstract': '', 'values': [46], 'color': '#49ded8', 'alpha': 1},
            # {'title': 'Cultivated Aquatic Vegetated: Woody Open (15 to 40 %)', 'abstract': '', 'values': [47], 'color': '#6ee9e4', 'alpha': 1},
            # {'title': 'Cultivated Aquatic Vegetated: Woody Sparse (4 to 15 %)', 'abstract': '', 'values': [48], 'color': '#95f4f0', 'alpha': 1},
            # {'title': 'Cultivated Aquatic Vegetated: Woody Scattered (1 to 4 %)', 'abstract': '', 'values': [49], 'color': '#bbfffc', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Herbaceous Closed (> 65 %)', 'abstract': '', 'values': [50], 'color': '#52e7c4', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Herbaceous Open (40 to 65 %)', 'abstract': '', 'values': [51], 'color': '#71edd0', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Herbaceous Open (15 to 40 %)', 'abstract': '', 'values': [52], 'color': '#90f3dc', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Herbaceous Sparse (4 to 15 %)', 'abstract': '', 'values': [53], 'color': '#aff9e8', 'alpha': 1},
            {'title': 'Cultivated Aquatic Vegetated: Herbaceous Scattered (1 to 4 %)', 'abstract': '', 'values': [54], 'color': '#cffff4', 'alpha': 1},
            {'title': '', 'abstract': '', 'values': [55], 'color': '#1ebf79', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody', 'abstract': '', 'values': [56], 'color': '#128e94', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous', 'abstract': '', 'values': [57], 'color': '#70ea86', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Closed (> 65 %)', 'abstract': '', 'values': [58], 'color': '#19ad6d', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Open (40 to 65 %)', 'abstract': '', 'values': [59], 'color': '#35b884', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Open (15 to 40 %)', 'abstract': '', 'values': [60], 'color': '#5dc39b', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Sparse (4 to 15 %)', 'abstract': '', 'values': [61], 'color': '#87ceb2', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Scattered (1 to 4 %)', 'abstract': '', 'values': [62], 'color': '#b0dac9', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Closed (> 65 %)', 'abstract': '', 'values': [63], 'color': '#19ad6d', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Closed (> 65 %) Water > 3 months (semi-) permenant', 'abstract': '', 'values': [64], 'color': '#19ad6d', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Closed (> 65 %) Water < 3 months (temporary or seasonal)', 'abstract': '', 'values': [65], 'color': '#19ad6d', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Open (40 to 65 %)', 'abstract': '', 'values': [66], 'color': '#35b884', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Open (40 to 65 %) Water > 3 months (semi-) permenant', 'abstract': '', 'values': [67], 'color': '#35b884', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Open (40 to 65 %) Water < 3 months (temporary or seasonal)', 'abstract': '', 'values': [68], 'color': '#35b884', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Open (15 to 40 %)', 'abstract': '', 'values': [69], 'color': '#5dc39b', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Open (15 to 40 %) Water > 3 months (semi-) permenant', 'abstract': '', 'values': [70], 'color': '#5dc39b', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Open (15 to 40 %) Water < 3 months (temporary or seasonal)', 'abstract': '', 'values': [71], 'color': '#5dc39b', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Sparse (4 to 15 %)', 'abstract': '', 'values': [72], 'color': '#87ceb2', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Sparse (4 to 15 %) Water > 3 months (semi-) permenant', 'abstract': '', 'values': [73], 'color': '#87ceb2', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Sparse (4 to 15 %) Water < 3 months (temporary or seasonal)', 'abstract': '', 'values': [74], 'color': '#87ceb2', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Scattered (1 to 4 %)', 'abstract': '', 'values': [75], 'color': '#b0dac9', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Scattered (1 to 4 %) Water > 3 months (semi-) permenant', 'abstract': '', 'values': [76], 'color': '#b0dac9', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Woody Scattered (1 to 4 %) Water < 3 months (temporary or seasonal)', 'abstract': '', 'values': [77], 'color': '#b0dac9', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Closed (> 65 %)', 'abstract': '', 'values': [78], 'color': '#27cc8b', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Closed (> 65 %) Water > 3 months (semi-) permenant', 'abstract': '', 'values': [79], 'color': '#27cc8b', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Closed (> 65 %) Water < 3 months (temporary or seasonal)', 'abstract': '', 'values': [80], 'color': '#27cc8b', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Open (40 to 65 %)', 'abstract': '', 'values': [81], 'color': '#42d89f', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Open (40 to 65 %) Water > 3 months (semi-) permenant', 'abstract': '', 'values': [82], 'color': '#42d89f', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Open (40 to 65 %) Water < 3 months (temporary or seasonal)', 'abstract': '', 'values': [83], 'color': '#42d89f', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Open (15 to 40 %)', 'abstract': '', 'values': [84], 'color': '#63e3b4', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Open (15 to 40 %) Water > 3 months (semi-) permenant', 'abstract': '', 'values': [85], 'color': '#63e3b4', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Open (15 to 40 %) Water < 3 months (temporary or seasonal)', 'abstract': '', 'values': [86], 'color': '#63e3b4', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Sparse (4 to 15 %)', 'abstract': '', 'values': [87], 'color': '#87efc9', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Sparse (4 to 15 %) Water > 3 months (semi-) permenant', 'abstract': '', 'values': [88], 'color': '#87efc9', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Sparse (4 to 15 %) Water < 3 months (temporary or seasonal)', 'abstract': '', 'values': [89], 'color': '#87efc9', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Scattered (1 to 4 %)', 'abstract': '', 'values': [90], 'color': '#abfadd', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Scattered (1 to 4 %) Water > 3 months (semi-) permenant', 'abstract': '', 'values': [91], 'color': '#abfadd', 'alpha': 1},
            {'title': 'Natural Aquatic Vegetated: Herbaceous Scattered (1 to 4 %) Water < 3 months (temporary or seasonal)', 'abstract': '', 'values': [92], 'color': '#abfadd', 'alpha': 1},
            {'title': 'Artificial Surface', 'abstract': '', 'values': [93], 'color': '#da5c69', 'alpha': 1},
            {'title': '', 'abstract': '', 'values': [94], 'color': '#f3ab69', 'alpha': 1},
            {'title': 'Natural Surface: Sparsely vegetated', 'abstract': '', 'values': [95], 'color': '#ffe68c', 'alpha': 1},
            {'title': 'Natural Surface: Very sparsely vegetated', 'abstract': '', 'values': [96], 'color': '#fad26e', 'alpha': 1},
            {'title': 'Natural Surface: Bare areas, unvegetated', 'abstract': '', 'values': [97], 'color': '#f3ab69', 'alpha': 1},
            {'title': 'Water', 'abstract': '', 'values': [98], 'color': '#4d9fdc', 'alpha': 1},
            {'title': '', 'abstract': '', 'values': [99], 'color': '#4d9fdc', 'alpha': 1},
            {'title': 'Water: Tidal area', 'abstract': '', 'values': [100], 'color': '#bbdce9', 'alpha': 1},
            {'title': 'Water: Perennial (> 9 months)', 'abstract': '', 'values': [101], 'color': '#1b55ba', 'alpha': 1},
            {'title': 'Water: Non-perennial (7 to 9 months)', 'abstract': '', 'values': [102], 'color': '#3479c9', 'alpha': 1},
            {'title': 'Water: Non-perennial (4 to 6 months)', 'abstract': '', 'values': [103], 'color': '#4f9dd9', 'alpha': 1},
            {'title': 'Water: Non-perennial (1 to 3 months)', 'abstract': '', 'values': [104], 'color': '#85cafd', 'alpha': 1},
            # {'title': 'Water: (Snow)', 'abstract': '', 'values': [105], 'color': '#fafafa', 'alpha': 1},
        ]
    },
    # "pq_masks": [
    #     {
    #         "band": "land",
    #         "invert": True,
    #         "enum": 0,
    #     }
    # ],
    "legend": {
        "show_legend": True,
        "url": "https://dea-public-data-dev.s3.ap-southeast-2.amazonaws.com/lccs/level4-web-legend.png"
    },
}


layers = {
    "title": "DEA Land Cover (Landsat)",
    "name": "",
    "layers": [
        {
            "title": "DEA Land Cover (Landsat)",
            "name": "ga_ls_landcover",
            "abstract": """
            Land cover is the observed physical cover on the Earth's surface including trees, shrubs, grasses, soils, exposed rocks, water bodies, plantations, crops and built structures. A consistent, Australia-wide land cover product helps the understanding of how the different parts of the environment change and inter-relate. Earth observation data recorded over a period of time allows the observation of the state of land cover at specific times and therefore the way that land cover changes.
        """,
            "product_name": "ga_ls_landcover_class_cyear_2",
            "bands": bands_landcover,
            "time_resolution": "year",
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "dynamic": True,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val2",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            # "flags": [
            #     {
            #         "band": "land",
            #         "product": "geodata_coast_100k",
            #         "ignore_time": True,
            #         "ignore_info_flags": [],
            #     }
            # ],
            "wcs": {
                "default_bands": ["level4"],
            },
            "styling": {
                "default_style": "level4",
                "styles": [style_c2_level4, style_c2_level3],
            },
        },
        {
            "title": "DEA Land Cover Environmental Descriptors",
            "name": "ga_ls_landcover_descriptors",
            "abstract": """
            Land cover is the observed physical cover on the Earth's surface including trees, shrubs, grasses, soils, exposed rocks, water bodies, plantations, crops and built structures. A consistent, Australia-wide land cover product helps the understanding of how the different parts of the environment change and inter-relate. Earth observation data recorded over a period of time allows the observation of the state of land cover at specific times and therefore the way that land cover changes.
        """,
            "product_name": "ga_ls_landcover_class_cyear_2",
            "bands": bands_eds,
            "time_resolution": "year",
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "dynamic": True,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val2",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            # "flags": [
            #     {
            #         "band": "land",
            #         "product": "geodata_coast_100k",
            #         "ignore_time": True,
            #         "ignore_info_flags": [],
            #     }
            # ],
            "wcs": {
                "default_bands": ["canopyco_veg_cat_l4d"],
            },
            "styling": {
                "default_style": "canopyco",
                "styles": [style_c2_level4_canopyco, style_c2_level4_lifeform, style_c2_level4_watersea, style_c2_level4_waterper, style_c2_level4_baregrad],
            },
            "feature_info": {
                "include_custom": {
                    "description": {
                        "function": class_description,
                    }
                }
            }
        }
    ]
}
