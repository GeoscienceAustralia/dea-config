from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

bands_tcw_percentile = {
    "TCW_PC_10": [],
    "TCW_PC_50": [],
    "TCW_PC_90": [],
}

style_tcw_10 = {
    "name": "tcw_10_percentile",
    "title": "Tasseled Cap Wetness 10th Percentile",
    "abstract": "The 10th Percentile of Tasseled Cap Wetness Index (1986-2018)",
    "needed_bands": ["TCW_PC_10"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "TCW_PC_10",
        },
    },
    "range": [-1200.0, 0.0],
    "mpl_ramp": "gist_earth_r",
    "legend": {
        "url": "https://data.dea.ga.gov.au/derivative/ga_ls_tcw_percentiles_2/tcw_percentiles_legend.png",
    },
}

style_tcw_50 = {
    "name": "tcw_50_percentile",
    "title": "Tasseled Cap Wetness 50th Percentile",
    "abstract": "The 50th Percentile of Tasseled Cap Wetness Index (1986-2018)",
    "needed_bands": ["TCW_PC_50"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "TCW_PC_50",
        },
    },
    "range": [-1200.0, 0.0],
    "mpl_ramp": "gist_earth_r",
    "legend": {
        "url": "https://data.dea.ga.gov.au/derivative/ga_ls_tcw_percentiles_2/tcw_percentiles_legend.png",
    },
}

style_tcw_90 = {
    "name": "tcw_90_percentile",
    "title": "Tasseled Cap Wetness 90th Percentile",
    "abstract": "The 90th Percentile of Tasseled Cap Wetness Index (1986-2018)",
    "needed_bands": ["TCW_PC_90"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "TCW_PC_90",
        },
    },
    "range": [-1200.0, 0.0],
    "mpl_ramp": "gist_earth_r",
    "legend": {
        "url": "https://data.dea.ga.gov.au/derivative/ga_ls_tcw_percentiles_2/tcw_percentiles_legend.png",
    },
}


layers = {
    "title": "DEA Wetness Percentiles (Landsat)",
    "abstract": "",
    "layers": [
        {
            "title": "DEA Wetness Percentiles (Landsat)",
            "name": "ga_ls_tcw_percentiles_2",
            "abstract": """Tasseled Cap Wetness Percentiles 25m 2.0.0
The Tasseled Cap Wetness Percentiles provide a multi-decadal summary of landscape wetness that can be used to identify wetlands and groundwater ecosystems.

They provide statistical summaries (10th, 50th and 90th percentiles) of the Tasseled Cap wetness index from 1987 to 2017.

They are intended for use as inputs into classification algorithms to identify potential wetlands and groundwater dependent ecosystems, and characterise salt flats, clay pans, salt lakes and coastal land forms.

Geoscience Australia Landsat Collection 2 Tasseled Cap Wetness Percentiles 1986-2018, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577).
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
The Tasseled Cap wetness transform translates the six spectral bands of Landsat into a single wetness index.  The wetness index can be used to identify areas in the landscape that are potentially wetlands or groundwater dependent ecosystems. The Tasseled Cap Wetness Percentiles capture how the wetness index behaves over time.  The percentiles are well suited to characterising wetlands, salt flats/salt lakes and coastal ecosystems. However, care should be applied when analysing the wetness index, as soil colour and fire scars can cause misleading results. In areas of high relief caused by cliffs or steep terrain, terrain shadows can cause false positives (a falsely high wetness index).
The 10th, 50th and 90th percentiles of the Tasseled Cap wetness index are intended to capture the extreme (10th and 90th percentile) values and long-term average (50th percentile) values of the wetness index.  Percentiles are used in preference to minimum, maximum and mean, as the min/max/mean statistical measures are more sensitive to undetected cloud/cloud shadow, and can be misleading for non-normally distributed data.
The Tasseled Cap Wetness Percentiles are intended to complement the Water Observations from Space (WOfS) algorithm. WOfS is designed to discriminate open water, but the Tasseled Cap wetness index identifies areas of water and areas where water and vegetation are mixed together; i.e. mangroves and palustrine wetlands.
If you are interested in terrestrial vegetation (where water in the pixel is not a factor), use the Fractional Cover product, which provides a better biophysical characterisation of green vegetation fraction, dry vegetation fraction and bare soil vegetation fraction.
In terms of limitations, caution should be used, especially with the Tasseled Cap wetness index results in areas where residual terrain shadow, or dark soils can cause high 'wetness' index values.
One of the limitations of using the Tasseled Cap wetness index is that it will identify all 'wet' things, including potential wetlands, groundwater dependent ecosystems, irrigated crops/pasture, man-made water storages and sewerage treatment, and does not discriminate between these. As such it should be used in conjunction with other contextual data to ensure that features identified using the Tasseled Cap Wetness Percentiles are features of interest rather than false positives.
We used the Tasseled Cap transforms described in Crist et al. (1985).
Crist, E. P. (1985). A TM Tasseled Cap equivalent transformation for reflectance factor data. Remote Sensing of Environment, 17(3), 301–306. https://doi.org/10.1016/0034-4257(85)90102-6
https://cmi.ga.gov.au/data-products/dea/337/dea-wetness-percentiles-landsat
For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "ga_ls_tcw_percentiles_2",
            "bands": bands_tcw_percentile,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": [
                    "TCW_PC_10",
                    "TCW_PC_50",
                    "TCW_PC_90",
                ],
            },
            "styling": {
                "default_style": "tcw_10_percentile",
                "styles": [style_tcw_10, style_tcw_50, style_tcw_90],
            },
        },
    ],
}
