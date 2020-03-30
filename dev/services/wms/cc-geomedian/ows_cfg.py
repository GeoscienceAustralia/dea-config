# Reslim
reslim_cambodia = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 25.0,
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    }
}

# bands
bands_ls = {
    "red": [],
    "green": [],
    "blue": [],
    "nir": ["near_infrared"],
    "swir1": ["shortwave_infrared_1", "near_shortwave_infrared"],
    "swir2": ["shortwave_infrared_2", "far_shortwave_infrared"],
}

bands_wofs = {
    "wofs": [],
}
# Style
style_ls_simple_rgb = {
    "name": "simple_rgb",
    "title": "Simple RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {
            "red": {
                "red": 1.0
            },
        "green": {
                "green": 1.0
            },
        "blue": {
                "blue": 1.0
            }
    },
    "scale_range": [0.0, 3000.0]
}

style_infra_red = {
    "name": "infra_red",
    "title": "False colour multi-band infra-red",
    "abstract": "Simple false-colour image, using the near and short-wave infra-red bands",
    "components": {
        "red": {
            "swir1": 1.0
        },
        "green": {
            "swir2": 1.0
        },
        "blue": {
            "nir": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_infra_green = {
    "name": "infrared_green",
    "title": "False colour SWIR, NIR and green",
    "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {
            "swir1": 1.0
        },
        "green": {
            "nir": 1.0
        },
        "blue": {
            "green": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_pure_blue = {
    "name": "blue",
    "title": "Spectral band 2 - Blue",
    "abstract": "Blue band, approximately 453nm to 511nm",
    "components": {
        "red": {
            "blue": 1.0
        },
        "green": {
            "blue": 1.0
        },
        "blue": {
            "blue": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_pure_green = {
    "name": "green",
    "title": "Spectral band 3 - Green",
    "abstract": "Green band, approximately 534nm to 588nm",
    "components": {
        "red": {
            "green": 1.0
        },
        "green": {
            "green": 1.0
        },
        "blue": {
            "green": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_pure_red = {
    "name": "red",
    "title": "Spectral band 4 - Red",
    "abstract": "Red band, roughly 637nm to 672nm",
    "components": {
        "red": {
            "red": 1.0
        },
        "green": {
            "red": 1.0
        },
        "blue": {
            "red": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_nir = {
    "name": "nir",
    "title": "Spectral band 5 - Near infra-red",
    "abstract": "Near infra-red band, roughly 853nm to 876nm",
    "components": {
        "red": {
            "nir": 1.0
        },
        "green": {
            "nir": 1.0
        },
        "blue": {
            "nir": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_swir1 = {
    "name": "swir1",
    "title": "Spectral band 6 - Short wave infra-red 1",
    "abstract": "Short wave infra-red band 1, roughly 1575nm to 1647nm",
    "components": {
        "red": {
            "swir1": 1.0
        },
        "green": {
            "swir1": 1.0
        },
        "blue": {
            "swir1": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_swir2 = {
    "name": "swir2",
    "title": "Spectral band 7 - Short wave infra-red 2",
    "abstract": "Short wave infra-red band 2, roughly 2117nm to 2285nm",
    "components": {
        "red": {
            "swir2": 1.0
        },
        "green": {
            "swir2": 1.0
        },
        "blue": {
            "swir2": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_ls_ndvi = {
    "name": "ndvi",
    "title": "NDVI - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
    "heat_mapped": True,

    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "pass_product_cfg": True,
        "kwargs": {
            "band1": "nir",
            "band2": "red"
        }
    },
    "needed_bands": ["red", "nir"],
    "range": [0.0, 1.0],

}

style_ls_ndwi = {
    "name": "ndwi",
    "title": "NDWI",
    "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "pass_product_cfg": True,
        "kwargs": {
            "band1": "green",
            "band2": "nir"
        }
    },
    "needed_bands": ["green", "nir"],
    "range": [0.0, 1.0],

}

style_ls_ndbi = {
    "name": "ndbi",
    "title": "NDBI",
    "abstract": "Normalised Difference Buildup Index - a derived index that correlates with the existence of urbanisation",
    "heat_mapped": True,
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "pass_product_cfg": True,
        "kwargs": {
            "band1": "swir2",
            "band2": "nir"
        }
    },
    "needed_bands": ["swir2", "nir"],
    "range": [0.0, 1.0],

}

style_rgb_ndvi = {
    "name": "rgb_ndvi",
    "title": "NDVI plus RGB",
    "abstract": "Normalised Difference Vegetation Index (blended with RGB) - a derived index that correlates well with the existence of vegetation",
    "component_ratio": 0.6,
    "heat_mapped": True,
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "pass_product_cfg": True,
        "kwargs": {
            "band1": "nir",
            "band2": "red"
        }
    },
    "needed_bands": ["red", "nir"],
    "range": [0.0, 1.0],
    "components": {
        "red": {
            "red": 1.0
        },
        "green": {
            "green": 1.0
        },
        "blue": {
            "blue": 1.0
        }
    },
    "scale_range": [0.0, 3000.0]
}

style_wofs_frequency = {
    "name": "WOfS_frequency",
    "title": " Water Summary",
    "abstract": "WOfS summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "pass_product_cfg": True,
        "kwargs": {
            "band": "wofs",
        }
    },
    "needed_bands": ["wofs"],
    "include_in_feature_info": False,
    "color_ramp": [
        {
            "value": 0.0,
            "color": "#ffffff",
            "alpha": 0.0,
        },
        {
            "value": 0.1,
            "color": "#d5fef9",
            "alpha": 0.0,
        },
        {
            "value": 2.0,
            "color": "#d5fef9",
        },
        {
            "value": 20.0,
            "color": "#71e3ff"
        },
        {
            "value": 40.0,
            "color": "#01ccff"
        },
        {
            "value": 60.0,
            "color": "#0178ff"
        },
        {
            "value": 80.0,
            "color": "#2701ff"
        },
        {
            "value": 100.0,
            "color": "#5700e3"
        }
    ],
    "legend": {
        "units": "%",
        "radix_point": 0,
        "scale_by": 1,
        "major_ticks": 10
    }
}
# Actual Configuration

ows_cfg = {
    "global": {
        # Master config for all services and products.
        "response_headers": {
            "Access-Control-Allow-Origin": "*",  # CORS header
        },
        "services": {
            "wms": True,
            "wcs": True,
            "wmts": True,
        },
        "published_CRSs": {
            "EPSG:3857": {  # Web Mercator
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:4326": {  # WGS-84
                "geographic": True,
                "vertical_coord_first": True
            },
            "EPSG:32648": {  # WGS 84 / UTM zone 48N
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
        },
        "allowed_urls": [
            "https://cambodiacube.services.dea.ga.gov.au",
            "https://cambodiacube.services.dea.ga.gov.au"
        ],

        # Metadata to go straight into GetCapabilities documents
        "title": "WMS server for Cambodia Datacube",
        "abstract": """Historic Landsat imagery for Cambodia.""",
        "info_url": "dea.ga.gov.au/",
        "keywords": [
            "Geomedian",
            "cambodia",
            "time-series",
        ],
        "contact_info": {
            "person": "",
            "organisation": "Geoscience Australia",
            "position": "Client Services",
            "address": {
                "type": "postal",
                "address": "GPO Box 378",
                "city": "Canberra",
                "state": "ACT",
                "postcode": "2906",
                "country": "Australia",
            },
            "telephone": "+61 2 6249 9111",
            "fax": "",
            "email": "client.services@ga.gov.au",
        },
        "fees": "",
        "access_constraints": "",
    },  # END OF global SECTION
    "wms": {
        # Config for WMS service, for all products/layers
        "s3_url": "https://data.dea.ga.gov.au",
        "s3_bucket": "dea-public-data",
        "s3_aws_zone": "ap-southeast-2",

        "max_width": 512,
        "max_height": 512,
    },  # END OF wms SECTION
    "wcs": {
        # Config for WCS service, for all products/coverages
        "default_geographic_CRS": "EPSG:4326",
        "formats": {
            "GeoTIFF": {
                "renderer": "datacube_ows.wcs_utils.get_tiff",
                "mime": "image/geotiff",
                "extension": "tif",
                "multi-time": False
            },
            "netCDF": {
                "renderer": "datacube_ows.wcs_utils.get_netcdf",
                "mime": "application/x-netcdf",
                "extension": "nc",
                "multi-time": True,
            },
        },
        "native_format": "GeoTIFF",
    },  # END OF wcs SECTION
    "layers": [
        {
            "title": "Cambodia Observation- OGC Web Services",
            "abstract": "Images from the Geomedian Surface Reflectance on Level2 Products",
            "layers": [
                # Hierarchical list of layers.  May be a combination of unnamed/unmappable folder-layers or named mappable layers.
                {
                    "title": "Surface Reflectance",
                    "abstract": "",
                    "layers": [

                        {
                            "title": "Surface Reflectance 25m Annual Geomedian (Landsat 8)",
                            "name": "ls_level2_geomedian_annual",
                            "abstract": "",
                            "product_name": "ls_level2_geomedian_annual",
                            "bands": bands_ls,
                            # "time_resolution": 'year',
                            "resource_limits": reslim_cambodia,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": True,
                            },
                            "wcs": {
                                "native_crs": "EPSG:32648",
                                "native_resolution": [25.0, 25.0],
                                "default_bands": ["red", "green", "blue"],
                            },
                            "styling": {
                                "default_style": "simple_rgb",
                                "styles": [
                                    style_ls_simple_rgb,
                                    style_infra_green, style_infra_red, style_ls_ndbi,
                                    style_ls_ndvi, style_ls_ndwi, style_nir, style_pure_blue,
                                    style_pure_green, style_pure_red, style_rgb_ndvi,
                                    style_swir1, style_swir2
                                ]
                            }
                        },
                        {
                            "title": "Surface Reflectance 25m Annual Geomedian (Landsat 7)",
                            "name": "cambodia_wofs",
                            "abstract": """
Water Observations from Space (WOfS) for Cambodia based pn USGS level 2 landsat surface reflectance. 
WOfS is produced by using a water classifier to classify when water is observed on the ground surface, next the presence of water is divided by the total observations to create a percentage of water presence over all observations. 
The WOfS layer was calculated with the datacube-stats.""",
                            "product_name": "wofs_grids_1987_2017",
                            "bands": bands_wofs,
                            "resource_limits": reslim_cambodia,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": True,
                            },
                            "wcs": {
                                "native_crs": "EPSG:32648",
                                "native_resolution": [25.0, 25.0],
                                "default_bands": ["wofs"],
                            },
                            "styling": {
                                "default_style": "WOfS_frequency",
                                "styles": [
                                    style_wofs_frequency,
                                ]
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
