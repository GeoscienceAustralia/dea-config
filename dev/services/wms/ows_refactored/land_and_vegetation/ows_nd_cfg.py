from ows_refactored.land_and_vegetation.band_lav_cfg import bands_ls
from ows_refactored.land_and_vegetation.style_lav_cfg import (
    styles_barest_earth_list, styles_barest_earth_mosaic_list)
from ows_refactored.ows_reslim_cfg import reslim_standard

ls8_be_layers = {
    "title": "GA Barest Earth (Landsat 8 OLI/TIRS)",
    "name": "ls8_barest_earth_mosaic",
    "abstract": """GA Barest Earth (Landsat 8 OLI/TIRS)

A `weighted geometric median’ approach has been used to estimate the median surface reflectance of the barest state (i.e., least vegetation) observed through Landsat-8 OLI observations from 2013 to September 2018 to generate a six-band Landsat-8 Barest Earth pixel composite mosaic over the Australian continent.
The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The weighted median approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.
Reference: Dale Roberts, John Wilford, and Omar Ghattas (2018). Revealing the Australian Continent at its Barest, submitted.
Mosaics are available for the following years:
Landsat 8: 2013 to 2017;

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "ls8_barest_earth_albers",
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
        "styles": styles_barest_earth_mosaic_list,
    },
}


ls30_be_layers = {
    "title": "GA Barest Earth (Landsat)",
    "name": "landsat_barest_earth",
    "abstract": """GA Barest Earth (Landsat)

An estimate of the spectra of the barest state (i.e., least vegetation) observed from imagery of the Australian continent collected by the Landsat 5, 7, and 8 satellites over a period of more than 30 years (1983 - 2018).
The bands include BLUE (0.452 - 0.512), GREEN (0.533 - 0.590), RED, (0.636 - 0.673) NIR (0.851 - 0.879), SWIR1 (1.566 - 1.651) and SWIR2 (2.107 - 2.294) wavelength regions. The approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time. The product reduces the influence of vegetation and allows for more direct mapping of soil and rock mineralogy.
This product complements the Landsat-8 Barest Earth which is based on the same algorithm but just uses Landsat8 satellite imagery from 2013-2108. Landsat-8's OLI sensor provides improved signal-to-noise radiometric (SNR) performance quantised over a 12-bit dynamic range compared to the 8-bit dynamic range of Landsat-5 and Landsat-7 data. However the Landsat 30+ Barest Earth has a greater capacity to find the barest ground due to the greater temporal depth.
Reference: Roberts, D., Wilford, J., Ghattas, O. (2019). Exposed Soil and Mineral Map of the Australian Continent Revealing the Land at its Barest. Nature Communications. Mosaics are available for the following years: Landsat 5 / Landsat 7 / Landsat 8 - 1983 to 2018;

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "landsat_barest_earth",
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
        "styles": styles_barest_earth_list,
    },
}
