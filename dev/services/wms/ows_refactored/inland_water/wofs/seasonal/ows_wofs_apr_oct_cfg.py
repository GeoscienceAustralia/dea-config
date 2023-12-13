from ows_refactored.inland_water.wofs.bands_wo_cfg import bands_wofs_sum
from ows_refactored.inland_water.wofs.styles_wo_cfg import (
    style_seasonal_wofs_clear_3, style_seasonal_wofs_summary_frequency_3,
    style_seasonal_wofs_summary_frequency_blue_3,
    style_seasonal_wofs_summary_frequency_cvf_3, style_seasonal_wofs_wet_3)
from ows_refactored.ows_reslim_cfg import reslim_standard

c3_statistics_layer = {
    "title": "DEA Water Observations April to October (Landsat)",
    "name": "ga_ls_wo_fq_apr_oct_3",
    "abstract": """**Geoscience Australia Water Observations, Seasonal Frequency Statistics, April to October (Landsat, Collection 3, 30 m, WO-STATS-APR-OCT, 3.1.6).**

The DEA Seasonal Water Observation (April to October) Statistic is a set of seasonal statistical summaries of the DEA Water Observations product. The product combines satellite observations, that occur during April to October within each year, into summary products that help the understanding of surface water across Australia. The layers available are: the count of clear observations; the count of wet observations; and the percentage of wet observations that were observed over the specified time period in the landscape.

**What this product offers**

Each dataset in this product consists of the following datasets:

- Clear Count: how many times an area could be clearly seen (i.e. not affected by clouds, shadows or other satellite observation problems)
- Wet Count: how many times water was detected in observations that were clear
- Water Summary: what percentage of clear observations were detected as wet (i.e. the ratio of wet to clear as a percentage)

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the input water classifications, and can be difficult to interpret on its own.


For more information, see https://docs.dea.ga.gov.au/data/product/dea-water-observations-statistics-landsat/

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_wo_fq_apr_oct_3",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_standard,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "time_resolution": "month",
    "flags": [
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": [],
        },
    ],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "seasonal_wofs_frequency_3",
        "styles": [
            style_seasonal_wofs_summary_frequency_3,
            style_seasonal_wofs_summary_frequency_cvf_3,
            style_seasonal_wofs_summary_frequency_blue_3,
            style_seasonal_wofs_wet_3,
            style_seasonal_wofs_clear_3,
        ],
    },
}
