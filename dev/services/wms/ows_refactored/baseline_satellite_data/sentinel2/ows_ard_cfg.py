from ows_refactored.baseline_satellite_data.sentinel2.band_s2_cfg import \
    bands_sentinel2
from ows_refactored.baseline_satellite_data.sentinel2.style_s2_cfg import \
    styles_s2_list
from ows_refactored.ows_reslim_cfg import reslim_for_sentinel2

s2b_layer = {
    "name": "ga_s2bm_ard_3",
    "title": "DEA Surface Reflectance (Sentinel-2B MSI)",
    "abstract": """Geoscience Australia Sentinel-2B MSI Analysis Ready Data Collection 3

This product takes Sentinel-2B imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

The imagery is captured using the Multispectral Instrument (MSI) sensor aboard Sentinel-2B.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows the analysis of surface reflectance data as is, without the need to apply additional corrections.

It contains two sub-products that provide corrections or attribution information:

   * DEA Surface Reflectance NBART (Sentinel-2B MSI) https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-nbart-sentinel-2b-msi/
   * DEA Surface Reflectance OA (Sentinel-2B MSI) https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-oa-sentinel-2b-msi/
   
The resolution is a 10/20/60 m grid based on the ESA Level 1C archive.

Full product description: https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-sentinel-2b-msi/

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "ga_s2bm_ard_3",
    "bands": bands_sentinel2,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, -10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "oa_s2cloudless_mask",
            "product": "ga_s2bm_ard_3",
            "ignore_time": False,
            "ignore_info_flags": []
        },
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_list},
}

s2a_layer = {
    "name": "ga_s2am_ard_3",
    "title": "DEA Surface Reflectance (Sentinel-2A MSI)",
    "abstract": """Geoscience Australia Sentinel-2A MSI Analysis Ready Data Collection 3

This product takes Sentinel-2A imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

The imagery is captured using the Multispectral Instrument (MSI) sensor aboard Sentinel-2A.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows the analysis of surface reflectance data as is, without the need to apply additional corrections.

It contains two sub-products that provide corrections or attribution information:

   * DEA Surface Reflectance NBART (Sentinel-2A MSI) https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-nbart-sentinel-2a-msi/
   * DEA Surface Reflectance OA (Sentinel-2A MSI) https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-oa-sentinel-2a-msi/

The resolution is a 10/20/60 m grid based on the ESA Level 1C archive.

Full product description: https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-sentinel-2a-msi/

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "ga_s2am_ard_3",
    "bands": bands_sentinel2,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, -10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "oa_s2cloudless_mask",
            "product": "ga_s2am_ard_3",
            "ignore_time": False,
            "ignore_info_flags": []
        },
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_list},
}

combined_layer = {
    "title": "DEA Surface Reflectance (Sentinel-2)",
    "name": "ga_s2m_ard_3",
    "abstract": """Geoscience Australia Sentinel-2 Analysis Ready Data Collection 3

This product takes Sentinel-2A and Sentinel-2B imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

The imagery is captured using the Multispectral Instrument (MSI) sensor aboard Sentinel-2A and Sentinel-2B.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows the analysis of surface reflectance data as is, without the need to apply additional corrections.

The resolution is a 10/20/60 m grid based on the ESA Level 1C archive.

Full Sentinel-2A product description: https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-sentinel-2a-msi/
Full Sentinel-2B product description: https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-sentinel-2b-msi/

For service status information, see https://status.dea.ga.gov.au""",
    "multi_product": True,
    "product_names": ["ga_s2am_ard_3", "ga_s2bm_ard_3"],
    "bands": bands_sentinel2,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, -10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "oa_s2cloudless_mask",
            "products": ["ga_s2am_ard_3", "ga_s2bm_ard_3"],
            "ignore_time": False,
            "ignore_info_flags": []
        },
        {
            "band": "land",
            "products": ["geodata_coast_100k", "geodata_coast_100k"],
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_list},
}
