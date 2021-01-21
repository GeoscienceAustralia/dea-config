from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35

bands_tmad = {
    "sdev": [],
    "edev": [],
    "bcdev": [],
}
style_tmad_sdev = {
    "name": "log_sdev",
    "title": "sdev",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_log",
        "mapped_bands": True,
        "kwargs": {"band": "sdev", "scale_factor": -100.0, "exponent": 1 / 1000.0},
    },
    "needed_bands": ["sdev"],
    "color_ramp": [
        {"value": 0.0, "color": "#ffffff", "alpha": 0},
        {
            "value": 0.1,
            "color": "#A02406",
        },
        {"value": 0.5, "color": "#FCF24B"},
        {
            "value": 0.9,
            "color": "#0CCD1D",
        },
    ],
    "legend": {
        "begin": "0.1",
        "end": "0.9",
        "decimal_places": 1,
        "tick_labels": {
            "0.1": {"label": "High\ntmad"},
            "0.9": {"label": "Low\ntmad"},
        },
    },
}

style_tmad_edev = {
    "name": "log_edev",
    "title": "edev",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_log",
        "mapped_bands": True,
        "kwargs": {"band": "edev", "scale_factor": -100.0, "exponent": 1 / 1000.0},
    },
    "needed_bands": ["edev"],
    "color_ramp": [
        {"value": 0.0, "color": "#ffffff", "alpha": 0},
        {
            "value": 0.1,
            "color": "#A02406",
        },
        {"value": 0.5, "color": "#FCF24B"},
        {
            "value": 0.9,
            "color": "#0CCD1D",
        },
    ],
    "legend": {
        "begin": "0.1",
        "end": "0.9",
        "tick_labels": {
            "0.1": {"label": "High\ntmad"},
            "0.9": {"label": "Low\ntmad"},
        },
    },
}

style_tmad_bcdev = {
    "name": "log_bcdev",
    "title": "bcdev",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_log",
        "mapped_bands": True,
        "kwargs": {"band": "bcdev", "scale_factor": -100.0, "exponent": 1 / 1000.0},
    },
    "needed_bands": ["bcdev"],
    "color_ramp": [
        {"value": 0.0, "color": "#ffffff", "alpha": 0},
        {
            "value": 0.1,
            "color": "#A02406",
        },
        {"value": 0.5, "color": "#FCF24B"},
        {
            "value": 0.9,
            "color": "#0CCD1D",
        },
    ],
    "legend": {
        "begin": "0.1",
        "end": "0.9",
        "tick_labels": {
            "0.1": {"label": "High\ntmad"},
            "0.9": {"label": "Low\ntmad"},
        },
    },
}

style_tmad_sdev_std = {
    "name": "arcsec_sdev",
    "title": "SMAD",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_arcsec",
        "mapped_bands": True,
        "kwargs": {"band": "sdev", "scale_from": [0.017, 0.15], "scale_to": [0.0, 4.0]},
    },
    "needed_bands": ["sdev"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\ntmad"},
            "4.0": {"label": "High\ntmad"},
        },
    },
}

style_tmad_edev_std = {
    "name": "log_edev",
    "title": "EMAD",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {"band": "edev", "scale_from": [0.025, 0.1], "scale_to": [0.0, 4.0]},
    },
    "needed_bands": ["edev"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\ntmad"},
            "4.0": {"label": "High\ntmad"},
        },
    },
}


style_tmad_bcdev_std = {
    "name": "log_bcdev",
    "title": "BCMAD",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {
            "band": "bcdev",
            "scale_from": [0.025, 0.13],
            "scale_to": [0.0, 4.0],
        },
    },
    "needed_bands": ["bcdev"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\ntmad"},
            "4.0": {"label": "High\ntmad"},
        },
    },
}

style_tmad_rgb_std = {
    "name": "tmad_rgb_std",
    "title": "TMAD multi-band false-colour (standard)",
    "abstract": "Good for cropland and forest",
    "components": {
        "red": {
            "function": "datacube_ows.band_utils.single_band_arcsec",
            "mapped_bands": True,
            "kwargs": {
                "band": "sdev",
                "scale_from": [0.017, 0.15],
            },
        },
        "green": {
            "function": "datacube_ows.band_utils.single_band_offset_log",
            "mapped_bands": True,
            "kwargs": {
                "band": "edev",
                "scale_from": [0.025, 0.1],
            },
        },
        "blue": {
            "function": "datacube_ows.band_utils.single_band_offset_log",
            "mapped_bands": True,
            "kwargs": {
                "band": "bcdev",
                "scale_from": [0.025, 0.13],
            },
        },
    },
    "additional_bands": ["sdev", "bcdev", "edev"],
}

style_tmad_rgb_sens = {
    "inherits": style_tmad_rgb_std,
    "name": "tmad_rgb_sens",
    "title": "TMAD multi-band false-colour (sensitive)",
    "abstract": "Good for arid land and desert",
    "components": {
        "red": {
            "kwargs": {
                "scale_from": [0.0005, 0.11],
            }
        },
        "green": {
            "kwargs": {
                "scale_from": [0.010, 0.09],
            }
        },
        "blue": {
            "kwargs": {
                "scale_from": [0.011, 0.07],
            }
        },
    },
}


style_tmad_sdev = {
    "name": "log_sdev",
    "title": "sdev",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_log",
        "mapped_bands": True,
        "kwargs": {"band": "sdev", "scale_factor": -100.0, "exponent": 1 / 1000.0},
    },
    "needed_bands": ["sdev"],
    "color_ramp": [
        {"value": 0.0, "color": "#ffffff", "alpha": 0},
        {
            "value": 0.1,
            "color": "#A02406",
        },
        {"value": 0.5, "color": "#FCF24B"},
        {
            "value": 0.9,
            "color": "#0CCD1D",
        },
    ],
    "legend": {
        "start": "0.1",
        "end": "0.9",
        "ticks": ["0.1", "0.9"],
        "tick_labels": {
            "0.1": {"label": "High\ntmad"},
            "0.9": {"label": "Low\ntmad"},
        },
    },
}

style_tmad_edev = {
    "name": "log_edev",
    "title": "edev",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_log",
        "mapped_bands": True,
        "kwargs": {"band": "edev", "scale_factor": -100.0, "exponent": 1 / 1000.0},
    },
    "needed_bands": ["edev"],
    "color_ramp": [
        {"value": 0.0, "color": "#ffffff", "alpha": 0},
        {
            "value": 0.1,
            "color": "#A02406",
        },
        {"value": 0.5, "color": "#FCF24B"},
        {
            "value": 0.9,
            "color": "#0CCD1D",
        },
    ],
    "legend": {
        "start": "0.1",
        "end": "0.9",
        "ticks": ["0.1", "0.9"],
        "tick_labels": {
            "0.1": {"label": "High\ntmad"},
            "0.9": {"label": "Low\ntmad"},
        },
    },
}

style_tmad_bcdev = {
    "name": "log_bcdev",
    "title": "bcdev",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_log",
        "mapped_bands": True,
        "kwargs": {"band": "bcdev", "scale_factor": -100.0, "exponent": 1 / 1000.0},
    },
    "needed_bands": ["bcdev"],
    "color_ramp": [
        {"value": 0.0, "color": "#ffffff", "alpha": 0},
        {
            "value": 0.1,
            "color": "#A02406",
        },
        {"value": 0.5, "color": "#FCF24B"},
        {
            "value": 0.9,
            "color": "#0CCD1D",
        },
    ],
    "legend": {
        "start": "0.1",
        "end": "0.9",
        "ticks": ["0.1", "0.9"],
        "tick_labels": {
            "0.1": {"label": "High\ntmad"},
            "0.9": {"label": "Low\ntmad"},
        },
    },
}

layers = {
    "title": "Surface Reflectance Triple Median Absolute Deviation",
    "abstract": "Surface Reflectance Triple Median Absolute Deviation 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)",
    "layers": [
        {
            "title": "Surface Reflectance Triple Median Absolute Deviation (Landsat 8 Annual Surface Reflectance TMAD)",
            "abstract": """
The three layers of the TMAD are calculated by computing the multidimensional distance between each observation in a
time series of multispectral (or higher dimensionality such as hyperspectral) satellite imagery with the
multidimensional median of the time series. The median used for this calculation is the geometric median corresponding
to the time series.  The TMAD is calculated over annual time periods on Earth observations from a single sensor by
default (such as the annual time series of Landsat 8 observations); however, it is applicable to multi-sensor time
series of any length that computing resources can support. For the purposes of the default Digital Earth Australia
product, TMADs are computed per calendar year, per sensor (Landsat 5, Landsat 7 and Landsat 8) from
terrain-illumination-corrected surface reflectance data (Analysis Ready Data), compared to the annual geometric
median of that data.
For more information, see http://pid.geoscience.gov.au/dataset/ga/130482
For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ls8_nbart_tmad_annual",
            # The Datacube name for the associated data product
            "product_name": "ls8_nbart_tmad_annual",
            "bands": bands_tmad,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["sdev", "edev", "bcdev"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "log_sdev",
                "styles": [
                    style_tmad_sdev,
                    style_tmad_edev,
                    style_tmad_bcdev,
                    style_tmad_sdev_std,
                    style_tmad_edev_std,
                    style_tmad_bcdev_std,
                    style_tmad_rgb_std,
                    style_tmad_rgb_sens,
                ],
            },
        },
        {
            "title": "Surface Reflectance Triple Median Absolute Deviation (Landsat 7 Annual Surface Reflectance TMAD)",
            "abstract": """
The three layers of the TMAD are calculated by computing the multidimensional distance between each observation in a
time series of multispectral (or higher dimensionality such as hyperspectral) satellite imagery with the
multidimensional median of the time series. The median used for this calculation is the geometric median corresponding
to the time series.  The TMAD is calculated over annual time periods on Earth observations from a single sensor by
default (such as the annual time series of Landsat 8 observations); however, it is applicable to multi-sensor time
series of any length that computing resources can support. For the purposes of the default Digital Earth Australia
product, TMADs are computed per calendar year, per sensor (Landsat 5, Landsat 7 and Landsat 8) from
terrain-illumination-corrected surface reflectance data (Analysis Ready Data), compared to the annual geometric
median of that data.
For more information, see http://pid.geoscience.gov.au/dataset/ga/130482
For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ls7_nbart_tmad_annual",
            # The Datacube name for the associated data product
            "product_name": "ls7_nbart_tmad_annual",
            "bands": bands_tmad,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["sdev", "edev", "bcdev"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "log_sdev",
                "styles": [
                    style_tmad_sdev,
                    style_tmad_edev,
                    style_tmad_bcdev,
                    style_tmad_sdev_std,
                    style_tmad_edev_std,
                    style_tmad_bcdev_std,
                    style_tmad_rgb_std,
                    style_tmad_rgb_sens,
                ],
            },
        },
        {
            "title": "Surface Reflectance Triple Median Absolute Deviation (Landsat 5 Annual Surface Reflectance TMAD)",
            "abstract": """
The three layers of the TMAD are calculated by computing the multidimensional distance between each observation in a
time series of multispectral (or higher dimensionality such as hyperspectral) satellite imagery with the
multidimensional median of the time series. The median used for this calculation is the geometric median corresponding
to the time series.  The TMAD is calculated over annual time periods on Earth observations from a single sensor by
default (such as the annual time series of Landsat 8 observations); however, it is applicable to multi-sensor time
series of any length that computing resources can support. For the purposes of the default Digital Earth Australia
product, TMADs are computed per calendar year, per sensor (Landsat 5, Landsat 7 and Landsat 8) from
terrain-illumination-corrected surface reflectance data (Analysis Ready Data), compared to the annual geometric
median of that data.
For more information, see http://pid.geoscience.gov.au/dataset/ga/130482
For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ls5_nbart_tmad_annual",
            # The Datacube name for the associated data product
            "product_name": "ls5_nbart_tmad_annual",
            "bands": bands_tmad,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "default_bands": ["sdev", "edev", "bcdev"],
                "native_resolution": [25, -25],
            },
            "styling": {
                "default_style": "log_sdev",
                "styles": [
                    style_tmad_sdev,
                    style_tmad_edev,
                    style_tmad_bcdev,
                    style_tmad_sdev_std,
                    style_tmad_edev_std,
                    style_tmad_bcdev_std,
                    style_tmad_rgb_std,
                    style_tmad_rgb_sens,
                ],
            },
        },
    ],
}
