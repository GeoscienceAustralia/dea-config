from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15
from ows_refactored.sentinel2.style_s2_cfg import styles_s2_list


bands_sentinel2_ard_nbar = {
    "nbar_coastal_aerosol": [
        "nbar_coastal_aerosol",
        "coastal_aerosol",
        "nbart_coastal_aerosol",
        "nbart_narrow_blue",
        "nbar_narrow_blue" "narrow_blue",
    ],
    "nbar_blue": ["nbar_blue", "blue", "nbart_blue"],
    "nbar_green": ["nbar_green", "green", "nbart_green"],
    "nbar_red": ["nbar_red", "red", "nbart_red"],
    "nbar_red_edge_1": ["nbar_red_edge_1", "red_edge_1", "nbart_red_edge_1"],
    "nbar_red_edge_2": ["nbar_red_edge_2", "red_edge_2", "nbart_red_edge_2"],
    "nbar_red_edge_3": ["nbar_red_edge_3", "red_edge_3", "nbart_red_edge_3"],
    "nbar_nir_1": ["nbar_nir_1", "nir", "nir_1", "nbart_nir_1"],
    "nbar_nir_2": ["nbar_nir_2", "nir2", "nbart_nir_2"],
    "nbar_swir_2": ["nbar_swir_2", "swir_2", "nbart_swir_2"],
    "nbar_swir_3": ["nbar_swir_3", "swir_3", "nbart_swir_3"],
}

layers = {
    "title": "Sentinel Definitive",
    "abstract": """
	This is a definitive archive of daily Sentinel-2 data.The Surface Reflectance product has been corrected to account for variationscaused by atmospheric properties, sun position and sensor view angle at time of image capture.These corrections have been applied to all satellite imagery in the Sentinel-2 archiveFor more information see http://pid.geoscience.gov.au/dataset/ga/129684
""",
    "layers": [
        {
            "name": "s2_ard_granule_nbar_t",
            "title": "Sentinel Definitive Surface Reflectance (Sentinel 2 (A and B combined))",
            "abstract": """
This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time.
The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive.
The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016
For more information see http://pid.geoscience.gov.au/dataset/ga/129684
For service status information, see https://status.dea.ga.gov.au
""",
            "multi_product": True,
            "product_names": ["ga_s2a_ard_nbar_granule", "ga_s2b_ard_nbar_granule"],
            "bands": bands_sentinel2_ard_nbar,
            "resource_limits": reslim_wms_min_zoom_15,
            "dynamic": True,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [10.0, 10.0],
                "default_bands": ["nbar_red", "nbar_green", "nbar_blue"],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": styles_s2_list
            },
        },
        {
            "name": "s2b_ard_granule_nbar_t",
            "title": "Sentinel Definitive Surface Reflectance (Sentinel 2B)",
            "abstract": """
This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time. The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive. For more information see http://pid.geoscience.gov.au/dataset/ga/129684 The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors. The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including: - Influence on the remote sensing signal from nearby land and/or atmospheric effects - Optically shallow water - Cloud cover Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016 For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ga_s2b_ard_nbar_granule",
            "bands": bands_sentinel2_ard_nbar,
            "resource_limits": reslim_wms_min_zoom_15,
            "dynamic": True,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [10.0, 10.0],
                "default_bands": ["nbar_red", "nbar_green", "nbar_blue"],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": styles_s2_list
            },
        },
        {
            "name": "s2a_ard_granule_nbar_t",
            "title": "Sentinel Definitive Surface Reflectance (Sentinel 2A)",
            "abstract": """
This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time. The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive. For more information see http://pid.geoscience.gov.au/dataset/ga/129684 The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors. The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including: - Influence on the remote sensing signal from nearby land and/or atmospheric effects - Optically shallow water - Cloud cover Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016 For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ga_s2a_ard_nbar_granule",
            "bands": bands_sentinel2_ard_nbar,
            "resource_limits": reslim_wms_min_zoom_15,
            "dynamic": True,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [10.0, 10.0],
                "default_bands": ["nbar_red", "nbar_green", "nbar_blue"],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": styles_s2_list
            },
        },
    ],
}
