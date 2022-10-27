from ows_refactored.baseline_satellite_data.sentinel2.band_s2_cfg import \
    bands_sentinel2_c3
from ows_refactored.baseline_satellite_data.sentinel2.style_s2_cfg import \
    styles_s2_c3_list
from ows_refactored.ows_reslim_cfg import reslim_for_sentinel2

s2b_c3_layer = {
    "name": "ga_s2bm_ard_3",
    "title": "DEA Surface Reflectance (Sentinel-2B MSI) Collection 3",
    "abstract": """Sentinel-2 Multispectral Instrument - Nadir BRDF Adjusted Reflectance + Terrain Illumination Correction (Sentinel-2B MSI)

This product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture.

These corrections have been applied to all satellite imagery in the Sentinel-2 archive. This is undertaken to allow comparison of imagery acquired at different times, in different seasons and in different geographic locations.

These products also indicate where the imagery has been affected by cloud or cloud shadow, contains missing data or has been affected in other ways. The Surface Reflectance products are useful as a fundamental starting point for any further analysis, and underpin all other optical derived Digital Earth Australia products.

This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time. The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive. For more information see http://pid.geoscience.gov.au/dataset/ga/129684 The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors. The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including: - Influence on the remote sensing signal from nearby land and/or atmospheric effects - Optically shallow water - Cloud cover Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

https://cmi.ga.gov.au/data-products/dea/190/dea-surface-reflectance-nbart-sentinel-2-msi

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "ga_s2bm_ard_3",
    "bands": bands_sentinel2_c3,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "s2cloudless_mask",
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
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_c3_list},
}

s2a_c3_layer = {
    "name": "ga_s2am_ard_3",
    "title": "DEA Surface Reflectance (Sentinel-2A MSI) Collection 3",
    "abstract": """Sentinel-2 Multispectral Instrument - Nadir BRDF Adjusted Reflectance + Terrain Illumination Correction (Sentinel-2A MSI)

This product takes Sentinel-2A imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

The imagery is captured using the Multispectral Instrument (MSI) sensor aboard Sentinel-2A.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows the analysis of surface reflectance data as is, without the need to apply additional corrections.

The resolution is a 10/20/60 m grid based on the ESA Level 1C archive.

https://cmi.ga.gov.au/data-products/dea/700/dea-surface-reflectance-sentinel-2-msi-collection-3

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "ga_s2am_ard_3",
    "bands": bands_sentinel2_c3,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "s2cloudless_mask",
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
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_c3_list},
}

combined_layer = {
    "title": "DEA Surface Reflectance (Sentinel-2 MSI) Collection 3",
    "name": "ga_s2m_ard_3",
    "abstract": """Sentinel-2 Multispectral Instrument - Nadir BRDF Adjusted Reflectance + Terrain Illumination Correction (Sentinel-2 MSI)

This product takes Sentinel-2A imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

The imagery is captured using the Multispectral Instrument (MSI) sensor aboard Sentinel-2A.

This product is a single, cohesive Analysis Ready Data (ARD) package, which allows the analysis of surface reflectance data as is, without the need to apply additional corrections.

The resolution is a 10/20/60 m grid based on the ESA Level 1C archive.

https://cmi.ga.gov.au/data-products/dea/700/dea-surface-reflectance-sentinel-2-msi-collection-3

For service status information, see https://status.dea.ga.gov.au""",
    "multi_product": True,
    "product_names": ["ga_s2am_ard_3", "ga_s2bm_ard_3"],
    "bands": bands_sentinel2_c3,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "s2cloudless_mask",
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
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_c3_list},
}
