# Static config for the wms metadata.
from colour import Color
from bisect import bisect
import xarray
import numpy as np
from functools import partial
import math

response_cfg = {
    "Access-Control-Allow-Origin": "*",  # CORS header
}

service_cfg = {
    ## Which web service(s) should be supported by this instance
    "wcs": False,
    "wms": True,

    ## Required config for WMS and/or WCS
    # Service title - appears e.g. in Terria catalog
    "title": "WMS server for Water Observation from Space",
    # Service URL.  Should a fully qualified URL
    "url": "https://ows.wms.gadevs.ga",

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
    "abstract": """Historic Landsat imagery for Australia.""",
    "keywords": [
        "wofs"
        "wofls",
        "wofs_summary",
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
    "access_constraints": "",
}

__ramp_values__ = [
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
]

__clear_ramp_values__ = [
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
        "color": "#026900"
    }
]

__water_ramp_values__ = [
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
        "color": "#5700E3"
    }
]

def __generate_color_ramp__(ramp_values, delta):
    def frange(start, stop, step):
        i = start
        while i < stop:
            yield i
            i += step
    from colour import Color
    values = []
    ramp = []
    alpha = []
    low = None
    high = None
    for i, pair in enumerate(ramp_values):
        if i == 0:
            low = pair
            continue
        high = pair
        prev = len(values)
        alpha_low = low.get("alpha", 1.0)
        alpha_high = high.get("alpha", 1.0)
        values.extend(frange(low["value"], high["value"], delta))
        if alpha_high != alpha_low:
            alpha_range = frange(alpha_low, alpha_high, (alpha_high - alpha_low) / delta)
        else:
            alpha_range = [1.0 for i in range(len(values))]
        ramp.extend(Color(low["color"]).range_to(Color(high["color"]), len(values) - prev))
        alpha.extend(alpha_range)
        low = pair
    return zip(values, ramp, alpha)

__wofs_summary_ramp__ = __generate_color_ramp__(__ramp_values__, 0.01)
__clear_summary_ramp__ = __generate_color_ramp__(__clear_ramp_values__, 5)
__water_summary_ramp__ = __generate_color_ramp__(__water_ramp_values__, 1)

def __get_calculate_summary_ramp__(ramp_values, ramp_colors, ramp_alpha):
    def calculate_ramp(data, band, imgband):
        def process(values, colors, alpha, imgband, data):
            if math.isnan(data):
                return data
            i = bisect(values, data)
            i = i if i < len(colors) else i - 1
            c = colors[i]
            a = alpha[i]
            val = a if imgband is "alpha" else getattr(c, imgband)
            return (val * 255.0)

        p = partial(process, ramp_values, ramp_colors, ramp_alpha, imgband)

        ramped = data.copy(deep=True)
        ramped.values = np.vectorize(p)(data.values)
        return ramped

    return calculate_ramp

__calculate_wofs_summary_ramp__ = __get_calculate_summary_ramp__(*zip(*__wofs_summary_ramp__))
__calculate_wofs_clear_ramp__ = __get_calculate_summary_ramp__(*zip(*__clear_summary_ramp__))
__calculate_wofs_water_ramp__ = __get_calculate_summary_ramp__(*zip(*__water_summary_ramp__))


layer_cfg = [
    # Layer Config is a list of platform configs
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "WOfS",
        "title": "Water_Observation_from_Space",
        "abstract": "WOfS",

        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
            # Included as a keyword  for the layer
            "label": "WOfS_Summary",
            # Included as a keyword  for the layer
            "type": "WOfS_Summary",
            # Included as a keyword  for the layer
            "variant": "Summary",
            # The WMS name for the layer
            "name": "wofs_summary",
            # The Datacube name for the associated data product
            "product_name": "wofs_summary",
            # The Datacube name for the associated pixel-quality product (optional)
            # The name of the associated Datacube pixel-quality product
            #"pq_dataset": "wofs_albers",
            # The name of the measurement band for the pixel-quality product
            # (Only required if pq_dataset is set)
            #"pq_band": "water",
            # Min zoom factor - sets the zoom level where the cutover from indicative polygons
            # to actual imagery occurs.
            "min_zoom_factor": 0.0,
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

            "styles": [
                {
                    "name": "WOfS_frequency",
                    "title": " Wet and Dry Count",
                    "abstract": "WOfS summary showing the frequency of Wetness",
                    "needed_bands": ["frequency"],
                    "components": {
                        "red": {
                            "frequency": __calculate_wofs_summary_ramp__
                        },
                        "green": {
                            "frequency": __calculate_wofs_summary_ramp__
                        },
                        "blue": {
                            "frequency": __calculate_wofs_summary_ramp__
                        },
                        "alpha": {
                            "frequency": __calculate_wofs_summary_ramp__
                        }
                    },
                    "scale_range": [ 0, 255 ],
                },
                {
                    "name": "clear_observations",
                    "title": "Clear Observations Count",
                    "abstract": "WOfS summary showing the count of clear observations",
                    "needed_bands": ["count_clear"],
                    "components": {
                        "red": {
                            "count_clear": __calculate_wofs_clear_ramp__
                        },
                        "green": {
                            "count_clear": __calculate_wofs_clear_ramp__
                        },
                        "blue": {
                            "count_clear": __calculate_wofs_clear_ramp__
                        },
                        "alpha": {
                            "count_clear": __calculate_wofs_clear_ramp__
                        }
                    },
                    "scale_range": [ 0, 255 ],
                },
                {
                    "name": "water_observations",
                    "title": "Water Observations Count",
                    "abstract": "WOfS summary showing the count of water observations",
                    "needed_bands": ["count_wet"],
                    "components": {
                        "red": {
                            "count_wet": __calculate_wofs_water_ramp__
                        },
                        "green": {
                            "count_wet": __calculate_wofs_water_ramp__
                        },
                        "blue": {
                            "count_wet": __calculate_wofs_water_ramp__
                        },
                        "alpha": {
                            "count_wet": __calculate_wofs_water_ramp__
                        }
                    },
                    "scale_range": [ 0, 255 ],
                }
            ],
            # Default style (if request does not specify style)
            # MUST be defined in the styles list above.

            # (Looks like Terria assumes this is the first style in the list, but this is
            #  not required by the standard.)
            "default_style": "WOfS_frequency",
            }

        ],
    },
]
