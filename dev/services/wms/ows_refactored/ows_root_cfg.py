# Refactor of 9k lines ows_cfg.py
from ows_refactored.ows_reslim_cfg import (
    reslim_wms_min_zoom_35,
    reslim_wms_min_zoom_15_cache_rules,
)

# Reusable Chunks 2. Band lists.


bands_mangrove = {
    "canopy_cover_class": [],
    "extent": [],
}


bands_multi_topog = {
    "regional": [],
    "intermediate": [],
    "local": [],
}

bands_weathering = {
    "intensity": [],
}


# Reusable Chunks 4. Styles


style_mangrove_cover_v2 = {
    "name": "mangrove",
    "title": "Mangrove Cover",
    "abstract": "",
    "value_map": {
        "canopy_cover_class": [
            {
                "title": "Not Observed",
                "abstract": "(Clear Obs < 3)",
                "flags": {"notobserved": True},
                "color": "#BDBDBD",
            },
            {
                "title": "Woodland",
                "abstract": "(20% - 50% cover)",
                "flags": {"woodland": True},
                "color": "#9FFF4C",
            },
            {
                "title": "Open Forest",
                "abstract": "(50% - 80% cover)",
                "flags": {"open_forest": True},
                "color": "#5ECC00",
            },
            {
                "title": "Closed Forest",
                "abstract": "(>80% cover)",
                "flags": {"closed_forest": True},
                "color": "#3B7F00",
            },
        ]
    },
    "legend": {},
}


style_mstp_rgb = {
    "name": "mstp_rgb",
    "title": "Multi-scale Topographic Position",
    "abstract": "red regional, green intermediate and blue local",
    "components": {
        "red": {"regional": 1.0},
        "green": {"intermediate": 1.0},
        "blue": {"local": 1.0},
    },
    "scale_range": [0.0, 255.0],
    "legend": {
        "url": "https://data.dea.ga.gov.au/multi-scale-topographic-position/mstp_legend.png"
    },
}

style_wii = {
    "name": "wii",
    "title": "Weathering Intensity",
    "abstract": "Weather Intensity Index (0-6)",
    "needed_bands": ["intensity"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "intensity",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#ffffff", "alpha": 0},
        {"value": 1, "color": "#2972a8", "legend": {"label": "Low\nClass 1"}},
        {"value": 3.5, "color": "#fcf24b"},
        {"value": 6, "color": "#a02406", "legend": {"label": "High\nClass 6"}},
    ],
    "legend": {
        "begin": 1,
        "end": 6,
        "decimal_places": 0,
        "tick_labels": {
            "1": {"label": "Low\nClass 1"},
            "6": {"label": "High\nClass 6"},
        },
        "strip_location": [0.1, 0.5, 0.8, 0.15],
    },
}

# End of Reuseable

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
    },  # END OF wmts SECTION
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
                # Hierarchical list of layers.  May be a combination of unnamed/unmappable folder-layers or named mappable layers.
                {
                    "include": "ows_refactored.surface_reflectance.ows_geomedian_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.surface_reflectance.ows_nd_cfg.ls8_be_layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.surface_reflectance.ows_nd_cfg.ls30_be_layers",
                    "type": "python",
                },
                {
                    "title": "Mangrove Canopy Cover",
                    "abstract": "",
                    "layers": [
                        {
                            "name": "mangrove_cover_v2_0_2",
                            "title": "Mangrove Canopy Cover 25m 100km tile (Mangrove Canopy Cover V2.0.2)",
                            "abstract": """
Mangrove canopy cover version 2.0.2, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
The mangrove canopy cover product provides valuable information about the extent and canopy density of mangroves for each year between 1987 and 2016 for the entire Australian coastline.
The canopy cover classes are:
20-50% (pale green), 50-80% (mid green), 80-100% (dark green).
The product consists of  a sequence (one per year) of 25 meter resolution maps that are generated by analysing the Landsat fractional cover (https://doi.org/10.6084/m9.figshare.94250.v1) developed by the Joint Remote Sensing Research Program and the Global Mangrove Watch layers (https://doi.org/10.1071/MF13177) developed by the Japanese Aerospace Exploration Agency.
For service status information, see https://status.dea.ga.gov.au
""",
                            "product_name": "mangrove_cover",
                            "bands": bands_mangrove,
                            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_extent_val",
                                "always_fetch_bands": ["extent"],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:3577",
                                "native_resolution": [25, -25],
                                "default_bands": ["canopy_cover_class", "extent"],
                            },
                            "styling": {
                                "default_style": "mangrove",
                                "styles": [
                                    style_mangrove_cover_v2,
                                ],
                            },
                        },
                    ],
                },
                {
                    "include": "ows_refactored.wofs.ows_wofs_cfg.layers",
                    "type": "python",
                },
                {
                    "title": "Near Real-Time",
                    "abstract": """
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data.
The Near Real-Time capability provides analysis-ready data that is processed on receipt using
the best-available ancillary information at the time to provide atmospheric corrections.
For more information see http://pid.geoscience.gov.au/dataset/ga/122229
""",
                    "layers": [
                        {
                            "include": "ows_refactored.sentinel2.ows_nrt_cfg.multi_layers",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.sentinel2.ows_nrt_cfg.s2b_layer",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.sentinel2.ows_nrt_cfg.s2a_layer",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.dev_only.ows_nrt_wo_cfg.layers",
                            "type": "python",
                        },
                    ],
                },
                {
                    "include": "ows_refactored.sentinel2.ows_ard_cfg.layers",
                    "type": "python",
                },
                {
                    "title": "Multi-Scale Topographic Position",
                    "abstract": "",
                    "layers": [
                        {
                            "title": "Multi-Scale Topographic Position 1 degree tile (Multi-Scale Topographic Position)",
                            "name": "multi_scale_topographic_position",
                            "abstract": """
A Multi-scale topographic position image of Australia has been generated by combining
a topographic position index and topographic ruggedness. Topographic Position Index (TPI) measures
the topographic slope position of landforms. Ruggedness informs on the roughness of the surface and
is calculated as the standard deviation of elevations. Both these terrain attributes are therefore
scale dependent and will vary according to the size of the analysis window. Based on an algorithm
developed by Lindsay et al. (2015) we have generated multi-scale topographic position model over the
Australian continent using 3 second resolution (~90m) DEM derived from the Shuttle Radar Topography
Mission (SRTM). The algorithm calculates topographic position scaled by the corresponding ruggedness
across three spatial scales (window sizes) of 0.2-8.1 Km; 8.2-65.2 Km and 65.6-147.6 Km. The derived
ternary image captures variations in topographic position across these spatial scales (blue local,
green intermediate and red regional) and gives a rich representation of nested landform features that
have broad application in understanding geomorphological and hydrological processes and in mapping
regolith and soils over the Australian continent. Lindsay, J, B., Cockburn, J.M.H. and Russell,
H.A.J. 2015. An integral image approach to performing multi-scale topographic position analysis,
Geomorphology 245, 51–61.
For service status information, see https://status.dea.ga.gov.au""",
                            "product_name": "multi_scale_topographic_position",
                            "bands": bands_multi_topog,
                            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:4326",
                                "native_resolution": [
                                    0.000833333333347,
                                    -0.000833333333347,
                                ],
                                "default_bands": ["regional", "intermediate", "local"],
                            },
                            "legend": {
                                "url": "https://data.dea.ga.gov.au/multi-scale-topographic-position/mstp_legend.png",
                            },
                            "styling": {
                                "default_style": "mstp_rgb",
                                "styles": [
                                    style_mstp_rgb,
                                ],
                            },
                        },
                    ],
                },
                {
                    "title": "Weathering Intensity",
                    "abstract": "",
                    "layers": [
                        {
                            "title": "Weathering Intensity 1 degree tile (Weathering Intensity)",
                            "name": "weathering_intensity",
                            "abstract": """
    Weathering intensity or the degree of weathering is an important characteristic of the
    earth’s surface that has a significant influence on the chemical and physical properties
    of surface materials. Weathering intensity largely controls the degree to which primary
    minerals are altered to secondary components including clay minerals and oxides. The
    degree of surface weathering is particularly important in Australia where variations in
    weathering intensity correspond to the nature and distribution of regolith (weathered
    bedrock and sediments) which mantles approximately 90% of the Australian continent. The
    weathering intensity prediction has been generated using the Random Forest decision tree
    machine learning algorithm. The algorithm is used to establish predictive relationships
    between field estimates of the degree of weathering and a comprehensive suite of
    covariate or predictive datasets. The covariates used to generate the model include
    satellite imagery, terrain attributes, airborne radiometric imagery and mapped geology.
    Correlations between the training dataset and the covariates were explored through the
    generation of 300 random tree models. An r-squared correlation of 0.85 is reported using
    5 K-fold cross-validation. The mean of the 300 models is used for predicting the
    weathering intensity and the uncertainty in the weathering intensity is estimated at
    each location via the standard deviation in the 300 model values. The predictive
    weathering intensity model is an estimate of the degree of surface weathering only. The
    interpretation of the weathering intensity is different for in-situ or residual
    landscapes compared with transported materials within depositional landscapes. In
    residual landscapes, weathering process are operating locally whereas in depositional
    landscapes the model is reflecting the degree of weathering either prior to erosion and
    subsequent deposition, or weathering of sediments after being deposited. The weathering
    intensity model has broad utility in assisting mineral exploration in variably weathered
    geochemical landscapes across the Australian continent, mapping chemical and physical
    attributes of soils in agricultural landscapes and in understanding the nature and
    distribution of weathering processes occurring within the upper regolith.
    For service status information, see https://status.dea.ga.gov.au""",
                            "product_name": "weathering_intensity",
                            "bands": bands_weathering,
                            "resource_limits": reslim_wms_min_zoom_35,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:4326",
                                "native_resolution": [
                                    0.000833333333347,
                                    -0.000833333333347,
                                ],
                                "default_bands": ["intensity"],
                            },
                            "styling": {
                                "default_style": "wii",
                                "styles": [
                                    style_wii,
                                ],
                            },
                        }
                    ],
                },
                {
                    "include": "ows_refactored.tcw.ows_tcw_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.fc.ows_fc_percentiles_cfg.fcp_g_layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.fc.ows_fc_percentiles_cfg.fcp_ngv_layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.fc.ows_fc_percentiles_cfg.fcp_bs_layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.fc.ows_fc_percentiles_cfg.fcp_median_layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.fc.ows_fc_percentiles_cfg.fcp_seasonal_layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.intertidal.ows_national_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.surface_reflectance.ows_tide_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.intertidal.ows_extents_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.dev_only.ows_hap_cfg.layer",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.aster.ows_aster_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.tmad.ows_tmad_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.fc.ows_fc_albers_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.insar.ows_insar_cfg.layers",
                    "type": "python",
                },
                {
                    "title": "Collection 3",
                    "abstract": """

                    """,
                    "layers": [
                        {
                            "include": "ows_refactored.c3.ows_c3_cfg.dea_c3_ls8_ard",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.c3.ows_c3_cfg.dea_c3_ls7_ard",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.c3.ows_c3_cfg.dea_c3_ls5_ard",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.wofs.ows_c3_wo_cfg.layers",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.fc.ows_c3_fc_cfg.layers",
                            "type": "python",
                        },
                    ],
                },
            ],
        },
    ],  # End of Layers List
}  # End of ows_cfg object
