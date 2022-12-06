from ows_refactored.baseline_satellite_data.sentinel2.band_s2_cfg import \
    bands_sentinel2
from ows_refactored.baseline_satellite_data.sentinel2.style_s2_cfg import \
    styles_s2_list
from ows_refactored.ows_reslim_cfg import reslim_for_sentinel2

combined_layer = {
    "title": "DEA Surface Reflectance (Sentinel-2 Near Real-Time)",
    "name": "s2_nrt_granule_nbar_t",
    "abstract": """Sentinel-2 Multispectral Instrument - Nadir BRDF Adjusted Reflectance + Terrain Illumination Correction near real time (Sentinel-2 MSI)

**This dataset has been replaced with an updated version. This service will be decommissioned in January 2023. For more information please see https://bit.ly/3FAeAcN**

This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For more information see http://pid.geoscience.gov.au/dataset/ga/122229
https://cmi.ga.gov.au/data-products/dea/190/dea-surface-reflectance-nbart-sentinel-2-msi

For service status information, see https://status.dea.ga.gov.au""",
    "multi_product": True,
    "product_names": ["s2a_nrt_granule", "s2b_nrt_granule"],
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
            "band": "fmask",
            "products": ["s2a_nrt_granule", "s2b_nrt_granule"],
            "ignore_time": False,
            "ignore_info_flags": [],
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

s2b_layer = {
    "name": "s2b_nrt_granule_nbar_t",
    "title": "DEA Surface Reflectance (Sentinel-2B MSI Near Real-Time)",
    "abstract": """Sentinel-2 Multispectral Instrument - Nadir BRDF Adjusted Reflectance + Terrain Illumination Correction (Sentinel-2B MSI) near real time

**This dataset has been replaced with an updated version. This service will be decommissioned in January 2023. For more information please see https://bit.ly/3FAeAcN**

This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For more information see http://pid.geoscience.gov.au/dataset/ga/122229
https://cmi.ga.gov.au/data-products/dea/190/dea-surface-reflectance-nbart-sentinel-2-msi

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "s2b_nrt_granule",
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
            "band": "fmask",
            "product": "s2b_nrt_granule",
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
    "name": "s2a_nrt_granule_nbar_t",
    "title": "DEA Surface Reflectance (Sentinel-2A MSI Near Real-Time)",
    "abstract": """Sentinel-2 Multispectral Instrument - Nadir BRDF Adjusted Reflectance + Terrain Illumination Correction (Sentinel-2A MSI) near real time

**This dataset has been replaced with an updated version. This service will be decommissioned in January 2023. For more information please see https://bit.ly/3FAeAcN**

This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016
https://cmi.ga.gov.au/data-products/dea/190/dea-surface-reflectance-nbart-sentinel-2-msi

For more information see http://pid.geoscience.gov.au/dataset/ga/122229
For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "s2a_nrt_granule",
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
            "band": "fmask",
            "product": "s2a_nrt_granule",
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
