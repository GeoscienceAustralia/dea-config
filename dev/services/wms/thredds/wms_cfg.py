# Static config for the wms metadata.
response_cfg = {
    "Access-Control-Allow-Origin": "*",  # CORS header
}

service_cfg = {
    # Which web service(s) should be supported by this instance
    "wcs": True,
    "wms": True,
    "wmts": True,

    # Required config for WMS and/or WCS
    # Service title - appears e.g. in Terria catalog
    "title": "Digital Earth Australia - OGC Web Services",
    # Service URL.  Should a fully qualified URL
    "url": ["https://dave.services.devkube.dea.ga.gov.au"],
    "human_url": "dea.ga.gov.au/",
    # Supported co-ordinate reference systems
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
        "EPSG:3577": {  # GDA-94, internal representation
            "geographic": False,
            "horizontal_coord": "x",
            "vertical_coord": "y",
        },
    },

    # Required config for WCS
    # Must be a geographic CRS in the published_CRSs list.  EPSG:4326 is recommended, but any geographic CRS should work.
    "default_geographic_CRS": "EPSG:4326",

    # Supported WCS formats
    "wcs_formats": {
        # Key is the format name, as used in DescribeCoverage XML
        "GeoTIFF": {
            # Renderer is the FQN of a Python function that takes:
            #   * A WCS Request object
            #   * Some ODC data to be rendered.
            "renderer": "datacube_wms.wcs_utils.get_tiff",
            # The MIME type of the image, as used in the Http Response.
            "mime": "image/geotiff",
            # The file extension to add to the filename.
            "extension": "tif",
            # Whether or not the file format supports multiple time slices.
            "multi-time": False
        },
        "netCDF": {
            "renderer": "datacube_wms.wcs_utils.get_netcdf",
            "mime": "application/x-netcdf",
            "extension": "nc",
            "multi-time": True,
        }
    },
    # The native wcs format must be declared in wcs_formats above.
    "native_wcs_format": "GeoTIFF",

    # Optional config for instances supporting WMS
    "max_width": 512,
    "max_height": 512,

    # Optional config for all services (WMS and/or WCS) - may be set to blank/empty, no defaults
    "abstract": """Digital Earth Australia OGC Web Services""",
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
        "fractional-cover"
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
    "preauthenticate_s3": True,
    "geotiff_georeference_source": "INTERNAL"
}

layer_cfg = [
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "Sentinel-2 Definitive",
        "title": "Sentinel Definitive",
        "abstract": "This is a definitive archive of daily Sentinel-2 Near Real Time data. "
                    "that is processed on receipt using the best-available ancillary information at the time to "
                    "provide atmospheric corrections. For more information see "
                    "http://pid.geoscience.gov.au/dataset/ga/122229",
        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "Sentinel 2 (A and B combined)",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "Surface Reflectance",
                "abstract": """
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For more information see http://pid.geoscience.gov.au/dataset/ga/122229

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For service status information, see https://status.dea.ga.gov.au""",
                # The WMS name for the layer
                "name": "s2_nrt_granule_nbar_t",
                # The Datacube name for the associated data product
                "multi_product": True,
                "product_name": ["s2a_ard_granule", "s2b_ard_granule"],
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_nrt_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 15.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi", "ndci"]
                },
                "wcs_default_bands": ["nbart_red", "nbart_green", "nbart_blue"],
                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "nbart_red": 1.0
                            },
                            "green": {
                                "nbart_green": 1.0
                            },
                            "blue": {
                                "nbart_blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
                        "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
                        "components": {
                            "red": {
                                "nbart_swir_2": 1.0
                            },
                            "green": {
                                "nbart_nir_1": 1.0
                            },
                            "blue": {
                                "nbart_green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "index_function": lambda data: (data["nbart_nir_1"] - data["nbart_red"]) / (data["nbart_nir_1"] + data["nbart_red"]),
                        "needed_bands": ["nbart_red", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 1.0
                            },
                            {
                                "value": 0.1,
                                "color": "#A35F18"
                            },
                            {
                                "value": 0.2,
                                "color": "#B88512"
                            },
                            {
                                "value": 0.3,
                                "color": "#CEAC0E"
                            },
                            {
                                "value": 0.4,
                                "color": "#E5D609"
                            },
                            {
                                "value": 0.5,
                                "color": "#FFFF0C"
                            },
                            {
                                "value": 0.6,
                                "color": "#C3DE09"
                            },
                            {
                                "value": 0.7,
                                "color": "#88B808"
                            },
                            {
                                "value": 0.8,
                                "color": "#529400"
                            },
                            {
                                "value": 0.9,
                                "color": "#237100"
                            },
                            {
                                "value": 1.0,
                                "color": "#114D04"
                            }
                        ]

                    },
                    {
                        "name": "nbr",
                        "title": "NBR",
                        "abstract": "The Normalized burn ratio (NBR) is used to identify burned areas. The formula is similar to a normalized difference vegetation index (NDVI), except that it uses near-infrared (NIR) and shortwave-infrared (SWIR) portions of the electromagnetic spectrum (Lopez, 1991; Key and Benson, 1995)",
                        "index_function": lambda data: (data["nbart_nir_1"] - data["nbart_swir_3"]) / (data["nbart_nir_1"] + data["nbart_swir_3"]),
                        "needed_bands": ["nbart_swir_3", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -1.0,
                                "color": "#d81e11",
                                "legend": {}
                            },
                            {
                                "value": -0.2,
                                "color": "#d81e11",
                            },
                            {
                                "value": -0.19999999,
                                "color": "#d81e11",
                                "alpha": 0.0,
                                "legend": {
                                    "label": ">-0.2"
                                }
                            },
                            {
                                "value": 1.0,
                                "color": "#d81e11",
                                "alpha": 0.0,
                            },
                        ]

                    },
                    {
                        "name": "ndwi",
                        "title": "NDWI - Green, NIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water",
                        "index_function": lambda data: (data["nbart_green"] - data["nbart_nir_1"]) / (
                                    data["nbart_nir_1"] + data["nbart_green"]),
                        "needed_bands": ["nbart_green", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 1.0
                            },
                            {
                                "value": 1.0,
                                "color": "#0303FF",
                            },
                        ]
                    },
                    {
                        "name": "ndci",
                        "title": "NDCI - Red Edge, Red",
                        "abstract": "Normalised Difference Chlorophyll Index - a derived index that correlates well with the existence of chlorophyll",
                        "index_function": lambda data: (data["nbart_red_edge_1"] - data["nbart_red"]) / (data["nbart_red_edge_1"] + data["nbart_red"]).where(((data["nbart_green"] - data["nbart_swir_3"]) / (data["nbart_green"] + data["nbart_swir_3"])) > 0.1),
                        "needed_bands": ["nbart_red_edge_1", "nbart_red", "nbart_green", "nbart_swir_3"],
                        "color_ramp": [
                            {
                                "value": -0.1,
                                "color": "#1696FF",
                                "legend": {
                                    "prefix": "<"
                                }
                            },
                            {
                                "value": -0.1,
                                "color": "#1696FF"
                            },
                            {
                                "value": 0.0,
                                "color": "#00FFDF",
                                "legend": {}
                            },
                            {
                                "value": 0.1,
                                "color": "#FFF50E",
                            },
                            {
                                "value": 0.2,
                                "color": "#FFB50A",
                                "legend": {}
                            },
                            {
                                "value": 0.4,
                                "color": "#FF530D",
                            },
                            {
                                "value": 0.5,
                                "color": "#FF0000",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ]
                    },
                    {
                        "name": "aerosol",
                        "title": "Narrow Blue - 440",
                        "abstract": "Coastal Aerosol or Narrow Blue band, approximately 435nm to 450nm",
                        "components": {
                            "red": {
                                "nbart_coastal_aerosol": 1.0
                            },
                            "green": {
                                "nbart_coastal_aerosol": 1.0
                            },
                            "blue": {
                                "nbart_coastal_aerosol": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "blue",
                        "title": "Blue - 490",
                        "abstract": "Blue band, approximately 453nm to 511nm",
                        "components": {
                            "red": {
                                "nbart_blue": 1.0
                            },
                            "green": {
                                "nbart_blue": 1.0
                            },
                            "blue": {
                                "nbart_blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "green",
                        "title": "Green - 560",
                        "abstract": "Green band, approximately 534nm to 588nm",
                        "components": {
                            "red": {
                                "nbart_green": 1.0
                            },
                            "green": {
                                "nbart_green": 1.0
                            },
                            "blue": {
                                "nbart_green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red",
                        "title": "Red - 670",
                        "abstract": "Red band, roughly 637nm to 672nm",
                        "components": {
                            "red": {
                                "nbart_red": 1.0
                            },
                            "green": {
                                "nbart_red": 1.0
                            },
                            "blue": {
                                "nbart_red": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red_edge_1",
                        "title": "Vegetation Red Edge - 710",
                        "abstract": "Near infra-red band, centred on 710nm",
                        "components": {
                            "red": {
                                "nbart_red_edge_1": 1.0
                            },
                            "green": {
                                "nbart_red_edge_1": 1.0
                            },
                            "blue": {
                                "nbart_red_edge_1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red_edge_2",
                        "title": "Vegetation Red Edge - 740",
                        "abstract": "Near infra-red band, centred on 740nm",
                        "components": {
                            "red": {
                                "nbart_red_edge_2": 1.0
                            },
                            "green": {
                                "nbart_red_edge_2": 1.0
                            },
                            "blue": {
                                "nbart_red_edge_2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red_edge_3",
                        "title": "Vegetation Red Edge - 780",
                        "abstract": "Near infra-red band, centred on 780nm",
                        "components": {
                            "red": {
                                "nbart_red_edge_3": 1.0
                            },
                            "green": {
                                "nbart_red_edge_3": 1.0
                            },
                            "blue": {
                                "nbart_red_edge_3": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "nir",
                        "title": "Near Infrared (NIR) - 840",
                        "abstract": "Near infra-red band, roughly 853nm to 876nm",
                        "components": {
                            "red": {
                                "nbart_nir_1": 1.0
                            },
                            "green": {
                                "nbart_nir_1": 1.0
                            },
                            "blue": {
                                "nbart_nir_1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "narrow_nir",
                        "title": "Narrow Near Infrared - 870",
                        "abstract": "Near infra-red band, centred on 865nm",
                        "components": {
                            "red": {
                                "nbart_nir_2": 1.0
                            },
                            "green": {
                                "nbart_nir_2": 1.0
                            },
                            "blue": {
                                "nbart_nir_2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir1",
                        "title": "Shortwave Infrared (SWIR) - 1610",
                        "abstract": "Short wave infra-red band 1, roughly 1575nm to 1647nm",
                        "components": {
                            "red": {
                                "nbart_swir_2": 1.0
                            },
                            "green": {
                                "nbart_swir_2": 1.0
                            },
                            "blue": {
                                "nbart_swir_2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir2",
                        "title": "Shortwave Infrared (SWIR) - 2190",
                        "abstract": "Short wave infra-red band 2, roughly 2117nm to 2285nm",
                        "components": {
                            "red": {
                                "nbart_swir_3": 1.0
                            },
                            "green": {
                                "nbart_swir_3": 1.0
                            },
                            "blue": {
                                "nbart_swir_3": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
            {
                # Included as a keyword  for the layer
                "label": "Sentinel 2B",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "Surface Reflectance",
                "abstract": """
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For more information see http://pid.geoscience.gov.au/dataset/ga/122229

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For service status information, see https://status.dea.ga.gov.au""",
                # The WMS name for the layer
                "name": "s2b_ard_granule_nbar_t",
                # The Datacube name for the associated data product
                "product_name": "s2b_ard_granule",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_nrt_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 15.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi", "ndci"]
                },
                "wcs_default_bands": ["nbart_red", "nbart_green", "nbart_blue"],
                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "nbart_red": 1.0
                            },
                            "green": {
                                "nbart_green": 1.0
                            },
                            "blue": {
                                "nbart_blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
                        "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
                        "components": {
                            "red": {
                                "nbart_swir_2": 1.0
                            },
                            "green": {
                                "nbart_nir_1": 1.0
                            },
                            "blue": {
                                "nbart_green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "index_function": lambda data: (data["nbart_nir_1"] - data["nbart_red"]) / (data["nbart_nir_1"] + data["nbart_red"]),
                        "needed_bands": ["nbart_red", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 1.0
                            },
                            {
                                "value": 0.1,
                                "color": "#A35F18"
                            },
                            {
                                "value": 0.2,
                                "color": "#B88512"
                            },
                            {
                                "value": 0.3,
                                "color": "#CEAC0E"
                            },
                            {
                                "value": 0.4,
                                "color": "#E5D609"
                            },
                            {
                                "value": 0.5,
                                "color": "#FFFF0C"
                            },
                            {
                                "value": 0.6,
                                "color": "#C3DE09"
                            },
                            {
                                "value": 0.7,
                                "color": "#88B808"
                            },
                            {
                                "value": 0.8,
                                "color": "#529400"
                            },
                            {
                                "value": 0.9,
                                "color": "#237100"
                            },
                            {
                                "value": 1.0,
                                "color": "#114D04"
                            }
                        ]

                    },
                    {
                        "name": "nbr",
                        "title": "NBR",
                        "abstract": "The Normalized burn ratio (NBR) is used to identify burned areas. The formula is similar to a normalized difference vegetation index (NDVI), except that it uses near-infrared (NIR) and shortwave-infrared (SWIR) portions of the electromagnetic spectrum (Lopez, 1991; Key and Benson, 1995)",
                        "index_function": lambda data: (data["nbart_nir_1"] - data["nbart_swir_3"]) / (data["nbart_nir_1"] + data["nbart_swir_3"]),
                        "needed_bands": ["nbart_swir_3", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -1.0,
                                "color": "#d81e11",
                                "legend": {}
                            },
                            {
                                "value": -0.2,
                                "color": "#d81e11",
                            },
                            {
                                "value": -0.19999999,
                                "color": "#d81e11",
                                "alpha": 0.0,
                                "legend": {
                                    "label": ">-0.2"
                                }
                            },
                            {
                                "value": 1.0,
                                "color": "#d81e11",
                                "alpha": 0.0,
                            },
                        ]

                    },
                    {
                        "name": "ndwi",
                        "title": "NDWI - Green, NIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water",
                        "index_function": lambda data: (data["nbart_green"] - data["nbart_nir_1"]) / (
                                    data["nbart_nir_1"] + data["nbart_green"]),
                        "needed_bands": ["nbart_green", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 1.0
                            },
                            {
                                "value": 1.0,
                                "color": "#0303FF",
                            },
                        ]
                    },
                    {
                        "name": "ndci",
                        "title": "NDCI - Red Edge, Red",
                        "abstract": "Normalised Difference Chlorophyll Index - a derived index that correlates well with the existence of chlorophyll",
                        "index_function": lambda data: (data["nbart_red_edge_1"] - data["nbart_red"]) / (data["nbart_red_edge_1"] + data["nbart_red"]).where(((data["nbart_green"] - data["nbart_swir_3"]) / (data["nbart_green"] + data["nbart_swir_3"])) > 0.1),
                        "needed_bands": ["nbart_red_edge_1", "nbart_red", "nbart_green", "nbart_swir_3"],
                        "color_ramp": [
                            {
                                "value": -0.1,
                                "color": "#1696FF",
                                "legend": {
                                    "prefix": "<"
                                }
                            },
                            {
                                "value": -0.1,
                                "color": "#1696FF"
                            },
                            {
                                "value": 0.0,
                                "color": "#00FFDF",
                                "legend": {}
                            },
                            {
                                "value": 0.1,
                                "color": "#FFF50E",
                            },
                            {
                                "value": 0.2,
                                "color": "#FFB50A",
                                "legend": {}
                            },
                            {
                                "value": 0.4,
                                "color": "#FF530D",
                            },
                            {
                                "value": 0.5,
                                "color": "#FF0000",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ]
                    },
                    {
                        "name": "aerosol",
                        "title": "Narrow Blue - 440",
                        "abstract": "Coastal Aerosol or Narrow Blue band, approximately 435nm to 450nm",
                        "components": {
                            "red": {
                                "nbart_coastal_aerosol": 1.0
                            },
                            "green": {
                                "nbart_coastal_aerosol": 1.0
                            },
                            "blue": {
                                "nbart_coastal_aerosol": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "blue",
                        "title": "Blue - 490",
                        "abstract": "Blue band, approximately 453nm to 511nm",
                        "components": {
                            "red": {
                                "nbart_blue": 1.0
                            },
                            "green": {
                                "nbart_blue": 1.0
                            },
                            "blue": {
                                "nbart_blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "green",
                        "title": "Green - 560",
                        "abstract": "Green band, approximately 534nm to 588nm",
                        "components": {
                            "red": {
                                "nbart_green": 1.0
                            },
                            "green": {
                                "nbart_green": 1.0
                            },
                            "blue": {
                                "nbart_green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red",
                        "title": "Red - 670",
                        "abstract": "Red band, roughly 637nm to 672nm",
                        "components": {
                            "red": {
                                "nbart_red": 1.0
                            },
                            "green": {
                                "nbart_red": 1.0
                            },
                            "blue": {
                                "nbart_red": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red_edge_1",
                        "title": "Vegetation Red Edge - 710",
                        "abstract": "Near infra-red band, centred on 710nm",
                        "components": {
                            "red": {
                                "nbart_red_edge_1": 1.0
                            },
                            "green": {
                                "nbart_red_edge_1": 1.0
                            },
                            "blue": {
                                "nbart_red_edge_1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red_edge_2",
                        "title": "Vegetation Red Edge - 740",
                        "abstract": "Near infra-red band, centred on 740nm",
                        "components": {
                            "red": {
                                "nbart_red_edge_2": 1.0
                            },
                            "green": {
                                "nbart_red_edge_2": 1.0
                            },
                            "blue": {
                                "nbart_red_edge_2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red_edge_3",
                        "title": "Vegetation Red Edge - 780",
                        "abstract": "Near infra-red band, centred on 780nm",
                        "components": {
                            "red": {
                                "nbart_red_edge_3": 1.0
                            },
                            "green": {
                                "nbart_red_edge_3": 1.0
                            },
                            "blue": {
                                "nbart_red_edge_3": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "nir",
                        "title": "Near Infrared (NIR) - 840",
                        "abstract": "Near infra-red band, roughly 853nm to 876nm",
                        "components": {
                            "red": {
                                "nbart_nir_1": 1.0
                            },
                            "green": {
                                "nbart_nir_1": 1.0
                            },
                            "blue": {
                                "nbart_nir_1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "narrow_nir",
                        "title": "Narrow Near Infrared - 870",
                        "abstract": "Near infra-red band, centred on 865nm",
                        "components": {
                            "red": {
                                "nbart_nir_2": 1.0
                            },
                            "green": {
                                "nbart_nir_2": 1.0
                            },
                            "blue": {
                                "nbart_nir_2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir1",
                        "title": "Shortwave Infrared (SWIR) - 1610",
                        "abstract": "Short wave infra-red band 1, roughly 1575nm to 1647nm",
                        "components": {
                            "red": {
                                "nbart_swir_2": 1.0
                            },
                            "green": {
                                "nbart_swir_2": 1.0
                            },
                            "blue": {
                                "nbart_swir_2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir2",
                        "title": "Shortwave Infrared (SWIR) - 2190",
                        "abstract": "Short wave infra-red band 2, roughly 2117nm to 2285nm",
                        "components": {
                            "red": {
                                "nbart_swir_3": 1.0
                            },
                            "green": {
                                "nbart_swir_3": 1.0
                            },
                            "blue": {
                                "nbart_swir_3": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
            {
                # Included as a keyword  for the layer
                "label": "Sentinel 2A",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "Surface Reflectance",
                "abstract": """
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For more information see http://pid.geoscience.gov.au/dataset/ga/122229

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For service status information, see https://status.dea.ga.gov.au""",
                # The WMS name for the layer
                "name": "s2a_ard_granule_nbar_t",
                # The Datacube name for the associated data product
                "product_name": "s2a_ard_granule",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_nrt_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 15.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi", "ndci"]
                },
                "wcs_default_bands": ["nbart_red", "nbart_green", "nbart_blue"],
                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "nbart_red": 1.0
                            },
                            "green": {
                                "nbart_green": 1.0
                            },
                            "blue": {
                                "nbart_blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
                        "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
                        "components": {
                            "red": {
                                "nbart_swir_2": 1.0
                            },
                            "green": {
                                "nbart_nir_1": 1.0
                            },
                            "blue": {
                                "nbart_green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "index_function": lambda data: (data["nbart_nir_1"] - data["nbart_red"]) / (
                                    data["nbart_nir_1"] + data["nbart_red"]),
                        "needed_bands": ["nbart_red", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 1.0
                            },
                            {
                                "value": 0.1,
                                "color": "#A35F18"
                            },
                            {
                                "value": 0.2,
                                "color": "#B88512"
                            },
                            {
                                "value": 0.3,
                                "color": "#CEAC0E"
                            },
                            {
                                "value": 0.4,
                                "color": "#E5D609"
                            },
                            {
                                "value": 0.5,
                                "color": "#FFFF0C"
                            },
                            {
                                "value": 0.6,
                                "color": "#C3DE09"
                            },
                            {
                                "value": 0.7,
                                "color": "#88B808"
                            },
                            {
                                "value": 0.8,
                                "color": "#529400"
                            },
                            {
                                "value": 0.9,
                                "color": "#237100"
                            },
                            {
                                "value": 1.0,
                                "color": "#114D04"
                            }
                        ]

                    },
                    {
                        "name": "nbr",
                        "title": "NBR",
                        "abstract": "The Normalized burn ratio (NBR) is used to identify burned areas. The formula is similar to a normalized difference vegetation index (NDVI), except that it uses near-infrared (NIR) and shortwave-infrared (SWIR) portions of the electromagnetic spectrum (Lopez, 1991; Key and Benson, 1995)",
                        "index_function": lambda data: (data["nbart_nir_1"] - data["nbart_swir_3"]) / (data["nbart_nir_1"] + data["nbart_swir_3"]),
                        "needed_bands": ["nbart_swir_3", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -1.0,
                                "color": "#d81e11",
                                "legend": {}
                            },
                            {
                                "value": -0.2,
                                "color": "#d81e11",
                            },
                            {
                                "value": -0.19999999,
                                "color": "#d81e11",
                                "alpha": 0.0,
                                "legend": {
                                    "label": ">-0.2"
                                }
                            },
                            {
                                "value": 1.0,
                                "color": "#d81e11",
                                "alpha": 0.0,
                            },
                        ]

                    },
                    {
                        "name": "ndwi",
                        "title": "NDWI - Green, NIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water",
                        "index_function": lambda data: (data["nbart_green"] - data["nbart_nir_1"]) / (
                                    data["nbart_nir_1"] + data["nbart_green"]),
                        "needed_bands": ["nbart_green", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 1.0
                            },
                            {
                                "value": 1.0,
                                "color": "#0303FF",
                            },
                        ]
                    },
                    {
                        "name": "ndci",
                        "title": "NDCI - Red Edge, Red",
                        "abstract": "Normalised Difference Chlorophyll Index - a derived index that correlates well with the existence of chlorophyll",
                        "index_function": lambda data: (data["nbart_red_edge_1"] - data["nbart_red"]) / (data["nbart_red_edge_1"] + data["nbart_red"]).where(((data["nbart_green"] - data["nbart_swir_3"]) / (data["nbart_green"] + data["nbart_swir_3"])) > 0.1),
                        "needed_bands": ["nbart_red_edge_1", "nbart_red", "nbart_green", "nbart_swir_3"],
                        "color_ramp": [
                            {
                                "value": -0.1,
                                "color": "#1696FF",
                                "legend": {
                                    "prefix": "<"
                                }
                            },
                            {
                                "value": -0.1,
                                "color": "#1696FF"
                            },
                            {
                                "value": 0.0,
                                "color": "#00FFDF",
                                "legend": {}
                            },
                            {
                                "value": 0.1,
                                "color": "#FFF50E",
                            },
                            {
                                "value": 0.2,
                                "color": "#FFB50A",
                                "legend": {}
                            },
                            {
                                "value": 0.4,
                                "color": "#FF530D",
                            },
                            {
                                "value": 0.5,
                                "color": "#FF0000",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ]
                    },
                    {
                        "name": "aerosol",
                        "title": "Narrow Blue - 440",
                        "abstract": "Coastal Aerosol or Narrow Blue band, approximately 435nm to 450nm",
                        "components": {
                            "red": {
                                "nbart_coastal_aerosol": 1.0
                            },
                            "green": {
                                "nbart_coastal_aerosol": 1.0
                            },
                            "blue": {
                                "nbart_coastal_aerosol": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "blue",
                        "title": "Blue - 490",
                        "abstract": "Blue band, approximately 453nm to 511nm",
                        "components": {
                            "red": {
                                "nbart_blue": 1.0
                            },
                            "green": {
                                "nbart_blue": 1.0
                            },
                            "blue": {
                                "nbart_blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "green",
                        "title": "Green - 560",
                        "abstract": "Green band, approximately 534nm to 588nm",
                        "components": {
                            "red": {
                                "nbart_green": 1.0
                            },
                            "green": {
                                "nbart_green": 1.0
                            },
                            "blue": {
                                "nbart_green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red",
                        "title": "Red - 670",
                        "abstract": "Red band, roughly 637nm to 672nm",
                        "components": {
                            "red": {
                                "nbart_red": 1.0
                            },
                            "green": {
                                "nbart_red": 1.0
                            },
                            "blue": {
                                "nbart_red": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red_edge_1",
                        "title": "Vegetation Red Edge - 710",
                        "abstract": "Near infra-red band, centred on 710nm",
                        "components": {
                            "red": {
                                "nbart_red_edge_1": 1.0
                            },
                            "green": {
                                "nbart_red_edge_1": 1.0
                            },
                            "blue": {
                                "nbart_red_edge_1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red_edge_2",
                        "title": "Vegetation Red Edge - 740",
                        "abstract": "Near infra-red band, centred on 740nm",
                        "components": {
                            "red": {
                                "nbart_red_edge_2": 1.0
                            },
                            "green": {
                                "nbart_red_edge_2": 1.0
                            },
                            "blue": {
                                "nbart_red_edge_2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red_edge_3",
                        "title": "Vegetation Red Edge - 780",
                        "abstract": "Near infra-red band, centred on 780nm",
                        "components": {
                            "red": {
                                "nbart_red_edge_3": 1.0
                            },
                            "green": {
                                "nbart_red_edge_3": 1.0
                            },
                            "blue": {
                                "nbart_red_edge_3": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "nir",
                        "title": "Near Infrared (NIR) - 840",
                        "abstract": "Near infra-red band, roughly 853nm to 876nm",
                        "components": {
                            "red": {
                                "nbart_nir_1": 1.0
                            },
                            "green": {
                                "nbart_nir_1": 1.0
                            },
                            "blue": {
                                "nbart_nir_1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "narrow_nir",
                        "title": "Narrow Near Infrared - 870",
                        "abstract": "Near infra-red band, centred on 865nm",
                        "components": {
                            "red": {
                                "nbart_nir_2": 1.0
                            },
                            "green": {
                                "nbart_nir_2": 1.0
                            },
                            "blue": {
                                "nbart_nir_2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir1",
                        "title": "Shortwave Infrared (SWIR) - 1610",
                        "abstract": "Short wave infra-red band 1, roughly 1575nm to 1647nm",
                        "components": {
                            "red": {
                                "nbart_swir_2": 1.0
                            },
                            "green": {
                                "nbart_swir_2": 1.0
                            },
                            "blue": {
                                "nbart_swir_2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir2",
                        "title": "Shortwave Infrared (SWIR) - 2190",
                        "abstract": "Short wave infra-red band 2, roughly 2117nm to 2285nm",
                        "components": {
                            "red": {
                                "nbart_swir_3": 1.0
                            },
                            "green": {
                                "nbart_swir_3": 1.0
                            },
                            "blue": {
                                "nbart_swir_3": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
        ],
    }
]
