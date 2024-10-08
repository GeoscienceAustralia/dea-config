from ows_refactored.baseline_satellite_data.landsat_annual.band_c3_ls_nbart_cfg import \
    bands_c3_ls_nbart
from ows_refactored.baseline_satellite_data.landsat_annual.style_c3_ls_cfg import \
    styles_c3_ls_list
from ows_refactored.ows_reslim_cfg import reslim_standard

layers = {
    "title": "DEA Surface Reflectance Calendar Year (Landsat)",
    "abstract": "",
    "layers": [
        {
            "title": "DEA GeoMAD (Landsat 8 & 9 OLI-TIRS)",
            "name": "ga_ls8cls9c_gm_cyear_3",
            "abstract": """Geoscience Australia Landsat 8 and 9 Geometric Median and Median Absolute Deviation Collection 3

This product provides statistical tools to exploit the time series of Earth Observation data available in Digital Earth Australia, providing annual images of general conditions and how much an area changes for a given year.

The geomedian part of the product provides an "average" cloud-free image over the given year. The geomedian image is calculated with a multi-dimensional median, using all the spectral measurements from the satellite imagery at the same time in order to maintain the relationships among the measurements.

The median absolute deviation part of the product uses three measures of variance, each of which provides a 'second order' high dimensional statistical composite for the given year. The three variance measures show much an area varies from the "average" in terms of 'distance' based on factors such as brightness and spectra:

Euclidean distance (EMAD)
Cosine (spectral) distance (SMAD)
Bray Curtis dissimilarity (BCMAD)
Together, they provide information on variance in the landscape over the given year and are useful for change detection applications.

v4.0.0 Changelog:
Cloud masks have been cleaned using a 3-pixel morphological opening on clouds and a 6-pixel dilation on cloud and shadows.
The south-west origin point of the DEA Summary Product Grid has been shifted 18 tiles west and 15 tiles south in this version.
A single combined product for Landsat 8 and 9 is provided. A standalone Landsat 8 product will no longer be provided from calendar year 2022 and onwards.
Band measurement names were updated for consistency with DEA's ARD products by adding the 'nbart' prefix.


For more information, see https://knowledge.dea.ga.gov.au/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls8cls9c_gm_cyear_3",
            "bands": bands_c3_ls_nbart,
            "time_resolution": "summary",
            "resource_limits": reslim_standard,
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {"default_style": "simple_rgb", "styles": styles_c3_ls_list},
        },
        {
            "title": "DEA GeoMAD (Landsat 7 ETM+)",
            "name": "ga_ls7e_gm_cyear_3",
            "abstract": """Geoscience Australia Landsat 7 Geometric Median and Median Absolute Deviation Collection 3

This product provides statistical tools to exploit the time series of Earth Observation data available in Digital Earth Australia, providing annual images of general conditions and how much an area changes for a given year.

The geomedian part of the product provides an "average" cloud-free image over the given year. The geomedian image is calculated with a multi-dimensional median, using all the spectral measurements from the satellite imagery at the same time in order to maintain the relationships among the measurements.

The median absolute deviation part of the product uses three measures of variance, each of which provides a 'second order' high dimensional statistical composite for the given year. The three variance measures show much an area varies from the "average" in terms of 'distance' based on factors such as brightness and spectra:

Euclidean distance (EMAD)
Cosine (spectral) distance (SMAD)
Bray Curtis dissimilarity (BCMAD)
Together, they provide information on variance in the landscape over the given year and are useful for change detection applications.

v4.0.0 Changelog:
Cloud masks have been cleaned using a 3-pixel morphological opening on clouds and a 6-pixel dilation on cloud and shadows.
The south-west origin point of the DEA Summary Product Grid has been shifted 18 tiles west and 15 tiles south in this version.
A single combined product for Landsat 8 and 9 is provided. A standalone Landsat 8 product will no longer be provided from calendar year 2022 and o$
Band measurement names were updated for consistency with DEA's ARD products by adding the 'nbart' prefix.

For more information, see https://knowledge.dea.ga.gov.au/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls7e_gm_cyear_3",
            "bands": bands_c3_ls_nbart,
            "time_resolution": "summary",
            "resource_limits": reslim_standard,
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {"default_style": "simple_rgb", "styles": styles_c3_ls_list},
        },
        {
            "title": "DEA GeoMAD (Landsat 5 TM)",
            "name": "ga_ls5t_gm_cyear_3",
            "abstract": """Geoscience Australia Landsat 5 Geometric Median and Median Absolute Deviation Collection 3

This product provides statistical tools to exploit the time series of Earth Observation data available in Digital Earth Australia, providing annual images of general conditions and how much an area changes for a given year.

The geomedian part of the product provides an "average" cloud-free image over the given year. The geomedian image is calculated with a multi-dimensional median, using all the spectral measurements from the satellite imagery at the same time in order to maintain the relationships among the measurements.

The median absolute deviation part of the product uses three measures of variance, each of which provides a 'second order' high dimensional statistical composite for the given year. The three variance measures show much an area varies from the "average" in terms of 'distance' based on factors such as brightness and spectra:

Euclidean distance (EMAD)
Cosine (spectral) distance (SMAD)
Bray Curtis dissimilarity (BCMAD)
Together, they provide information on variance in the landscape over the given year and are useful for change detection applications.

v4.0.0 Changelog:
Cloud masks have been cleaned using a 3-pixel morphological opening on clouds and a 6-pixel dilation on cloud and shadows.
The south-west origin point of the DEA Summary Product Grid has been shifted 18 tiles west and 15 tiles south in this version.
A single combined product for Landsat 8 and 9 is provided. A standalone Landsat 8 product will no longer be provided from calendar year 2022 and o$
Band measurement names were updated for consistency with DEA's ARD products by adding the 'nbart' prefix.

For more information, see https://knowledge.dea.ga.gov.au/data/product/dea-geometric-median-and-median-absolute-deviation-landsat/

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls5t_gm_cyear_3",
            "bands": bands_c3_ls_nbart,
            "time_resolution": "summary",
            "resource_limits": reslim_standard,
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {"default_style": "simple_rgb", "styles": styles_c3_ls_list},
        }
    ],
}
