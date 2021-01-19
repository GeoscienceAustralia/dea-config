
reslim_wofs_obs = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 35.0,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    },
}

bands_fc_3 = {
    "bs": ["bare_soil"],
    "pv": ["photosynthetic_vegetation", "green_vegetation"],
    "npv": ["non_photosynthetic_vegetation", "brown_vegetation"],
    "ue": [],
}

style_fc_3_simple = {
    "name": "simple_fc",
    "title": "Fractional Cover",
    "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
    "components": {"red": {"bs": 1.0}, "green": {"pv": 1.0}, "blue": {"npv": 1.0}},
    "scale_range": [0.0, 100.0],
    # "pq_masks": [
    #     {
    #         "flags": {"dry": True},
    #     },
    #     {
    #         "flags": {
    #             "terrain_or_low_angle": False,
    #             "high_slope": False,
    #             "cloud_shadow": False,
    #             "cloud": False,
    #             "sea": False,
    #         }
    #     },
    # ],
}

bands_wofs_obs = {
    "water": [],
}

style_c3_wofs_obs = {
    "name": "observations",
    "title": "Observations",
    "abstract": "Observations",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {
                    "or": {
                        # "terrain_or_low_angle": True,
                        "terrain_shadow": True,
                        "cloud_shadow": True,
                        "cloud": True,
                        "high_slope": True,
                        "noncontiguous": True,
                    }
                },
                "color": "#707070",
            },
            #     {
            #     # Possible Sea Glint, also mark as invalid
            #     "title": "",
            #     "abstract": "",
            #     "flags": {"dry": True, "sea": True},
            #     "color": "#707070",
            # },
            # {
            #     "title": "Dry",
            #     "abstract": "Dry",
            #     "flags": {
            #         "dry": True,
            #         "sea": False,
            #     },
            #     "color": "#D99694",
            # },
            # {
            #     "title": "Wet",
            #     "abstract": "Wet or Sea",
            #     "flags": {"or": {"wet": True, "sea": True}},
            #     "color": "#4F81BD",
            # },
        ]
    },
}

style_c3_wofs_obs_wet_only = {
    "name": "wet",
    "title": "Wet Only",
    "abstract": "Wet Only",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {
                    "or": {
                        # "terrain_or_low_angle": True,

                        "terrain_shadow": True,
                        "cloud_shadow": True,
                        "cloud": True,
                        "high_slope": True,
                        "noncontiguous": True,
                    }
                },
                "color": "#707070",
                "mask": True,
            },
            # {
            #     # Possible Sea Glint, also mark as invalid
            #     "title": "",
            #     "abstract": "",
            #     "flags": {"dry": True, "sea": True},
            #     "color": "#707070",
            #     "mask": True,
            # },
            # {
            #     "title": "Dry",
            #     "abstract": "Dry",
            #     "flags": {
            #         "dry": True,
            #         "sea": False,
            #     },
            #     "color": "#D99694",
            #     "mask": True,
            # },
            # {
            #     "title": "Wet",
            #     "abstract": "Wet or Sea",
            #     "flags": {"or": {"wet": True, "sea": True}},
            #     "color": "#4F81BD",
            # },
        ]
    },
}


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
            "EPSG:4326": {"geographic": True, "vertical_coord_first": True},  # WGS-84
            "EPSG:3577": {  # GDA-94, internal representation
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:3111": {  # VicGrid94 for delwp.vic.gov.au
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "WIKID:102171": {  # VicGrid94 alias for delwp.vic.gov.au
                "alias": "EPSG:3111"
            },
        },
        "allowed_urls": [
            "https://ows.services.dea.ga.gov.au",
            "https://ows.services.dev.dea.ga.gov.au",
            "https://ows.dev.dea.ga.gov.au",
            "https://ows.dea.ga.gov.au",
            "https://nc-ows.dev.dea.ga.gov.au",
        ],
        # Metadata to go straight into GetCapabilities documents
        "title": "Digital Earth Australia - OGC Web Services",
        "abstract": "Digital Earth Australia OGC Web Services",
        "info_url": "dea.ga.gov.au/",
        "keywords": [
            "geomedian",
            "WOfS",
            "mangrove",
            "bare-earth",
            "NIDEM",
            "HLTC",
            "landsat",
            "australia",
            "time-series",
            "fractional-cover",
        ],
        "contact_info": {
            "person": "Digital Earth Australia",
            "organisation": "Geoscience Australia",
            "position": "",
            "address": {
                "type": "postal",
                "address": "GPO Box 378",
                "city": "Canberra",
                "state": "ACT",
                "postcode": "2609",
                "country": "Australia",
            },
            "telephone": "+61 2 6249 9111",
            "fax": "",
            "email": "earth.observation@ga.gov.au",
        },
        "fees": "",
        "access_constraints": "© Commonwealth of Australia (Geoscience Australia) 2018. "
        "This product is released under the Creative Commons Attribution 4.0 International Licence. "
        "http://creativecommons.org/licenses/by/4.0/legalcode",
    },  # END OF global SECTION
    "wms": {
        # Config for WMS service, for all products/layers
        "s3_url": "https://data.dea.ga.gov.au",
        "s3_bucket": "dea-public-data",
        "s3_aws_zone": "ap-southeast-2",
        "max_width": 512,
        "max_height": 512,
    },  # END OF wms SECTION
    "wmts": {
        # Config for WMTS service, for all products/layers
        "tile_matrix_sets": {
            "EPSG:3111": {
                "crs": "EPSG:3111",
                "matrix_origin": (1786000.0, 3081000.0),
                "tile_size": (512, 512),
                "scale_set": [
                    7559538.928601667,
                    3779769.4643008336,
                    1889884.7321504168,
                    944942.3660752084,
                    472471.1830376042,
                    236235.5915188021,
                    94494.23660752083,
                    47247.11830376041,
                    23623.559151880207,
                    9449.423660752083,
                    4724.711830376042,
                    2362.355915188021,
                    1181.1779575940104,
                    755.9538928601667,
                ],
                "matrix_exponent_initial_offsets": (1, 0),
            },
        }
    }, # END OF wmts SECTION
    "wcs": {
        # Config for WCS service, for all products/coverages
        "default_geographic_CRS": "EPSG:4326",
        "formats": {
            "GeoTIFF": {
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_tiff",
                    "2": "datacube_ows.wcs2_utils.get_tiff",
                },
                "mime": "image/geotiff",
                "extension": "tif",
                "multi-time": False,
            },
            "netCDF": {
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_netcdf",
                    "2": "datacube_ows.wcs2_utils.get_netcdf",
                },
                "mime": "application/x-netcdf",
                "extension": "nc",
                "multi-time": True,
            },
        },
        "native_format": "GeoTIFF",
    },  # END OF wcs SECTION
    "layers": [
        {
            "title": "Digital Earth Australia - OGC Web Services",
            "abstract": "Digital Earth Australia OGC Web Services",
            "layers": [
                {
                    "title": "Collection 3",
                    "abstract": """

                    """,
                    "layers": [
                        {
                            "title": "Collection 3 Water",
                            "name": "ga_ls_wo_3",
                            "abstract": """
Water Observations from Space (WOfS) provides surface water observations derived from satellite imagery for all of Australia. The current product (Version 2.1.5) includes observations taken from 1986 to the present, from the Landsat 5, 7 and 8 satellites. WOfS covers all of mainland Australia and Tasmania but excludes off-shore Territories.

The WOfS product allows users to get a better understanding of where water is normally present in a landscape, where water is seldom observed, and where inundation has occurred occasionally.

Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water. The details of the WOfS algorithm and derived statistics are available at http://dx.doi.org/10.1016/j.rse.2015.11.003.

For service status information, see https://status.dea.ga.gov.au
""",
                            "product_name": "ga_ls_wo_3",
                            "bands": bands_wofs_obs,
                            "resource_limits": reslim_wofs_obs,
                            "dynamic": True,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_bitflag",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                                "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
                            },
                            "wcs": {
                                "native_crs": "EPSG:3577",
                                "native_resolution": [25, -25],
                                "default_bands": ["water"],
                            },
                            "styling": {
                                "default_style": "observations",
                                "styles": [style_c3_wofs_obs, style_c3_wofs_obs_wet_only],
                            },
                        },
                        {
                            "title": "Collection 3 fc",
                            "name": "ga_ls_fc_3",
                            "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. This product contains Fractional Cover dervied from the Landsat 5, 7 and 8 satellites For service status information, see https://status.dea.ga.gov.au
""",
                            "product_name": "ga_ls_fc_3",
                            "bands": bands_fc_3,
                            "resource_limits": reslim_wofs_obs,
                            "dynamic": True,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "flags": {
                                "band": "water",
                                "products": [
                                    "ga_ls_wo_3",
                                    "ga_ls_wo_3",
                                    "ga_ls_wo_3",
                                ],
                                "ignore_time": False,
                                "ignore_info_flags": [],
                                "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
                            },
                            "wcs": {
                                "native_crs": "EPSG:3577",
                                "default_bands": ["bs", "pv", "npv"],
                                "native_resolution": [25, -25],
                            },
                            "styling": {
                                "default_style": "simple_fc",
                                "styles": [
                                    style_fc_3_simple,
                                ],
                            },
                        },
                    ]
                }
            ],
        },
    ],  # End of Layers List
}  # End of ows_cfg object
