from ows_refactored.baseline_satellite_data.landsat_annual.band_ls_cfg import \
    bands_ls
from ows_refactored.baseline_satellite_data.landsat_annual.style_ls_cfg import \
    styles_tide_list
from ows_refactored.ows_reslim_cfg import reslim_standard

layers = {
    "title": "High and Low Tide Composites (HLTC)",
    "abstract": """High and Low Tide Composites (HLTC)

This product is deprecated; users are advised to transition to using DEA Tidal Composites instead: https://knowledge.dea.ga.gov.au/data/product/dea-tidal-composites/

For service status information, see https://status.dea.ga.gov.au
    """,
    "layers": [
        {
            "title": "High Tide Composite (HLTC)",
            "name": "high_tide_composite",
            "abstract": """High Tide and Low Tide Composites 2.0.0 (Landsat, High Tide)

This product is deprecated; users are advised to transition to using DEA Tidal Composites instead: https://knowledge.dea.ga.gov.au/data/product/dea-tidal-composites/

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "high_tide_comp_20p",
            "bands": bands_ls,
            "time_resolution": "summary",
            "resource_limits": reslim_standard,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": styles_tide_list,
            },
        },
        {
            "title": "Low Tide Composite (HLTC)",
            "name": "low_tide_composite",
            "abstract": """High Tide and Low Tide Composites 2.0.0 (Landsat, Low Tide)

This product is deprecated; users are advised to transition to using DEA Tidal Composites instead: https://knowledge.dea.ga.gov.au/data/product/dea-tidal-composites/

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "low_tide_comp_20p",
            "time_resolution": "summary",
            "bands": bands_ls,
            "resource_limits": reslim_standard,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": styles_tide_list,
            },
        },
    ],
}
