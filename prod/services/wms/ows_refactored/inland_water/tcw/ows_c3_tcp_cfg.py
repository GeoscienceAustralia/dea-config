from ows_refactored.ows_reslim_cfg import reslim_standard

bands_tci_percentile = {
    "wet_pc_10": [],
    "wet_pc_50": [],
    "wet_pc_90": [],
    "green_pc_10": [],
    "green_pc_50": [],
    "green_pc_90": [],
    "bright_pc_10": [],
    "bright_pc_50": [],
    "bright_pc_90": [],
}

wet_legend = {
    "begin": -1200,
    "end": 0,
    "tick_every": 120,
    "title": "Tasseled Cap Wetness",
    "rcParams": {"font.size": 9},
}

green_legend = {
    "begin": 0,
    "end": 2000,
    "tick_every": 200,
    "title": "Tasseled Cap Greenness",
    "rcParams": {"font.size": 9},
}

bright_legend = {
    "begin": 0,
    "end": 4000,
    "tick_every": 400,
    "title": "Tasseled Cap Brightness",
    "rcParams": {"font.size": 9},
}


style_tcw_10 = {
    "name": "wet_10_percentile",
    "title": "Tasseled Cap Wetness 10th Percentile",
    "abstract": "The 10th Percentile of Tasseled Cap Wetness Index",
    "needed_bands": ["wet_pc_10"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "wet_pc_10",
        },
    },
    "range": [-1200.0, 0.0],
    "mpl_ramp": "gist_earth_r",
    "legend": wet_legend,
}

style_tcw_50 = {
    "name": "wet_50_percentile",
    "title": "Tasseled Cap Wetness 50th Percentile",
    "abstract": "The 50th Percentile of Tasseled Cap Wetness Index",
    "needed_bands": ["wet_pc_50"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "wet_pc_50",
        },
    },
    "range": [-1200.0, 0.0],
    "mpl_ramp": "gist_earth_r",
    "legend": wet_legend,
}

style_tcw_90 = {
    "name": "wet_90_percentile",
    "title": "Tasseled Cap Wetness 90th Percentile",
    "abstract": "The 90th Percentile of Tasseled Cap Wetness Index",
    "needed_bands": ["wet_pc_90"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "wet_pc_90",
        },
    },
    "range": [-1200.0, 0.0],
    "mpl_ramp": "gist_earth_r",
    "legend": wet_legend
}

style_tcg_10 = {
    "name": "green_10_percentile",
    "title": "Tasseled Cap Greenness 10th Percentile",
    "abstract": "The 10th Percentile of Tasseled Cap Greenness Index",
    "needed_bands": ["green_pc_10"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "green_pc_10",
        },
    },
    "range": [0, 2000],
    "mpl_ramp": "YlGn",
    "legend": green_legend
}

style_tcg_50 = {
    "name": "green_50_percentile",
    "title": "Tasseled Cap Greenness 50th Percentile",
    "abstract": "The 50th Percentile of Tasseled Cap Greenness Index",
    "needed_bands": ["green_pc_50"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "green_pc_50",
        },
    },
    "range": [0, 2000],
    "mpl_ramp": "YlGn",
    "legend": green_legend
}

style_tcg_90 = {
    "name": "green_90_percentile",
    "title": "Tasseled Cap Greenness 90th Percentile",
    "abstract": "The 90th Percentile of Tasseled Cap Greenness Index",
    "needed_bands": ["green_pc_90"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "green_pc_90",
        },
    },
    "range": [0, 2000],
    "mpl_ramp": "YlGn",
    "legend": green_legend
}

style_tcb_10 = {
    "name": "bright_10_percentile",
    "title": "Tasseled Cap Brightness 10th Percentile",
    "abstract": "The 10th Percentile of Tasseled Cap Brightness Index",
    "needed_bands": ["bright_pc_10"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bright_pc_10",
        },
    },
    "range": [0, 4000.0],
    "mpl_ramp": "Wistia",
    "legend": bright_legend
}

style_tcb_50 = {
    "name": "bright_50_percentile",
    "title": "Tasseled Cap Brightness 50th Percentile",
    "abstract": "The 50th Percentile of Tasseled Cap Brightness Index",
    "needed_bands": ["bright_pc_50"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bright_pc_50",
        },
    },
    "range": [0, 4000.0],
    "mpl_ramp": "Wistia",
    "legend": bright_legend
}

style_tcb_90 = {
    "name": "bright_90_percentile",
    "title": "Tasseled Cap Brightness 90th Percentile",
    "abstract": "The 90th Percentile of Tasseled Cap Brightness Index",
    "needed_bands": ["bright_pc_90"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bright_pc_90",
        },
    },
    "range": [0, 4000.0],
    "mpl_ramp": "Wistia",
    "legend": bright_legend
}

layers = {
    "title": "DEA Tasseled Cap Indices Percentiles (Landsat)",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Tasseled Cap Indices Percentiles Calendar Year (Landsat)",
            "name": "ga_ls_tc_pc_cyear_3",
            "abstract": """Tasseled Cap Indices Percentiles 30m 1.0.0

The Tasseled Cap Indices Percentiles provide an annual summary of landscape wetness, greenness and brightness indices that can be used to identify wetlands and groundwater ecosystems.

They provide annual statistical summaries (10th, 50th and 90th percentiles) of the Tasseled Cap indices.

They are intended for use as inputs into classification algorithms to identify potential wetlands and groundwater dependent ecosystems, and characterise salt flats, clay pans, salt lakes and coastal land forms.

Geoscience Australia Landsat Collection 3 Tasseled Cap Indices Percentiles, 30 metre, Australian Albers Equal Area projection (EPSG:3577).
Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Areas that are partially covered in water, or where water is mixed with vegetation when viewed from above, provide habitat for a wide range of aquatic organisms.
The ability to map partial inundation is also crucial to understand patterns of human water use. We need to be able to identify potential wetlands and groundwater dependent ecosystems on the Australian continent so that they can be monitored and managed.
The Tasseled Cap Wetness Percentiles provide a multi-decadal summary of landscape wetness that can be used to identify wetlands and groundwater ecosystems.
They provide statistical summaries (10th, 50th and 90th percentiles) of the Tasseled Cap wetness index from 1987 to 2017.
They are intended for use as inputs into classification algorithms to identify potential wetlands and groundwater dependent ecosystems, and characterise salt flats, clay pans, salt lakes and coastal land forms.
This product provides valuable discrimination for characterising:
    - vegetated wetlands,
    - salt flats,
    - salt lakes,
    - coastal land cover classes
The Tasseled Cap indices transform translates the six spectral bands of Landsat into a single wetness index.  The wetness index can be used to identify areas in the landscape that are potentially wetlands or groundwater dependent ecosystems. The Tasseled Cap Indices Percentiles capture how the wetness, greeness and brightness index behaves over time.  The percentiles are well suited to characterising wetlands, salt flats/salt lakes and coastal ecosystems. However, care should be applied when analysing the wetness index, as soil colour and fire scars can cause misleading results. In areas of high relief caused by cliffs or steep terrain, terrain shadows can cause false positives (a falsely high wetness index).
The 10th, 50th and 90th percentiles of the Tasseled Cap Indices are intended to capture the extreme (10th and 90th percentile) values and long-term average (50th percentile) values of the indices.  Percentiles are used in preference to minimum, maximum and mean, as the min/max/mean statistical measures are more sensitive to undetected cloud/cloud shadow, and can be misleading for non-normally distributed data.
The Tasseled Cap Indices Percentiles are intended to complement the Water Observations (WO) algorithm. WO is designed to discriminate open water, but the Tasseled Cap wetness index identifies areas of water and areas where water and vegetation are mixed together; i.e. mangroves and palustrine wetlands.
If you are interested in terrestrial vegetation (where water in the pixel is not a factor), use the Fractional Cover product, which provides a better biophysical characterisation of green vegetation fraction, dry vegetation fraction and bare soil vegetation fraction.
In terms of limitations, caution should be used, especially with the Tasseled Cap Indices results in areas where residual terrain shadow, or dark soils can cause high 'wetness' index values.
One of the limitations of using the Tasseled Cap wetness index is that it will identify all 'wet' things, including potential wetlands, groundwater dependent ecosystems, irrigated crops/pasture, man-made water storages and sewerage treatment, and does not discriminate between these. As such it should be used in conjunction with other contextual data to ensure that features identified using the Tasseled Cap Wetness Percentiles are features of interest rather than false positives.
We used the Tasseled Cap transforms described in Crist et al. (1985).
Crist, E. P. (1985). A TM Tasseled Cap equivalent transformation for reflectance factor data. Remote Sensing of Environment, 17(3), 301–306. https://doi.org/10.1016/0034-4257(85)90102-6

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls_tc_pc_cyear_3",
            "bands": bands_tci_percentile,
            "resource_limits": reslim_standard,
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "time_resolution": "summary",
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "wet_10_percentile",
                "styles": [
                    style_tcw_10,
                    style_tcw_50,
                    style_tcw_90,
                    style_tcg_10,
                    style_tcg_50,
                    style_tcg_90,
                    style_tcb_10,
                    style_tcb_50,
                    style_tcb_90,
                ],
            },
        },
    ],
}
