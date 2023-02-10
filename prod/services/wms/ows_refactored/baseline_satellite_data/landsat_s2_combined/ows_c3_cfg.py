from ows_refactored.baseline_satellite_data.landsat_s2_combined.style_combined_cfg import \
    styles_combined
from ows_refactored.ows_reslim_cfg import reslim_for_sentinel2

# bands definition
bands_ls_s2_shared = {
    "nbart_blue": ["nbart_blue", "blue"],
    "nbart_green": ["nbart_green", "green"],
    "nbart_red": ["nbart_red", "red"],
}

combined_layer = {
    "title": "DEA Surface Reflectance (Landsat and Sentinel-2)",
    "name": "s2_ls_combined",
    "abstract": """Geoscience Australia Landsat and Sentinel-2 Analysis Ready Data Collection 3

This product takes Sentinel-2 and Landsat imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change.

Where Sentinel-2 and Landsat data are both available, the higher resolution Sentinel-2 data is used.

This product combines:

   * Sentinel-2A https://cmi.ga.gov.au/data-products/dea/683/dea-surface-reflectance-sentinel-2a-msi
   * Sentinel-2B https://cmi.ga.gov.au/data-products/dea/825/dea-surface-reflectance-sentinel-2b-msi
   * Landsat-5 https://cmi.ga.gov.au/data-products/dea/358/dea-surface-reflectance-landsat-5-tm
   * Landsat-7 https://cmi.ga.gov.au/data-products/dea/475/dea-surface-reflectance-landsat-7-etm
   * Landsat-8 https://cmi.ga.gov.au/data-products/dea/365/dea-surface-reflectance-landsat-8-oli-tirs
   * Landsat-9

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
    "styling": {
        "default_style": "true_colour",
        "styles": styles_combined
    },
}
