from ows_refactored.ows_reslim_cfg import reslim_standard
from ows_refactored.sea_ocean_coast.intertidal_c3.style_intertidal_cfg import \
    styles_intertidal_list

bands_intertidal = {
    "elevation": [],
    "elevation_uncertainty": [],
    "exposure": [],
    "extents": [],
    "ta_hat": [],
    "ta_hot": [],
    "ta_lat": [],
    "ta_lot": [],
    "ta_offset_high": [],
    "ta_offset_low": [],
    "ta_spread": [],
    "qa_ndwi_corr": [],
    "qa_ndwi_freq": [],
    "qa_count_clear": [],
}

abstract_intertidal = """Geoscience Australia Sentinel-2 Landsat Intertidal Calendar Year Collection 3

The DEA Intertidal product suite maps the changing extent, elevation and topography of Australia's exposed intertidal zone, the complex zone that defines the interface between land and sea.

Incorporating both Sentinel-2 and Landsat data, the product suite provides an annual 10 m resolution elevation product for the intertidal zone, enabling users to better monitor and understand some of the most dynamic regions of Australia’s coastlines. Utilising an improved tidal modelling capability, the product suite includes a continental scale mapping of intertidal exposure over time, enabling scientists and managers to integrate the data into ecological and migratory species applications and modelling.

Product documentation: https://knowledge.dea.ga.gov.au/data/product/dea-intertidal/

Service status information: https://status.dea.ga.gov.au"""

dea_intertidal_layer = {
    "title": "DEA Intertidal (Sentinel-2, Landsat)",
    "name": "ga_s2ls_intertidal_cyear_3",
    "abstract": abstract_intertidal,
    "product_name": "ga_s2ls_intertidal_cyear_3",
    "bands": bands_intertidal,
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
        "default_style": "intertidal_elevation_adaptive",
        "styles": styles_intertidal_list,
    },
}
