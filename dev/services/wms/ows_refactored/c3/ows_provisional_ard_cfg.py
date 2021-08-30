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
    "title": "Geoscience Australia Near Real-Time (Provisional) Landsat Nadir BRDF Adjusted Reflectance Terrain Collection 3",
    "abstract": """
This is a provisional version of 90-day rolling archive of daily Landsat Near Real-time surface reflectance
data, which is processed on receipt using the best-available ancillary information at the time to provide atmospheric
corrections.

For service status information, see https://status.dea.ga.gov.au
    """,
    "layers": [
        {
            "title": "Geoscience Australia Near Real-Time (Provisional) Landsat 8 Nadir BRDF Adjusted Reflectance Terrain Collection 3",
            "abstract": """
This is a provisional version of 90-day rolling archive of daily Landsat-8 Near Real-time surface reflectance
data, which is processed on receipt using the best-available ancillary information at the time to provide atmospheric
corrections.

The imagery is captured using the Operational Land Imager (OLI) and Thermal Infra-Red Scanner (TIRS) sensors aboard Landsat 8.

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ga_ls8c_ard_provisional_3",
            # The Datacube name for the associated data product
            "product_name": "ga_ls8c_ard_provisional_3",
            "bands": bands_c3_ls_8,
            "resource_limits": reslim_wms_min_zoom_15,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": [
                # flags is now a list of flag band definitions - NOT a dictionary with identifiers
                {
                    "band": "oa_fmask",
                    "product": "ga_ls8c_ard_provisional_3",
                    "ignore_time": False,
                    "ignore_info_flags": [],
                },
                {
                    "band": "land",
                    "product": "geodata_coast_100k",
                    "ignore_time": True,
                    "ignore_info_flags": []
                },
            ],
            "wcs": {
                "default_bands": ["nbart_red", "nbart_green", "nbart_blue"],
            },
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_8},
        },
        {
            "title": "Geoscience Australia Near Real-Time (Provisional) Landsat 7 Nadir BRDF Adjusted Reflectance Terrain Collection 3",
            "abstract": """
This is a provisional version of 90-day rolling archive of daily Landsat-8 Near Real-time surface reflectance
data, which is processed on receipt using the best-available ancillary information at the time to provide atmospheric
corrections.

The imagery is captured using the Enhanced Thematic Mapper Plus (ETM+) sensors aboard Landsat 7.

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ga_ls7e_ard_provisional_3",
            # The Datacube name for the associated data product
            "product_name": "ga_ls7e_ard_provisional_3",
            "bands": bands_c3_ls_7,
            "resource_limits": reslim_wms_min_zoom_15,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": [
                # flags is now a list of flag band definitions - NOT a dictionary with identifiers
                {
                    "band": "oa_fmask",
                    "product": "ga_ls7e_ard_provisional_3",
                    "ignore_time": False,
                    "ignore_info_flags": [],
                },
                {
                    "band": "land",
                    "product": "geodata_coast_100k",
                    "ignore_time": True,
                    "ignore_info_flags": []
                },
            ],
            "wcs": {
                "default_bands": ["nbart_red", "nbart_green", "nbart_blue"],
            },
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_7},
        },
        {
            "title": "Geoscience Australia Near Real-Time (Provisional) Landsat Nadir BRDF Adjusted Reflectance Terrain Collection 3",
            "name": "ga_ls_ard_provisional_3",
            "abstract": """
This is a provisional version of 90-day rolling archive of daily Landsat Near Real-time surface reflectance
data, which is processed on receipt using the best-available ancillary information at the time to provide atmospheric
corrections.

For service status information, see https://status.dea.ga.gov.au""",
            "multi_product": True,
            "product_names": [
                "ga_ls7e_ard_provisional_3",
                "ga_ls8c_ard_provisional_3",
            ],
            "bands": bands_c3_ls_common,
            "resource_limits": reslim_wms_min_zoom_15,
            "dynamic": True,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "flags": [
                {
                    "band": "oa_fmask",
                    "products": [
                        "ga_ls7e_ard_provisional_3",
                        "ga_ls8c_ard_provisional_3",
                    ],
                    "ignore_time": False,
                    "ignore_info_flags": [],
                },
                {
                    "band": "land",
                    "products": [
                        "geodata_coast_100k",
                        "geodata_coast_100k",
                    ],
                    "ignore_time": True,
                    "ignore_info_flags": []
                },
            ],
            "wcs": {
                "default_bands": ["nbart_red", "nbart_green", "nbart_blue"],
            },
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_common},
        },
    ],
}
