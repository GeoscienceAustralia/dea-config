from ows_refactored.baseline_satellite_data.landsat_s2_combined.style_combined_cfg import \
    styles_combined
from ows_refactored.ows_reslim_cfg import reslim_for_sentinel2

# bands definition
bands_ls_s2_shared = {
    "nbart_blue": ["nbart_blue", "blue"],
    "nbart_green": ["nbart_green", "green"],
    "nbart_red": ["nbart_red", "red"],
    "nbart_common_nir": ["nbart_common_nir", "nir"],
    "nbart_common_swir_1": ["nbart_common_swir_1", "swir1"],
    "nbart_common_swir_2": ["nbart_common_swir_2", "swir2"],
    "oa_fmask": ["oa_fmask"]
}

combined_layer = {
    "title": "DEA Surface Reflectance (Landsat and Sentinel-2)",
    "name": "s2_ls_combined",
    "abstract": """Geoscience Australia Landsat and Sentinel-2 Analysis Ready Data Collection 3

This product takes Sentinel-2 and Landsat imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

Where Sentinel-2 and Landsat data are both available, the higher resolution Sentinel-2 data is used.

This product combines:

   * Sentinel-2A https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-sentinel-2a-msi/
   * Sentinel-2B https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-sentinel-2b-msi/
   * Landsat-5 https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-landsat-5-tm/
   * Landsat-7 https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-landsat-7-etm/
   * Landsat-8 https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-landsat-8-oli-tirs/
   * Landsat-9 https://docs.dea.ga.gov.au/data/product/dea-surface-reflectance-landsat-9-oli-tirs/

For service status information, see https://status.dea.ga.gov.au""",
    "multi_product": True,
    "product_names": [
        # Sentinel-2 listed first to set priority on overlap areas.
        "ga_s2am_ard_3",
        "ga_s2bm_ard_3",
        # Landsat listed second.
        "ga_ls5t_ard_3",
        "ga_ls7e_ard_3",
        "ga_ls8c_ard_3",
        "ga_ls9c_ard_3",
    ],
    "bands": bands_ls_s2_shared,
    "resource_limits": reslim_for_sentinel2,
    "dynamic": True,
    # pseudo-"native" CRS and resolution for WCS
    "native_crs": "EPSG:3577",
    "native_resolution": [10, -10],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "oa_fmask",
            "products": [
                # Should line up with product_names above.
                "ga_s2am_ard_3",
                "ga_s2bm_ard_3",
                "ga_ls5t_ard_3",
                "ga_ls7e_ard_3",
                "ga_ls8c_ard_3",
                "ga_ls9c_ard_3",
            ],
            "ignore_time": False,
            "ignore_info_flags": [],
        },
        {
            "band": "land",
            "products": [
                # Should line up with product_names above.
                "geodata_coast_100k",
                "geodata_coast_100k",
                "geodata_coast_100k",
                "geodata_coast_100k",
                "geodata_coast_100k",
                "geodata_coast_100k",
            ],
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {
        "default_style": "true_colour",
        "styles": styles_combined
    },
}
