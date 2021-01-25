# Migration of wms_cfg.py.  As at commit  c44c5e61c7fb9
import copy
from ows_refactored.ows_legend_cfg import (
    legend_idx_0_1_5ticks,
    legend_idx_percentage_by_20,
    legend_idx_0_100_pixel_fc_bs_25ticks,
    legend_idx_percentage_by_25,
    legend_idx_twentyplus_3ticks,
    legend_idx_thirtyplus_4ticks,
    legend_idx_0_100_pixel_fc_25ticks,
    legend_idx_0_100_pixel_fc_ngv_25ticks,
)

from ows_refactored.ows_reslim_cfg import (
    reslim_wms_min_zoom_500_max_datasets,
    reslim_wms_min_zoom_35,
    reslim_wms_min_zoom_15_cache_rules,
    reslim_wms_min_zoom_10,
    reslim_wms_min_zoom_15,
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

bands_tcw_percentile = {
    "TCW_PC_10": [],
    "TCW_PC_50": [],
    "TCW_PC_90": [],
}


bands_nidem = {"nidem": []}


bands_hap = {
    "Band_1": [],
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

style_tcw_10 = {
    "name": "tcw_10_percentile",
    "title": "Tasseled Cap Wetness 10th Percentile",
    "abstract": "The 10th Percentile of Tasseled Cap Wetness Index (1986-2018)",
    "needed_bands": ["TCW_PC_10"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "TCW_PC_10",
        },
    },
    "range": [-1200.0, 0.0],
    "mpl_ramp": "gist_earth_r",
    "legend": {
        "url": "https://data.dea.ga.gov.au/derivative/ga_ls_tcw_percentiles_2/tcw_percentiles_legend.png",
    },
}

style_tcw_50 = {
    "name": "tcw_50_percentile",
    "title": "Tasseled Cap Wetness 50th Percentile",
    "abstract": "The 50th Percentile of Tasseled Cap Wetness Index (1986-2018)",
    "needed_bands": ["TCW_PC_50"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "TCW_PC_50",
        },
    },
    "range": [-1200.0, 0.0],
    "mpl_ramp": "gist_earth_r",
    "legend": {
        "url": "https://data.dea.ga.gov.au/derivative/ga_ls_tcw_percentiles_2/tcw_percentiles_legend.png",
    },
}

style_tcw_90 = {
    "name": "tcw_90_percentile",
    "title": "Tasseled Cap Wetness 90th Percentile",
    "abstract": "The 90th Percentile of Tasseled Cap Wetness Index (1986-2018)",
    "needed_bands": ["TCW_PC_90"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "TCW_PC_90",
        },
    },
    "range": [-1200.0, 0.0],
    "mpl_ramp": "gist_earth_r",
    "legend": {
        "url": "https://data.dea.ga.gov.au/derivative/ga_ls_tcw_percentiles_2/tcw_percentiles_legend.png",
    },
}


style_nidem = {
    "name": "NIDEM",
    "title": "National Intertidal Digital Elevation Model",
    "abstract": "National Intertidal Digital Elevation Model 25 m v1.0.0",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "nidem",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["nidem"],
    "color_ramp": [
        {"value": -2.51, "color": "#440154"},
        {
            "value": -2.5,
            "color": "#440154",
        },
        {
            "value": -2.34,
            "color": "#460e61",
        },
        {
            "value": -2.18,
            "color": "#471b6e",
        },
        {"value": -2.02, "color": "#472877"},
        {"value": -1.86, "color": "#45347f"},
        {"value": -1.7, "color": "#413f85"},
        {"value": -1.58, "color": "#3b4d8a"},
        {"value": -1.42, "color": "#37578b"},
        {"value": -1.26, "color": "#32618c"},
        {
            "value": -1.1,
            "color": "#2e6b8d",
        },
        {"value": -0.94, "color": "#2a748e"},
        {"value": -0.78, "color": "#267d8e"},
        {"value": -0.62, "color": "#23868d"},
        {"value": -0.46, "color": "#208f8c"},
        {"value": -0.3, "color": "#1e9889"},
        {"value": -0.14, "color": "#1fa186"},
        {
            "value": 0.0,
            "color": "#26ac7f",
        },
        {"value": 0.14, "color": "#32b579"},
        {"value": 0.3, "color": "#41bd70"},
        {"value": 0.46, "color": "#54c566"},
        {"value": 0.62, "color": "#69cc59"},
        {"value": 0.78, "color": "#80d24b"},
        {"value": 0.94, "color": "#99d83c"},
        {
            "value": 1.1,
            "color": "#b2dc2c",
        },
        {"value": 1.26, "color": "#cce01e"},
        {"value": 1.42, "color": "#e5e31a"},
        {
            "value": 1.5,
            "color": "#fde724",
        },
    ],
    "legend": {
        "begin": "-2.5",
        "end": "1.5",
        "ticks": ["-2.5", "-1.1", "0.0", "1.5"],
        "units": "metres",
        "tick_labels": {
            "1.5": {"prefix": ">"},
            "-2.5": {"prefix": "<"},
        },
    },
}


style_hap_simple_gray = {
    "name": "simple_gray",
    "title": "Simple gray",
    "abstract": "Simple grayscale image",
    "components": {
        "red": {"Band_1": 1.0},
        "green": {"Band_1": 1.0},
        "blue": {"Band_1": 1.0},
    },
    "scale_range": [0.0, 255],
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
                            "include": "ows_refactored.wofs.ows_nrt_wo_cfg.layers",
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
                    "title": "DEA Wetness Percentiles (Landsat)",
                    "abstract": "",
                    "layers": [
                        {
                            "title": "DEA Wetness Percentiles (Landsat)",
                            "name": "ga_ls_tcw_percentiles_2",
                            "abstract": """
Geoscience Australia Landsat Collection 2 Tasseled Cap Wetness Percentiles 1986-2018, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577).
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Areas that are partially covered in water, or where water is mixed with vegetation when viewed from above, provide habitat for a wide range of aquatic organisms.
The ability to map partial inundation is also crucial to understand patterns of human water use. We need to be able to identify potential wetlands and groundwater dependent ecosystems on the Australian continent so that they can be monitored and managed.
The Tasseled Cap Wetness Percentiles provide a multi-decadal summary of landscape wetness that can be used to identify wetlands and groundwater ecosystems.
They provide statistical summaries (10th, 50th and 90th percentiles) of the Tasseled Cap wetness index from 1987 to 2017.
They are intended for use as inputs into classification algorithms to identify potential wetlands and groundwater dependent ecosystems, and characterise salt flats, clay pans, salt lakes and coastal land forms.
This product provides valuable discrimination for characterising:
    - vegetated wetlands,
    - salt flats,
    - salt lakes,
    - coastal land cover classes
The Tasseled Cap wetness transform translates the six spectral bands of Landsat into a single wetness index.  The wetness index can be used to identify areas in the landscape that are potentially wetlands or groundwater dependent ecosystems. The Tasseled Cap Wetness Percentiles capture how the wetness index behaves over time.  The percentiles are well suited to characterising wetlands, salt flats/salt lakes and coastal ecosystems. However, care should be applied when analysing the wetness index, as soil colour and fire scars can cause misleading results. In areas of high relief caused by cliffs or steep terrain, terrain shadows can cause false positives (a falsely high wetness index).
The 10th, 50th and 90th percentiles of the Tasseled Cap wetness index are intended to capture the extreme (10th and 90th percentile) values and long-term average (50th percentile) values of the wetness index.  Percentiles are used in preference to minimum, maximum and mean, as the min/max/mean statistical measures are more sensitive to undetected cloud/cloud shadow, and can be misleading for non-normally distributed data.
The Tasseled Cap Wetness Percentiles are intended to complement the Water Observations from Space (WOfS) algorithm. WOfS is designed to discriminate open water, but the Tasseled Cap wetness index identifies areas of water and areas where water and vegetation are mixed together; i.e. mangroves and palustrine wetlands.
If you are interested in terrestrial vegetation (where water in the pixel is not a factor), use the Fractional Cover product, which provides a better biophysical characterisation of green vegetation fraction, dry vegetation fraction and bare soil vegetation fraction.
In terms of limitations, caution should be used, especially with the Tasseled Cap wetness index results in areas where residual terrain shadow, or dark soils can cause high 'wetness' index values.
One of the limitations of using the Tasseled Cap wetness index is that it will identify all 'wet' things, including potential wetlands, groundwater dependent ecosystems, irrigated crops/pasture, man-made water storages and sewerage treatment, and does not discriminate between these. As such it should be used in conjunction with other contextual data to ensure that features identified using the Tasseled Cap Wetness Percentiles are features of interest rather than false positives.
We used the Tasseled Cap transforms described in Crist et al. (1985).
Crist, E. P. (1985). A TM Tasseled Cap equivalent transformation for reflectance factor data. Remote Sensing of Environment, 17(3), 301–306. https://doi.org/10.1016/0034-4257(85)90102-6
For service status information, see https://status.dea.ga.gov.au""",
                            "product_name": "ga_ls_tcw_percentiles_2",
                            "bands": bands_tcw_percentile,
                            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:3577",
                                "default_bands": [
                                    "TCW_PC_10",
                                    "TCW_PC_50",
                                    "TCW_PC_90",
                                ],
                                "native_resolution": [25, -25],
                            },
                            "styling": {
                                "default_style": "tcw_10_percentile",
                                "styles": [style_tcw_10, style_tcw_50, style_tcw_90],
                            },
                        },
                    ],
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
                    "title": "National Intertidal Digital Elevation Model",
                    "abstract": "",
                    "layers": [
                        {
                            "name": "NIDEM",
                            "title": "National Intertidal Digital Elevation Model nidem_v1.0.0 grid (NIDEM 25m)",
                            "abstract": """
The National Intertidal Digital Elevation Model (NIDEM; Bishop-Taylor et al. 2019) is a continental-scale elevation dataset for Australia's exposed intertidal zone. NIDEM provides the first three-dimensional representation of Australia's intertidal sandy beaches and shores, tidal flats and rocky shores and reefs at 25 m spatial resolution, addressing a key gap between the availability of sub-tidal bathymetry and terrestrial elevation data. NIDEM was generated by combining global tidal modelling with a 30-year time series archive of spatially and spectrally calibrated Landsat satellite data managed within the Digital Earth Australia (DEA) platform. NIDEM complements existing intertidal extent products, and provides data to support a new suite of use cases that require a more detailed understanding of the three-dimensional topography of the intertidal zone, such as hydrodynamic modelling, coastal risk management and ecological habitat mapping.
*Overview*
Intertidal environments support important ecological habitats (e.g. sandy beaches and shores, tidal flats and rocky shores and reefs), and provide many valuable benefits such as storm surge protection, carbon storage and natural resources for recreational and commercial use. However, intertidal zones are faced with increasing threats from coastal erosion, land reclamation (e.g. port construction), and sea level rise. Accurate elevation data describing the height and shape of the coastline is needed to help predict when and where these threats will have the greatest impact. However, this data is expensive and challenging to map across the entire intertidal zone of a continent the size of Australia.
The rise and fall of the ocean can be used to describe the three-dimensional shape of the coastline by mapping the land-sea boundary (or 'waterline') across a range of known tides (e.g. low tide, high tide). Assuming that these waterlines represent lines of constant height relative to mean sea level (MSL), elevations can be modelled for the area of coastline located between the lowest and highest observed tide. To model the elevation of Australia's entire intertidal zone, 30 years of satellite images of the coastline (between 1986 and 2016 inclusive) were obtained from the archive of spatially and spectrally calibrated Landsat observations managed within the Digital Earth Australia (DEA) platform. Using the improved tidal modelling framework of the Intertidal Extents Model v2.0 (ITEM 2.0; Sagar et al. 2017, 2018), each satellite observation in the 30 year time series could be accurately associated with a modelled tide height using the global TPX08 ocean tidal model. These satellite observations were converted into a water index (NDWI), composited into discrete ten percent intervals of the observed tide range (e.g. the lowest 10% of observed tides etc), and used to extract waterlines using a spatially consistent and automated waterline extraction procedure. Triangulated irregular network (TIN) interpolation was then used to derive elevations relative to modelled mean sea level for each 25 x 25 m Landsat pixel across approximately 15,387 sq. km of intertidal terrain along Australia's entire coastline.
NIDEM differs from previous methods used to model the elevation of the intertidal zone which have predominately focused on extracting waterlines from a limited selection of satellite images using manual digitisation and visual interpretation (e.g. Chen and Rau 1998; Zhao et al. 2008; Liu et al. 2013; Chen et al. 2016). This manual process introduces subjectivity, is impractical to apply at a continental-scale, and has inherent restrictions based on the availability of high quality image data at appropriate tidal stages. By developing an automated approach to generating satellite-derived elevation data based on a 30 year time series of observations managed within the Digital Earth Australia (DEA) platform, it was possible to produce the first continental-scale three-dimensional model of the intertidal zone.
*Accuracy*
To assess the accuracy of NIDEM, we compared modelled elevations against three independent elevation and bathymetry validation datasets: the DEM of Australia derived from LiDAR 5 Metre Grid (Geoscience Australia, 2015), elevation data collected from Real Time Kinematic (RTK) GPS surveys (Danaher & Collett, 2006; HydroSurvey Australia, 2009), and 1.0 m resolution multibeam bathymetry surveys (Solihuddin et al., 2016). We assessed overall accuracy across three distinct intertidal environments: sandy beaches and shores, tidal flats, and rocky shores and reefs:
    - Sandy beaches and shores, 5 sites: Pearson's correlation = 0.92, Spearman's correlation = 0.93, RMSE +/- 0.41 m
    - Tidal flats, 9 sites: Pearson's correlation = 0.78, Spearman's correlation = 0.81, RMSE +/- 0.39 m
    - Rocky shores and reefs, 7 sites: Pearson's correlation = 0.46, Spearman's correlation = 0.79, RMSE +/- 2.98 m
*Limitations*
NIDEM covers the exposed intertidal zone which includes sandy beaches and shores, tidal flats and rocky shores and reefs. The model excludes intertidal vegetation communities such as mangroves.
Areas with comparatively steep coastlines and small tidal ranges are poorly captured in the 25 m spatial resolution input Landsat data and resulting NIDEM model. This includes much of the south eastern and southern Australian coast (e.g. New South Wales, Victoria, Tasmania).
Poor validation results for rocky shore and reef sites within the southern Kimberly region highlighted limitations in the NIDEM model that occur when the global OTPS TPX08 Atlas Tidal Model was unable to predict complex and asynchronous local tidal patterns. This is likely to also reduce model accuracy in complex estuaries and coastal wetlands where river flow or vegetative resistance causes hydrodynamic attenuation in tidal flow.
The complex temporal behaviour of tides mean that a sun synchronous sensor like Landsat does not observe the full range of the tidal cycle at all locations. This causes spatial bias in the proportion of the tidal range observed in different regions, which can prevent NIDEM from providing elevation data for areas of the intertidal zone exposed or inundated at the extremes of the tidal range. Accordingly, NIDEM provides elevation data for the portion of the tidal range observed by Landsat, rather than the full tidal range.
While image compositing and masking methods have been applied to remove the majority of noise and non-tidal artefacts from NIDEM, issues remain in several locations. It is recommended that the data be used with caution in the following areas:
    - The Recherche Archipelago in southern Western Australia
    - Port Phillip Bay in Victoria
    - The eastern coast of Tasmania and King Island
    - Saunders Reef and surrounds in the northern Coral Sea
*Data access and additional information*
    - Journal article: Bishop-Taylor et al. 2019 (https://doi.org/10.1016/j.ecss.2019.03.006)
    - Data available on THREDDS: http://dapds00.nci.org.au/thredds/catalogs/fk4/nidem_1_0.html
    - eCat catalogue listing including data access: http://pid.geoscience.gov.au/dataset/ga/123678
    - CMI listing for extended metadata: https://cmi.ga.gov.au/pd/NIDEM_25_1.0.0
For service status information, see https://status.dea.ga.gov.au""",
                            "product_name": "nidem",
                            "bands": bands_nidem,
                            "time_resolution": "year",
                            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
                            "flags": {
                                "band": "land",
                                "product": "geodata_coast_100k",
                                "ignore_time": True,
                                "ignore_info_flags": [],
                            },
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:3577",
                                "default_bands": ["nidem"],
                                "native_resolution": [25, -25],
                            },
                            "styling": {
                                "default_style": "NIDEM",
                                "styles": [
                                    style_nidem,
                                ],
                            },
                        },
                    ],
                },
                {
                    "include": "ows_refactored.tide.ows_tide_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.tide.ows_intertidal_cfg.layers",
                    "type": "python",
                },
                {
                    "title": "Projects",
                    "abstract": "",
                    "layers": [
                        {
                            "title": "Projects munged historical airborne photography (HAP)",
                            "name": "historical_airborne_photography",
                            "abstract": "Historical Airborne Photography",
                            "product_name": "historical_airborne_photography",
                            "bands": bands_hap,
                            "resource_limits": reslim_wms_min_zoom_500_max_datasets,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:3577",
                                "default_bands": ["Band_1"],
                                "native_resolution": [1.0, 1.0],
                            },
                            "styling": {
                                "default_style": "simple_gray",
                                "styles": [
                                    style_hap_simple_gray,
                                ],
                            },
                        }
                    ],
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
                    ],
                },
            ],
        },
    ],  # End of Layers List
}  # End of ows_cfg object
