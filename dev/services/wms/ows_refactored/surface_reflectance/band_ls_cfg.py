bands_ls = {
    "red": ["red"],
    "green": ["green"],
    "blue": ["blue"],
    "nir": ["nir", "near_infrared"],
    "swir1": ["swir1", "shortwave_infrared_1", "near_shortwave_infrared"],
    "swir2": ["swir2", "shortwave_infrared_2", "far_shortwave_infrared"],
}

bands_ls8 = bands_ls.copy()
bands_ls8.update(
    {
        "coastal_aerosol": ["coastal_aerosol"],
    }
)
