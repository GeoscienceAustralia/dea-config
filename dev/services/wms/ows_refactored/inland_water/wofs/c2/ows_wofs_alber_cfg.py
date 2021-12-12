from ows_refactored.inland_water.wofs.bands_wo_cfg import bands_wofs_obs
from ows_refactored.inland_water.wofs.c2.ows_wofs_summary_cfg import (
    style_wofs_obs, style_wofs_obs_wet_only)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35

layer = {
    "title": "DEA Water Observations (Landsat, C2)",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "DEA Water Observations (Landsat, C2)",
            "name": "wofs_albers",
            "abstract": """Water Observations from Space 25m 2.1.5 (Landsat)

Water Observations from Space (WOfS) provides surface water observations derived from satellite imagery for all of Australia. The current product (Version 2.1.5) includes observations taken from 1986 to the present, from the Landsat 5, 7 and 8 satellites. WOfS covers all of mainland Australia and Tasmania but excludes off-shore Territories.

The WOfS product allows users to get a better understanding of where water is normally present in a landscape, where water is seldom observed, and where inundation has occurred occasionally.

Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water. The details of the WOfS algorithm and derived statistics are available at http://dx.doi.org/10.1016/j.rse.2015.11.003.

https://cmi.ga.gov.au/data-products/dea/142/dea-water-observations-landsat

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "wofs_albers",
            "bands": bands_wofs_obs,
            "resource_limits": reslim_wms_min_zoom_35,
            "dynamic": True,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_bitflag",
                "always_fetch_bands": [],
                "manual_merge": False,
                "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
            },
            "styling": {
                "default_style": "observations",
                "styles": [style_wofs_obs, style_wofs_obs_wet_only],
            },
        },
    ],
}
