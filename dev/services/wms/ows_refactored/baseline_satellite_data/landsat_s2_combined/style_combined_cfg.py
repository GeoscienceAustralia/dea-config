style_combined_true_colour = {
    "name": "true_colour",
    "title": "True Colour",
    "abstract": "True-colour image, using the red, green and blue bands",
    "components": {
        "red": {"nbart_red": 1.0},
        "green": {"nbart_green": 1.0},
        "blue": {"nbart_blue": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_combined_pure_blue = {
    "name": "blue",
    "title": "Blue - 480",
    "abstract": "Blue band, centered on 480nm",
    "components": {
        "red": {"nbart_blue": 1.0},
        "green": {"nbart_blue": 1.0},
        "blue": {"nbart_blue": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_combined_pure_green = {
    "name": "green",
    "title": "Green - 560",
    "abstract": "Green band, centered on 560nm",
    "components": {
        "red": {"nbart_green": 1.0},
        "green": {"nbart_green": 1.0},
        "blue": {"nbart_green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_combined_pure_red = {
    "name": "red",
    "title": "Red - 660",
    "abstract": "Red band, centered on 660nm",
    "components": {
        "red": {"nbart_red": 1.0},
        "green": {"nbart_red": 1.0},
        "blue": {"nbart_red": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


# Styles grouping
styles_combined = [
    style_combined_true_colour,
    style_combined_pure_blue,
    style_combined_pure_green,
    style_combined_pure_red,
]


