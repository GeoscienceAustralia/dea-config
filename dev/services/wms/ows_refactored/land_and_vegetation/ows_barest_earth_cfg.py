from ows_refactored.land_and_vegetation.band_lav_cfg import \
    bands_s2_barest_earth
from ows_refactored.land_and_vegetation.style_lav_cfg import \
    styles_s2_barest_earth_list
from ows_refactored.ows_reslim_cfg import reslim_for_sentinel2

layers = {
    "title": "GA Barest Earth (Sentinel-2)",
    "name": "s2_barest_earth",
    "abstract": """GA Barest Earth (Sentinel-2)

Abstract

The Sentinel-2 Bare Earth thematic product provides the first national scale mosaic of the Australian continent to support improved mapping of soil and geology. The bare earth algorithm using all available Sentinel-2 A and Sentinel-2 B observations up to September 2020 preferentially weights bare pixels through time to significantly reduce the effect of seasonal vegetation in the imagery. The result are image pixels that are more likely to reflect the mineralogy and/or geochemistry of soil and bedrock.  The algorithm uses a high-dimensional weighted geometric median approach that maintains the spectral relationships across all Sentinel-2 bands. A similar bare earth algorithm has been applied to Geoscience Australia’s deeper Landsat time series archive (please search for "Landsat barest Earth".  Both bare earth products have spectral bands in the visible near infrared and shortwave infrared region of the electromagnetic spectrum. However, the main visible and near-infrared Sentinel-2 bands have a spatial resolution of 10 meters compared to 30m for the Landsat TM equivalents. The weighted median approach is robust to outliers (such as cloud, shadows, saturation, corrupted pixels) and also maintains the relationship between all the spectral wavelengths in the spectra observed through time.

Not all the sentinel-2 bands have been processed - we have excluded atmospheric bands including 1, 9 and 10. The remaining bands have been re-number 1-10 and these bands correlate to the original bands in brackets below:
1 = blue (2) , 2 = green (3) , 3 = red (4), 4 = vegetation red edge (5), 5 =  vegetation red edge (6), 6=  vegetation red edge (7), 7 = NIR(8), 8 = Narrow NIR (8a), 9 = SWIR1 (11) and 10 = SWIR2(12).

All 10 bands have been resampled to 10 meters to facilitate band integration and use in machine learning.

Pixel quality and the degree of barest recorded on the ground will largely depend on the number of ‘clean’ cloud free bare earth observation. We have noticed some image artefacts near the vicinity of Lake Eyre where highly reflective surface materials are not being well separated by the cloud filter – these artefacts  will be address in a future improved version of the bare earth model.

Lineage Statement

Large-scale image composites are increasingly important for a variety of applications such as land cover mapping, soil and bedrock mapping, change detection, and the generation of high-quality data to parameterise and validate bio-physical and geophysical models. A number of compositing methodologies are being used in remote sensing in general, however challenges such as maintaining the spectral relationship between bands, mitigating against boundary artifacts due to mosaicking scenes from different epochs, and ensuring spatial regularity across the mosaic image still exist.

The creation of good composite images is a particularly important technology since the opening of the Landsat archive by the United States Geological Survey. The greater availability of satellite imagery has resulted in demand to provide large regional mosaics that are representative of conditions over specific time periods while also being free of clouds and other unwanted image noise. One approach is the stitching together of a number of clear images. Another is the creation of mosaics where pixels from different epochs are combined based on some algorithm from a time series of observations. This ‘pixel composite’ approach to mosaic generation provides a more consistent result compared with stitching clear images due to the improved color balance created by the combining of one-by-one pixel representative images. Another strength of pixel-based composites is their ability to be automated for application to very large data collections and time series such as national satellite data archives.

The Bare Earth pixel composite mosaic (BE-PCM) provides an approach that leverages high-dimensional statistical theory to deliver a spectrally consistent, artefact-free pixel composite product that is representative of the barest (i.e., least vegetation) state at each pixel over the specific time period.

The BE-PCM is derived from Sentinel-2 A and Sentinel-2 B observations from 2014 to September 2020 corrected to measurements of NBAR surface reflectance (e.g., SR-N_25_2.0.0 or SR-NT_25_2.0.0). The data are masked for cloud, shadows and other image artefacts using the pixel quality product (PQ_25_2.0.0) to help provide as clear a set of observations as possible from which to calculate the BE-PCM.

The BE-PCM methodology and algorithm is given in Roberts, Wilford, Ghattas (2018). The technology builds on the earlier work of Roberts et al. (2017) where a method for producing cloud-free pixel composite mosaics using ‘geometric medians’ was proposed.

Note: The constituent pixels in the BE-PCM pixel composite mosaics are synthetic, meaning that the pixels have not been physically observed by the satellite. Rather they are the computed high-dimensional median of a time series of pixels which gives a robust estimate of the median state of the Earth at its barest (i.e., least vegetation).

References

Roberts, D., Wilford, J., Ghattas, O. (2018). Revealing the Australian Continent at its Barest. Submitted and under review.

Roberts, D., Mueller, N., Mcintyre, A. (2017). High-dimensional pixel composites from earth observation time series.
IEEE Transactions on Geoscience and Remote Sensing 55 (11), 6254-6264

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "s2_barest_earth",
    "bands": bands_s2_barest_earth,
    # "time_resolution": 'year',
    "resource_limits": reslim_for_sentinel2,
    "native_crs": "EPSG:3577",
    "native_resolution": [10, -10],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_barest_earth_list},
}
