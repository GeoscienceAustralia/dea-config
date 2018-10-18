# Static config for the wms metadata.
response_cfg = {
    "Access-Control-Allow-Origin": "*",  # CORS header
}

service_cfg = {
    ## Which web service(s) should be supported by this instance
    "wcs": True,
    "wms": True,

    ## Required config for WMS and/or WCS
    # Service title - appears e.g. in Terria catalog
    "title": "Digital Earth Australia - OGC Web Services",
    # Service URL.  Should a fully qualified URL
    "url": "https://ows.services.devkube.dea.ga.gov.au",
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
        "abstract": "Data is only visible at higher resolutions; when zoomed-out the available area will be displayed "
                    "as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite "
                    "mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian "
                    "image is the statistical median of all observations for that pixel from a calendar year. "
                    "Annual mosaics are available for the following years: "
                    "Landsat 5: 1988 to 1999, 2004 to 2007, 2009 to 2011; "
                    "Landsat 7: 2000 to 2017; "
                    "Landsat 8: 2013 to 2017; "
                    "For more information, see http://pid.geoscience.gov.au/dataset/ga/120374"
                    "For product definition, see http://dea-public-data.s3-ap-southeast-2.amazonaws.com/geomedian-australia/v2.1.0/Product%20Description.pdf",

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
                                "value": -1.0,
                                "color": "#FFFFFF",
                                "alpha": 0.0
                            },
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
                                "value": -1.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
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
                "label": "Landsat 7",
                # Included as a keyword  for the layer
                "type": "Annual Geomedian",
                # Included as a keyword  for the layer
                "variant": "25m",
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
                                "value": -1.0,
                                "color": "#FFFFFF",
                                "alpha": 0.0
                            },
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
                                "value": -1.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
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
                "label": "Landsat 5",
                # Included as a keyword  for the layer
                "type": "Annual Geomedian",
                # Included as a keyword  for the layer
                "variant": "25m",
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
                                "value": -1.0,
                                "color": "#FFFFFF",
                                "alpha": 0.0
                            },
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
                                "value": -1.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
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
    Landsat 8: 2013 to 2017""",
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
    Landsat 8: 2013 to 2017""",
                # The WMS name for the layer
                "name": "ls8_barest_earth_mosaic",
                # The Datacube name for the associated data product
                "product_name": "ls8_barest_earth_albers",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 35.0,
                # To render the blue box if the no. of datasets exceeds 1000
                # "max_datasets_wms": 1000,
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
                                "value": -1.0,
                                "color": "#FFFFFF",
                                "alpha": 0.0
                            },
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
in some locations dense dwarf/shrub mangroves that are less than 2 metres tall may be mis-labelled as woodland/open forest/closed forest.""",
                "type": "100km tile",
                "variant": "25m",
                "name": "mangrove_cover",
                "product_name": "mangrove_cover",
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
Water Observations from Space - Filtered Statistics is a set of statistical summaries of the water observations contained in Water Observations from Space.

This product is Water Observations from Space - Filtered Statistics, consisting of a Confidence layer that compares the Water Observations from Space - Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the Water Observations from Space - Statistics water summary where Confidence is low.
The Filtered Water Summary provides the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out.

This layer is Filtered Water Summary: A simplified version of the Water Summary, showing the frequency of water observations where the Confidence is above a cutoff level.
This layer gives a noise-reduced view of surface water across Australia. Even though confidence filtering is applied to the Filtered Water Summary, some cloud and shadow, and sensor noise does persist.

For more information please see: http://dea-public-data.s3-ap-southeast-2.amazonaws.com/WOfS/filtered_summary/v2.1.0/Product%20Description.pdf""",

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
                    "styles": ["WOfS_filtered_frequency"]
                },
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
                    }
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
Water Observations from Space - Statistics is a set of statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Statistics, a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Wet Count: how many times water was detected in observations that were clear

For more information please see: http://dea-public-data.s3-ap-southeast-2.amazonaws.com/WOfS/summary/v2.1.0/Product%20Description.pdf""",
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
Water Observations from Space - Statistics is a set of statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Statistics, a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Clear Count: how many times an area could be clearly seen (ie. not affected by clouds, shadows or other satellite observation problems)

For more information please see: http://dea-public-data.s3-ap-southeast-2.amazonaws.com/WOfS/summary/v2.1.0/Product%20Description.pdf""",
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
                                "value": 10,
                                "color": "#B21800"
                            },
                            {
                                "value": 25,
                                "color": "#FF4400"
                            },
                            {
                                "value": 50,
                                "color": "#FF8000"
                            },
                            {
                                "value": 100,
                                "color": "#FFA200"
                            },
                            {
                                "value": 150,
                                "color": "#FFC000"
                            },
                            {
                                "value": 200,
                                "color": "#FFD500"
                            },
                            {
                                "value": 250,
                                "color": "#FFF300"
                            },
                            {
                                "value": 300,
                                "color": "#E6FF00"
                            },
                            {
                                "value": 350,
                                "color": "#BCFF00"
                            },
                            {
                                "value": 400,
                                "color": "#89FF00"
                            },
                            {
                                "value": 500,
                                "color": "#68C400"
                            },
                            {
                                "value": 600,
                                "color": "#44C400"
                            },
                            {
                                "value": 700,
                                "color": "#03B500"
                            },
                            {
                                "value": 800,
                                "color": "#039500"
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
Water Observations from Space - Statistics is a set of statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - Statistics, a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage)

For more information please see: http://dea-public-data.s3-ap-southeast-2.amazonaws.com/WOfS/summary/v2.1.0/Product%20Description.pdf""",
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
                    "styles": ["WOfS_frequency"]
                },
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
Water Observations from Space - Filtered Statistics is a set of statistical summaries of the water observations contained in Water Observations from Space.

This product is Water Observations from Space - Filtered Statistics, consisting of a Confidence layer that compares the Water Observations from Space - Statistics water summary to other national water datasets, and the Filtered Water Summary which uses the Confidence to mask areas of the Water Observations from Space - Statistics water summary where Confidence is low.
The Filtered Water Summary provides the long term understanding of the recurrence of water in the landscape, with much of the noise due to misclassification filtered out.

This layer is Confidence: the degree of agreement between water shown in the Water Summary and other national datasets.
The Confidence layer provides understanding of whether the water shown in the Water Summary agrees with where water should exist in the landscape, such as due to sloping land or whether water has been detected in a location by other means.

For more information please see: http://dea-public-data.s3-ap-southeast-2.amazonaws.com/WOfS/filtered_summary/v2.1.0/Product%20Description.pdf""",

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
                "styles": [
                    {
                        "name": "wofs_confidence",
                        "title": "Confidence",
                        "abstract": "WOfS Confidence",
                        "needed_bands": ["confidence"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#FFFFFF",
                                "alpha": 0
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
            }

        ],
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "Sentinel-2 NRT",
        "title": "Near Real-Time",
        "abstract": "This is a 30-day rolling archive of daily Sentinel-2 Near Real Time data. "
                    "Data is only visible at higher resolutions: when zoomed-out the available areas for that day "
                    "will be displayed as shaded regions. The Near Real-Time capability provides analysis-ready data "
                    "that is processed on receipt using the best-available ancillary information at the time to "
                    "provide atmospheric corrections. For more information see "
                    "http://pid.geoscience.gov.au/dataset/ga/122229",
        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "Sentinel 2B",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "Surface Reflectance",
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
                    "styles": ["ndvi", "ndwi"]
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
                                "value": -1.0,
                                "color": "#FFFFFF",
                                "alpha": 0.0
                            },
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
                        "index_function": lambda data: (data["nbart_green"] - data["nbart_nir_1"]) / (data["nbart_nir_1"] + data["nbart_green"]),
                        "needed_bands": ["nbart_green", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -1.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
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
                "label": "Sentinel 2A",
                # Included as a keyword  for the layer
                "type": "",
                # Included as a keyword  for the layer
                "variant": "Surface Reflectance",
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
                    "styles": ["ndvi", "ndwi"]
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
                                "value": -1.0,
                                "color": "#FFFFFF",
                                "alpha": 0.0
                            },
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
                        "index_function": lambda data: (data["nbart_green"] - data["nbart_nir_1"]) / (data["nbart_nir_1"] + data["nbart_green"]),
                        "needed_bands": ["nbart_green", "nbart_nir_1"],
                        "color_ramp": [
                            {
                                "value": -1.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
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
                Geomorphology 245, 51–61.""",
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
                    "url": "https://s3-ap-southeast-2.amazonaws.com/dea-public-data/multi-scale-topographic-position/mstp_legend.png",
                    # "styles": ["mstp_rgb"]
                },
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
                            "distribution of weathering processes occurring within the upper regolith.",
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
                            "legend_values": [1, 6],
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
Fractional Cover Percentiles version 2.0.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time.  The percentile summaries are designed to make it easier to analyse and interpret fractional cover.  For example the 90th percentile of bare soil for a particular year will identify areas that have experienced a high portion of bare soil during that year.  The fractional cover algorithm was developed by the Joint Remote Sensing Research Program.
This contains a (10th, 50th and 90th percentile) for green vegetation observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.
""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_green_veg",
                "product_name": "fc_percentile_albers_annual",
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
                "styles": [
                    {
                        "name": "green_veg_10",
                        "title": "10th Percentile",
                        "abstract": "10th Percentile of Green Vegetation",
                        "needed_bands": ["PV_PC_10"],
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
                        ]
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
                        ]
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
                        ]
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
Fractional Cover Percentiles version 2.0.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time.  The percentile summaries are designed to make it easier to analyse and interpret fractional cover.  For example the 90th percentile of bare soil for a particular year will identify areas that have experienced a high portion of bare soil during that year.  The fractional cover algorithm was developed by the Joint Remote Sensing Research Program.
This contains a (10th, 50th and 90th percentile) for non-green vegetation observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.
""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_non_green_veg",
                "product_name": "fc_percentile_albers_annual",
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
                "styles": [
                    {
                        "name": "non_green_veg_10",
                        "title": "10th Percentile",
                        "abstract": "10th Percentile of Non Green Vegetation",
                        "needed_bands": ["NPV_PC_10"],
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
                        ]
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
                        ]
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
                        ]
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
Fractional Cover Percentiles version 2.0.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time.  The percentile summaries are designed to make it easier to analyse and interpret fractional cover.  For example the 90th percentile of bare soil for a particular year will identify areas that have experienced a high portion of bare soil during that year.  The fractional cover algorithm was developed by the Joint Remote Sensing Research Program.
This contains a (10th, 50th and 90th percentile) for bare soil observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.
""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_bare_ground",
                "product_name": "fc_percentile_albers_annual",
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
                "styles": [
                    {
                        "name": "bare_ground_10",
                        "title": "10th Percentile",
                        "abstract": "10th Percentile of Bare Soil",
                        "needed_bands": ["BS_PC_10"],
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
                        ]
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
                        ]
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
                        ]
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
Fractional Cover Percentiles version 2.0.0, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time.  The percentile summaries are designed to make it easier to analyse and interpret fractional cover.  For example the 90th percentile of bare soil for a particular year will identify areas that have experienced a high portion of bare soil during that year.  The fractional cover algorithm was developed by the Joint Remote Sensing Research Program.
This contains a three band combination of the 50th Percentile for green vegetation, non green vegetation and bare soil observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.
""",
                "type": "100km tile",
                "variant": "25m",
                "name": "fcp_rgb",
                "product_name": "fc_percentile_albers_annual",
                "min_zoom_factor": 15.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data[band] != data[band].nodata,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                "legend": {
                    "url": "https://s3-ap-southeast-2.amazonaws.com/dea-public-data/fractional-cover/fc-percentile/annual/v2.1.0/fcp_legend.png",
                },
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
                        "scale_range": [0.0, 100.0]
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
                            "and ecological habitat mapping.",
                "type": "Grid",
                "variant": "nidem-v1.0.0 25m",
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
                "styles": [
                    {
                        "name": "NIDEM",
                        "title": "National Intertidal Digital Elevation Model",
                        "abstract": "National Intertidal Digital Elevation Model 25 m v1.0.0",
                        "needed_bands": ["nidem"],
                        "color_ramp": [
                            {
                                'value': -2.5,
                                'color': '#440154',
                                'alpha': 0
                            },
                            {

                                'value': -2.5,
                                'color': '#440154',
                                'legend': {
                                    'label': '<2.50 m'
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
                                'color': '#2e6b8d'
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
                                'value': -0.2,
                                'color': '#26ac7f',
                                'legend': {
                                    'label': '0.00 m'
                                }
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
                                    'label': '>1.50 m'
                                }
                            }
                        ],
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
]

