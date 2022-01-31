from ows_refactored.land_and_vegetation.fc.band_fc_cfg import \
    bands_fc_percentile
from ows_refactored.land_and_vegetation.fc.flag_fc_cfg import \
    fc_percentile_flags
from ows_refactored.land_and_vegetation.fc.style_fc_cfg import (
    style_fc_rgb, styles_fc_bare_list, styles_fc_gv_list, styles_fc_ngv_list)
from ows_refactored.ows_reslim_cfg import reslim_standard

fcp_annual_layers = {
    "title": "Annual Fractional Cover Summaries",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Fractional Cover Percentiles (Landsat, Annual, Green Vegetation)",
            "name": "fcp_green_veg",
            "abstract": """Fractional Cover 25m Percentiles 2.2.1 (Landsat, Annual, Green Vegetation)

Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

This contains the percentage of green vegetation per pixel at the 10th, 50th (median) and 90th percentiles for observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

https://cmi.ga.gov.au/data-products/dea/120/dea-fractional-cover-percentiles-landsat

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "fc_percentile_albers_annual",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_standard,
            "flags": fc_percentile_flags,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {"default_style": "green_veg_10", "styles": styles_fc_gv_list},
        },
        {
            "title": "DEA Fractional Cover Percentiles (Landsat, Annual, Non-Green Vegetation)",
            "name": "fcp_non_green_veg",
            "abstract": """Fractional Cover 25m Percentiles 2.2.1 (Landsat, Annual, Non-Green Vegetation)

Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

This contains the percentage of non-green vegetation per pixel at the 10th, 50th (median) and 90th percentiles for observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

https://cmi.ga.gov.au/data-products/dea/120/dea-fractional-cover-percentiles-landsat

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "fc_percentile_albers_annual",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_standard,
            "flags": fc_percentile_flags,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "non_green_veg_10",
                "styles": styles_fc_ngv_list,
            },
        },
        {
            "title": "DEA Fractional Cover Percentiles (Landsat, Annual, Bare Ground)",
            "name": "fcp_bare_ground",
            "abstract": """Fractional Cover 25m Percentiles 2.2.1 (Landsat, Annual, Bare Ground)

Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover This contains the percentage of bare soil per pixel at the 10th, 50th (median) and 90th percentiles for observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year. Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

https://cmi.ga.gov.au/data-products/dea/120/dea-fractional-cover-percentiles-landsat

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "fc_percentile_albers_annual",
            "bands": bands_fc_percentile,
            "resource_limits": reslim_standard,
            "flags": fc_percentile_flags,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "bare_ground_10",
                "styles": styles_fc_bare_list,
            },
        }
    ],
}

fcp_rgb_layer = {
    "title": "DEA Fractional Cover Percentiles (Landsat, Annual)",
    "name": "fcp_rgb",
    "abstract": """Fractional Cover 25m Percentiles 2.2.1 (Landsat, Annual)

Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.

Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program.

This contains a three band combination of the 50th Percentile for green vegetation, non green vegetation and bare soil observations acquired in each full calendar year (1st of January - 31st December) from 1987 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

https://cmi.ga.gov.au/data-products/dea/120/dea-fractional-cover-percentiles-landsat

For service status information, see https://status.dea.ga.gov.au""",
    "product_name": "fc_percentile_albers_annual",
    "bands": bands_fc_percentile,
    "resource_limits": reslim_standard,
    "flags": fc_percentile_flags,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "fc_rgb",
        "styles": [style_fc_rgb],
    },
}
