from ows_refactored.ows_reslim_cfg import reslim_standard
from ows_refactored.sea_ocean_coast.tidal_composites_c3.style_tidal_composites_cfg import \
    styles_tidal_composites_list

bands_tidal_composites = {
    "low_red": [],
    "low_green": [],
    "low_blue": [],
    "low_swir_2": [],
    "low_nir_1": [],
    "high_red": [],
    "high_green": [],
    "high_blue": [],
    "high_swir_2": [],
    "high_nir_1": [],
    "qa_low_threshold": [],
    "qa_high_threshold": [],
    "qa_count_clear": [],
}

abstract_tidal_composites = """Geoscience Australia Sentinel-2 Tidal Composites Calendar Year Collection 3

Digital Earth Australia (DEA) Tidal Composites are cloud-free imagery mosaics of Australia's coasts, estuaries and reefs at low and high tide. Calculated using a geometric median of Sentinel-2 imagery from the highest and lowest 15% of observed tides, DEA Tidal Composites deliver an annually updated snapshot of high and low tide Australian coastal environments.

Product documentation: https://knowledge.dea.ga.gov.au/data/product/dea-tidal-composites/

Service status information: https://status.dea.ga.gov.au"""

dea_tidal_composites_layer = {
    "title": "DEA Tidal Composites (Sentinel-2)",
    "name": "ga_s2_tidal_composites_cyear_3",
    "abstract": abstract_tidal_composites,
    "product_name": "ga_s2_tidal_composites_cyear_3",
    "bands": bands_tidal_composites,
    "time_resolution": "summary",
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [10, -10],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "low_true",
        "styles": styles_tidal_composites_list,
    },
}
