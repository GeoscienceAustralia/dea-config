from ows_refactored.inland_water.wofs.bands_wo_cfg import bands_wofs_sum
from ows_refactored.inland_water.wofs.style_wofs_cfg import (
    style_seasonal_wofs_summary_frequency,
    style_seasonal_wofs_summary_frequency_blue, style_wofs_seasonal_clear,
    style_wofs_seasonal_wet)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

c3_statistics_layer = {
    "title": "DEA Water Observations April to October (Landsat, C3)",
    "name": "wofs_apr_oct_summary_statistics_3",
    "abstract": """DEA Water Observations Statistics 30m 3.1.6 (Landsat, April - October, Frequency)
The DEA Water Observations April to October Statistic is a set of seasonal statistical summaries of the DEA Water Observations product that combines the many years of observations into summary products that help the understanding of surface water across Australia. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains: 
1) Water summary- what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage).

No clear observations of water causes an area to appear transparent,
red through to yellow represent areas seen to be wet up to 30% of the time,
green through to light blue represent areas seen to be wet 40-60% of the time,
deep blue and purple correspond to an area being wet through 80%-100% of clear observations.

2) Wet observation count- how many times water was detected in observations that were clear.
No clear observations of water causes an area to appear transparent,
1-6 total clear observations of water correlate with red and yellow colours,
7-12 clear observations of water correlate with green through to light blue,
12+ clear observations of water correlates with increasingly dark shades of blue.


3) Clear observation count- how many times an area could be clearly seen (i.e. not affected by clouds, shadows or other satellite observation problems).
No clear observations causes an area to appear transparent,
1-15 total clear observations correlates with red and yellow colours,
18-22 clear observations correlates with light green,
23+ clear observations correlates with inreasingly dark shades of green.

https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_wo_fq_apr_oct_3",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "time_resolution": "month",
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "seasonal_WOfS_frequency",
        "styles": [
            style_seasonal_wofs_summary_frequency,
            style_seasonal_wofs_summary_frequency_blue,
            style_wofs_seasonal_wet,
            style_wofs_seasonal_clear,

        ],
    },
}
