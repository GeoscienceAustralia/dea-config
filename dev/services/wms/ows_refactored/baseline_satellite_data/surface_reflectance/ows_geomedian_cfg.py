from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35
from ows_refactored.baseline_satellite_data.surface_reflectance.band_ls_cfg import bands_ls
from ows_refactored.baseline_satellite_data.surface_reflectance.style_ls_cfg import styles_ls_list

layers = {
    "title": "Surface Reflectance",
    "abstract": "",
    "layers": [
        {
            "title": "Surface Reflectance 25m Annual Geomedian (Landsat 8)",
            "name": "ls8_nbart_geomedian_annual",
            "abstract": """
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 8: 2013 to 2017;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374

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
            "title": "Surface Reflectance 25m Annual Geomedian (Landsat 7)",
            "name": "ls7_nbart_geomedian_annual",
            "abstract": """
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 7: 2000 to 2017;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374

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
            "title": "Surface Reflectance 25m Annual Geomedian (Landsat 5)",
            "name": "ls5_nbart_geomedian_annual",
            "abstract": """
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed
as a shaded region. The surface reflectance geometric median (geomedian) is a pixel composite
mosaic of a time series of earth observations. The value of a pixel in a an annual geomedian
image is the statistical median of all observations for that pixel from a calendar year.
Annual mosaics are available for the following years:

Landsat 5: 1988 to 1999, 2004 to 2007, 2009 to 2011;

For more information, see http://pid.geoscience.gov.au/dataset/ga/120374

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
    ],
}
