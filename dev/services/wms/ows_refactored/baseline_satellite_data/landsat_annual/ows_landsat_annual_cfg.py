from ows_refactored.baseline_satellite_data.landsat_annual.band_ls_cfg import (
    bands_ls, bands_tmad)
from ows_refactored.baseline_satellite_data.landsat_annual.style_ls_cfg import (
    styles_ls_list, styles_tmad_list)
from ows_refactored.ows_reslim_cfg import (reslim_wms_min_zoom_15,
                                           reslim_wms_min_zoom_35)

layers = {
    "title": "DEA Surface Reflectance Calendar Year (Landsat)",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Surface Reflectance Calendar Year (Landsat 8 OLI-TIRS)",
            "name": "ls8_nbart_geomedian_annual",
            "abstract": """Surface Reflectance 25m Geomedian 2.0.0 (Landsat 8 OLI-TIRS)
The surface reflectance geomedian product provides an average cloud-free image over the given time period. The geomedian image is calculated with a multi-dimensional median, using all the spectral measurements from the satellite imagery at the same time in order to maintain the relationships among the measurements.
As of version 2.0.0, the geometric median products are available as annual datasets, each created from one calendar year of earth observation data from a single satellite.

Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 8: 2013 to 2017;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374
https://cmi.ga.gov.au/data-products/dea/140/dea-surface-reflectance-geomedian-landsat

For service status information, see https://status.dea.ga.gov.au
                    """,
            "product_name": "ls8_nbart_geomedian_annual",
            "bands": bands_ls,
            # "time_resolution": 'year',
            "resource_limits": reslim_wms_min_zoom_35,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["red", "green", "blue"],
            },
            "styling": {"default_style": "simple_rgb", "styles": styles_ls_list},
        },
        {
            "title": "DEA Surface Reflectance Calendar Year (Landsat 7 ETM+)",
            "name": "ls7_nbart_geomedian_annual",
            "abstract": """Surface Reflectance 25m Geomedian 2.0.0 (Landsat 7 ETM+)
The surface reflectance geomedian product provides an average cloud-free image over the given time period. The geomedian image is calculated with a multi-dimensional median, using all the spectral measurements from the satellite imagery at the same time in order to maintain the relationships among the measurements.

As of version 2.0.0, the geometric median products are available as annual datasets, each created from one calendar year of earth observation data from a single satellite.

Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 7: 2000 to 2017;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374
https://cmi.ga.gov.au/data-products/dea/140/dea-surface-reflectance-geomedian-landsat

For service status information, see https://status.dea.ga.gov.au
            """,
            "product_name": "ls7_nbart_geomedian_annual",
            "bands": bands_ls,
            "resource_limits": reslim_wms_min_zoom_35,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["red", "green", "blue"],
            },
            "styling": {"default_style": "simple_rgb", "styles": styles_ls_list},
        },
        {
            "title": "DEA Surface Reflectance Calendar Year (Landsat 5 TM)",
            "name": "ls5_nbart_geomedian_annual",
            "abstract": """Surface Reflectance 25m Geomedian 2.0.0 (Landsat 5 TM)
The surface reflectance geomedian product provides an average cloud-free image over the given time period. The geomedian image is calculated with a multi-dimensional median, using all the spectral measurements from the satellite imagery at the same time in order to maintain the relationships among the measurements.

As of version 2.0.0, the geometric median products are available as annual datasets, each created from one calendar year of earth observation data from a single satellite.

Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 5: 1988 to 1999, 2004 to 2007, 2009 to 2011;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374
https://cmi.ga.gov.au/data-products/dea/140/dea-surface-reflectance-geomedian-landsat
For service status information, see https://status.dea.ga.gov.au
                    """,
            "product_name": "ls5_nbart_geomedian_annual",
            "bands": bands_ls,
            "resource_limits": reslim_wms_min_zoom_35,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["red", "green", "blue"],
            },
            "styling": {"default_style": "simple_rgb", "styles": styles_ls_list},
        },
        {
            "title": "DEA Surface Reflectance Median Absolute Deviation (Landsat 8 OLI-TIRS)",
            "abstract": """Surface Reflectance Euclidean, Spectral and Bray-Curtis Median Absolute Deviation 2.1.0 (Landsat 8 OLI-TIRS)
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
https://cmi.ga.gov.au/data-products/dea/346/dea-surface-reflectance-median-absolute-deviation-landsat
For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ls8_nbart_tmad_annual",
            # The Datacube name for the associated data product
            "product_name": "ls8_nbart_tmad_annual",
            "bands": bands_tmad,
            "resource_limits": reslim_wms_min_zoom_15,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["sdev", "edev", "bcdev"],
            },
            "styling": {
                "default_style": "arcsec_sdev",
                "styles": styles_tmad_list,
            },
        },
        {
            "title": "DEA Surface Reflectance Median Absolute Deviation (Landsat 7 ETM+)",
            "abstract": """Surface Reflectance Euclidean, Spectral and Bray-Curtis Median Absolute Deviation 2.1.0 (Landsat 7 ETM+)
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
https://cmi.ga.gov.au/data-products/dea/346/dea-surface-reflectance-median-absolute-deviation-landsat
For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ls7_nbart_tmad_annual",
            # The Datacube name for the associated data product
            "product_name": "ls7_nbart_tmad_annual",
            "bands": bands_tmad,
            "resource_limits": reslim_wms_min_zoom_15,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["sdev", "edev", "bcdev"],
            },
            "styling": {
                "default_style": "arcsec_sdev",
                "styles": styles_tmad_list,
            },
        },
        {
            "title": "DEA Surface Reflectance Median Absolute Deviation (Landsat 5 TM)",
            "abstract": """Surface Reflectance Euclidean, Spectral and Bray-Curtis Median Absolute Deviation 2.1.0 (Landsat 5 TM)
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
https://cmi.ga.gov.au/data-products/dea/346/dea-surface-reflectance-median-absolute-deviation-landsat
For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ls5_nbart_tmad_annual",
            # The Datacube name for the associated data product
            "product_name": "ls5_nbart_tmad_annual",
            "bands": bands_tmad,
            "resource_limits": reslim_wms_min_zoom_15,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["sdev", "edev", "bcdev"],
            },
            "styling": {
                "default_style": "arcsec_sdev",
                "styles": styles_tmad_list,
            },
        },
    ],
}
