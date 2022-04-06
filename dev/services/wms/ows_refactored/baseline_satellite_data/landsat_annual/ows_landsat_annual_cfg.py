from ows_refactored.baseline_satellite_data.landsat_annual.band_c3_ls_cfg import \
    bands_c3_ls
from ows_refactored.baseline_satellite_data.landsat_annual.style_c3_ls_cfg import \
    styles_c3_ls_list
from ows_refactored.ows_reslim_cfg import reslim_standard

layers = {
    "title": "DEA Surface Reflectance Calendar Year (Landsat)",
    "abstract": "",
    "layers": [
        {
            "title": "DEA GeoMAD (Landsat 8 OLI-TIRS)",
            "name": "ga_ls8c_nbart_gm_cyear_3",
            "abstract": """DEA Geometric Median and Median Absolute Deviation (Landsat 8 OLI-TIRS)

This product provides statistical tools to exploit the time series of Earth Observation data available in Digital Earth Australia, providing annual images of general conditions and how much an area changes for a given year.

The geomedian part of the product provides an "average" cloud-free image over the given year. The geomedian image is calculated with a multi-dimensional median, using all the spectral measurements from the satellite imagery at the same time in order to maintain the relationships among the measurements.

The median absolute deviation part of the product uses three measures of variance, each of which provides a 'second order' high dimensional statistical composite for the given year. The three variance measures show much an area varies from the "average" in terms of 'distance' based on factors such as brightness and spectra:

Euclidean distance (EMAD)
Cosine (spectral) distance (SMAD)
Bray Curtis dissimilarity (BCMAD)
Together, they provide information on variance in the landscape over the given year and are useful for change detection applications.

For more information, see https://cmi.ga.gov.au/data-products/dea/645/dea-geomad-landsat

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls8c_nbart_gm_cyear_3",
            "bands": bands_c3_ls,
            "time_resolution": "year",
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
            "name": "ga_ls7e_nbart_gm_cyear_3",
            "abstract": """DEA Geometric Median and Median Absolute Deviation (Landsat 7 ETM+)

This product provides statistical tools to exploit the time series of Earth Observation data available in Digital Earth Australia, providing annual images of general conditions and how much an area changes for a given year.

The geomedian part of the product provides an "average" cloud-free image over the given year. The geomedian image is calculated with a multi-dimensional median, using all the spectral measurements from the satellite imagery at the same time in order to maintain the relationships among the measurements.

The median absolute deviation part of the product uses three measures of variance, each of which provides a 'second order' high dimensional statistical composite for the given year. The three variance measures show much an area varies from the "average" in terms of 'distance' based on factors such as brightness and spectra:

Euclidean distance (EMAD)
Cosine (spectral) distance (SMAD)
Bray Curtis dissimilarity (BCMAD)
Together, they provide information on variance in the landscape over the given year and are useful for change detection applications.

For more information, see https://cmi.ga.gov.au/data-products/dea/645/dea-geomad-landsat

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls7e_nbart_gm_cyear_3",
            "bands": bands_c3_ls,
            "time_resolution": "year",
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
            "name": "ga_ls5t_nbart_gm_cyear_3",
            "abstract": """DEA Geometric Median and Median Absolute Deviation (Landsat 5 TM)

This product provides statistical tools to exploit the time series of Earth Observation data available in Digital Earth Australia, providing annual images of general conditions and how much an area changes for a given year.

The geomedian part of the product provides an "average" cloud-free image over the given year. The geomedian image is calculated with a multi-dimensional median, using all the spectral measurements from the satellite imagery at the same time in order to maintain the relationships among the measurements.

The median absolute deviation part of the product uses three measures of variance, each of which provides a 'second order' high dimensional statistical composite for the given year. The three variance measures show much an area varies from the "average" in terms of 'distance' based on factors such as brightness and spectra:

Euclidean distance (EMAD)
Cosine (spectral) distance (SMAD)
Bray Curtis dissimilarity (BCMAD)
Together, they provide information on variance in the landscape over the given year and are useful for change detection applications.

For more information, see https://cmi.ga.gov.au/data-products/dea/645/dea-geomad-landsat

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls5t_nbart_gm_cyear_3",
            "bands": bands_c3_ls,
            "time_resolution": "year",
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
