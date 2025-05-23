from ows_refactored.ows_reslim_cfg import reslim_for_lccs

bands_landcover = {
    "level3": [],
    "level4": [],
}

style_c3_level3 = {
    "name": "level3",
    "title": "Basic",
    "abstract": "Standardised colouring of Level 3 land cover classes",
    "value_map": {
        "level3": [
            {'title': "", 'abstract': "", 'values': [255], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "Cultivated Terrestrial Vegetation", 'abstract': "", 'values': [111], 'color': '#ACBC2D', 'alpha': 1},
            {'title': "Natural Terrestrial Vegetation", 'abstract': "", 'values': [112], 'color': '#0E7912', 'alpha': 1},
            {'title': "Natural Aquatic Vegetation", 'abstract': "", 'values': [124], 'color': '#1EBF79', 'alpha': 1},
            {'title': "Artificial Surface", 'abstract': "", 'values': [215], 'color': '#DA5C69', 'alpha': 1},
            {'title': "Natural Bare Surface", 'abstract': "", 'values': [216], 'color': '#F3AB69', 'alpha': 1},
            {'title': "Water", 'abstract': "", 'values': [220], 'color': '#4D9FDC', 'alpha': 1}
        ]
    },
    "legend": {"width": 3.0, "height": 1.5},
}


style_c3_level4_lifeform = {
    "name": "lifeform",
    "title": "Lifeform",
    "abstract": "Lifeform (L4): woody / herbaceous",
    "value_map": {
        "level4": [
            {'title': "", 'abstract': "", 'values': [255], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "Woody", 'abstract': "", 'values': [2, 9, 10, 11, 12, 13, 20, 27, 28, 29, 30, 31, 38, 45, 46, 47, 48, 49, 56, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], 'color': '#0E7912', 'alpha': 1},
            {'title': "Herbaceous", 'abstract': "", 'values': [3, 14, 15, 16, 17, 18, 21, 32, 33, 34, 35, 36, 39, 50, 51, 52, 53, 54, 57, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], 'color': '#77A71E', 'alpha': 1}
        ]
    },
}


style_c3_level4_canopyco = {
    "name": "canopyco",
    "title": "Vegetation Cover",
    "abstract": "Vegetation Cover (L4)",
    "value_map": {
        'level4': [
            {'title': "", 'abstract': "", 'values': [255], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "Closed Vegetation", 'abstract': "(> 65 %)", 'values': [4, 9, 14, 22, 27, 32, 40, 45, 50, 58, 63, 64, 65, 78, 79, 80], 'color': '#0E7912', 'alpha': 1},
            {'title': "Open Vegetation", 'abstract': "(40 to 65 %)", 'values': [5, 10, 15, 23, 28, 33, 41, 46, 51, 59, 66, 67, 68, 81, 82, 83], 'color': '#2D8D2F', 'alpha': 1},
            {'title': "Open Vegetation", 'abstract': "(15 to 40 %)", 'values': [6, 11, 16, 24, 29, 34, 42, 47, 52, 60, 69, 70, 71, 84, 85, 86], 'color': '#50A052', 'alpha': 1},
            {'title': "Sparse Vegetation", 'abstract': "(4 to 15 %)", 'values': [7, 12, 17, 25, 30, 35, 43, 48, 53, 61, 72, 73, 74, 87, 88, 89], 'color': '#75B476', 'alpha': 1},
            {'title': "Scattered Vegetation", 'abstract': "(1 to 4 %)", 'values': [8, 13, 18, 26, 31, 36, 44, 49, 54, 62, 75, 76, 77, 90, 91, 92], 'color': '#9AC79C', 'alpha': 1}
        ]
    },
}


style_c3_level4_watersea = {
    "name": "watersea",
    "title": "Water Seasonality",
    "abstract": "Water Seasonality (L4) in vegetated areas",
    "value_map": {
        "level4": [
            {'title': "", 'abstract': "", 'values': [255], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "> 3 months", 'abstract': "(semi) permanent", 'values': [64, 67, 70, 73, 76, 79, 82, 85, 88, 91], 'color': '#19AD6D', 'alpha': 1},
            {'title': "< 3 months", 'abstract': "temporary or seasonal", 'values': [65, 68, 71, 74, 77, 80, 83, 86, 89, 92], 'color': '#B0DAC9', 'alpha': 1}
        ]
    },
}


style_c3_level4_waterper = {
    "name": "waterper",
    "title": "Water Persistence",
    "abstract": "Water persistence in non-vegetated areas",
    "value_map": {
        "level4": [
            {'title': "", 'abstract': "", 'values': [255], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "Perennial", 'abstract': "(> 9 months)", 'values': [101], 'color': '#1b55ba', 'alpha': 1},
            {'title': "Non-perennial", 'abstract': "(7 to 9 months)", 'values': [102], 'color': '#3479C9', 'alpha': 1},
            {'title': "Non-perennial", 'abstract': "(4 to 6 months)", 'values': [103], 'color': '#4F9DD9', 'alpha': 1},
            {'title': "Non-perennial", 'abstract': "(1 to 3 months)", 'values': [104], 'color': '#71CAFD', 'alpha': 1}
        ]
    }
}


style_c3_level4_baregrad = {
    "name": "baregrad",
    "title": "Bare Gradation",
    "abstract": "Level of vegetation in predominantly bare areas",
    "value_map": {
        "level4": [
            {'title': "", 'abstract': "", 'values': [255], 'color': '#FFFFFF', 'alpha': 0},
            {'title': "Sparsely Vegetated", 'abstract': "", 'values': [95], 'color': '#FFE68C', 'alpha': 1},
            {'title': "Very Sparsely Vegetated", 'abstract': "", 'values': [96], 'color': '#FAD26E', 'alpha': 1},
            {'title': "Bare Areas, Unvegetated", 'abstract': "", 'values': [97], 'color': '#F3AB69', 'alpha': 1}
        ]
    },
}


style_c3_level4 = {
    "name": "level4",
    "title": "Detailed",
    "abstract": "Standardised colouring of Level 4 land cover classes",
    "value_map": {
        "level4": [
            {'title': "", 'abstract': "", 'values': [255], 'color': '#FFFFFF', 'alpha': 0},
            {'title': 'Cultivated Terrestrial Vegetated', 'abstract': '', 'values': [1], 'color': '#97bb1a', 'alpha': 1},
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
    "legend": {
        "show_legend": True,
        "url": "https://data.dea.ga.gov.au/derivative/ga_ls_landcover_class_cyear_3/level4-web-legend.png"
    },
}


layers = {
    "title": "DEA Land Cover Collection 3",
    "name": "",
    "layers": [
        {
            "title": "DEA Land Cover Collection 3 Calendar Year (Landsat)",
            "name": "ga_ls_landcover_c3",
            "abstract": """DEA Land Cover Collection 3 Calendar Year (Landsat)

Land cover is the observed physical cover on the Earth's surface including trees, shrubs, grasses, soils, exposed rocks, water bodies, plantations, crops and built structures. A consistent, Australia-wide land cover product helps the understanding of how the different parts of the environment change and inter-relate. Earth observation data recorded over a period of time allows the observation of the state of land cover at specific times and therefore the way that land cover changes.

For more information, see https://knowledge.dea.ga.gov.au/data/product/dea-land-cover-landsat/

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls_landcover_class_cyear_3",
            "bands": bands_landcover,
            "time_resolution": "summary",
            "resource_limits": reslim_for_lccs,
            "dynamic": True,
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "image_processing": {
                "extent_mask_func": [],
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "level4",
                "styles": [style_c3_level3, style_c3_level4],
            },
            "feature_info": {
                "include_custom": {
                    "description": {
                        "function": "ows_refactored.land_and_vegetation.landcover.lc_c3_class_desc.class_labels",
                    }
                }
            }
        },
        {
            "title": "DEA Land Cover Environmental Descriptors",
            "name": "ga_ls_landcover_c3_descriptors",
            "abstract": """DEA Land Cover Environmental Descriptors

Land cover is the observed physical cover on the Earth's surface including trees, shrubs, grasses, soils, exposed rocks, water bodies, plantations, crops and built structures. A consistent, Australia-wide land cover product helps the understanding of how the different parts of the environment change and inter-relate. Earth observation data recorded over a period of time allows the observation of the state of land cover at specific times and therefore the way that land cover changes.

For more information, see https://knowledge.dea.ga.gov.au/data/product/dea-land-cover-landsat/

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls_landcover_class_cyear_3",
            "bands": bands_landcover,
            "time_resolution": "summary",
            "resource_limits": reslim_for_lccs,
            "dynamic": True,
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "image_processing": {
                "extent_mask_func": [],
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "canopyco",
                "styles": [style_c3_level4_canopyco, style_c3_level4_lifeform, style_c3_level4_watersea, style_c3_level4_waterper, style_c3_level4_baregrad],
            },
            "feature_info": {
                "include_custom": {
                    "description": {
                        "function": "ows_refactored.land_and_vegetation.landcover.lc_c3_class_desc.class_labels",
                    }
                }
            }
        }
    ]
}
