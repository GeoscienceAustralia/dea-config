from ows_refactored.surface_reflectance.style_ls_cfg import (
    styles_barest_earth_list,
    styles_ls_list,
)
from ows_refactored.surface_reflectance.band_ls_cfg import bands_ls
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_35

ls8_be_layers = {
    "title": "Landsat-8 Barest Earth",
    "abstract": """
                A `weighted geometric median’ approach has been used to estimate the median surface reflectance of the barest state (i.e., least vegetation) observed through Landsat-8 OLI observations from 2013 to September 2018 to generate a six-band Landsat-8 Barest Earth pixel composite mosaic over the Australian continent.
                The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The weighted median approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.
                Reference: Dale Roberts, John Wilford, and Omar Ghattas (2018). Revealing the Australian Continent at its Barest, submitted.
                Mosaics are available for the following years:
                    Landsat 8: 2013 to 2017;
                            """,
    "layers": [
        {
            "title": "Landsat-8 Barest Earth 25m albers (Landsat-8)",
            "name": "ls8_barest_earth_mosaic",
            "abstract": """
                A `weighted geometric median’ approach has been used to estimate the median surface reflectance of the barest state (i.e., least vegetation) observed through Landsat-8 OLI observations from 2013 to September 2018 to generate a six-band Landsat-8 Barest Earth pixel composite mosaic over the Australian continent.
                The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The weighted median approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.
                Reference: Dale Roberts, John Wilford, and Omar Ghattas (2018). Revealing the Australian Continent at its Barest, submitted.
                Mosaics are available for the following years:
                    Landsat 8: 2013 to 2017;
                For service status information, see https://status.dea.ga.gov.au
                                    """,
            "product_name": "ls8_barest_earth_albers",
            "bands": bands_ls,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["red", "green", "blue"],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": styles_barest_earth_list,
            },
        }
    ],
}


ls30_be_layers = {
    "title": "Landsat 30+ Barest Earth",
    "abstract": """
                	An estimate of the spectra of the barest state (i.e., least vegetation) observed from imagery of the Australian continent collected by the Landsat 5, 7, and 8 satellites over a period of more than 30 years (1983 - 2018). The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy. This product complements the Landsat-8 Barest Earth which is based on the same algorithm but just uses Landsat8 satellite imagery from 2013-2108. Landsat-8's OLI sensor provides improved signal-to-noise radiometric (SNR) performance quantised over a 12-bit dynamic range compared to the 8-bit dynamic range of Landsat-5 and Landsat-7 data. However the Landsat 30+ Barest Earth has a greater capacity to find the barest ground due to the greater temporal depth. Reference: Roberts, D., Wilford, J., Ghattas, O. (2019). Exposed Soil and Mineral Map of the Australian Continent Revealing the Land at its Barest. Nature Communications. Mosaics are available for the following years: Landsat 5 / Landsat 7 / Landsat 8 - 1983 to 2018;
                            """,
    "layers": [
        {
            "title": "Landsat 30+ Barest Earth 25m albers (Combined Landsat)",
            "name": "landsat_barest_earth",
            "abstract": """
                	An estimate of the spectra of the barest state (i.e., least vegetation) observed from imagery of the Australian continent collected by the Landsat 5, 7, and 8 satellites over a period of more than 30 years (1983 - 2018).
                    The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.
                    This product complements the Landsat-8 Barest Earth which is based on the same algorithm but just uses Landsat8 satellite imagery from 2013-2108. Landsat-8's OLI sensor provides improved signal-to-noise radiometric (SNR) performance quantised over a 12-bit dynamic range compared to the 8-bit dynamic range of Landsat-5 and Landsat-7 data. However the Landsat 30+ Barest Earth has a greater capacity to find the barest ground due to the greater temporal depth.
                    Reference: Roberts, D., Wilford, J., Ghattas, O. (2019). Exposed Soil and Mineral Map of the Australian Continent Revealing the Land at its Barest. Nature Communications. Mosaics are available for the following years: Landsat 5 / Landsat 7 / Landsat 8 - 1983 to 2018; For service status information, see https://status.dea.ga.gov.au
                                    """,
            "product_name": "landsat_barest_earth",
            "bands": bands_ls,
            "resource_limits": reslim_wms_min_zoom_35,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["red", "green", "blue"],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": styles_barest_earth_list,
            },
        }
    ],
}
