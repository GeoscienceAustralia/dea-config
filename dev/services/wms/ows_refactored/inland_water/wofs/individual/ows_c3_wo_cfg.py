from ows_refactored.inland_water.wofs.bands_wo_cfg import bands_wofs_obs
from ows_refactored.inland_water.wofs.styles_wo_cfg import (
    style_c3_wofs_obs, style_c3_wofs_obs_wet_only)
from ows_refactored.ows_reslim_cfg import reslim_standard

layer = {
    "title": "DEA Water Observations (Landsat)",
    "name": "ga_ls_wo_3",
    "abstract": """**Geoscience Australia Water Observations (Landsat, Collection 3, 30 m, Individual Observations, 3.1.6).**


Water Observations are the principal Digital Earth Australia (DEA) Water product (previously known as Water Observations from Space (WOfS)). This product shows where surface water was observed within each individual Landsat (5, 7 and 8) satellite image on each particular day since mid 1986. These daily data layers are termed Water Observations (WOs).

WOs show the extent of water in a corresponding Landsat scene, along with the degree to which the scene was obscured by clouds, shadows or where sensor problems cause parts of a scene to not be observable.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the input water classifications, and can be difficult to interpret on its own.

For more information, see https://docs.dea.ga.gov.au/data/product/dea-water-observations-landsat/

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "ga_ls_wo_3",
    "bands": bands_wofs_obs,
    "resource_limits": reslim_standard,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "flags": [
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": [],
        },
        {
            "band": "water",
            "product": "ga_ls_wo_3",
            "ignore_time": False,
            "ignore_info_flags": [],
            "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
        },
    ],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_bitflag",
        "always_fetch_bands": [],
        "manual_merge": False,
        "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
    },
    "styling": {
        "default_style": "observations",
        "styles": [style_c3_wofs_obs, style_c3_wofs_obs_wet_only],
    },
}
