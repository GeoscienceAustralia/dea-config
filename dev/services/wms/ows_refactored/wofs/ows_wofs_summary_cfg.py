from ows_refactored.ows_reslim_cfg import (
    reslim_wms_min_zoom_15_cache_rules,
    reslim_wms_min_zoom_35,
)
from ows_refactored.ows_legend_cfg import (
    legend_idx_percentage_by_20,
    legend_idx_percentage_by_25,
    legend_idx_twentyplus_3ticks,
    legend_idx_thirtyplus_4ticks,
)
from ows_refactored.wofs.bands_wo_cfg import (
    bands_wofs_filt_sum,
    bands_wofs_sum,
    bands_wofs_obs,
)

layers = {
    "title": "Water Observations from Space",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "Water Observations from Space 25m Wet Count (WOfS Statistics)",
            "name": "wofs_summary_wet",
            "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products which help the understanding of surface water across Australia.  The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains Wet Count: how many times water was detected in observations that were clear. No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary.

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["count_wet"],
            },
            "styling": {
                "default_style": "water_observations",
                "styles": [
                    style_wofs_count_wet,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Clear Count (WOfS Statistics)",
            "name": "wofs_summary_clear",
            "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products which help the understanding of surface water across Australia.  The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains Clear Count: how many times an area could be clearly seen (ie. not affected by clouds, shadows or other satellite observation problems). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary.

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["count_clear"],
            },
            "styling": {
                "default_style": "clear_observations",
                "styles": [
                    style_wofs_count_clear,
                ],
            },
        },
        {
            "title": "Water Observations from Space 25m Water Summary (WOfS Statistics)	",
            "name": "Water Observations from Space Statistics",
            "abstract": """
Water Observations from Space (WOfS) Statistics is a set of statistical summaries of the WOfS product which combines WOfS observations into summary products that help the understanding of surface water across Australia. WOfS Statistics is calculated from the full depth time series (1986 – 2018). The water detected for each location is summed through time and then compared to the number of clear observations of that location. The result is a percentage value of the number of times water was observed at the location. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time (water summary).

This layer contains the Water Summary: the percentage of clear observations which were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.

As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of the water summary.

For more information please see: https://data.dea.ga.gov.au/WOfS/summary/v2.1.0/Product%20Description.pdf

For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:3577",
                "native_resolution": [25, -25],
                "default_bands": ["frequency"],
            },
            "styling": {
                "default_style": "WOfS_frequency",
                "styles": [
                    style_wofs_frequency,
                    style_wofs_frequency_blue,
                ],
            },
        },
    ],
}
