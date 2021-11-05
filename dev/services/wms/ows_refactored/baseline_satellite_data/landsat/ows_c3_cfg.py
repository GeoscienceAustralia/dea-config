from ows_refactored.baseline_satellite_data.landsat.style_c3_cfg import (
    styles_c3_ls_7, styles_c3_ls_8, styles_c3_ls_common)
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
    "title": "DEA Surface Reflectance (Landsat)",
    "abstract": """Collection 3 represents a consistent processing and upgrade to the Geoscience Australia's Landsat baseline and derivative products.

For service status information, see https://status.dea.ga.gov.au""",
    "layers": [
        {
            "title": "DEA Surface Reflectance USGS C2 Test (Landsat 8 OLI-TIRS)",
            "abstract": """Geoscience Australia Landsat 8 OLI-TIRS Analysis Ready Data Collection 3
This product takes Landsat 8 imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

The imagery is captured using the Operational Land Imager (OLI) and Thermal Infra-Red Scanner (TIRS) sensors aboard Landsat 8.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains three sub-products that provide corrections or attribution information:

DEA Surface Reflectance NBAR (Landsat 8 OLI-TIRS) https://cmi.ga.gov.au/data-products/dea/402/dea-surface-reflectance-nbar-landsat-8-oli-tirs
DEA Surface Reflectance NBART (Landsat 8 OLI-TIRS) https://cmi.ga.gov.au/data-products/dea/400/dea-surface-reflectance-nbart-landsat-8-oli-tirs
DEA Surface Reflectance OA (Landsat 8 OLI-TIRS) https://cmi.ga.gov.au/data-products/dea/404/dea-surface-reflectance-oa-landsat-8-oli-tirs
The resolution is a 30 m grid based on the USGS Landsat Collection 1 archive.

https://cmi.ga.gov.au/data-products/dea/365/dea-surface-reflectance-landsat-8-oli-tirs

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ga_ls8c_ard_c2_3",
            # The Datacube name for the associated data product
            "product_name": "ga_ls8c_ard_c2_3",
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
                    "product": "ga_ls8c_ard_c2_3",
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
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_8},
        },
        {
            "title": "DEA Surface Reflectance (Landsat 8 OLI-TIRS)",
            "abstract": """Geoscience Australia Landsat 8 OLI-TIRS Analysis Ready Data Collection 3
This product takes Landsat 8 imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

The imagery is captured using the Operational Land Imager (OLI) and Thermal Infra-Red Scanner (TIRS) sensors aboard Landsat 8.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains three sub-products that provide corrections or attribution information:

DEA Surface Reflectance NBAR (Landsat 8 OLI-TIRS) https://cmi.ga.gov.au/data-products/dea/402/dea-surface-reflectance-nbar-landsat-8-oli-tirs
DEA Surface Reflectance NBART (Landsat 8 OLI-TIRS) https://cmi.ga.gov.au/data-products/dea/400/dea-surface-reflectance-nbart-landsat-8-oli-tirs
DEA Surface Reflectance OA (Landsat 8 OLI-TIRS) https://cmi.ga.gov.au/data-products/dea/404/dea-surface-reflectance-oa-landsat-8-oli-tirs
The resolution is a 30 m grid based on the USGS Landsat Collection 1 archive.

https://cmi.ga.gov.au/data-products/dea/365/dea-surface-reflectance-landsat-8-oli-tirs

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ga_ls8c_ard_3",
            # The Datacube name for the associated data product
            "product_name": "ga_ls8c_ard_3",
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
                    "product": "ga_ls8c_ard_3",
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
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_8},
        },
        {
            "title": "DEA Surface Reflectance (Landsat 7 ETM+)",
            "abstract": """Geoscience Australia Landsat 7 ETM+ Analysis Ready Data Collection 3
This product takes Landsat 7 Enhanced Thematic Mapper Plus (ETM+) imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains three sub-products that provide corrections or attribution information:

DEA Surface Reflectance NBAR (Landsat 7 ETM+) https://cmi.ga.gov.au/data-products/dea/476/dea-surface-reflectance-nbar-landsat-7-etm
DEA Surface Reflectance NBART (Landsat 7 ETM+) https://cmi.ga.gov.au/data-products/dea/399/dea-surface-reflectance-nbart-landsat-7-etm
DEA Surface Reflectance OA (Landsat 7 ETM+) https://cmi.ga.gov.au/data-products/dea/478/dea-surface-reflectance-oa-landsat-7-etm
The resolution is a 30 m grid based on the USGS Landsat Collection 1 archive.

https://cmi.ga.gov.au/data-products/dea/475/dea-surface-reflectance-landsat-7-etm

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ga_ls7e_ard_3",
            # The Datacube name for the associated data product
            "product_name": "ga_ls7e_ard_3",
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
                    "product": "ga_ls7e_ard_3",
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
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_7},
        },
        {
            "title": "DEA Surface Reflectance (Landsat 5 TM)",
            "abstract": """Geoscience Australia Landsat 5 TM Analysis Ready Data Collection 3
This product takes Landsat 5 Thematic Mapper (TM) imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains three sub-products that provide corrections or attribution information:

DEA Surface Reflectance NBAR (Landsat 5 TM) https://cmi.ga.gov.au/data-products/dea/367/dea-surface-reflectance-nbar-landsat-5-tm
DEA Surface Reflectance NBART (Landsat 5 TM) https://cmi.ga.gov.au/data-products/dea/477/dea-surface-reflectance-nbart-landsat-5-tm
DEA Surface Reflectance OA (Landsat 5 TM) https://cmi.ga.gov.au/data-products/dea/369/dea-surface-reflectance-oa-landsat-5-tm
The resolution is a 30 m grid based on the USGS Landsat Collection 1 archive.

https://cmi.ga.gov.au/data-products/dea/358/dea-surface-reflectance-landsat-5-tm

For service status information, see https://status.dea.ga.gov.au""",
            # The WMS name for the layer
            "name": "ga_ls5t_ard_3",
            # The Datacube name for the associated data product
            "product_name": "ga_ls5t_ard_3",
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
                # flags is now a list of flag band definitions - NOT a dictionary with identifiers
                {
                    "band": "oa_fmask",
                    "product": "ga_ls5t_ard_3",
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
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_common},
        },
        {
            "title": "DEA Surface Reflectance (Landsat 8 OLI-TIRS, Provisional)",
            "abstract": """Geoscience Australia Landsat 8 OLI-TIRS Analysis Ready Data Provisional Collection 3

This product takes Landsat 8 imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.
The imagery is captured using the Operational Land Imager (OLI) and Thermal Infra-Red Scanner (TIRS) sensors aboard Landsat 8.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains sub-products that provide corrections or attribution information:

DEA Surface Reflectance NBART (Landsat 8 OLI-TIRS)

DEA Surface Reflectance OA (Landsat 8 OLI-TIRS)

The resolution is a 30 m grid based on the USGS Landsat Collection 1 archive.

https://cmi.ga.gov.au/data-products/dea/365/dea-surface-reflectance-landsat-8-oli-tirs

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
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_8},
        },
        {
            "title": "DEA Surface Reflectance (Landsat 7 ETM+, Provisional)",
            "abstract": """Geoscience Australia Landsat 7 ETM+ Analysis Ready Data Provisional Collection 3

This product takes Landsat 7 Enhanced Thematic Mapper Plus (ETM+) imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains sub-products that provide corrections or attribution information:

DEA Surface Reflectance NBART (Landsat 7 ETM+)

DEA Surface Reflectance OA (Landsat 7 ETM+)

The resolution is a 30 m grid based on the USGS Landsat Collection 1 archive.

https://cmi.ga.gov.au/data-products/dea/475/dea-surface-reflectance-landsat-7-etm

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
            "styling": {"default_style": "true_colour", "styles": styles_c3_ls_7},
        },
        {
            "include": "ows_refactored.baseline_satellite_data.landsat.ows_c3_cfg.combined_provisional_layer",
            "type": "python",
        },
    ],
}

combined_layer = {
    "title": "DEA Surface Reflectance (Landsat)",
    "name": "ga_ls_ard_3",
    "abstract": """Geoscience Australia Landsat Analysis Ready Data Collection 3
This product takes Landsat imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

This product combines:
Landsat 8 imagery https://cmi.ga.gov.au/data-products/dea/365/dea-surface-reflectance-landsat-8-oli-tirs,
Landsat 7 imagery https://cmi.ga.gov.au/data-products/dea/475/dea-surface-reflectance-landsat-7-etm and
Landsat 5 Imagery https://cmi.ga.gov.au/data-products/dea/358/dea-surface-reflectance-landsat-5-tm

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
                "ga_ls5t_ard_3",
                "ga_ls7e_ard_3",
                "ga_ls8c_ard_3",
            ],
            "ignore_time": False,
            "ignore_info_flags": [],
        },
        {
            "band": "land",
            "products": [
                "geodata_coast_100k",
                "geodata_coast_100k",
                "geodata_coast_100k",
            ],
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {"default_style": "true_colour", "styles": styles_c3_ls_common},
}

combined_provisional_layer = {
    "title": "DEA Surface Reflectance (Landsat, Provisional)",
    "name": "ga_ls_ard_provisional_3",
    "abstract": """Geoscience Australia Landsat Analysis Ready Data Provisional Collection 3

This product takes Landsat 7 Enhanced Thematic Mapper Plus (ETM+) and Landsat 8 OLI-TIRS imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is, without the need to apply additional corrections.

It contains sub-products that provide corrections or attribution information:

DEA Surface Reflectance NBART (Landsat 7 ETM+, Landsat 8 OLI-TIRS)

DEA Surface Reflectance OA (Landsat 7 ETM+, Landsat 8 OLI-TIRS)

The resolution is a 30 m grid based on the USGS Landsat Collection 1 archive.

https://cmi.ga.gov.au/data-products/dea/475/dea-surface-reflectance-landsat-7-etm

https://cmi.ga.gov.au/data-products/dea/365/dea-surface-reflectance-landsat-8-oli-tirs

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
    "styling": {"default_style": "true_colour", "styles": styles_c3_ls_common},
}
