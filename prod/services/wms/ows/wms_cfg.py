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
    "url": "https://ows.services.dea.ga.gov.au",
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
    # Max tile height/width.  If not specified, default to 256x256
    "max_width": 512,
    "max_height": 512,

    # Optional config for all services (WMS and/or WCS) - may be set to blank/empty, no defaults
    "abstract": """Digital Earth Australia OGC Web Services""",
    "keywords": [
        "geomedian",
        "WOfS",
        "mangrove",
        "landsat",
        "australia",
        "time-series",
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
                    "For more information, see http://pid.geoscience.gov.au/dataset/ga/120374",

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

]
