from ows_refactored.c3.style_c3_cfg import (styles_c3_ls_7, styles_c3_ls_8,
                                            styles_c3_ls_common)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15

# bands definition
bands_c3_ls_common = {
    "nbart_blue": ["nbart_blue"],
    "nbart_green": ["nbart_green"],
    "nbart_red": ["nbart_red"],
    "nbart_nir": ["nbart_nir", "nbart_near_infrared"],
    "nbart_swir_1": ["nbart_swir_1", "nbart_shortwave_infrared_1"],
    "nbart_swir_2": ["nbart_swir_2", "nbart_shortwave_infrared_2"],
    "oa_fmask": ["oa_fmask", "fmask"],
}


bands_c3_ls_7 = bands_c3_ls_common.copy()
bands_c3_ls_7.update(
    {
        "nbart_panchromatic": ["nbart_panchromatic"],
    }
)


bands_c3_ls_8 = bands_c3_ls_7.copy()
bands_c3_ls_8.update(
    {
        "nbart_coastal_aerosol": ["coastal_aerosol", "nbart_coastal_aerosol"],
    }
)

layers = {
    "title": "Geoscience Australia Landsat Nadir BRDF Adjusted Reflectance Terrain Collection 3",
    "abstract": """
    The United States Geological Survey's (USGS) Landsat satellite program has been capturing images of the Australian continent for more than 30 years. This data is highly useful for land and coastal mapping studies.

In particular, the light reflected from the Earth’s surface (surface reflectance) is important for monitoring environmental resources – such as agricultural production and mining activities – over time.

We need to make accurate comparisons of imagery acquired at different times, seasons and geographic locations. However, inconsistencies can arise due to variations in atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect. These need to be reduced or removed to ensure the data is consistent and can be compared over time.

For service status information, see https://status.dea.ga.gov.au
    """,
    "layers": [
        {
            "title": "Geoscience Australia Landsat 8 Nadir BRDF Adjusted Reflectance Terrain Collection 3",
            "abstract": """
This product takes Landsat 8 imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

The imagery is captured using the Operational Land Imager (OLI) and Thermal Infra-Red Scanner (TIRS) sensors aboard Landsat 8.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains three sub-products that provide corrections or attribution information:

Surface Reflectance NBAR 3 (Landsat 8 OLI-TIRS)
Surface Reflectance NBART 3 (Landsat 8 OLI-TIRS)
Surface Reflectance OA 3 (Landsat 8 OLI-TIRS)
The resolution is a 30 m grid based on the USGS Landsat Collection 1 archive.""",
            # The WMS name for the layer
            "name": "ga_ls8c_ard_3",
            # The Datacube name for the associated data product
            "product_name": "ga_ls8c_ard_3",
            "bands": bands_c3_ls_8,
            "resource_limits": reslim_wms_min_zoom_15,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": [
                # flags is now a list of flag band definitions - NOT a dictionary with identifiers
                {
                    "band": "oa_fmask",
                    "product": "ga_ls8c_ard_3",
                    "ignore_time": False,
                    "ignore_info_flags": [],
                },
            ],
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["nbart_red", "nbart_green", "nbart_blue"],
            },
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_8},
        },
        {
            "title": "Geoscience Australia Landsat 7 Nadir BRDF Adjusted Reflectance Terrain Collection 3",
            "abstract": """
The United States Geological Survey's (USGS) Landsat satellite program has been capturing images of the Australian continent for more than 30 years. This data is highly useful for land and coastal mapping studies.
In particular, the light reflected from the Earth’s surface (surface reflectance) is important for monitoring environmental resources – such as agricultural production and mining activities – over time.

We need to make accurate comparisons of imagery acquired at different times, seasons and geographic locations. However, inconsistencies can arise due to variations in atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect. These need to be reduced or removed to ensure the data is consistent and can be compared over time.

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ga_ls7e_ard_3",
            # The Datacube name for the associated data product
            "product_name": "ga_ls7e_ard_3",
            "bands": bands_c3_ls_7,
            "resource_limits": reslim_wms_min_zoom_15,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": [
                # flags is now a list of flag band definitions - NOT a dictionary with identifiers
                {
                    "band": "oa_fmask",
                    "product": "ga_ls7e_ard_3",
                    "ignore_time": False,
                    "ignore_info_flags": [],
                },
            ],
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["nbart_red", "nbart_green", "nbart_blue"],
            },
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_7},
        },
        {
            "title": "Geoscience Australia Landsat 5 Nadir BRDF Adjusted Reflectance Terrain Collection 3",
            "abstract": """
The United States Geological Survey's (USGS) Landsat satellite program has been capturing images of the Australian continent for more than 30 years. This data is highly useful for land and coastal mapping studies.

In particular, the light reflected from the Earth’s surface (surface reflectance) is important for monitoring environmental resources – such as agricultural production and mining activities – over time.

We need to make accurate comparisons of imagery acquired at different times, seasons and geographic locations. However, inconsistencies can arise due to variations in atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect. These need to be reduced or removed to ensure the data is consistent and can be compared over time.


For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ga_ls5t_ard_3",
            # The Datacube name for the associated data product
            "product_name": "ga_ls5t_ard_3",
            "bands": bands_c3_ls_common,
            "resource_limits": reslim_wms_min_zoom_15,
            "dynamic": True,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": [
                # flags is now a list of flag band definitions - NOT a dictionary with identifiers
                {
                    "band": "oa_fmask",
                    "product": "ga_ls5t_ard_3",
                    "ignore_time": False,
                    "ignore_info_flags": [],
                },
            ],
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["nbart_red", "nbart_green", "nbart_blue"],
            },
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_common},
        },
        {
            "title": "Geoscience Australia Landsat Nadir BRDF Adjusted Reflectance Terrain Collection 3",
            "name": "dea_c3_ls_combined",
            "abstract": """
The United States Geological Survey's (USGS) Landsat satellite program has been capturing images of the Australian continent for more than 30 years. This data is highly useful for land and coastal mapping studies.

In particular, the light reflected from the Earth’s surface (surface reflectance) is important for monitoring environmental resources – such as agricultural production and mining activities – over time.

We need to make accurate comparisons of imagery acquired at different times, seasons and geographic locations. However, inconsistencies can arise due to variations in atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect. These need to be reduced or removed to ensure the data is consistent and can be compared over time.

For service status information, see https://status.dea.ga.gov.au""",
            "multi_product": True,
            "product_names": [
                "ga_ls5t_ard_3",
                "ga_ls7e_ard_3",
                "ga_ls8c_ard_3",
            ],
            "bands": bands_c3_ls_common,
            "resource_limits": reslim_wms_min_zoom_15,
            "dynamic": True,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": [
                {
                    "band": "oa_fmask",
                    "products": [
                        "ga_ls5t_ard_3",
                        "ga_ls7e_ard_3",
                        "ga_ls8c_ard_3",
                    ],
                    "ignore_time": False,
                    "ignore_info_flags": [],
                },
            ],
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["nbart_red", "nbart_green", "nbart_blue"],
            },
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_common},
        },
    ],
}
