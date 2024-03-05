from ows_refactored.land_and_vegetation.fc.band_fc_cfg import \
    bands_fc_percentile
from ows_refactored.land_and_vegetation.fc.flag_fc_cfg import \
    fc_percentile_flags
from ows_refactored.land_and_vegetation.fc.style_fc_cfg import \
    styles_fc_pc_list
from ows_refactored.ows_reslim_cfg import reslim_standard

layer = {
    "title": "DEA Fractional Cover Percentiles Calendar Year (Landsat)",
    "name": "ga_ls_fc_pc_cyear_3",
    "abstract": """Fractional Cover 30m Percentiles 3.0.0 (Landsat, Annual)
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 30m x 30m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program.
This contains the percentage of green vegetation, non-green vegetation and bare soil per pixel at the 10th, 50th (median) and 90th percentiles respectively for observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.
Fractional Cover products use Water Observations (WO) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 3 clear observations over the year.
https://docs.dea.ga.gov.au/data/product/dea-fractional-cover-percentiles-landsat/
For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "ga_ls_fc_pc_cyear_3",
    "bands": bands_fc_percentile,
    "resource_limits": reslim_standard,
    "flags": fc_percentile_flags,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "time_resolution": "summary",
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "fc_rgb",
        "styles": styles_fc_pc_list,
    },
}
