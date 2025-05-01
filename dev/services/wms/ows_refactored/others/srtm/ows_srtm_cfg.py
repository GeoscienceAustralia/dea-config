from ows_refactored.others.srtm.style_srtm_cfg import styles_srtm_list
from ows_refactored.ows_reslim_cfg import reslim_unlimited

bands_srtm = {
    "dem": [],
}

abstract_srtm = """Geoscience Australia SRTM 1 second DEM

The 1 second Shuttle Radar Topography Mission (SRTM) Digital Elevation Models Version 1.0 package comprises three surface models: the Digital Elevation Model (DEM), the Smoothed Digital Elevation Model (DEM-S) and the Hydrologically Enforced Digital Elevation Model (DEM-H). The DEMs were derived from the SRTM data acquired by NASA in February 2000."""

dea_srtm_layer = {
    "title": "GA SRTM 1 second DEM",
    "name": "ga_srtm_dem1sv1_0",
    "abstract": abstract_srtm,
    "product_name": "ga_srtm_dem1sv1_0",
    "bands": bands_srtm,
    "time_resolution": "summary",
    "resource_limits": reslim_unlimited,
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.00027777777778,
        -0.00027777777778,
    ],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "dem_greyscale",
        "styles": styles_srtm_list,
    },
}
