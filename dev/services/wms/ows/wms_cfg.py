# Static config for the wms metadata.
response_cfg = {
    "Access-Control-Allow-Origin": "*",  # CORS header
}

service_cfg = {
    ## Which web service(s) should be supported by this instance
    "wcs": True,
    "wms": True,
    "wmts": True,

    ## Required config for WMS and/or WCS
    # Service title - appears e.g. in Terria catalog
    "title": "Digital Earth Australia - OGC Web Services",
    # Service URL.  Should a fully qualified URL
    "url": [
        "https://ows.services.dea.ga.gov.au",
        "https://ows.services.devkube.dea.ga.gov.au",
        "https://nrt.services.dea.ga.gov.au",
        "https://geomedian.services.dea.ga.gov.au",
        "https://geomedianau.dea.ga.gov.au",
        "https://geomedian.dea.ga.gov.au",
        "https://nrt.dea.ga.gov.au",
        "https://nrt-au.dea.ga.gov.au"],
    "human_url": "dea.ga.gov.au/",
    "s3_url": "https://data.dea.ga.gov.au",
    "s3_bucket": "dea-public-data",
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

    ## Required config for WCS
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

    ## Optional config for instances supporting WMS
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
    # Layer Config is a list of platform configs
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "Geomedian_AU_NBART",
        "title": "Surface Reflectance",
        "abstract": "",

        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
            # Included as a keyword  for the layer
                "label": "Landsat 8",
                # Included as a keyword  for the layer
                "type": "Annual Geomedian",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "abstract": """
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 8: 2013 to 2017;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374

For service status information, see https://status.dea.ga.gov.au""",
                "name": "ls8_nbart_geomedian_annual",
                # The Datacube name for the associated data product
                "product_name": "ls8_nbart_geomedian_annual",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "ls8_level1_usgs",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_manual_data_merge": True,
                # "data_manual_merge": True,
                # "pq_band": "quality",
                # "always_fetch_bands": [ "quality" ],
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],
               
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [ ],
                "apply_solar_corrections": False,
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi"]
                },
                "wcs_default_bands": ["red", "green", "blue"],
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

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
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
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
                    },
                    #
                    # Examples of non-linear heat-mapped styles.
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
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
                        "name": "ndwi",
                        "title": "NDWI - Green, SWIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (data["swir1"] + data["green"]),
                        "needed_bands": ["green", "swir1"],
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
                        "name": "blue",
                        "title": "Blue - 480",
                        "abstract": "Blue band, centered on 480nm",
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
                    },
                    {
                        "name": "green",
                        "title": "Green - 560",
                        "abstract": "Green band, centered on 560nm",
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
                    },
                    {
                        "name": "red",
                        "title": "Red - 660",
                        "abstract": "Red band, centered on 660nm",
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
                    },
                    {
                        "name": "nir",
                        "title": "Near Infrared (NIR) - 870",
                        "abstract": "Near infra-red band, centered on 870nm",
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
                    },
                    {
                        "name": "swir1",
                        "title": "Shortwave Infrared (SWIR) - 1610",
                        "abstract": "Short wave infra-red band 1, centered on 1610nm",
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
                    },
                    {
                        "name": "swir2",
                        "title": "Shortwave Infrared (SWIR) - 2200",
                        "abstract": "Short wave infra-red band 2, centered on 2200nm",
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
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
            {
                # Included as a keyword  for the layer
                "label": "Landsat 7",
                # Included as a keyword  for the layer
                "type": "Annual Geomedian",
                # Included as a keyword  for the layer
                "variant": "25m",
                "abstract": """
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 7: 2000 to 2017;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374

For service status information, see https://status.dea.ga.gov.au""",
                # The WMS name for the layer
                "name": "ls7_nbart_geomedian_annual",
                # The Datacube name for the associated data product
                "product_name": "ls7_nbart_geomedian_annual",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "ls8_level1_usgs",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_manual_data_merge": True,
                # "data_manual_merge": True,
                # "pq_band": "quality",
                # "always_fetch_bands": [ "quality" ],
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],

                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi"]
                },
                "wcs_default_bands": ["red", "green", "blue"],
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

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
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
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
                    },
                    #
                    # Examples of non-linear heat-mapped styles.
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
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
                        "name": "ndwi",
                        "title": "NDWI - Green, SWIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (data["swir1"] + data["green"]),
                        "needed_bands": ["green", "swir1"],
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
                        "name": "blue",
                        "title": "Blue - 490",
                        "abstract": "Blue band, centered on 490nm",
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
                    },
                    {
                        "name": "green",
                        "title": "Green - 560",
                        "abstract": "Green band, centered on 560nm",
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
                    },
                    {
                        "name": "red",
                        "title": "Red - 660",
                        "abstract": "Red band, centered on 660nm",
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
                    },
                    {
                        "name": "nir",
                        "title": "Near Infrared (NIR) - 840",
                        "abstract": "Near infra-red band, centered on 840nm",
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
                    },
                    {
                        "name": "swir1",
                        "title": "Shortwave Infrared (SWIR) - 1650",
                        "abstract": "Short wave infra-red band 1, centered on 1650nm",
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
                    },
                    {
                        "name": "swir2",
                        "title": "Shortwave Infrared (SWIR) - 2220",
                        "abstract": "Short wave infra-red band 2, centered on 2220nm",
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
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
            {
                # Included as a keyword  for the layer
                "label": "Landsat 5",
                # Included as a keyword  for the layer
                "type": "Annual Geomedian",
                # Included as a keyword  for the layer
                "variant": "25m",
                "abstract": """
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 5: 1988 to 1999, 2004 to 2007, 2009 to 2011; 

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374

For service status information, see https://status.dea.ga.gov.au""",
                # The WMS name for the layer
                "name": "ls5_nbart_geomedian_annual",
                # The Datacube name for the associated data product
                "product_name": "ls5_nbart_geomedian_annual",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "ls8_level1_usgs",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_manual_data_merge": True,
                # "data_manual_merge": True,
                # "pq_band": "quality",
                # "always_fetch_bands": [ "quality" ],
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],

                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi"]
                },
                "wcs_default_bands": ["red", "green", "blue"],
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

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
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
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
                    },
                    #
                    # Examples of non-linear heat-mapped styles.
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
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
                        "name": "ndwi",
                        "title": "NDWI - Green, SWIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (data["swir1"] + data["green"]),
                        "needed_bands": ["green", "swir1"],
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
                        "name": "blue",
                        "title": "Blue - 490",
                        "abstract": "Blue band, centered on 490nm",
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
                    },
                    {
                        "name": "green",
                        "title": "Green - 560",
                        "abstract": "Green band, centered on 560nm",
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
                    },
                    {
                        "name": "red",
                        "title": "Red - 660",
                        "abstract": "Red band, centered on 660nm",
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
                    },
                    {
                        "name": "nir",
                        "title": "Near Infrared (NIR) - 840",
                        "abstract": "Near infra-red band, centered on 840nm",
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
                    },
                    {
                        "name": "swir1",
                        "title": "Shortwave Infrared (SWIR) - 1650",
                        "abstract": "Short wave infra-red band 1, centered on 1650nm",
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
                    },
                    {
                        "name": "swir2",
                        "title": "Shortwave Infrared (SWIR) - 2220",
                        "abstract": "Short wave infra-red band 2, centered on 2220nm",
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
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            }
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "landsat8_barest_earth",
        "title": "Barest Earth",
        "abstract": """
A `weighted geometric median’ approach has been used to estimate the median surface reflectance of the barest state (i.e., least vegetation) observed through Landsat-8 OLI observations from 2013 to September 2018 to generate a six-band Landsat-8 Barest Earth pixel composite mosaic over the Australian continent.

The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The weighted median approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.

Reference: Dale Roberts, John Wilford, and Omar Ghattas (2018). Revealing the Australian Continent at its Barest, submitted.

Mosaics are available for the following years:
    Landsat 8: 2013 to 2017;
    """,
        # Link removed until eCat record is "published_external", not "published_internal"
        # For more information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/122573

        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "Landsat 8",
                # Included as a keyword  for the layer
                "type": "Barest Earth",
                # Included as a keyword  for the layer
                "variant": "25m",
                "abstract": """
A `weighted geometric median’ approach has been used to estimate the median surface reflectance of the barest state (i.e., least vegetation) observed through Landsat-8 OLI observations from 2013 to September 2018 to generate a six-band Landsat-8 Barest Earth pixel composite mosaic over the Australian continent.

The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The weighted median approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.

Reference: Dale Roberts, John Wilford, and Omar Ghattas (2018). Revealing the Australian Continent at its Barest, submitted.

Mosaics are available for the following years:
    Landsat 8: 2013 to 2017;

For service status information, see https://status.dea.ga.gov.au""",
                # Link removed until eCat record is "published_external", not "published_internal"
                # For more information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/122573

                # The WMS name for the layer
                "name": "ls8_barest_earth_mosaic",
                # The Datacube name for the associated data product
                "product_name": "ls8_barest_earth_albers",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 35.0,
                #"max_datasets_wms": 1000,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi"]
                },
                "wcs_default_bands": ["red", "green", "blue"],
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
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
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
                    },
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
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
                        "name": "blue",
                        "title": "Blue - 480",
                        "abstract": "Blue band, centered on 480nm",
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
                    },
                    {
                        "name": "green",
                        "title": "Green - 560",
                        "abstract": "Green band, centered on 560nm",
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
                    },
                    {
                        "name": "red",
                        "title": "Red - 660",
                        "abstract": "Red band, centered on 660nm",
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
                    },
                    {
                        "name": "nir",
                        "title": "Near Infrared (NIR) - 870",
                        "abstract": "Near infra-red band, centered on 870nm",
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
                    },
                    {
                        "name": "swir1",
                        "title": "Shortwave Infrared (SWIR) - 1610",
                        "abstract": "Short wave infra-red band 1, centered on 1610nm",
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
                    },
                    {
                        "name": "swir2",
                        "title": "Shortwave Infrared (SWIR) - 2200",
                        "abstract": "Short wave infra-red band 2, centered on 2200nm",
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
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",

            }
        ]
    },
    {
        "name": "mangrove_cover",
        "title": "Mangrove Canopy Cover",
        "abstract": "",
        "products": [
            {
                "label": "Mangrove Canopy Cover",
                "abstract": """
Mangrove canopy cover version 1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.

The mangrove canopy cover product provides valuable information about the extent and canopy density of mangroves for each year between 1987 and 2016 for the entire Australian coastline.
The canopy cover classes are:
20-50% (pale green), 50-80% (mid green), 80-100% (dark green).

The product consists of  a sequence (one per year) of 25 meter resolution maps that are generated by analysing the Landsat fractional cover (https://doi.org/10.6084/m9.figshare.94250.v1) developed by the Joint Remote Sensing Research Program and the Global Mangrove Watch layers (https://doi.org/10.1071/MF13177) developed by the Japanese Aerospace Exploration Agency.

The mangrove canopy cover version 1 product has the following caveats:
it underestimates the overall extent of mangroves.
it doesn’t detect small mangrove communities i.e. smaller estuaries in NSW and Victoria
that there is localised confusion between mangroves and wooded freshwater wetlands i.e. Melaleuca swamps, and
in some locations dense dwarf/shrub mangroves that are less than 2 metres tall may be mis-labelled as woodland/open forest/closed forest.

For service status information, see https://status.dea.ga.gov.au""",
                "type": "100km tile",
                "variant": "25m",
                "name": "mangrove_cover",
                "product_name": "mangrove_cover_test",
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data["extent"] == 1,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": ["extent"],
                "apply_solar_corrections": False,
                "legend": {
                    "styles": ["mangrove"]
                },
                "wcs_default_bands": ["canopy_cover_class", "extent"],
                "styles": [
                    {
                        "name": "mangrove",
                        "title": "Mangrove Cover",
                        "abstract": "",
                        "value_map": {
                            "canopy_cover_class": [
                                {
                                    "title": "Woodland",
                                    "abstract": "(20% - 50% cover)",
                                    "flags": {
                                        "woodland": True
                                    },
                                    "color": "#9FFF4C"
                                },
                                {
                                    "title": "Open Forest",
                                    "abstract": "(50% - 80% cover)",
                                    "flags": {
                                        "open_forest": True
                                    },
                                    "color": "#5ECC00"
                                },
                                {
                                    "title": "Closed Forest",
                                    "abstract": "(>80% cover)",
                                    "flags": {
                                        "closed_forest": True
                                    },
                                    "color": "#3B7F00"
                                },
                            ]
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "mangrove",
            },
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "WOfS",
        "title": "Water Observations from Space",
        "abstract": "WOfS",

        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "WOfS Filtered Statistics",
                # Included as a keyword  for the layer
                "type": "Filtered Water Summary",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_filtered_summary",
                # The Datacube name for the associated data product
                "product_name": "wofs_filtered_summary",
                
                "abstract": """
Water Observations from Space (WOfS) Filtered Statistics helps provide the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. WOfS Filtered Statistics consists of a Confidence layer that compares the WOfS Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the WOfS Statistics water summary where Confidence is low. 

This layer is Filtered Water Summary: A simplified version of the Water Summary, showing the frequency of water observations where the Confidence is above a cutoff level.  No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

The Filtered Water Summary layer is a noise-reduced view of surface water across Australia. Even though confidence filtering is applied to the Filtered Water Summary, some cloud and shadow, and sensor noise does persist. 

For more information please see: https://data.dea.ga.gov.au/?prefix=WOfS/filtered_summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au""",

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
                "legend": {
                    # "url": ""
                    "styles": [
                        "WOfS_filtered_frequency",
                        "WOfS_filtered_frequency_blues_transparent"]
                },
                "wcs_default_bands": ["wofs_filtered_summary"],
                "styles": [
                    {
                        "name": "WOfS_filtered_frequency",
                        "title": "Filtered Water Summary",
                        "abstract": "WOfS filtered summary showing the frequency of Wetness",
                        "needed_bands": ["wofs_filtered_summary"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.002,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.005,
                                "color": "#8e0101",
                                "alpha": 0.25
                            },
                            {
                                "value": 0.01,
                                "color": "#cf2200",
                                "alpha": 0.75
                            },
                            {
                                "value": 0.02,
                                "color": "#e38400"
                            },
                            {
                                "value": 0.05,
                                "color": "#e3df00"
                            },
                            {
                                "value": 0.1,
                                "color": "#a6e300"
                            },
                            {
                                "value": 0.2,
                                "color": "#62e300"
                            },
                            {
                                "value": 0.3,
                                "color": "#00e32d"
                            },
                            {
                                "value": 0.4,
                                "color": "#00e384"
                            },
                            {
                                "value": 0.5,
                                "color": "#00e3c8"
                            },
                            {
                                "value": 0.6,
                                "color": "#00c5e3"
                            },
                            {
                                "value": 0.7,
                                "color": "#0097e3"
                            },
                            {
                                "value": 0.8,
                                "color": "#005fe3"
                            },
                            {
                                "value": 0.9,
                                "color": "#000fe3"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                    {
                        "name": "WOfS_filtered_frequency_blues_transparent",
                        "title": "Water Summary (Blue)",
                        "abstract": "WOfS filtered summary showing the frequency of Wetness",
                        "needed_bands": ["wofs_filtered_summary"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#ffffff",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.001,
                                "color": "#d5fef9",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.02,
                                "color": "#d5fef9",
                            },
                            {
                                "value": 0.2,
                                "color": "#71e3ff"
                            },
                            {
                                "value": 0.4,
                                "color": "#01ccff"
                            },
                            {
                                "value": 0.6,
                                "color": "#0178ff"
                            },
                            {
                                "value": 0.8,
                                "color": "#2701ff"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "WOfS_filtered_frequency",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Statistics",
                # Included as a keyword  for the layer
                "type": "Wet Count",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_summary_wet",
                # The Datacube name for the associated data product
                "product_name": "wofs_summary",
                "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products which help the understanding of surface water across Australia.  The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. 

This layer contains Wet Count: how many times water was detected in observations that were clear. No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary. 

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["water_observations"]
                },
                "wcs_default_bands": ["count_wet"],
                "styles": [
                    {
                        "name": "water_observations",
                        "title": "Wet Count",
                        "abstract": "WOfS summary showing the count of water observations",
                        "needed_bands": ["count_wet"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#666666",
                                "alpha": 0
                            },
                            {
                                "value": 2,
                                "color": "#890000"
                            },
                            {
                                "value": 5,
                                "color": "#990000"
                            },
                            {
                                "value": 10,
                                "color": "#E38400"
                            },
                            {
                                "value": 25,
                                "color": "#E3DF00"
                            },
                            {
                                "value": 50,
                                "color": "#A6E300"
                            },
                            {
                                "value": 100,
                                "color": "#00E32D"
                            },
                            {
                                "value": 150,
                                "color": "#00E3C8"
                            },
                            {
                                "value": 200,
                                "color": "#0097E3"
                            },
                            {
                                "value": 250,
                                "color": "#005FE3"
                            },
                            {
                                "value": 300,
                                "color": "#000FE3"
                            },
                            {
                                "value": 350,
                                "color": "#000EA9"
                            },
                            {
                                "value": 400,
                                "color": "#5700E3",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 100
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "water_observations",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Statistics",
                # Included as a keyword  for the layer
                "type": "Clear Count",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_summary_clear",
                # The Datacube name for the associated data product
                "product_name": "wofs_summary",
                "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products which help the understanding of surface water across Australia.  The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. 

This layer contains Clear Count: how many times an area could be clearly seen (ie. not affected by clouds, shadows or other satellite observation problems). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary. 

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["clear_observations"]
                },
                "wcs_default_bands": ["count_clear"],
                "styles": [
                    {
                        "name": "clear_observations",
                        "title": "Clear Count",
                        "abstract": "WOfS summary showing the count of clear observations",
                        "needed_bands": ["count_clear"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#FFFFFF",
                                "alpha": 0
                            },
                            {
                                # purely for legend display
                                # we should not get fractional
                                # values in this styles
                                "value": 10,
                                "color": "#b21800",
                                "alpha": 1
                            },
                            {
                                "value": 100,
                                "color": "#ef8500"
                            },
                            {
                                "value": 200,
                                "color": "#ffb800"
                            },
                            {
                                "value": 300,
                                "color": "#ffd300"
                            },
                            {
                                "value": 400,
                                "color": "#ffe300"
                            },
                            {
                                "value": 500,
                                "color": "#fff300"
                            },
                            {
                                "value": 600,
                                "color": "#d0f800"
                            },
                            {
                                "value": 700,
                                "color": "#a0fd00"
                            },
                            {
                                "value": 800,
                                "color": "#6ee100"
                            },
                            {
                                "value": 901,
                                "color": "#39a500"
                            },
                            {
                                "value": 1000,
                                "color": "#026900",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 100,
                            "axes_position": [0.05, 0.5, 0.89, 0.15]
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "clear_observations",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Statistics",
                # Included as a keyword  for the layer
                "type": "Water Summary",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "Water Observations from Space Statistics",
                # The Datacube name for the associated data product
                "product_name": "wofs_summary",
                "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product which combines WOfS observations into summary products that help the understanding of surface water across Australia. WOfS Statistics is calculated from the full depth time series (1986 – 2018). The water detected for each location is summed through time and then compared to the number of clear observations of that location. The result is a percentage value of the number of times water was observed at the location. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time (water summary). 

This layer contains the Water Summary: the percentage of clear observations which were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary. 

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["WOfS_frequency", "WOfS_frequency_blues_transparent"]
                },
                "wcs_default_bands": ["frequency"],
                "styles": [
                    {
                        "name": "WOfS_frequency",
                        "title": " Water Summary",
                        "abstract": "WOfS summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.002,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.005,
                                "color": "#8e0101",
                                "alpha": 0.25
                            },
                            {
                                "value": 0.01,
                                "color": "#cf2200",
                                "alpha": 0.75
                            },
                            {
                                "value": 0.02,
                                "color": "#e38400"
                            },
                            {
                                "value": 0.05,
                                "color": "#e3df00"
                            },
                            {
                                "value": 0.1,
                                "color": "#a6e300"
                            },
                            {
                                "value": 0.2,
                                "color": "#62e300"
                            },
                            {
                                "value": 0.3,
                                "color": "#00e32d"
                            },
                            {
                                "value": 0.4,
                                "color": "#00e384"
                            },
                            {
                                "value": 0.5,
                                "color": "#00e3c8"
                            },
                            {
                                "value": 0.6,
                                "color": "#00c5e3"
                            },
                            {
                                "value": 0.7,
                                "color": "#0097e3"
                            },
                            {
                                "value": 0.8,
                                "color": "#005fe3"
                            },
                            {
                                "value": 0.9,
                                "color": "#000fe3"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                    {
                        "name": "WOfS_frequency_blues_transparent",
                        "title": "Water Summary (Blue)",
                        "abstract": "WOfS summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#ffffff",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.001,
                                "color": "#d5fef9",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.02,
                                "color": "#d5fef9",
                            },
                            {
                                "value": 0.2,
                                "color": "#71e3ff"
                            },
                            {
                                "value": 0.4,
                                "color": "#01ccff"
                            },
                            {
                                "value": 0.6,
                                "color": "#0178ff"
                            },
                            {
                                "value": 0.8,
                                "color": "#2701ff"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "WOfS_frequency",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Filtered Statistics",
                # Included as a keyword  for the layer
                "type": "Confidence",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_filtered_summary_confidence",
                # The Datacube name for the associated data product
                "product_name": "wofs_filtered_summary",
                
                "abstract": """
Water Observations from Space (WOfS) Filtered Statistics helps provide the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out. WOfS Filtered Statistics consists of a Confidence layer that compares the WOfS Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the WOfS Statistics water summary where Confidence is low.
 
This layer is Confidence: the degree of agreement between water shown in the Water Summary and other national datasets. Areas where there is less than 1% confidence appears black, areas with confidence for between 1% 10% confidence are styled between black and red, areas with 25% confidence are styled yellow, areas with 75% confidence and above correspond to green.

The Confidence layer provides understanding of whether the water shown in the Water Summary agrees with where water should exist in the landscape, such as due to sloping land or whether water has been detected in a location by other means. 

For more information please see: https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au""",

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
                "legend": {
                    # "url": ""
                    "styles": ["wofs_confidence"]
                },
                "wcs_default_bands": ["confidence"],
                "styles": [
                    {
                        "name": "wofs_confidence",
                        "title": "Confidence",
                        "abstract": "WOfS Confidence",
                        "needed_bands": ["confidence"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#000000",
                            },
                            {
                                "value": 0.01,
                                "color": "#000000"
                            },
                            {
                                "value": 0.02,
                                "color": "#990000"
                            },
                            {
                                "value": 0.05,
                                "color": "#CF2200"
                            },
                            {
                                "value": 0.1,
                                "color": "#E38400"
                            },
                            {
                                "value": 0.25,
                                "color": "#E3DF00"
                            },
                            {
                                "value": 0.5,
                                "color": "#A6E300"
                            },
                            {
                                "value": 0.75,
                                "color": "#62E300"
                            },
                            {
                                "value": 1.0,
                                "color": "#00E32D"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.25
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "wofs_confidence",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Annual Statistics",
                # Included as a keyword  for the layer
                "type": "Wet Count",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_annual_summary_wet",
                # The Datacube name for the associated data product
                "product_name": "wofs_annual_summary",
                "abstract": """
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.
For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["annual_water_observations"]
                },
                "wcs_default_bands": ["count_wet"],
                "styles": [
                    {
                        "name": "annual_water_observations",
                        "title": "Wet Count",
                        "abstract": "WOfS annual summary showing the count of water observations",
                        "needed_bands": ["count_wet"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#666666",
                                "alpha": 0
                            },
                            {
                                # purely for legend display
                                # we should not get fractional
                                # values in this styles
                                "value": 0.2,
                                "color": "#990000",
                                "alpha": 1
                            },
                            {
                                "value": 2,
                                "color": "#990000"
                            },
                            {
                                "value": 4,
                                "color": "#E38400"
                            },
                            {
                                "value": 6,
                                "color": "#E3DF00"
                            },
                            {
                                "value": 8,
                                "color": "#00E32D"
                            },
                            {
                                "value": 10,
                                "color": "#00E3C8"
                            },
                            {
                                "value": 12,
                                "color": "#0097E3"
                            },
                            {
                                "value": 14,
                                "color": "#005FE3"
                            },
                            {
                                "value": 16,
                                "color": "#000FE3"
                            },
                            {
                                "value": 18,
                                "color": "#000EA9"
                            },
                            {
                                "value": 20,
                                "color": "#5700E3",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 10
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "annual_water_observations",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Annual Statistics",
                # Included as a keyword  for the layer
                "type": "Clear Count",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_annual_summary_clear",
                # The Datacube name for the associated data product
                "product_name": "wofs_annual_summary",
                "abstract": """                
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green.
For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["annual_clear_observations"]
                },
                "wcs_default_bands": ["count_clear"],
                "styles": [
                    {
                        "name": "annual_clear_observations",
                        "title": "Clear Count",
                        "abstract": "WOfS annual summary showing the count of clear observations",
                        "needed_bands": ["count_clear"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#FFFFFF",
                                "alpha": 0
                            },
                            {
                                # purely for legend display
                                # we should not get fractional
                                # values in this styles
                                "value": 0.2,
                                "color": "#B21800",
                                "alpha": 1
                            },
                            {
                                "value": 1,
                                "color": "#B21800"
                            },
                            {
                                "value": 4,
                                "color": "#ef8500"
                            },
                            {
                                "value": 8,
                                "color": "#ffb800"
                            },
                            {
                                "value": 10,
                                "color": "#ffd000"
                            },
                            {
                                "value": 13,
                                "color": "#fff300"
                            },
                            {
                                "value": 16,
                                "color": "#fff300"
                            },
                            {
                                "value": 20,
                                "color": "#c1ec00"
                            },
                            {
                                "value": 24,
                                "color": "#6ee100"
                            },
                            {
                                "value": 28,
                                "color": "#39a500"
                            },
                            {
                                "value": 30,
                                "color": "#026900",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 10,
                            "axes_position": [0.05, 0.5, 0.89, 0.15]
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "annual_clear_observations",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Annual Statistics",
                # Included as a keyword  for the layer
                "type": "Water Summary",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_annual_summary_statistics",
                # The Datacube name for the associated data product
                "product_name": "wofs_annual_summary",
                "abstract": """
Water Observations from Space - Annual Statistics is a set of annual statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Annual Statistics, a set of annual statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.
For more information please see: https://data.dea.ga.gov.au/WOfS/annual_summary/v2.1.5/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["annual_WOfS_frequency",
                               "annual_WOfS_frequency_blues_transparent"]
                },
                "wcs_default_bands": ["frequency"],
                "styles": [
                    {
                        "name": "annual_WOfS_frequency",
                        "title": " Water Summary",
                        "abstract": "WOfS annual summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.02,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.05,
                                "color": "#8e0101",
                                "alpha": 0.25
                            },
                            {
                                "value": 0.1,
                                "color": "#cf2200",
                                "alpha": 0.75
                            },
                            {
                                "value": 0.2,
                                "color": "#e38400"
                            },
                            {
                                "value": 0.3,
                                "color": "#e3df00"
                            },
                            {
                                "value": 0.4,
                                "color": "#62e300"
                            },
                            {
                                "value": 0.5,
                                "color": "#00e32d"
                            },
                            {
                                "value": 0.6,
                                "color": "#00e3c8"
                            },
                            {
                                "value": 0.7,
                                "color": "#0097e3"
                            },
                            {
                                "value": 0.8,
                                "color": "#005fe3"
                            },
                            {
                                "value": 0.9,
                                "color": "#000fe3"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                    {
                        "name": "annual_WOfS_frequency_blues_transparent",
                        "title": "Water Summary (Blue)",
                        "abstract": "WOfS annual summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#ffffff",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.001,
                                "color": "#d5fef9",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.02,
                                "color": "#d5fef9",
                            },
                            {
                                "value": 0.2,
                                "color": "#71e3ff"
                            },
                            {
                                "value": 0.4,
                                "color": "#01ccff"
                            },
                            {
                                "value": 0.6,
                                "color": "#0178ff"
                            },
                            {
                                "value": 0.8,
                                "color": "#2701ff"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "annual_WOfS_frequency",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS April - October Statistics",
                # Included as a keyword  for the layer
                "type": "Wet Count",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_apr_oct_summary_wet",
                # The Datacube name for the associated data product
                "product_name": "wofs_apr_oct_summary",
                "abstract": """
Water Observations from Space - April to October Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["seasonal_water_observations"]
                },
                "wcs_default_bands": ["count_wet"],
                "styles": [
                    {
                        "name": "seasonal_water_observations",
                        "title": "Wet Count",
                        "abstract": "WOfS seasonal summary showing the count of water observations",
                        "needed_bands": ["count_wet"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#666666",
                                "alpha": 0
                            },
                            {
                                # purely for legend display
                                # we should not get fractional
                                # values in this styles
                                "value": 0.2,
                                "color": "#990000",
                                "alpha": 1
                            },
                            {
                                "value": 2,
                                "color": "#990000"
                            },
                            {
                                "value": 4,
                                "color": "#E38400"
                            },
                            {
                                "value": 6,
                                "color": "#E3DF00"
                            },
                            {
                                "value": 8,
                                "color": "#00E32D"
                            },
                            {
                                "value": 10,
                                "color": "#00E3C8"
                            },
                            {
                                "value": 12,
                                "color": "#0097E3"
                            },
                            {
                                "value": 14,
                                "color": "#005FE3"
                            },
                            {
                                "value": 16,
                                "color": "#000FE3"
                            },
                            {
                                "value": 18,
                                "color": "#000EA9"
                            },
                            {
                                "value": 20,
                                "color": "#5700E3",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 10
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "seasonal_water_observations",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS April - October Summary Statistics",
                # Included as a keyword  for the layer
                "type": "Clear Count",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_apr_oct_summary_clear",
                # The Datacube name for the associated data product
                "product_name": "wofs_apr_oct_summary",
                "abstract": """                
Water Observations from Space - April to October Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green.

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["seasonal_clear_observations"]
                },
                "wcs_default_bands": ["count_clear"],
                "styles": [
                    {
                        "name": "seasonal_clear_observations",
                        "title": "Clear Count",
                        "abstract": "WOfS seasonal summary showing the count of clear observations",
                        "needed_bands": ["count_clear"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#FFFFFF",
                                "alpha": 0
                            },
                            {
                                # purely for legend display
                                # we should not get fractional
                                # values in this styles
                                "value": 0.2,
                                "color": "#B21800",
                                "alpha": 1
                            },
                            {
                                "value": 1,
                                "color": "#B21800"
                            },
                            {
                                "value": 4,
                                "color": "#ef8500"
                            },
                            {
                                "value": 8,
                                "color": "#ffb800"
                            },
                            {
                                "value": 10,
                                "color": "#ffd000"
                            },
                            {
                                "value": 13,
                                "color": "#fff300"
                            },
                            {
                                "value": 16,
                                "color": "#fff300"
                            },
                            {
                                "value": 20,
                                "color": "#c1ec00"
                            },
                            {
                                "value": 24,
                                "color": "#6ee100"
                            },
                            {
                                "value": 28,
                                "color": "#39a500"
                            },
                            {
                                "value": 30,
                                "color": "#026900",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 10,
                            "axes_position": [0.05, 0.5, 0.89, 0.15]
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "seasonal_clear_observations",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS April - October Statistics",
                # Included as a keyword  for the layer
                "type": "Water Summary",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_apr_oct_summary_statistics",
                # The Datacube name for the associated data product
                "product_name": "wofs_apr_oct_summary",
                "abstract": """
Water Observations from Space - Seasonal Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["seasonal_WOfS_frequency",
                               "seasonal_WOfS_frequency_blues_transparent"]
                },
                "wcs_default_bands": ["frequency"],
                "styles": [
                    {
                        "name": "seasonal_WOfS_frequency",
                        "title": " Water Summary",
                        "abstract": "WOfS seasonal summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.02,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.05,
                                "color": "#8e0101",
                                "alpha": 0.25
                            },
                            {
                                "value": 0.1,
                                "color": "#cf2200",
                                "alpha": 0.75
                            },
                            {
                                "value": 0.2,
                                "color": "#e38400"
                            },
                            {
                                "value": 0.3,
                                "color": "#e3df00"
                            },
                            {
                                "value": 0.4,
                                "color": "#62e300"
                            },
                            {
                                "value": 0.5,
                                "color": "#00e32d"
                            },
                            {
                                "value": 0.6,
                                "color": "#00e3c8"
                            },
                            {
                                "value": 0.7,
                                "color": "#0097e3"
                            },
                            {
                                "value": 0.8,
                                "color": "#005fe3"
                            },
                            {
                                "value": 0.9,
                                "color": "#000fe3"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                    {
                        "name": "seasonal_WOfS_frequency_blues_transparent",
                        "title": "Water Summary (Blue)",
                        "abstract": "WOfS seasonal summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#ffffff",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.001,
                                "color": "#d5fef9",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.02,
                                "color": "#d5fef9",
                            },
                            {
                                "value": 0.2,
                                "color": "#71e3ff"
                            },
                            {
                                "value": 0.4,
                                "color": "#01ccff"
                            },
                            {
                                "value": 0.6,
                                "color": "#0178ff"
                            },
                            {
                                "value": 0.8,
                                "color": "#2701ff"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "seasonal_WOfS_frequency",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS November - March Statistics",
                # Included as a keyword  for the layer
                "type": "Wet Count",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_nov_mar_summary_wet",
                # The Datacube name for the associated data product
                "product_name": "wofs_nov_mar_summary",
                "abstract": """
Water Observations from Space - November to March Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["seasonal_water_observations"]
                },
                "wcs_default_bands": ["count_wet"],
                "styles": [
                    {
                        "name": "seasonal_water_observations",
                        "title": "Wet Count",
                        "abstract": "WOfS seasonal summary showing the count of water observations",
                        "needed_bands": ["count_wet"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#666666",
                                "alpha": 0
                            },
                            {
                                # purely for legend display
                                # we should not get fractional
                                # values in this styles
                                "value": 0.2,
                                "color": "#990000",
                                "alpha": 1
                            },
                            {
                                "value": 2,
                                "color": "#990000"
                            },
                            {
                                "value": 4,
                                "color": "#E38400"
                            },
                            {
                                "value": 6,
                                "color": "#E3DF00"
                            },
                            {
                                "value": 8,
                                "color": "#00E32D"
                            },
                            {
                                "value": 10,
                                "color": "#00E3C8"
                            },
                            {
                                "value": 12,
                                "color": "#0097E3"
                            },
                            {
                                "value": 14,
                                "color": "#005FE3"
                            },
                            {
                                "value": 16,
                                "color": "#000FE3"
                            },
                            {
                                "value": 18,
                                "color": "#000EA9"
                            },
                            {
                                "value": 20,
                                "color": "#5700E3",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 10
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "seasonal_water_observations",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS November - March Summary Statistics",
                # Included as a keyword  for the layer
                "type": "Clear Count",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_nov_mar_summary_clear",
                # The Datacube name for the associated data product
                "product_name": "wofs_nov_mar_summary",
                "abstract": """                
Water Observations from Space - November to March Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green.

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["seasonal_clear_observations"]
                },
                "wcs_default_bands": ["count_clear"],
                "styles": [
                    {
                        "name": "seasonal_clear_observations",
                        "title": "Clear Count",
                        "abstract": "WOfS seasonal summary showing the count of clear observations",
                        "needed_bands": ["count_clear"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#FFFFFF",
                                "alpha": 0
                            },
                            {
                                # purely for legend display
                                # we should not get fractional
                                # values in this styles
                                "value": 0.2,
                                "color": "#B21800",
                                "alpha": 1
                            },
                            {
                                "value": 1,
                                "color": "#B21800"
                            },
                            {
                                "value": 4,
                                "color": "#ef8500"
                            },
                            {
                                "value": 8,
                                "color": "#ffb800"
                            },
                            {
                                "value": 10,
                                "color": "#ffd000"
                            },
                            {
                                "value": 13,
                                "color": "#fff300"
                            },
                            {
                                "value": 16,
                                "color": "#fff300"
                            },
                            {
                                "value": 20,
                                "color": "#c1ec00"
                            },
                            {
                                "value": 24,
                                "color": "#6ee100"
                            },
                            {
                                "value": 28,
                                "color": "#39a500"
                            },
                            {
                                "value": 30,
                                "color": "#026900",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 10,
                            "axes_position": [0.05, 0.5, 0.89, 0.15]
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "seasonal_clear_observations",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS November - March Statistics",
                # Included as a keyword  for the layer
                "type": "Water Summary",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_nov_mar_summary_statistics",
                # The Datacube name for the associated data product
                "product_name": "wofs_nov_mar_summary",
                "abstract": """
Water Observations from Space - Seasonal Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - November to March Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

For service status information, see https://status.dea.ga.gov.au""",
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
                "legend": {
                    # "url": ""
                    "styles": ["seasonal_WOfS_frequency",
                               "seasonal_WOfS_frequency_blues_transparent"]
                },
                "wcs_default_bands": ["frequency"],
                "styles": [
                    {
                        "name": "seasonal_WOfS_frequency",
                        "title": " Water Summary",
                        "abstract": "WOfS seasonal summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.02,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.05,
                                "color": "#8e0101",
                                "alpha": 0.25
                            },
                            {
                                "value": 0.1,
                                "color": "#cf2200",
                                "alpha": 0.75
                            },
                            {
                                "value": 0.2,
                                "color": "#e38400"
                            },
                            {
                                "value": 0.3,
                                "color": "#e3df00"
                            },
                            {
                                "value": 0.4,
                                "color": "#62e300"
                            },
                            {
                                "value": 0.5,
                                "color": "#00e32d"
                            },
                            {
                                "value": 0.6,
                                "color": "#00e3c8"
                            },
                            {
                                "value": 0.7,
                                "color": "#0097e3"
                            },
                            {
                                "value": 0.8,
                                "color": "#005fe3"
                            },
                            {
                                "value": 0.9,
                                "color": "#000fe3"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                    {
                        "name": "seasonal_WOfS_frequency_blues_transparent",
                        "title": "Water Summary (Blue)",
                        "abstract": "WOfS seasonal summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#ffffff",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.001,
                                "color": "#d5fef9",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.02,
                                "color": "#d5fef9",
                            },
                            {
                                "value": 0.2,
                                "color": "#71e3ff"
                            },
                            {
                                "value": 0.4,
                                "color": "#01ccff"
                            },
                            {
                                "value": 0.6,
                                "color": "#0178ff"
                            },
                            {
                                "value": 0.8,
                                "color": "#2701ff"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "seasonal_WOfS_frequency",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Daily Observations",
                # Included as a keyword  for the layer
                "type": "albers",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_albers",
                # The Datacube name for the associated data product
                "product_name": "wofs_albers",
                "abstract": """
Water Observations from Space (WOfS) provides surface water observations derived from satellite imagery for all of Australia. The current product (Version 2.1.5) includes observations taken from 1986 to the present, from the Landsat 5, 7 and 8 satellites. WOfS covers all of mainland Australia and Tasmania but excludes off-shore Territories.

The WOfS product allows users to get a better understanding of where water is normally present in a landscape, where water is seldom observed, and where inundation has occurred occasionally.

Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water. The details of the WOfS algorithm and derived statistics are available at http://dx.doi.org/10.1016/j.rse.2015.11.003.

For service status information, see https://status.dea.ga.gov.au""",
                #"pq_band": "water",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [200, 180, 180, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] & data[band].attrs['nodata']) == 0,
                # "pq_manual_merge": True,
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [
                    "nodata",
                    "noncontiguous",
                ],
                # Include UTC dates for GSKY lookup
                "feature_info_include_utc_dates": True,
                "data_manual_merge": False,
                "always_fetch_bands": [ ],
                "apply_solar_corrections": False,
                "fuse_func": "datacube_wms.wms_utils.wofls_fuser",
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "legend": {
                    "styles": ["observations"]
                },
                "wcs_default_bands": ["water"],
                "styles": [
                    {
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
                                          "terrain_or_low_angle": True,
                                          "cloud_shadow": True,
                                          "cloud": True,
                                          "high_slope": True,
                                          "noncontiguous": True
                                        }
                                    },
                                    "color": "#707070"
                                },
                                {
                                    # Possible Sea Glint, also mark as invalid
                                    "title": "",
                                    "abstract": "",
                                    "flags": {
                                        "dry": True,
                                        "sea": True
                                    },
                                    "color": "#707070"
                                },
                                {
                                    "title": "Dry",
                                    "abstract": "Dry",
                                    "flags": {
                                        "dry": True,
                                        "sea": False,
                                    },
                                    "color": "#D99694"
                                },
                                {
                                    "title": "Wet",
                                    "abstract": "Wet or Sea",
                                    "flags": {
                                      "or": {
                                        "wet": True,
                                        "sea": True
                                      }
                                    },
                                    "color": "#4F81BD"
                                }
                            ]
                        }
                    },
                    {
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
                                          "terrain_or_low_angle": True,
                                          "cloud_shadow": True,
                                          "cloud": True,
                                          "high_slope": True,
                                          "noncontiguous": True
                                        }
                                    },
                                    "color": "#707070",
                                    "mask": True
                                },
                                {
                                    # Possible Sea Glint, also mark as invalid
                                    "title": "",
                                    "abstract": "",
                                    "flags": {
                                        "dry": True,
                                        "sea": True
                                    },
                                    "color": "#707070",
                                    "mask": True
                                },
                                {
                                    "title": "Dry",
                                    "abstract": "Dry",
                                    "flags": {
                                        "dry": True,
                                        "sea": False,
                                    },
                                    "color": "#D99694",
                                    "mask": True
                                },
                                {
                                    "title": "Wet",
                                    "abstract": "Wet or Sea",
                                    "flags": {
                                      "or": {
                                        "wet": True,
                                        "sea": True
                                      }
                                    },
                                    "color": "#4F81BD"
                                }
                            ]
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

           
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "observations",
             }
        ],
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "Sentinel-2 NRT",
        "title": "Near Real-Time",
        "abstract": "This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. "
                    "The Near Real-Time capability provides analysis-ready data "
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
                "abstract":"""
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
                "product_name": ["s2a_nrt_granule", "s2b_nrt_granule"],
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
                                    "prefix" : "<"
                                }
                            },
                            {
                                "value": -0.1,
                                "color": "#1696FF"
                            },
                            {
                                "value": 0.0,
                                "color": "#00FFDF",
                                "legend": { }
                            },
                            {
                                "value": 0.1,
                                "color": "#FFF50E",
                            },
                            {
                                "value": 0.2,
                                "color": "#FFB50A",
                                "legend": { }
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
                "abstract":"""
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
                "name": "s2b_nrt_granule_nbar_t",
                # The Datacube name for the associated data product
                "product_name": "s2b_nrt_granule",
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
                                    "prefix" : "<"
                                }
                            },
                            {
                                "value": -0.1,
                                "color": "#1696FF"
                            },
                            {
                                "value": 0.0,
                                "color": "#00FFDF",
                                "legend": { }
                            },
                            {
                                "value": 0.1,
                                "color": "#FFF50E",
                            },
                            {
                                "value": 0.2,
                                "color": "#FFB50A",
                                "legend": { }
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
                "name": "s2a_nrt_granule_nbar_t",
                # The Datacube name for the associated data product
                "product_name": "s2a_nrt_granule",
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
                                    "prefix" : "<"
                                }
                            },
                            {
                                "value": -0.1,
                                "color": "#1696FF"
                            },
                            {
                                "value": 0.0,
                                "color": "#00FFDF",
                                "legend": { }
                            },
                            {
                                "value": 0.1,
                                "color": "#FFF50E",
                            },
                            {
                                "value": 0.2,
                                "color": "#FFB50A",
                                "legend": { }
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
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "Sentinel-2 Definitive",
        "title": "Sentinel Definitive",
        "abstract": "This is a definitive archive of daily Sentinel-2 data. ",
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
This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time.

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For service status information, see https://status.dea.ga.gov.au""",
                # The WMS name for the layer
                "name": "s2_ard_granule_nbar_t",
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
This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time.

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
This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time.

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
    },
    {
        "name": "multi_scale_topographic_position",
        "title": "Multi-Scale Topographic Position",
        "abstract": "",
        "products": [
            {
                "label": "Multi-Scale Topographic Position",
                "abstract": """A Multi-scale topographic position image of Australia has been generated by combining 
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
                "type": "1 degree tile",
                "variant": "",
                "name": "multi_scale_topographic_position",
                "product_name": "multi_scale_topographic_position",
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": ["regional", "intermediate", "local"],
                "apply_solar_corrections": False,
                "legend": {
                    "url": "https://data.dea.ga.gov.au/multi-scale-topographic-position/mstp_legend.png",
                    # "styles": ["mstp_rgb"]
                },
                "wcs_default_bands": ["regional", "intermediate", "local"],
                "styles": [
                    {
                        "name": "mstp_rgb",
                        "title": "Multi-scale Topographic Position",
                        "abstract": "red regional, green intermediate and blue local",
                        "components": {
                            "red": {
                                "regional": 1.0
                            },
                            "green": {
                                "intermediate": 1.0
                            },
                            "blue": {
                                "local": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 255.0]
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "mstp_rgb",
            },
        ]
    },
    {
        "name": "weathering_intensity",
        "title": "Weathering Intensity",
        "abstract": "",
        "products": [
            {
                "label": "Weathering Intensity",
                "abstract": "Weathering intensity or the degree of weathering is an important characteristic of the "
                            "earth’s surface that has a significant influence on the chemical and physical properties "
                            "of surface materials. Weathering intensity largely controls the degree to which primary "
                            "minerals are altered to secondary components including clay minerals and oxides. The "
                            "degree of surface weathering is particularly important in Australia where variations in "
                            "weathering intensity correspond to the nature and distribution of regolith (weathered "
                            "bedrock and sediments) which mantles approximately 90% of the Australian continent. The "
                            "weathering intensity prediction has been generated using the Random Forest decision tree "
                            "machine learning algorithm. The algorithm is used to establish predictive relationships "
                            "between field estimates of the degree of weathering and a comprehensive suite of "
                            "covariate or predictive datasets. The covariates used to generate the model include "
                            "satellite imagery, terrain attributes, airborne radiometric imagery and mapped geology. "
                            "Correlations between the training dataset and the covariates were explored through the "
                            "generation of 300 random tree models. An r-squared correlation of 0.85 is reported using "
                            "5 K-fold cross-validation. The mean of the 300 models is used for predicting the "
                            "weathering intensity and the uncertainty in the weathering intensity is estimated at "
                            "each location via the standard deviation in the 300 model values. The predictive "
                            "weathering intensity model is an estimate of the degree of surface weathering only. The "
                            "interpretation of the weathering intensity is different for in-situ or residual "
                            "landscapes compared with transported materials within depositional landscapes. In "
                            "residual landscapes, weathering process are operating locally whereas in depositional "
                            "landscapes the model is reflecting the degree of weathering either prior to erosion and "
                            "subsequent deposition, or weathering of sediments after being deposited. The weathering "
                            "intensity model has broad utility in assisting mineral exploration in variably weathered "
                            "geochemical landscapes across the Australian continent, mapping chemical and physical "
                            "attributes of soils in agricultural landscapes and in understanding the nature and "
                            "distribution of weathering processes occurring within the upper regolith."
                            "For service status information, see https://status.dea.ga.gov.au",
                "type": "1 degree tile",
                "variant": "",
                "name": "weathering_intensity",
                "product_name": "weathering_intensity",
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": ["intensity"],
                "apply_solar_corrections": False,
                "legend": {
                    "styles": ["wii"]
                },
                "wcs_default_bands": ["intensity"],
                "styles": [
                    {
                        "name": "wii",
                        "title": "Weathering Intensity",
                        "abstract": "Weather Intensity Index (0-6)",
                        "needed_bands": ["intensity"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffff',
                                'alpha': 0
                            },
                            {
                                'value': 1,
                                'color': '#2972a8',
                                'legend': {
                                    'label': 'Low\nClass 1'
                                }
                            },
                            {
                                'value': 3.5,
                                'color': '#fcf24b'
                            },
                            {
                                'value': 6,
                                'color': '#a02406',
                                'legend': {
                                    'label': 'High\nClass 6'
                                }
                            }
                        ],
                        "legend": {
                            "axes_position": [0.1, 0.5, 0.8, 0.15]
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "wii",
            },
        ]
    },
    {
        "name": "fcp_green_veg",
        "title": "Fractional Cover Percentiles - Green Vegetation",
        "abstract": "",
        "products": [
            {
                "label": "Fractional Cover Percentiles - Green Vegetation",
                "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

This contains the percentage of green vegetation per pixel at the 10th, 50th (median) and 90th percentiles for observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_green_veg",
                "product_name": "fc_percentile_albers_annual",
                "pq_dataset": "geodata_coast_100k",
                "pq_band": "land",
                "pq_ignore_time": True,
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": [ ],
                "apply_solar_corrections": False,
                "legend": {
                    "styles": ["green_veg_10"]
                },
                "wcs_default_bands": ["PV_PC_10", "PV_PC_50", "PV_PC_90"],
                "styles": [
                    {
                        "name": "green_veg_10",
                        "title": "10th Percentile",
                        "abstract": "10th Percentile of Green Vegetation",
                        "needed_bands": ["PV_PC_10"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffcc',
                                'legend': {}
                            },
                            {
                                'value': 25,
                                'color': '#c2e699',
                                'legend': {}
                            },
                            {
                                'value': 50,
                                'color': '#78c679',
                                'legend': {}
                            },
                            {
                                'value': 75,
                                'color': '#31a354',
                                'legend': {}
                            },
                            {
                                'value': 100,
                                'color': '#006837',
                                'legend': {}
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                        "legend": {
                            "units": "% / pixel",
                            "title": "Percentage of Pixel that is Green Vegetation",
                            "rcParams": {
                                "font.size": 9
                            }
                        }
                    },
                    {
                        "name": "green_veg_50",
                        "title": "50th Percentile",
                        "abstract": "50th Percentile of Green Vegetation",
                        "needed_bands": ["PV_PC_50"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffcc'
                            },
                            {
                                'value': 25,
                                'color': '#c2e699'
                            },
                            {
                                'value': 50,
                                'color': '#78c679'
                            },
                            {
                                'value': 75,
                                'color': '#31a354'
                            },
                            {
                                'value': 100,
                                'color': '#006837'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                    {
                        "name": "green_veg_90",
                        "title": "90th Percentile",
                        "abstract": "90th Percentile of Green Vegetation",
                        "needed_bands": ["PV_PC_90"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffcc'
                            },
                            {
                                'value': 25,
                                'color': '#c2e699'
                            },
                            {
                                'value': 50,
                                'color': '#78c679'
                            },
                            {
                                'value': 75,
                                'color': '#31a354'
                            },
                            {
                                'value': 100,
                                'color': '#006837'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "green_veg_10",
            },
        ]
    },
    {
        "name": "fcp_non_green_veg",
        "title": "Fractional Cover Percentiles - Non Green Vegetation",
        "abstract": "",
        "products": [
            {
                "label": "Fractional Cover Percentiles - Non Green Vegetation",
                "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

This contains the percentage of non-green vegetation per pixel at the 10th, 50th (median) and 90th percentiles for observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_non_green_veg",
                "product_name": "fc_percentile_albers_annual",
                "pq_dataset": "geodata_coast_100k",
                "pq_band": "land",
                "pq_ignore_time": True,
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                "legend": {
                    "styles": ["non_green_veg_10"]
                },
                "wcs_default_bands": ["NPV_PC_10", "NPV_PC_50", "NPV_PC_90"],
                "styles": [
                    {
                        "name": "non_green_veg_10",
                        "title": "10th Percentile",
                        "abstract": "10th Percentile of Non Green Vegetation",
                        "needed_bands": ["NPV_PC_10"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffd4',
                                'legend': {}
                            },
                            {
                                'value': 25,
                                'color': '#fed98e',
                                'legend': {}
                            },
                            {
                                'value': 50,
                                'color': '#fe9929',
                                'legend': {}
                            },
                            {
                                'value': 75,
                                'color': '#d95f0e',
                                'legend': {}
                            },
                            {
                                'value': 100,
                                'color': '#993404',
                                'legend': {}
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                        "legend": {
                            "units": "% / pixel",
                            "title": "Percentage of Pixel that is Non-Green Vegetation",
                            "rcParams": {
                                "font.size": 9
                            }
                        }
                    },
                    {
                        "name": "non_green_veg_50",
                        "title": "50th Percentile",
                        "abstract": "50th Percentile of Non Green Vegetation",
                        "needed_bands": ["NPV_PC_50"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffd4'
                            },
                            {
                                'value': 25,
                                'color': '#fed98e'
                            },
                            {
                                'value': 50,
                                'color': '#fe9929'
                            },
                            {
                                'value': 75,
                                'color': '#d95f0e'
                            },
                            {
                                'value': 100,
                                'color': '#993404'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                    {
                        "name": "non_green_veg_90",
                        "title": "90th Percentile",
                        "abstract": "90th Percentile of Non Green Vegetation",
                        "needed_bands": ["NPV_PC_90"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffd4'
                            },
                            {
                                'value': 25,
                                'color': '#fed98e'
                            },
                            {
                                'value': 50,
                                'color': '#fe9929'
                            },
                            {
                                'value': 75,
                                'color': '#d95f0e'
                            },
                            {
                                'value': 100,
                                'color': '#993404'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "non_green_veg_10",
            },
        ]
    },
    {
        "name": "fcp_bare_soil",
        "title": "Fractional Cover Percentiles - Bare Soil",
        "abstract": "",
        "products": [
            {
                "label": "Fractional Cover Percentiles - Bare Soil",
                "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time.  The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

This contains the percentage of bare soil per pixel at the 10th, 50th (median) and 90th percentiles for observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_bare_ground",
                "product_name": "fc_percentile_albers_annual",
                "pq_dataset": "geodata_coast_100k",
                "pq_band": "land",
                "pq_ignore_time": True,
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                "legend": {
                    "styles": ["bare_ground_10"]
                },
                "wcs_default_bands": ["BS_PC_10", "BS_PC_50", "BS_PC_90"],
                "styles": [
                    {
                        "name": "bare_ground_10",
                        "title": "10th Percentile",
                        "abstract": "10th Percentile of Bare Soil",
                        "needed_bands": ["BS_PC_10"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#feebe2',
                                'legend': {}
                            },
                            {
                                'value': 25,
                                'color': '#fbb4b9',
                                'legend': {}
                            },
                            {
                                'value': 50,
                                'color': '#f768a1',
                                'legend': {}
                            },
                            {
                                'value': 75,
                                'color': '#c51b8a',
                                'legend': {}
                            },
                            {
                                'value': 100,
                                'color': '#7a0177',
                                'legend': {}
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                        "legend": {
                            "units": "% / pixel",
                            "title": "Percentage of Pixel that is Bare Soil",
                            "rcParams": {
                                "font.size": 9
                            }
                        }
                    },
                    {
                        "name": "bare_ground_50",
                        "title": "50th Percentile",
                        "abstract": "50th Percentile of Bare Soil",
                        "needed_bands": ["BS_PC_50"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#feebe2'
                            },
                            {
                                'value': 25,
                                'color': '#fbb4b9'
                            },
                            {
                                'value': 50,
                                'color': '#f768a1'
                            },
                            {
                                'value': 75,
                                'color': '#c51b8a'
                            },
                            {
                                'value': 100,
                                'color': '#7a0177'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                    {
                        "name": "bare_ground_90",
                        "title": "90th Percentile",
                        "abstract": "90th Percentile of Bare Soil",
                        "needed_bands": ["BS_PC_90"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#feebe2'
                            },
                            {
                                'value': 25,
                                'color': '#fbb4b9'
                            },
                            {
                                'value': 50,
                                'color': '#f768a1'
                            },
                            {
                                'value': 75,
                                'color': '#c51b8a'
                            },
                            {
                                'value': 100,
                                'color': '#7a0177'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "bare_ground_10",
            },
        ]
    },
    {
        "name": "fcp_rgb",
        "title": "Fractional Cover Percentiles - Median",
        "abstract": "",
        "products": [
            {
                "label": "Fractional Cover Percentiles - Median",
                "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program.

This contains a three band combination of the 50th Percentile for green vegetation, non green vegetation and bare soil observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_rgb",
                "product_name": "fc_percentile_albers_annual",
                "pq_dataset": "geodata_coast_100k",
                "pq_band": "land",
                "pq_ignore_time": True,
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                "legend": {
                    "url": "https://data.dea.ga.gov.au/fractional-cover/fc-percentile/annual/v2.1.0/fcp_legend.png",
                },
                "wcs_default_bands": ["BS_PC_50", "PV_PC_50", "NPV_PC_50"],
                "styles": [
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "BS_PC_50": 1.0
                            },
                            "green": {
                                "PV_PC_50": 1.0
                            },
                            "blue": {
                                "NPV_PC_50": 1.0
                            }
                        },
                        "scale_range": [0.0, 100.0],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
        ]
    },
    {
        "name": "fcp_seasonal",
        "title": "Fractional Cover Percentiles Seasonal",
        "abstract": "",
        "products": [
            {
                "label": "Green Vegetation",
                "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

 FC-PERCENTILE-SEASONAL-SUMMARY, this contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_seasonal_green_veg",
                "product_name": "fc_percentile_albers_seasonal",
                "pq_dataset": "geodata_coast_100k",
                "pq_band": "land",
                "pq_ignore_time": True,
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": [ ],
                "apply_solar_corrections": False,
                "legend": {
                    "styles": ["green_veg_10"]
                },
                "wcs_default_bands": ["PV_PC_10", "PV_PC_50", "PV_PC_90"],
                "styles": [
                    {
                        "name": "green_veg_10",
                        "title": "10th Percentile",
                        "abstract": "10th Percentile of Green Vegetation",
                        "needed_bands": ["PV_PC_10"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffcc',
                                'legend': {}
                            },
                            {
                                'value': 25,
                                'color': '#c2e699',
                                'legend': {}
                            },
                            {
                                'value': 50,
                                'color': '#78c679',
                                'legend': {}
                            },
                            {
                                'value': 75,
                                'color': '#31a354',
                                'legend': {}
                            },
                            {
                                'value': 100,
                                'color': '#006837',
                                'legend': {}
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                        "legend": {
                            "units": "% / pixel",
                            "title": "Percentage of Pixel that is Green Vegetation",
                            "rcParams": {
                                "font.size": 9
                            }
                        }
                    },
                    {
                        "name": "green_veg_50",
                        "title": "50th Percentile",
                        "abstract": "50th Percentile of Green Vegetation",
                        "needed_bands": ["PV_PC_50"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffcc'
                            },
                            {
                                'value': 25,
                                'color': '#c2e699'
                            },
                            {
                                'value': 50,
                                'color': '#78c679'
                            },
                            {
                                'value': 75,
                                'color': '#31a354'
                            },
                            {
                                'value': 100,
                                'color': '#006837'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                    {
                        "name": "green_veg_90",
                        "title": "90th Percentile",
                        "abstract": "90th Percentile of Green Vegetation",
                        "needed_bands": ["PV_PC_90"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffcc'
                            },
                            {
                                'value': 25,
                                'color': '#c2e699'
                            },
                            {
                                'value': 50,
                                'color': '#78c679'
                            },
                            {
                                'value': 75,
                                'color': '#31a354'
                            },
                            {
                                'value': 100,
                                'color': '#006837'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "green_veg_10",
            },
            {
                "label": "Non Green Vegetation",
                "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

 FC-PERCENTILE-SEASONAL-SUMMARY, this contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_seasonal_non_green_veg",
                "product_name": "fc_percentile_albers_seasonal",
                "pq_dataset": "geodata_coast_100k",
                "pq_band": "land",
                "pq_ignore_time": True,
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                "legend": {
                    "styles": ["non_green_veg_10"]
                },
                "wcs_default_bands": ["NPV_PC_10", "NPV_PC_50", "NPV_PC_90"],
                "styles": [
                    {
                        "name": "non_green_veg_10",
                        "title": "10th Percentile",
                        "abstract": "10th Percentile of Non Green Vegetation",
                        "needed_bands": ["NPV_PC_10"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffd4',
                                'legend': {}
                            },
                            {
                                'value': 25,
                                'color': '#fed98e',
                                'legend': {}
                            },
                            {
                                'value': 50,
                                'color': '#fe9929',
                                'legend': {}
                            },
                            {
                                'value': 75,
                                'color': '#d95f0e',
                                'legend': {}
                            },
                            {
                                'value': 100,
                                'color': '#993404',
                                'legend': {}
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                        "legend": {
                            "units": "% / pixel",
                            "title": "Percentage of Pixel that is Non-Green Vegetation",
                            "rcParams": {
                                "font.size": 9
                            }
                        }
                    },
                    {
                        "name": "non_green_veg_50",
                        "title": "50th Percentile",
                        "abstract": "50th Percentile of Non Green Vegetation",
                        "needed_bands": ["NPV_PC_50"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffd4'
                            },
                            {
                                'value': 25,
                                'color': '#fed98e'
                            },
                            {
                                'value': 50,
                                'color': '#fe9929'
                            },
                            {
                                'value': 75,
                                'color': '#d95f0e'
                            },
                            {
                                'value': 100,
                                'color': '#993404'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                    {
                        "name": "non_green_veg_90",
                        "title": "90th Percentile",
                        "abstract": "90th Percentile of Non Green Vegetation",
                        "needed_bands": ["NPV_PC_90"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#ffffd4'
                            },
                            {
                                'value': 25,
                                'color': '#fed98e'
                            },
                            {
                                'value': 50,
                                'color': '#fe9929'
                            },
                            {
                                'value': 75,
                                'color': '#d95f0e'
                            },
                            {
                                'value': 100,
                                'color': '#993404'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "non_green_veg_10",
            },
            {
                "label": "Bare Soil",
                "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time.  The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

FC-PERCENTILE-SEASONAL-SUMMARY, this contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons
Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_seasonal_bare_ground",
                "product_name": "fc_percentile_albers_seasonal",
                "pq_dataset": "geodata_coast_100k",
                "pq_band": "land",
                "pq_ignore_time": True,
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                "legend": {
                    "styles": ["bare_ground_10"]
                },
                "wcs_default_bands": ["BS_PC_10", "BS_PC_50", "BS_PC_90"],
                "styles": [
                    {
                        "name": "bare_ground_10",
                        "title": "10th Percentile",
                        "abstract": "10th Percentile of Bare Soil",
                        "needed_bands": ["BS_PC_10"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#feebe2',
                                'legend': {}
                            },
                            {
                                'value': 25,
                                'color': '#fbb4b9',
                                'legend': {}
                            },
                            {
                                'value': 50,
                                'color': '#f768a1',
                                'legend': {}
                            },
                            {
                                'value': 75,
                                'color': '#c51b8a',
                                'legend': {}
                            },
                            {
                                'value': 100,
                                'color': '#7a0177',
                                'legend': {}
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                        "legend": {
                            "units": "% / pixel",
                            "title": "Percentage of Pixel that is Bare Soil",
                            "rcParams": {
                                "font.size": 9
                            }
                        }
                    },
                    {
                        "name": "bare_ground_50",
                        "title": "50th Percentile",
                        "abstract": "50th Percentile of Bare Soil",
                        "needed_bands": ["BS_PC_50"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#feebe2'
                            },
                            {
                                'value': 25,
                                'color': '#fbb4b9'
                            },
                            {
                                'value': 50,
                                'color': '#f768a1'
                            },
                            {
                                'value': 75,
                                'color': '#c51b8a'
                            },
                            {
                                'value': 100,
                                'color': '#7a0177'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                    {
                        "name": "bare_ground_90",
                        "title": "90th Percentile",
                        "abstract": "90th Percentile of Bare Soil",
                        "needed_bands": ["BS_PC_90"],
                        "color_ramp": [
                            {
                                'value': 0,
                                'color': '#feebe2'
                            },
                            {
                                'value': 25,
                                'color': '#fbb4b9'
                            },
                            {
                                'value': 50,
                                'color': '#f768a1'
                            },
                            {
                                'value': 75,
                                'color': '#c51b8a'
                            },
                            {
                                'value': 100,
                                'color': '#7a0177'
                            }
                        ],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "bare_ground_10",
            },
            {
                "label": "Median",
                "abstract": """
Fractional Cover Percentiles version 2.2.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program.

 FC-PERCENTILE-SEASONAL-SUMMARY, this contains a (10th, 50th and 90th percentile) of BS, PV and NPV of observations acquired within each calendar season (DJF, MAM, JJA, SON). This product is available for the most recent 8 seasons

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_seasonal_rgb",
                "product_name": "fc_percentile_albers_seasonal",
                "pq_dataset": "geodata_coast_100k",
                "pq_band": "land",
                "pq_ignore_time": True,
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                "legend": {
                    "url": "https://data.dea.ga.gov.au/fractional-cover/fc-percentile/annual/v2.1.0/fcp_legend.png",
                },
                "wcs_default_bands": ["BS_PC_50", "PV_PC_50", "NPV_PC_50"],
                "styles": [
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "BS_PC_50": 1.0
                            },
                            "green": {
                                "PV_PC_50": 1.0
                            },
                            "blue": {
                                "NPV_PC_50": 1.0
                            }
                        },
                        "scale_range": [0.0, 100.0],
                        "pq_masks": [
                            {
                                "flags": {
                                    'sea': True,
                                },
                                "invert": True,
                            },
                        ],
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
        ]
    },
    {
        "name": "nidem",
        "title": "National Intertidal Digital Elevation Model",
        "abstract": "",
        "products": [
            {
                "label": "NIDEM 25m",
                "abstract": "The National Intertidal Digital Elevation Model (NIDEM) product is a continental-scale "
                            "dataset providing continuous elevation data for Australia's exposed intertidal zone. "
                            "NIDEM provides the first three-dimensional representation of Australia's intertidal zone "
                            "(excluding off-shore Territories and intertidal mangroves) at 25 m spatial resolution, "
                            "addressing a key gap between the availability of sub-tidal bathymetry and "
                            "terrestrial elevation data. NIDEM was generated by combining global tidal modelling "
                            "with a 30-year time series archive of spatially and spectrally calibrated "
                            "Landsat satellite data managed within the Digital Earth Australia (DEA) platform. "
                            "NIDEM complements existing intertidal extent products, and provides data to support a "
                            "new suite of use cases that require a more detailed understanding of the three-dimensional "
                            "topography of the intertidal zone, such as hydrodynamic modelling, coastal risk management "
                            "and ecological habitat mapping."
                            "For service status information, see https://status.dea.ga.gov.au",
                "type": "grid",
                "variant": "nidem_v1.0.0",
                "name": "NIDEM",
                "product_name": "nidem",
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": ["nidem"],
                "apply_solar_corrections": False,
                "legend": {
                    "styles": ["NIDEM"]
                },
                "wcs_default_bands": ["nidem"],
                "styles": [
                    {
                        "name": "NIDEM",
                        "title": "National Intertidal Digital Elevation Model",
                        "abstract": "National Intertidal Digital Elevation Model 25 m v1.0.0",
                        "needed_bands": ["nidem"],
                        "color_ramp": [
                            {
                                'value': -2.51,
                                'color': '#440154'
                            },
                            {

                                'value': -2.5,
                                'color': '#440154',
                                'legend': {
                                    "prefix": "<"
                                }
                            },
                            {
                                'value': -2.34,
                                'color': '#460e61',
                            },
                            {
                                'value': -2.18,
                                'color': '#471b6e',
                            },
                            {
                                'value': -2.02,
                                'color': '#472877'
                            },
                            {
                                'value': -1.86,
                                'color': '#45347f'
                            },
                            {
                                'value': -1.7,
                                'color': '#413f85'
                            },
                            {
                                'value': -1.58,
                                'color': '#3b4d8a'
                            },
                            {
                                'value': -1.42,
                                'color': '#37578b'
                            },
                            {
                                'value': -1.26,
                                'color': '#32618c'
                            },

                            {
                                'value': -1.1,
                                'color': '#2e6b8d',
                                "legend": {}
                            },
                            {
                                'value': -0.94,
                                'color': '#2a748e'
                            },
                            {
                                'value': -0.78,
                                'color': '#267d8e'
                            },
                            {
                                'value': -0.62,
                                'color': '#23868d'
                            },
                            {
                                'value': -0.46,
                                'color': '#208f8c'
                            },
                            {
                                'value': -0.3,
                                'color': '#1e9889'
                            },
                            {
                                'value': -0.14,
                                'color': '#1fa186'
                            },
                            {
                                'value': 0.0,
                                'color': '#26ac7f',
                                "legend": { }
                            },
                            {
                                'value': 0.14,
                                'color': '#32b579'
                            },
                            {
                                'value': 0.3,
                                'color': '#41bd70'
                            },
                            {
                                'value': 0.46,
                                'color': '#54c566'
                            },
                            {
                                'value': 0.62,
                                'color': '#69cc59'
                            },
                            {
                                'value': 0.78,
                                'color': '#80d24b'
                            },
                            {
                                'value': 0.94,
                                'color': '#99d83c'
                            },
                            {
                                'value': 1.1,
                                'color': '#b2dc2c',
                            },
                            {
                                'value': 1.26,
                                'color': '#cce01e'
                            },
                            {
                                'value': 1.42,
                                'color': '#e5e31a'
                            },
                            {
                                'value': 1.5,
                                'color': '#fde724',
                                'legend': {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "units": "metres"
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "NIDEM",
            },
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "HLTC Composites",
        "title": "High Tide Low Tide Composite",
        "abstract": "The High and Low Tide Composites product is composed of two surface reflectance composite mosaics "
                    "of Landsat TM and ETM+ (Landsat 5 and Landsat 7 respectively) and OLI (Landsat 8) "
                    "surface reflectance data (Li et al., 2012). These products have been produced using "
                    "Digital Earth Australia (DEA). The two mosaics allow cloud free and noise reduced visualisation "
                    "of the shallow water and inter-tidal coastal regions of Australia, as observed at "
                    "high and low tide respectively.The composites are generated utilising the geomedian approach of "
                    "Roberts et al (2017) to ensure a valid surface reflectance spectra suitable for uses such as "
                    "habitat mapping. The time range used for composite generation in each polygon of the mosaic is "
                    "tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud "
                    "free composite to be generated. The concepts of the Observed Tidal Range (OTR), "
                    "and Highest and Lowest Observed Tide (HOT, LOT) are discussed and described fully in Sagar et al. "
                    "(2017) and the product description for the ITEM v 1.0 product (Geoscience Australia, 2016).",

        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "High Tide",
                "abstract":"""
High Tide and Low Tide Composites 2.0.0
               
The High and Low Tide Composites product is composed of two surface reflectance composite mosaics of Landsat TM and ETM+ (Landsat 5 and Landsat 7 respectively) and OLI (Landsat 8) surface reflectance data (Li et al., 2012). These products have been produced using Digital Earth Australia (DEA). 
The two mosaics allow cloud free and noise reduced visualisation of the shallow water and inter-tidal coastal regions of Australia, as observed at high and low tide respectively (Sagar et al. 2018).
                
The composites are generated utilising the geomedian approach of Roberts et al (2017) to ensure a valid surface reflectance spectra suitable for uses such as habitat mapping. 
The time range used for composite generation in each polygon of the mosaic is tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud free composite to be generated. The concepts of the Observed Tidal Range (OTR), and Highest and Lowest Observed Tide (HOT, LOT) are discussed and described fully in Sagar et al. (2017) and the product description for the ITEM v 1.0 product (Geoscience Australia, 2016).
                            
*Overview*
                
Inter-tidal zones are difficult regions to characterise due to the dynamic nature of the tide. They are highly changeable environments, subject to forcings from the land, sea and atmosphere and yet they form critical habitats for a wide range of organisms from birds to fish and sea grass. 
By harnessing the long archive of satellite imagery over Australia's coastal zones in the DEA and pairing the images with regional tidal modelling, the archive can be sorted by tide height rather than date, enabling the inter-tidal zone to be viewed at any stage of the tide regime.
                
The High Low Tide Composites (HLTC_25) product is composed of two mosaics, distinguished by tide height, representing a composite image of the synthetic geomedian surface reflectance from Landsats 5 TM, Landsat 7 ETM+ and Landsat 8 OLI NBAR data (Li et al., 2012; Roberts et al., 2017). Oregon State Tidal Prediction (OTPS) software (Egbert and Erofeeva, 2002, 2010) was used to generate tide heights, relative to mean sea level, for the Australian continental coastline, split into 306 distinct tidal regions. 
These time and date stamped tidal values were then attributed to all coastal tile observations for their time of acquisition, creating a range of observed tide heights for the Australian coastline. The two mosaics in HLTC_25 are composited from the highest and lowest 20 % of observed tide in the ensemble and are termed HOT and LOT respectively. 
A geomedian composite for each Landsat band is calculated from the tiles in each ensemble subset to produce the respective HOT and LOT composites. Note that Landsat 7 ETM+ observations are excluded after May 2003 due to a large number of data artifacts.
                
The time range used for composite generation in each of the 306 polygons of the mosaics are tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud free composite to be generated. 
The maximum epoch for which the products are calculated is between 1995-2017, although this varies due to data resolution and observation quality. The product also includes a count of clear observations per pixel for both mosaics and attribute summaries per polygon that include the date range, the highest and lowest modeled astronomical tide as well as the highest and lowest observed tide for that time range, the total observation count and the maximum count of observations for any one pixel in the polygon, the polygon ID number (from 1 to 306), the polygon centroid in longitude and latitude and the count of tide stages attributed to every observation used in that polygon of the mosaic. For the count of tidal stage observations, e = ebbing tide, f = flowing tide, ph = peak high tide and pl = peak low tide. 
The tide stages were calculated bycomparison to the modeled tide data for 15 minutes either side of the observation to determine the ebb, flow or peak movement of the tide.
                
Observations are filtered to remove poor quality observations including cloud, cloud shadow and band saturation (of any band).
For service status information, see https://status.dea.ga.gov.au""",
                # Included as a keyword  for the layer
                "type": "Tidal Composite",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "high_tide_composite",
                # The Datacube name for the associated data product
                "product_name": "high_tide_comp_20p",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "ls8_level1_usgs",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_manual_data_merge": True,
                # "data_manual_merge": True,
                # "pq_band": "quality",
                # "always_fetch_bands": [ "quality" ],
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],

                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi"]
                },
                "wcs_default_bands": ["red", "green", "blue"],
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

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
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 0.30]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
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
                        "scale_range": [0.0, 0.30]
                    },
                    #
                    # Examples of non-linear heat-mapped styles.
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
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
                        "name": "ndwi",
                        "title": "NDWI - Green, SWIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (
                                    data["swir1"] + data["green"]),
                        "needed_bands": ["green", "swir1"],
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
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
            {
                # Included as a keyword  for the layer
                "label": "Low Tide",
                "abstract": """
High Tide and Low Tide Composites 2.0.0
               
The High and Low Tide Composites product is composed of two surface reflectance composite mosaics of Landsat TM and ETM+ (Landsat 5 and Landsat 7 respectively) and OLI (Landsat 8) surface reflectance data (Li et al., 2012). These products have been produced using Digital Earth Australia (DEA). 
The two mosaics allow cloud free and noise reduced visualisation of the shallow water and inter-tidal coastal regions of Australia, as observed at high and low tide respectively (Sagar et al. 2018).
                
The composites are generated utilising the geomedian approach of Roberts et al (2017) to ensure a valid surface reflectance spectra suitable for uses such as habitat mapping. 
The time range used for composite generation in each polygon of the mosaic is tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud free composite to be generated. The concepts of the Observed Tidal Range (OTR), and Highest and Lowest Observed Tide (HOT, LOT) are discussed and described fully in Sagar et al. (2017) and the product description for the ITEM v 1.0 product (Geoscience Australia, 2016).
                            
*Overview*
                
Inter-tidal zones are difficult regions to characterise due to the dynamic nature of the tide. They are highly changeable environments, subject to forcings from the land, sea and atmosphere and yet they form critical habitats for a wide range of organisms from birds to fish and sea grass. 
By harnessing the long archive of satellite imagery over Australia's coastal zones in the DEA and pairing the images with regional tidal modelling, the archive can be sorted by tide height rather than date, enabling the inter-tidal zone to be viewed at any stage of the tide regime.
                
The High Low Tide Composites (HLTC_25) product is composed of two mosaics, distinguished by tide height, representing a composite image of the synthetic geomedian surface reflectance from Landsats 5 TM, Landsat 7 ETM+ and Landsat 8 OLI NBAR data (Li et al., 2012; Roberts et al., 2017). Oregon State Tidal Prediction (OTPS) software (Egbert and Erofeeva, 2002, 2010) was used to generate tide heights, relative to mean sea level, for the Australian continental coastline, split into 306 distinct tidal regions. 
These time and date stamped tidal values were then attributed to all coastal tile observations for their time of acquisition, creating a range of observed tide heights for the Australian coastline. The two mosaics in HLTC_25 are composited from the highest and lowest 20 % of observed tide in the ensemble and are termed HOT and LOT respectively. 
A geomedian composite for each Landsat band is calculated from the tiles in each ensemble subset to produce the respective HOT and LOT composites. Note that Landsat 7 ETM+ observations are excluded after May 2003 due to a large number of data artifacts.
                
The time range used for composite generation in each of the 306 polygons of the mosaics are tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud free composite to be generated. 
The maximum epoch for which the products are calculated is between 1995-2017, although this varies due to data resolution and observation quality. The product also includes a count of clear observations per pixel for both mosaics and attribute summaries per polygon that include the date range, the highest and lowest modeled astronomical tide as well as the highest and lowest observed tide for that time range, the total observation count and the maximum count of observations for any one pixel in the polygon, the polygon ID number (from 1 to 306), the polygon centroid in longitude and latitude and the count of tide stages attributed to every observation used in that polygon of the mosaic. For the count of tidal stage observations, e = ebbing tide, f = flowing tide, ph = peak high tide and pl = peak low tide. 
The tide stages were calculated bycomparison to the modeled tide data for 15 minutes either side of the observation to determine the ebb, flow or peak movement of the tide.
                
Observations are filtered to remove poor quality observations including cloud, cloud shadow and band saturation (of any band).
For service status information, see https://status.dea.ga.gov.au""",
                # Included as a keyword  for the layer
                "type": "Tidal Composite",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "low_tide_composite",
                # The Datacube name for the associated data product
                "product_name": "low_tide_comp_20p",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "ls8_level1_usgs",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_manual_data_merge": True,
                # "data_manual_merge": True,
                # "pq_band": "quality",
                # "always_fetch_bands": [ "quality" ],
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],

                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi"]
                },
                "wcs_default_bands": ["red", "green", "blue"],
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

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
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 0.30]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
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
                        "scale_range": [0.0, 0.30]
                    },
                    #
                    # Examples of non-linear heat-mapped styles.
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
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
                        "name": "ndwi",
                        "title": "NDWI - Green, SWIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (
                                    data["swir1"] + data["green"]),
                        "needed_bands": ["green", "swir1"],
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
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "ITEM",
        "title": "Intertidal Extents Model",
        "abstract": "The Intertidal Extents Model (ITEM) product is a national dataset of the exposed intertidal zone; "
                    "the land between the observed highest and lowest tide. ITEM provides the extent and topography of "
                    "the intertidal zone of Australia's coastline (excluding off-shore Territories). "
                    "This information was collated using observations in the Landsat archive since 1986. "
                    "ITEM can be a valuable complimentary dataset to both onshore LiDAR survey data and coarser offshore "
                    "bathymetry data, enabling a more realistic representation of the land and ocean interface.",

        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "Relative Layer",
                "abstract": """
The Intertidal Extents Model (ITEM v2.0) product analyses GA’s historic archive of satellite imagery to derive a model of the spatial extents of the intertidal zone throughout the tidal cycle. The model can assist in understanding the relative elevation profile of the intertidal zone, 
delineating exposed areas at differing tidal heights and stages.

The product differs from previous methods used to map the intertidal zone which have been predominately focused on analysing a small number of individual satellite images per location (e.g Ryu et al., 2002; Murray et al., 2012). 
By utilising a full 30 year time series of observations and a global tidal model (Egbert and Erofeeva, 2002), the methodology enables us to overcome the requirement for clear, high quality observations acquired concurrent to the time of high and low tide.

*Accuracy and limitations*
                  
Due the sun-synchronous nature of the various Landsat sensor observations; it is unlikely that the full physical extents of the tidal range in any cell will be observed. Hence, terminology has been adopted for the product to reflect the highest modelled tide observed in a given cell (HOT) and the lowest modelled tide observed (LOT) (see Sagar et al. 2017). These measures are relative to Mean Sea Level, and have no consistent relationship to Lowest (LAT) and Highest Astronomical Tide (HAT).

The inclusion of the lowest (LMT) and highest (HMT) modelled tide values for each tidal polygon indicates the highest and lowest tides modelled for that location across the full time series by the OTPS model. The relative difference between the LOT and LMT (and HOT and HMT) heights gives an indication of the extent of the tidal range represented in the Relative Extents Model.

As in ITEM v1.0, v2.0 contains some false positive land detection in open ocean regions. These are a function of the lack of data at the extremes of the observed tidal range, and features like glint and undetected cloud in these data poor regions/intervals. Methods to isolate and remove these features are in development for future versions. Issues in the DEA archive and data noise in the Esperance, WA region off Cape Le Grande and Cape Arid (Polygons 236,201,301) has resulted in significant artefacts in the model, and use of the model in this area is not recommended.
                
The Confidence layer is designed to assess the reliability of the Relative Extent Model. Within each tidal range percentile interval, the pixel-based standard deviation of the NDWI values for all observations in the interval subset is calculated. The average standard deviation across all tidal range intervals is then calculated and retained as a quality indicator in this product layer.

The Confidence Layer reflects the pixel based consistency of the NDWI values within each subset of observations, based on the tidal range. Higher standard deviation values indicate water classification changes not based on the tidal cycle, and hence lower confidence in the extent model.

Possible drivers of these changes include:

Inadequacies of the tidal model, due perhaps to complex coastal bathymetry or estuarine structures not captured in the model. These effects have been reduced in ITEM v2.0 compared to previous versions, through the use of an improved tidal modelling frameworkChange in the structure and exposure of water/non-water features NOT driven by tidal variation. 
For example, movement of sand banks in estuaries, construction of man-made features (ports etc.).Terrestrial/Inland water features not influenced by the tidal cycle.
File naming:
THE RELATIVE EXTENTS MODEL v2.0
ITEM_REL_<TIDAL POLYGON NUMBER>_<LONGITUDE>_<LATITUDE>
TIDAL POLYGON NUMBER relates to the id of the tidal polygon referenced by the file
LONGITUDE is the longitude of the centroid of the tidal polygon
LATITUDE is the latitude of the centroid of the tidal polygon

THE CONFIDENCE LAYER v2.0
ITEM_STD_<TIDAL POLYGON NUMBER>_<LONGITUDE>_<LATITUDE>
TIDAL POLYGON NUMBER relates to the id of the tidal polygon referenced by the file
LONGITUDE is the longitude of the centroid of the tidal polygon
LATITUDE is the latitude of the centroid of the tidal polygon

*Overview*

The Intertidal Extents Model product is a national scale gridded dataset characterising the spatial extents of the exposed intertidal zone, at intervals of the observed tidal range (Sagar et al. 2017).The current version (2.0) utilises all Landsat observations (5, 7, and 8) for Australian coastal regions (excluding off-shore Territories) between 1986 and 2016 (inclusive).

ITEM v2.0 has implemented an improved tidal modelling framework (see Sagar et al. 2018) over that utilised in ITEM v1.0. The expanded Landsat archive within the Digital Earth Australia (DEA) has also enabled the model extent to be increased to cover a number of offshore reefs, including the full Great Barrier Reef and southern sections of the Torres Strait Islands. 
The DEA archive and new tidal modelling framework has improved the coverage and quality of the ITEM v2.0 relative extents model, particularly in regions where AGDC cell boundaries in ITEM v1.0 produced discontinuities or the imposed v1.0 cell structure resulted in poor quality tidal modelling (see Sagar et al. 2017).
For service status information, see https://status.dea.ga.gov.au""",

                # Included as a keyword  for the layer
                "type": "ITEM v2.0.0",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "ITEM_V2.0.0",
                # The Datacube name for the associated data product
                "product_name": "item_v2",
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": ["relative"],
                "apply_solar_corrections": False,
                "legend": {
                    "url": "https://data.dea.ga.gov.au/item_v2/v2.0.1/relative/ITEM_REL_Legend.png"
                },
                "wcs_default_bands": ["relative"],
                "styles": [
                    {
                        "name": "relative_layer",
                        "title": "relative layer",
                        "abstract": "The Relative Extents Model (item_v2) 25m v2.0.0",
                        "needed_bands": ["relative"],
                        "color_ramp": [
                            {
                                'value': 0.0,
                                'color': '#000000',
                                'alpha': 0.0
                            },
                            {
                                'value': 1.0,
                                'color': '#d7191c',
                                'alpha': 1.0
                            },
                            {

                                'value': 2.0,
                                'color': '#ec6e43',
                            },
                            {
                                'value': 3.0,
                                'color': '#fdb96e',
                            },
                            {

                                'value': 4.0,
                                'color': '#fee7a4',
                            },
                            {
                                'value': 5.0,
                                'color': '#e7f5b7',
                            },
                            {

                                'value': 6.0,
                                'color': '#b7e1a7',
                            },
                            {
                                'value': 7.0,
                                'color': '#74b6ad',
                            },
                            {

                                'value': 8.0,
                                'color': '#2b83ba'
                            },
                            {
                                'value': 9.0,
                                'color': '#000000',
                                'alpha': 0.0
                            },
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 10.0,
                            "major_ticks": 1
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "relative_layer",
            },
            {
                # Included as a keyword  for the layer
                "label": "Confidence Layer",
                "abstract": """
The Intertidal Extents Model (ITEM v2.0) product analyses GA’s historic archive of satellite imagery to derive a model of the spatial extents of the intertidal zone throughout the tidal cycle. The model can assist in understanding the relative elevation profile of the intertidal zone, 
delineating exposed areas at differing tidal heights and stages.

The product differs from previous methods used to map the intertidal zone which have been predominately focused on analysing a small number of individual satellite images per location (e.g Ryu et al., 2002; Murray et al., 2012). 
By utilising a full 30 year time series of observations and a global tidal model (Egbert and Erofeeva, 2002), the methodology enables us to overcome the requirement for clear, high quality observations acquired concurrent to the time of high and low tide.

*Accuracy and limitations*
                  
Due the sun-synchronous nature of the various Landsat sensor observations; it is unlikely that the full physical extents of the tidal range in any cell will be observed. Hence, terminology has been adopted for the product to reflect the highest modelled tide observed in a given cell (HOT) and the lowest modelled tide observed (LOT) (see Sagar et al. 2017). These measures are relative to Mean Sea Level, and have no consistent relationship to Lowest (LAT) and Highest Astronomical Tide (HAT).

The inclusion of the lowest (LMT) and highest (HMT) modelled tide values for each tidal polygon indicates the highest and lowest tides modelled for that location across the full time series by the OTPS model. The relative difference between the LOT and LMT (and HOT and HMT) heights gives an indication of the extent of the tidal range represented in the Relative Extents Model.

As in ITEM v1.0, v2.0 contains some false positive land detection in open ocean regions. These are a function of the lack of data at the extremes of the observed tidal range, and features like glint and undetected cloud in these data poor regions/intervals. Methods to isolate and remove these features are in development for future versions. Issues in the DEA archive and data noise in the Esperance, WA region off Cape Le Grande and Cape Arid (Polygons 236,201,301) has resulted in significant artefacts in the model, and use of the model in this area is not recommended.
                
The Confidence layer is designed to assess the reliability of the Relative Extent Model. Within each tidal range percentile interval, the pixel-based standard deviation of the NDWI values for all observations in the interval subset is calculated. The average standard deviation across all tidal range intervals is then calculated and retained as a quality indicator in this product layer.

The Confidence Layer reflects the pixel based consistency of the NDWI values within each subset of observations, based on the tidal range. Higher standard deviation values indicate water classification changes not based on the tidal cycle, and hence lower confidence in the extent model.

Possible drivers of these changes include:

Inadequacies of the tidal model, due perhaps to complex coastal bathymetry or estuarine structures not captured in the model. These effects have been reduced in ITEM v2.0 compared to previous versions, through the use of an improved tidal modelling frameworkChange in the structure and exposure of water/non-water features NOT driven by tidal variation. 
For example, movement of sand banks in estuaries, construction of man-made features (ports etc.).Terrestrial/Inland water features not influenced by the tidal cycle.
File naming:
THE RELATIVE EXTENTS MODEL v2.0
ITEM_REL_<TIDAL POLYGON NUMBER>_<LONGITUDE>_<LATITUDE>
TIDAL POLYGON NUMBER relates to the id of the tidal polygon referenced by the file
LONGITUDE is the longitude of the centroid of the tidal polygon
LATITUDE is the latitude of the centroid of the tidal polygon

THE CONFIDENCE LAYER v2.0
ITEM_STD_<TIDAL POLYGON NUMBER>_<LONGITUDE>_<LATITUDE>
TIDAL POLYGON NUMBER relates to the id of the tidal polygon referenced by the file
LONGITUDE is the longitude of the centroid of the tidal polygon
LATITUDE is the latitude of the centroid of the tidal polygon

*Overview*

The Intertidal Extents Model product is a national scale gridded dataset characterising the spatial extents of the exposed intertidal zone, at intervals of the observed tidal range (Sagar et al. 2017).The current version (2.0) utilises all Landsat observations (5, 7, and 8) for Australian coastal regions (excluding off-shore Territories) between 1986 and 2016 (inclusive).

ITEM v2.0 has implemented an improved tidal modelling framework (see Sagar et al. 2018) over that utilised in ITEM v1.0. The expanded Landsat archive within the Digital Earth Australia (DEA) has also enabled the model extent to be increased to cover a number of offshore reefs, including the full Great Barrier Reef and southern sections of the Torres Strait Islands. 
The DEA archive and new tidal modelling framework has improved the coverage and quality of the ITEM v2.0 relative extents model, particularly in regions where AGDC cell boundaries in ITEM v1.0 produced discontinuities or the imposed v1.0 cell structure resulted in poor quality tidal modelling (see Sagar et al. 2017).
For service status information, see https://status.dea.ga.gov.au""",
                # Included as a keyword  for the layer
                "type": "ITEM v2.0.0",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "ITEM_V2.0.0_Conf",
                # The Datacube name for the associated data product
                "product_name": "item_v2_conf",
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "fuse_func": "datacube_wms.wms_utils.item_fuser",
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": ["stddev"],
                "apply_solar_corrections": False,
                "legend": {
                    "styles": ["confidence_layer"]
                },
                "wcs_default_bands": ["stddev"],
                "styles": [
                    {
                        "name": "confidence_layer",
                        "title": "confidence layer",
                        "abstract": "The Confidence layer (item_v2_conf) 25m v2.0.0",
                        "needed_bands": ["stddev"],
                        "color_ramp": [
                            {
                                'value': 0.0,
                                'color': '#2b83ba',
                                'alpha': 0.0
                            },
                            {

                                'value': 0.01,
                                'color': '#2b83ba',
                                'legend': {
                                    "prefix": "<"
                                }
                            },
                            {
                                'value': 0.055,
                                'color': '#55a1b2',
                            },
                            {
                                'value': 0.1,
                                'color': '#80bfab',
                            },
                            {
                                'value': 0.145,
                                'color': '#abdda4',
                            },
                            {
                                'value': 0.19,
                                'color': '#c7e8ad',
                            },
                            {
                                'value': 0.235,
                                'color': '#e3f3b6',
                            },
                            {
                                'value': 0.28,
                                'color': '#fdbf6f',
                            },
                            {
                                'value': 0.325,
                                'color': '#e37d1c',
                            },
                            {
                                'value': 0.37,
                                'color': '#e35e1c',
                            },
                            {
                                'value': 0.415,
                                'color': '#e31a1c',
                            },
                            {
                                'value': 0.46,
                                'color': '#e31a1c',
                            },
                            {
                                'value': 0.505,
                                'color': '#e31a1c',
                            },
                            {
                                'value': 0.55,
                                'color': '#e31a1c',
                                'legend': {
                                    "prefix": ">"
                                }
                            },
                        ],
                        "legend": {
                            "units": "NDWI standard deviation"
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "confidence_layer",
            },
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "water_bodies",
        "title": "Projects",
        "abstract": "Projects",
        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
#            {
#                # Included as a keyword  for the layer
#                "label": "Water Bodies",
#                "abstract": "NSW Water Bodies Project"
#                            "For service status information, see https://status.dea.ga.gov.au",
#                # Included as a keyword  for the layer
#                "type": "NSW",
#                # Included as a keyword  for the layer
#                "variant": "25m",
#                # The WMS name for the layer
#                "name": "water_bodies",
#                # The Datacube name for the associated data product
#                "product_name": "water_bodies",
#                "min_zoom_factor": 15.0,
#                "zoomed_out_fill_colour": [150, 180, 200, 160],
#                "time_zone": 9,
#                "extent_mask_func": lambda data, band: data[band] != 65535,
#                # include links to csv, {dam_id: 2611} becomes ".../026/02611.csv"
#                "feature_info_include_custom": lambda data: {
#                    'timeseries': f"https://data.dea.ga.gov.au"
#                    f"/projects/WaterBodies/feature_info/"
#                    f"{data['dam_id'] // 100:03}/{data['dam_id']:05}.csv"
#                },
#                "ignore_info_flags": [],
#                "data_manual_merge": False,
#                "always_fetch_bands": ["dam_id"],
#                "apply_solar_corrections": False,
#                "legend": {
#                    "styles": []
#                },
#                "wcs_default_bands": ["dam_id"],
#                "styles": [
#                    {
#                        "name": "dam_id",
#                        "title": "Water Body",
#                        "abstract": "",
#                        "needed_bands": ["dam_id"],
#                        "color_ramp": [
#                            {
#                                'value': 0,
#                                'color': '#11ccff',
#                                'alpha': 1.0
#                            },
#                            {
#                                'value': 65534,
#                                'color': '#11ccff',
#                                'alpha': 1.0
#                            },
#                        ],
#                        "legend": {
#                        }
#                    },
#                ],
#                # Default style (if request does not specify style)
#                # MUST be defined in the styles list above.
#                # (Looks like Terria assumes this is the first style in the list, but this is
#                #  not required by the standard.)
#                "default_style": "dam_id",
#            },
            {
                # Included as a keyword  for the layer
                "label": "HAP",
                # Included as a keyword  for the layer
                "type": "historical airborne photography",
                # Included as a keyword  for the layer
                "variant": "munged",
                # The WMS name for the layer
                "name": "historical_airborne_photography",
                # The Datacube name for the associated data product
                "product_name": "historical_airborne_photography",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 500.0,
                # Min zoom factor (above) works well for small-tiled requests, (e.g. 256x256 as sent by Terria).
                # However, for large-tiled requests (e.g. as sent by QGIS), large and intensive queries can still
                # go through to the datacube.
                # max_datasets_wms specifies a maximum number of datasets that a GetMap request can retrieve.
                # Indicatative polygons are displayed if a request exceeds the limits imposed by EITHER max_dataset_wms
                # OR min_zoom_factor.
                # max_datasets_wms should be set in conjunction with min_zoom_factor so that Terria style 256x256
                # tiled requests respond consistently - you never want to see a mixture of photographic tiles and polygon
                # tiles at a given zoom level.  i.e. max_datasets_wms should be greater than the number of datasets
                # required for most intensive possible photographic query given the min_zoom_factor.
                # Note that the ideal value may vary from product to product depending on the size of the dataset
                # extents for the product.
                # Defaults to zero, which is interpreted as no dataset limit.
                # 6 seems to work with a min_zoom_factor of 500.0 for "old-style" Net-CDF albers tiled data.
                "max_datasets_wms": 6,
                # max_datasets_wcs is the WCS equivalent of max_datasets_wms.  The main requirement for setting this
                # value is to avoid gateway timeouts on overly large WCS requests (and reduce server load).
                "max_datasets_wcs": 16,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],

                'wcs_default_bands':['Band_1'],

                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                # LS7:  http://www.indexdatabase.de/db/s-single.php?id=8
                # LS8:  http://www.indexdatabase.de/db/s-single.php?id=168
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "simple_gray",
                        "title": "Simple gray",
                        "abstract": "Simple grayscale image",
                        "components": {
                            "red": {
                                "Band_1": 1.0
                            },
                            "green": {
                                "Band_1": 1.0
                            },
                            "blue": {
                                "Band_1": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 255]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_gray",
            }
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "National ASTER Map",
        "title": "National ASTER Map of Australia",
        "abstract": """
This datsaet comprises a set of 14+ geoscience products made up of mosaiced ASTER scenes across Australia.
The individual geoscience products are a compbination of bands and band ratios to highlight different mineral groups and parameters including:
False colour composite
CSIRO Landsat TM Regolith Ratios
Green vegetation content
Ferric oxide content
Ferric oxide composition
Ferrous iron index
Opaque index
AlOH group content
AlOH group composition
Kaolin group index
FeOH group content
MgOH group content
MgOH group composition
Ferrous iron content in MgOH/carbonate""",
        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "False Colour Mosaic",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
False colour RGB composite

Red: B3

Green: B2

Blue: B1

(red = green vegetation)

Use this image to help understand non-geological differences within and between ASTER scenes caused by green vegetation (red), fire scars, thin and thick cloud and cloud shadows.

Use band 2 only for a gray-scale background to the content, composition and index colour products.""",
                # The WMS name for the layer
                "name": "aster_false_colour",
                # The Datacube name for the associated data product
                "product_name": "aster_false_colour",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                "wcs_default_bands": ["Band_1", "Band_2", "Band_3"],
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
                        "name": "false_colour",
                        "title": "False Colour",
                        "abstract": "Simple false-colour image using ASTER Bands 3 as red, 2 as green and 1 as blue",
                        "components": {
                            "red": {
                                "Band_1": 1.0
                            },
                            "green": {
                                "Band_2": 1.0
                            },
                            "blue": {
                                "Band_3": 1.0
                            }
                        },
                        "scale_range": [0.0, 255.0]
                    },
                    {
                        "name": "gray",
                        "title": "B2 Grayscale",
                        "abstract": "Simple grayscale image using ASTER Band 2",
                        "components": {
                            "red": {
                                "Band_2": 1.0
                            },
                            "green": {
                                "Band_2": 1.0
                            },
                            "blue": {
                                "Band_2": 1.0
                            }
                        },
                        "scale_range": [0.0, 255.0]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "false_colour",
            },  # ASTER False Colour
            {
                # Included as a keyword  for the layer
                "label": "Regolith Ratios",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
3 band RGB composite

Red: B3/B2

Green: B3/B7

Blue: B4/B7

(white = green vegetation)

Use this image to help interpret:

(1) the amount of green vegetation cover (appears as white);

(2) basic spectral separation (colour) between different regolith and geological units and regions/provinces; and

(3) evidence for unmasked cloud (appears as green).""",
                # The WMS name for the layer
                "name": "aster_regolith_ratios",
                # The Datacube name for the associated data product
                "product_name": "aster_regolith_ratios",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                "wcs_default_bands": ["Band_1", "Band_2", "Band_3"],
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
                                "Band_1": 1.0
                            },
                            "green": {
                                "Band_2": 1.0
                            },
                            "blue": {
                                "Band_3": 1.0
                            }
                        },
                        "scale_range": [0.0, 255.0]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },  # ASTER Regolith Ratios
            {
                # Included as a keyword  for the layer
                "label": "AlOH Group Composition",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: B5/B7

Blue is well ordered kaolinite, Al-rich muscovite/illite, paragonite, pyrophyllite

Red is Al-poor (Si-rich) muscovite (phengite)

Useful for mapping:

(1) exposed saprolite/saprock is often white mica or Al-smectite (warmer colours) whereas transported materials are often kaolin-rich (cooler colours);

(2) clays developed over carbonates, especially Al-smectite (montmorillonite, beidellite) will produce middle to warmers colours;

(3) stratigraphic mapping based on different clay-types; and

(4) lithology-overprinting hydrothermal alteration, e.g. Si-rich and K-rich phengitic mica (warmer colours).

Combine with Ferrous iron in MgOH and FeOH content products to look for evidence of overlapping/juxtaposed potassic metasomatism in ferromagnesian parents rocks (e.g. Archaean greenstone associated Au mineralisation) +/- associated distal propyllitic alteration (e.g. chlorite, amphibole).""",
                # The WMS name for the layer
                "name": "aster_aloh_group_composition",
                # The Datacube name for the associated data product
                "product_name": "aster_aloh_group_composition",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B5/B7 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "0.9"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "1.3"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue is well ordered kaolinite,\nRed is Al-poor (Si-rich) muscovite (phengite)",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER AlOH Group Composition
            {
                # Included as a keyword  for the layer
                "label": "AlOH Group Content",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: (B5+B7)/B6

Blue is low abundance

Red is high abundance

(potentially includes: phengite, muscovite, paragonite, lepidolite, illite, brammalite, montmorillonite, beidellite, kaolinite, dickite)

Useful for mapping:

(1) exposed saprolite/saprock;

(2) clay-rich stratigraphic horizons;

(3) lithology-overprinting hydrothermal phyllic (e.g. white mica) alteration; and

(4) clay-rich diluents in ore systems (e.g. clay in iron ore).

Also combine with AlOH composition to help map:

(1) exposed in situ parent material persisting through “cover” which can be expressed as:

(a) more abundant AlOH content + (b) long-wavelength (warmer colour) AlOH composition (e.g. muscovite/phengite).""",
                # The WMS name for the layer
                "name": "aster_aloh_group_content",
                # The Datacube name for the associated data product
                "product_name": "aster_aloh_group_content",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "(B5+B7)/B6 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "2.0"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "2.25"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue is low content,\nRed is high content",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER AlOH Group Content
            {
                # Included as a keyword  for the layer
                "label": "FeOH Group Content",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: (B6+B8)/B7

Blue is low content,

Red is high content

(potentially includes: chlorite, epidote, jarosite, nontronite, gibbsite, gypsum, opal-chalcedony

Useful for mapping:

(1) jarosite (acid conditions) – in combination with ferric oxide content (high);

(2) gypsum/gibbsite – in combination with ferric oxide content (low);

(3) magnesite - in combination with ferric oxide content (low) and MgOH content (moderate-high);

(4) chlorite (e.g. propyllitic alteration) – in combination with Ferrous in MgOH (high); and

(5) epidote (calc-silicate alteration) – in combination with Ferrous in MgOH (low).""",
                # The WMS name for the layer
                "name": "aster_feoh_group_content",
                # The Datacube name for the associated data product
                "product_name": "aster_feoh_group_content",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                "wcs_default_bands": ["Band_1"],
                "legend": {
                    # "url": ""
                    "styles": ["ramp"]
                },
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
                        "name": "ramp",
                        "title": "(B6+B8)/B7 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "2.03"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "2.25"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue is low content,\nRed is high content",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER FeOH Group Content
            {
                # Included as a keyword  for the layer
                "label": "Ferric Oxide Composition",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: B2/B1

Blue-cyan is goethite rich,

Green is hematite-goethite,

Red-yellow is hematite-rich

Useful For:

(1) Mapping transported materials (including palaeochannels) characterised by hematite (relative to geothite). Combine with AlOH composition to find co-located areas of hematite and poorly ordered kaolin to map transported materials; and 

(2) hematite-rish areas in drier conditions (eg above the water table) whereas goethite-rich in wetter conditions (eg at/below the water or areas recently exposed). May also be climate driven.""",
                # The WMS name for the layer
                "name": "aster_ferric_oxide_composition",
                # The Datacube name for the associated data product
                "product_name": "aster_ferric_oxide_composition",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B2/B1 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "0.5"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "3.3"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue-cyan is non-hematitie,\nRed-yellow is hematite-rich",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER Ferric Oxide Composition
            {
                # Included as a keyword  for the layer
                "label": "Ferric Oxide Content",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: B4/B3

Blue is low abundance,

Red is high abundance

Useful for:

(1) Exposed iron ore (hematite-goethite).Use in combination with the “Opaques index” to help separate/map dark (a) surface lags (e.g. maghemite gravels) which can be misidentified in visible and false colour imagery; and (b) magnetite in BIF and/or bedded iron ore; and

(2) Acid conditions: combine with FeOH Group content to help map jarosite which will have high values in both products.

Mapping hematite versus goethite mapping is NOT easily achieved as ASTER’s spectral bands were not designed to capture diagnostic iron oxide spectral behaviour.

However, some information on visible colour relating in part to differences in hematite and/or goethite content can be obtained using a ratio of B2/B1 especially when this is masked using a B4/B3 to locate those pixels with sufficient iro oxide content.
""",
                # The WMS name for the layer
                "name": "aster_ferric_oxide_content",
                # The Datacube name for the associated data product
                "product_name": "aster_ferric_oxide_content",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B4/B3 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "1.1"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "2.1"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue is low abundance,\nRed is high abundance",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER Ferric Oxide Content
            {
                # Included as a keyword  for the layer
                "label": "Ferrous Iron Content in MgOH",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: B5/B4

Blue is low ferrous iron content in carbonate and MgOH minerals like talc and tremolite.

Red is high ferrous iron content in carbonate and MgOH minerals like chlorite and actinolite.

Useful for mapping:

(1) un-oxidised “parent rocks” – i.e. mapping exposed parent rock materials (warm colours) in transported cover; 

(2) talc/tremolite (Mg-rich – cool colours) versus actinolite (Fe-rich – warm colours);

(3) ferrous-bearing carbonates (warm colours) potentially associated with metasomatic “alteration”;

(4) calcite/dolomite which are ferrous iron-poor (cool colours); and

(5) epidote, which is ferrous iron poor (cool colours) – in combination with FeOH content product (high).""",
                # The WMS name for the layer
                "name": "aster_ferrous_iron_content_in_mgoh",
                # The Datacube name for the associated data product
                "product_name": "aster_ferrous_iron_content_in_mgoh",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B5/B4 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "0.1"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "2.0"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue is low ferrous iron content,\nRed is high ferrous iron content",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER Ferrous Iron Content in MgOH
            {
                # Included as a keyword  for the layer
                "label": "Ferrous Iron Index",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: B5/B4

Blue is low abundance,

Red is high abundance

This product can help map exposed “fresh” (un-oxidised) rocks (warm colours) especially mafic and ultramafic lithologies rich in ferrous silicates (e.g. actinolite, chlorite) and/or ferrous carbonates (e.g. ferroan dolomite, ankerite, siderite).

Applying an MgOH Group content mask to this product helps to isolate ferrous bearing non-OH bearing minerals like pyroxenes (e.g. jadeite) from OH-bearing or carbonate-bearing ferrous minerals like actinolite or ankerite, respectively.

Also combine with the FeOH Group content product to find evidence for ferrous-bearing chlorite (e.g. chamosite).
""",
                # The WMS name for the layer
                "name": "aster_ferrous_iron_index",
                # The Datacube name for the associated data product
                "product_name": "aster_ferrous_iron_index",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B5/B4 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "0.75"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "1.025"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue is low abundance,\nRed is high abundance",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER Ferrous Iron Index
            {
                # Included as a keyword  for the layer
                "label": "Green Vegetation",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: B3/B2

Blue is low content,

Red is high content

Use this image to help interpret the amount of “obscuring/complicating” green vegetation cover.""",
                # The WMS name for the layer
                "name": "aster_green_vegetation",
                # The Datacube name for the associated data product
                "product_name": "aster_green_vegetation",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B3/B2 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "1.4"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "4"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue is low content,\nRed is high content",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER Green Vegetation
            {
                # Included as a keyword  for the layer
                "label": "Gypsum Index",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band Ratio: (B10+B12)/B11

Blue is low gypsum content,

Red is high gypsum content

Useful for mapping:

(1) evaporative environments (e.g. salt lakes) and associated arid aeolian systems (e.g. dunes);

(2) acid waters (e.g. from oxidising sulphides) invading carbonate rich materials including around mine environments; and

(3) hydrothermal (e.g. volcanic) systems.""",
                # The WMS name for the layer
                "name": "aster_gypsum_index",
                # The Datacube name for the associated data product
                "product_name": "aster_gypsum_index",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "(B10+B12)/B11 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "0.47"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "0.5"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue is low content,\nRed is high content",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER Gypsum Index
            {
                # Included as a keyword  for the layer
                "label": "Kaolin Group Index",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band Ratio: B6/B5

Blue is low content,

Red is high content

(potentially includes: pyrophyllite, alunite, well-ordered kaolinite)


Useful for mapping:

(1) different clay-type stratigraphic horizons;

(2) lithology-overprinting hydrothermal alteration, e.g. high sulphidation, “advanced argillic” alteration comprising pyrophyllite, alunite, kaolinite/dickite; and

(3) well-ordered kaolinite (warmer colours) versus poorly-ordered kaolinite (cooler colours) which can be used for mapping in situ versus transported materials, respectively.""",
                # The WMS name for the layer
                "name": "aster_kaolin_group_index",
                # The Datacube name for the associated data product
                "product_name": "aster_kaolin_group_index",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B6/B5 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "1.0"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "1.125"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue is low content,\nRed is high content",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER Kaolin Group Index
            {
                # Included as a keyword  for the layer
                "label": "MgOH Group Composition",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: B7/B8

Blue-cyan is magnesite-dolomite, amphibole, chlorite

Red is calcite, epidote, amphibole

Useful for mapping:

(1) exposed saprolite/saprock is often white mica or Al-smectite (warmer colours) whereas transported materials are often kaolin-rich (cooler colours);

(2) clays developed over carbonates, especially Al-smectite (montmorillonite, beidellite) will produce middle to warmers colours.

(3) stratigraphic mapping based on different clay-types; and

(4) lithology-overprinting hydrothermal alteration, e.g. Si-rich and K-rich phengitic mica (warmer colours).

Combine with Ferrous iron in MgOH and FeOH content products to look for evidence of overlapping/juxtaposed potassic metasomatism in ferromagnesian parents rocks (e.g. Archaean greenstone associated Au mineralisation) +/- associated distal propyllitic alteration (e.g. chlorite, amphibole).""",
                # The WMS name for the layer
                "name": "aster_mgoh_group_composition",
                # The Datacube name for the associated data product
                "product_name": "aster_mgoh_group_composition",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B7/B8 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "0.6"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "1.4"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue-cyan is magnesite-dolomite, amphibole, \nRed is calcite, epidote, amphibole",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER MgOH Group Composition
            {
                # Included as a keyword  for the layer
                "label": "MgOH Group Content",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: (B6+B9/(B7+B8)

Blue is low content,

Red is high content

(potentially includes: calcite, dolomite, magnesite, chlorite, epidote, amphibole, talc, serpentine)

Useful for mapping:

(1) “hydrated” ferromagnesian rocks rich in OH-bearing tri-octahedral silicates like actinolite, serpentine, chlorite and talc;

(2) carbonate-rich rocks, including shelf (palaeo-reef) and valley carbonates(calcretes, dolocretes and magnecretes); and

(3) lithology-overprinting hydrothermal alteration, e.g. “propyllitic alteration” comprising chlorite, amphibole and carbonate.

The nature (composition) of the silicate or carbonate mineral can be further assessed using the MgOH composition product.""",
                # The WMS name for the layer
                "name": "aster_mgoh_group_content",
                # The Datacube name for the associated data product
                "product_name": "aster_mgoh_group_content",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "(B6+B9/(B7+B8) ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "1.05"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "1.2"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue low content,\nRed is high content",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER MgOH Group Content
            {
                # Included as a keyword  for the layer
                "label": "Opaque Index",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: B1/B4

Blue is low abundance,

Red is high abundance

(potentially includes  carbon black (e.g. ash), magnetite, Mn oxides, and sulphides in unoxidised envornments

Useful for mapping:

(1) magnetite-bearing rocks (e.g. BIF);

(2) maghemite gravels;

(3) manganese oxides;

(4) graphitic shales.

Note 1: (1) and (4) above can be evidence for “reduced” rocks when interpreting REDOX gradients.

Combine with AlOH group Content (high values) and Composition (high values) products, to find evidence for any invading “oxidised” hydrothermal fluids which may have interacted with reduced rocks evident in the Opaques index product.""",
                # The WMS name for the layer
                "name": "aster_opaque_index",
                # The Datacube name for the associated data product
                "product_name": "aster_opaque_index",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B1/B4 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "0.4"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "0.9"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue low content,\nRed is high content",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER Opaque Index
            {
                # Included as a keyword  for the layer
                "label": "Silica Index",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: B13/B10

Blue is low silica content,

Red is high silica content

(potentially includes Si-rich minerals, such as quartz, feldspars, Al-clays)

Geoscience Applications:

Broadly equates to the silica content though the intensity (depth) of this reststrahlen feature is also affected by particle size &lt;250 micron.

Useful product for mapping:

(1) colluvial/alluvial materials;

(2) silica-rich (quartz) sediments (e.g. quartzites);

(3) silification and silcretes; and

(4) quartz veins.

Use in combination with quartz index, which is often correlated with the Silica index.""",
                # The WMS name for the layer
                "name": "aster_silica_index",
                # The Datacube name for the associated data product
                "product_name": "aster_silica_index",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B13/B10 ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "1.0"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "1.35"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue low silica content,\nRed is high silica content",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER Silica Index
            {
                # Included as a keyword  for the layer
                "label": "Quartz Index",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """
Band ratio: B11/(B10+B12)

Blue is low quartz content,

Red is high quartz content

Geoscience Applications:

Use in combination with Silica index to more accurately map “crystalline” quartz rather than poorly ordered silica (e.g. opal), feldspars and compacted clays.""",
                # The WMS name for the layer
                "name": "aster_quartz_index",
                # The Datacube name for the associated data product
                "product_name": "aster_quartz_index",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "s2b_ard_granule",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_quality",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
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
                    "styles": ["ramp"]
                },
                "wcs_default_bands": ["Band_1"],
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
                        "name": "ramp",
                        "title": "B11/(B10+B12) ",
                        "abstract": "",
                        "index_function": lambda data: data["Band_1"],
                        "needed_bands": ["Band_1"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0,
                                "legend": {
                                    "label": "0.50"
                                }
                            },
                            {
                                "value": 1,
                                "color": "#000000"
                            },
                            {
                                "value": 10,
                                "color": "#2d002b"
                            },
                            {
                                "value": 25,
                                "color": "#550071"
                            },
                            {
                                "value": 60,
                                "color": "#0400ff"
                            },
                            {
                                "value": 90,
                                "color": "#0098ff"
                            },
                            {
                                "value": 110,
                                "color": "#00ffff"
                            },
                            {
                                "value": 130,
                                "color": "#00ff94"
                            },
                            {
                                "value": 150,
                                "color": "#00ff2a"
                            },
                            {
                                "value": 170,
                                "color": "#3fff00"
                            },
                            {
                                "value": 210,
                                "color": "#ffee00"
                            },
                            {
                                "value": 230,
                                "color": "#ff8300"
                            },
                            {
                                "value": 255.0,
                                "color": "#ff0000",
                                "legend": {
                                    "label": "0.52"
                                }
                            }
                        ],
                        "legend": {
                            "units": "Blue low quartz content,\nRed is high quartz content",
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "ramp",
            },  # ASTER Quartz Index
        ],
    },
    {
        "name": "Fractional Cover",
        "title": "Fractional Cover",
        "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
        "products": [
            {
            # Included as a keyword  for the layer
            "label": "Fractional Cover Landsat 5",
            # Included as a keyword  for the layer
            "type": "100km tile",
            # Included as a keyword  for the layer
            "variant": "25m",
            "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 5 satellite

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ls5_fc_albers",
            # The Datacube name for the associated data product
            "product_name": "ls5_fc_albers",
            # The Datacube name for the associated pixel-quality product (optional)
            # The name of the associated Datacube pixel-quality product
            "pq_dataset": "wofs_albers",
            # The name of the measurement band for the pixel-quality product
            # (Only required if pq_dataset is set)
            "pq_band": "water",
            # Fuse function for pq data
            "pq_fuse_func": "datacube_wms.wms_utils.wofls_fuser",
            # Min zoom factor - sets the zoom level where the cutover from indicative polygons
            # to actual imagery occurs.
            "min_zoom_factor": 10.0,
            # The fill-colour of the indicative polygons when zoomed out.
            # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
            "zoomed_out_fill_colour": [ 150, 180, 200, 160],
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
            "legend": {
                "url": "https://data.dea.ga.gov.au/fractional-cover/fc-percentile/annual/v2.1.0/fcp_legend.png",
            },
            "wcs_default_bands": ["BS", "PV", "NPV"],
            "styles": [
                {
                    "name": "simple_fc",
                    "title": "Fractional Cover",
                    "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
                    "components": {
                        "red": {
                            "BS": 1.0
                        },
                        "green": {
                            "PV": 1.0
                        },
                        "blue": {
                            "NPV": 1.0
                        }
                    },
                    "scale_range": [0.0, 100.0],
                    "pq_masks": [
                        {
                            "flags": {
                                'dry': True
                            },
                        },
                        {
                            "flags": {
                                "terrain_or_low_angle": False,
                                "high_slope": False,
                                "cloud_shadow": False,
                                "cloud": False,
                                "sea": False
                            }
                        },
                    ]
                }
            ],
            # Default style (if request does not specify style)
            # MUST be defined in the styles list above.

            # (Looks like Terria assumes this is the first style in the list, but this is
            #  not required by the standard.)
            "default_style": "simple_fc",
            },
            {
            # Included as a keyword  for the layer
            "label": "Fractional Cover Landsat 7",
            # Included as a keyword  for the layer
            "type": "100km tile",
            # Included as a keyword  for the layer
            "variant": "25m",
            "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 7 satellite

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ls7_fc_albers",
            # The Datacube name for the associated data product
            "product_name": "ls7_fc_albers",
            # The Datacube name for the associated pixel-quality product (optional)
            # The name of the associated Datacube pixel-quality product
            "pq_dataset": "wofs_albers",
            # The name of the measurement band for the pixel-quality product
            # (Only required if pq_dataset is set)
            "pq_band": "water",
            # Fuse function for pq data
            "pq_fuse_func": "datacube_wms.wms_utils.wofls_fuser",
            # Min zoom factor - sets the zoom level where the cutover from indicative polygons
            # to actual imagery occurs.
            "min_zoom_factor": 10.0,
            # The fill-colour of the indicative polygons when zoomed out.
            # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
            "zoomed_out_fill_colour": [ 150, 180, 200, 160],
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
            "legend": {
                "url": "https://data.dea.ga.gov.au/fractional-cover/fc-percentile/annual/v2.1.0/fcp_legend.png",
            },
            "wcs_default_bands": ["BS", "PV", "NPV"],
            "styles": [
                {
                    "name": "simple_fc",
                    "title": "Fractional Cover",
                    "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
                    "components": {
                        "red": {
                            "BS": 1.0
                        },
                        "green": {
                            "PV": 1.0
                        },
                        "blue": {
                            "NPV": 1.0
                        }
                    },
                    "scale_range": [0.0, 100.0],
                    "pq_masks": [
                        {
                            "flags": {
                                'dry': True
                            },
                        },
                        {
                            "flags": {
                                "terrain_or_low_angle": False,
                                "high_slope": False,
                                "cloud_shadow": False,
                                "cloud": False,
                                "sea": False
                            }
                        },
                    ]
                }
            ],
            # Default style (if request does not specify style)
            # MUST be defined in the styles list above.

            # (Looks like Terria assumes this is the first style in the list, but this is
            #  not required by the standard.)
            "default_style": "simple_fc",
            },
            {
            # Included as a keyword  for the layer
            "label": "Fractional Cover Landsat 8",
            # Included as a keyword  for the layer
            "type": "100km tile",
            # Included as a keyword  for the layer
            "variant": "25m",
            "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 8 satellite

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ls8_fc_albers",
            # The Datacube name for the associated data product
            "product_name": "ls8_fc_albers",
            # The Datacube name for the associated pixel-quality product (optional)
            # The name of the associated Datacube pixel-quality product
            "pq_dataset": "wofs_albers",
            # The name of the measurement band for the pixel-quality product
            # (Only required if pq_dataset is set)
            "pq_band": "water",
            # Fuse function for pq data
            "pq_fuse_func": "datacube_wms.wms_utils.wofls_fuser",
            # Min zoom factor - sets the zoom level where the cutover from indicative polygons
            # to actual imagery occurs.
            "min_zoom_factor": 10.0,
            # The fill-colour of the indicative polygons when zoomed out.
            # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
            "zoomed_out_fill_colour": [ 150, 180, 200, 160],
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
            "legend": {
                    "url": "https://data.dea.ga.gov.au/fractional-cover/fc-percentile/annual/v2.1.0/fcp_legend.png",
            },
            "wcs_default_bands": ["BS", "PV", "NPV"],
            "styles": [
                {
                    "name": "simple_fc",
                    "title": "Fractional Cover",
                    "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
                    "components": {
                        "red": {
                            "BS": 1.0
                        },
                        "green": {
                            "PV": 1.0
                        },
                        "blue": {
                            "NPV": 1.0
                        }
                    },
                    "scale_range": [0.0, 100.0],
                    "pq_masks": [
                        {
                            "flags": {
                                'dry': True
                            },
                        },
                        {
                            "flags": {
                                "terrain_or_low_angle": False,
                                "high_slope": False,
                                "cloud_shadow": False,
                                "cloud": False,
                                "sea": False
                            }
                        },
                    ]
                }
            ],
            # Default style (if request does not specify style)
            # MUST be defined in the styles list above.

            # (Looks like Terria assumes this is the first style in the list, but this is
            #  not required by the standard.)
            "default_style": "simple_fc",
            },
            {
            # Included as a keyword  for the layer
            "label": "Fractional Cover Combined",
            # Included as a keyword  for the layer
            "type": "100km tile",
            # Included as a keyword  for the layer
            "variant": "25m",
            "abstract": """
Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 5, 7 and 8 satellites

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "fc_albers_combined",
            # The Datacube name for the associated data product
            "multi_product": True,
            "product_name": ["ls5_fc_albers", "ls7_fc_albers", "ls8_fc_albers"],
            # The Datacube name for the associated pixel-quality product (optional)
            # The name of the associated Datacube pixel-quality product
            "pq_dataset": ["wofs_albers", "wofs_albers", "wofs_albers"],
            # The name of the measurement band for the pixel-quality product
            # (Only required if pq_dataset is set)
            "pq_band": "water",
            # Fuse function for pq data
            "pq_fuse_func": "datacube_wms.wms_utils.wofls_fuser",
            # Min zoom factor - sets the zoom level where the cutover from indicative polygons
            # to actual imagery occurs.
            "min_zoom_factor": 10.0,
            # The fill-colour of the indicative polygons when zoomed out.
            # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
            "zoomed_out_fill_colour": [ 150, 180, 200, 160],
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
            "legend": {
                    "url": "https://data.dea.ga.gov.au/fractional-cover/fc-percentile/annual/v2.1.0/fcp_legend.png",
            },
            "wcs_default_bands": ["BS", "PV", "NPV"],
            "styles": [
                {
                    "name": "simple_fc",
                    "title": "Fractional Cover",
                    "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
                    "components": {
                        "red": {
                            "BS": 1.0
                        },
                        "green": {
                            "PV": 1.0
                        },
                        "blue": {
                            "NPV": 1.0
                        }
                    },
                    "scale_range": [0.0, 100.0],
                    "pq_masks": [
                        {
                            "flags": {
                                'dry': True
                            },
                        },
                        {
                            "flags": {
                                "terrain_or_low_angle": False,
                                "high_slope": False,
                                "cloud_shadow": False,
                                "cloud": False,
                                "sea": False
                            }
                        },
                    ]
                }
            ],
            # Default style (if request does not specify style)
            # MUST be defined in the styles list above.

            # (Looks like Terria assumes this is the first style in the list, but this is
            #  not required by the standard.)
            "default_style": "simple_fc",
            },
        ]
    }
]

