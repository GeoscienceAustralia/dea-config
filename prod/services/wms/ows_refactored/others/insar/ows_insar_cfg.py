###############################################################################################
# Styling Summary of InSAR:
# Velocities in mm/yr (for all satellites): -30 (blue) … 0 (white) … + 30 (red)
# Uncertainty (std-dev) of velocities in mm/yr (for Envisat and Radarsat-2): 0 (white) … +6 (red)
# Uncertainty (std-dev) of velocities in mm/yr (for ALOS): 0 (white) … +24 (red)
# Displacements in mm (for all satellites): -100 (blue) … 0 (white) … + 100 (red)
# Uncertainty (std-dev) of displacements in mm (for Envisat and Radarsat-2): 0 (white) … +20 (red)
# Uncertainty (std-dev) of displacements in mm (for ALOS): 0 (white) … +80 (red)
###############################################################################################
import copy

from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

# InSAR Displacements / Velocity
insar_disp_bands = {"ew": [], "ud": [], "ewstd": [], "upstd": []}

insar_vel_bands = {"ew": [], "ud": [], "ewstd": [], "upstd": []}

style_insar_velocity = {
    "name": "insar_velocity",
    "title": "InSAR Velocity",
    "abstract": "Average InSAR Velocity in mm/year",
    "needed_bands": ["velocity"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "velocity",
        },
    },
    # Should the index_function value be shown as a derived band in GetFeatureInfo responses.
    # Defaults to true for style types with an index function.
    "include_in_feature_info": False,
    "range": [-30.0, 30.0],
    "mpl_ramp": "RdBu_r",
    "legend": {
        "begin": -30,
        "end": 30,
        "ticks_every": 30,
        "units": "mm/year",
        "decimal_places": 0,
    },
}

style_insar_velocity_ud = copy.deepcopy(style_insar_velocity)
style_insar_velocity_ud["name"] = "insar_velocity_ud"
style_insar_velocity_ud["title"] = "InSAR Velocity Up-Down "
style_insar_velocity_ud["needed_bands"] = ["ud"]
style_insar_velocity_ud["index_function"]["kwargs"]["band"] = "ud"

style_insar_velocity_ew = copy.deepcopy(style_insar_velocity)
style_insar_velocity_ew["name"] = "insar_velocity_ew"
style_insar_velocity_ew["title"] = "InSAR Velocity East-West "
style_insar_velocity_ew["needed_bands"] = ["ew"]
style_insar_velocity_ew["index_function"]["kwargs"]["band"] = "ew"

style_insar_displacement = {
    "name": "insar_displacement",
    "title": "InSAR Cumulative Displacement",
    "abstract": "Cumulative InSAR Displacment mm",
    "needed_bands": ["displacement"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "displacement",
        },
    },
    # Should the index_function value be shown as a derived band in GetFeatureInfo responses.
    # Defaults to true for style types with an index function.
    "include_in_feature_info": False,
    "range": [-100.0, 100.0],
    "mpl_ramp": "RdBu_r",
    "legend": {
        "begin": -100,
        "end": 100,
        "units": "mm",
        "decimal_places": 0,
        "ticks_every": 100,
    },
}

style_insar_disp_ud = copy.deepcopy(style_insar_displacement)
style_insar_disp_ud["name"] = "insar_disp_ud"
style_insar_disp_ud["title"] = "InSAR Displacement Up-Down "
style_insar_disp_ud["needed_bands"] = ["ud"]
style_insar_disp_ud["index_function"]["kwargs"]["band"] = "ud"

style_insar_disp_ew = copy.deepcopy(style_insar_displacement)
style_insar_disp_ew["name"] = "insar_disp_ew"
style_insar_disp_ew["title"] = "InSAR Displacement East-West "
style_insar_disp_ew["needed_bands"] = ["ew"]
style_insar_disp_ew["index_function"]["kwargs"]["band"] = "ew"

style_insar_stddev_l = {
    "name": "insar_stddev_l",
    "title": "InSAR Cumulative Displacement Uncertainty",
    "abstract": "Uncertainty in mm",
    "needed_bands": ["disp_std"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "disp_std",
        },
    },
    # Should the index_function value be shown as a derived band in GetFeatureInfo responses.
    # Defaults to true for style types with an index function.
    "include_in_feature_info": False,
    "range": [0.0, 80.0],
    "mpl_ramp": "Reds",
    "legend": {
        "begin": 0,
        "end": 80,
        "ticks_every": 40,
        "units": "mm",
        "decimal_places": 0,
    },
}

# Create up-down/east-west varieties using deepcopy
style_insar_stddev_l_ud = copy.deepcopy(style_insar_stddev_l)
style_insar_stddev_l_ud["name"] = "insar_disp_ud_std"
style_insar_stddev_l_ud["title"] = "InSAR Displacement Uncertainty Up-Down "
style_insar_stddev_l_ud["needed_bands"] = ["upstd"]
style_insar_stddev_l_ud["index_function"]["kwargs"]["band"] = "upstd"

style_insar_stddev_l_ew = copy.deepcopy(style_insar_stddev_l)
style_insar_stddev_l_ew["name"] = "insar_disp_ew_std"
style_insar_stddev_l_ew["title"] = "InSAR Displacement Uncertainty East-West "
style_insar_stddev_l_ew["needed_bands"] = ["ewstd"]
style_insar_stddev_l_ew["index_function"]["kwargs"]["band"] = "ewstd"

# Create C-band style using a copy constructor
style_insar_stddev_c_ud = copy.deepcopy(style_insar_stddev_l_ud)
style_insar_stddev_c_ud["range"] = [0.0, 20.0]
style_insar_stddev_c_ud["legend"]["begin"] = 0
style_insar_stddev_c_ud["legend"]["end"] = 20
style_insar_stddev_c_ud["legend"]["ticks_every"] = 10

style_insar_stddev_c_ew = copy.deepcopy(style_insar_stddev_l_ew)
style_insar_stddev_c_ew["range"] = [0.0, 20.0]
style_insar_stddev_c_ew["legend"]["begin"] = 0
style_insar_stddev_c_ew["legend"]["end"] = 20
style_insar_stddev_c_ew["legend"]["ticks_every"] = 10

style_insar_stddev_lv = {
    "name": "insar_stddev_lv",
    "title": "InSAR Velocity Uncertainty",
    "abstract": "Uncertainty in mm",
    "needed_bands": ["vel_std"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "vel_std",
        },
    },
    # Should the index_function value be shown as a derived band in GetFeatureInfo responses.
    # Defaults to true for style types with an index function.
    "include_in_feature_info": False,
    "range": [0.0, 24.0],
    "mpl_ramp": "Reds",
    "legend": {
        "begin": 0,
        "end": 24,
        "ticks_every": 12,
        "units": "mm/year",
        "decimal_places": 0,
    },
}

# Create up-down/east-west varieties using deepcopy
style_insar_stddev_lv_ud = copy.deepcopy(style_insar_stddev_lv)
style_insar_stddev_lv_ud["name"] = "insar_vel_ud_std"
style_insar_stddev_lv_ud["title"] = "InSAR Velocity Uncertainty Up-Down "
style_insar_stddev_lv_ud["needed_bands"] = ["upstd"]
style_insar_stddev_lv_ud["index_function"]["kwargs"]["band"] = "upstd"

style_insar_stddev_lv_ew = copy.deepcopy(style_insar_stddev_lv)
style_insar_stddev_lv_ew["name"] = "insar_vel_ew_std"
style_insar_stddev_lv_ew["title"] = "InSAR Velocity Uncertainty East-West "
style_insar_stddev_lv_ew["needed_bands"] = ["ewstd"]
style_insar_stddev_lv_ew["index_function"]["kwargs"]["band"] = "ewstd"

# Create C-band style using a copy constructor
style_insar_stddev_cv_ud = copy.deepcopy(style_insar_stddev_lv_ud)
style_insar_stddev_cv_ud["range"] = [0.0, 6.0]
style_insar_stddev_cv_ud["legend"]["begin"] = 0
style_insar_stddev_cv_ud["legend"]["end"] = 6
style_insar_stddev_cv_ud["legend"]["ticks_every"] = 3

style_insar_stddev_cv_ew = copy.deepcopy(style_insar_stddev_lv_ew)
style_insar_stddev_cv_ew["range"] = [0.0, 6.0]
style_insar_stddev_cv_ew["legend"]["begin"] = 0
style_insar_stddev_cv_ew["legend"]["end"] = 6
style_insar_stddev_cv_ew["legend"]["ticks_every"] = 3

# Layer segments for various INSAR Datasets
alos_layers = [
    {
        "title": "ALOS Displacement",
        "abstract": """
            Cumulative displacement time series derived from combination of
             ascending and descending line-of-sight InSAR data from six ALOS data stacks in
             the Sydney Basin area. Original data points were interpolated to 50 m pixel spacing.
             The time series spans the period 2008-02-11 to 2010-10-22, interpolated to 12-day sampling.
             The reference (i.e. zero displacement) for the time series is 2008-04-23.
            """,
        "name": "alos_displacement",
        # The ODC product name for the associated data product
        "product_name": "cemp_insar_alos_displacement",
        "bands": insar_disp_bands,
        "resource_limits": reslim_wms_min_zoom_15_cache_rules,
        "native_crs": "EPSG:32756",
        "native_resolution": [50, -50],
        "image_processing": {
            "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        },
        "styling": {
            "default_style": "insar_disp_ud",
            "styles": [
                style_insar_disp_ud,
                style_insar_disp_ew,
                style_insar_stddev_l_ud,
                style_insar_stddev_l_ew,
            ],
        },
    },
    {
        "title": "ALOS Velocity",
        "abstract": """
            Velocity (linear displacement rate) of ground movement derived from combination
             of ascending and descending line-of-sight InSAR data from six ALOS data
             stacks in the Sydney Basin area. Original data points were interpolated to 50 m
             pixel spacing. The velocity is calculated for the period 2006-05-16 to 2011-01-07.
            """,
        "name": "alos_velocity",
        # The ODC product name for the associated data product
        "product_name": "cemp_insar_alos_velocity",
        "bands": insar_vel_bands,
        "resource_limits": reslim_wms_min_zoom_15_cache_rules,
        "native_crs": "EPSG:32756",
        "native_resolution": [50, -50],
        "image_processing": {
            "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        },
        "styling": {
            "default_style": "insar_velocity_ud",
            "styles": [
                style_insar_velocity_ud,
                style_insar_velocity_ew,
                style_insar_stddev_lv_ud,
                style_insar_stddev_lv_ew,
            ],
        },
    },
]

envisat_layers = [
    {
        "title": "ENVISAT Displacement",
        "abstract": """
            Cumulative displacement time series derived from combination of ascending and descending
            line-of-sight InSAR data from seven Envisat data stacks in the Sydney Basin area. Original
            data points were interpolated to 50 m pixel spacing. The time series spans the period 2006-06-26
            to 2010-08-28, interpolated to 12-day sampling. The reference (i.e. zero displacement) for
            the time series is 2007-04-10.
            """,
        "name": "envisat_displacement",
        # The ODC product name for the associated data product
        "product_name": "cemp_insar_envisat_displacement",
        "bands": insar_disp_bands,
        "resource_limits": reslim_wms_min_zoom_15_cache_rules,
        "native_crs": "EPSG:32756",
        "native_resolution": [50, -50],
        "image_processing": {
            "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        },
        "styling": {
            "default_style": "insar_disp_ud",
            "styles": [
                style_insar_disp_ud,
                style_insar_disp_ew,
                style_insar_stddev_c_ud,
                style_insar_stddev_c_ew,
            ],
        },
    },
    {
        "title": "ENVISAT Velocity",
        "abstract": """
            Velocity (linear displacement rate) of ground movement derived from combination of ascending
            and descending line-of-sight InSAR data from seven Envisat data stacks in the Sydney Basin area.
            Original data points were interpolated to 50 m pixel spacing. The velocity is calculated for the
            period 2006-06-02 to 2010-09-25.
            """,
        "name": "envisat_velocity",
        # The ODC product name for the associated data product
        "product_name": "cemp_insar_envisat_velocity",
        "bands": insar_vel_bands,
        "resource_limits": reslim_wms_min_zoom_15_cache_rules,
        "native_crs": "EPSG:32756",
        "native_resolution": [50, -50],
        "image_processing": {
            "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        },
        "styling": {
            "default_style": "insar_velocity_ud",
            "styles": [
                style_insar_velocity_ud,
                style_insar_velocity_ew,
                style_insar_stddev_cv_ud,
                style_insar_stddev_cv_ew,
            ],
        },
    },
]

rs2_layers = [
    {
        "title": "RADARSAT2 Displacement",
        "abstract": """
            Cumulative displacement time series derived from combination of ascending
             and descending line-of-sight InSAR data from two Radarsat-2 data stacks
             in the Sydney Basin area. Original data points were interpolated to 50
             m pixel spacing. The time series spans the period 2015-07-15 to 2019-05-31,
             interpolated to 12-day sampling. The reference (i.e. zero displacement) for
             the time series is 2015-07-15.
            """,
        "name": "radarsat2_displacement",
        # The ODC product name for the associated data product
        "product_name": "cemp_insar_radarsat2_displacement",
        "bands": insar_disp_bands,
        "resource_limits": reslim_wms_min_zoom_15_cache_rules,
        "native_crs": "EPSG:32756",
        "native_resolution": [50, -50],
        "image_processing": {
            "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        },
        "styling": {
            "default_style": "insar_disp_ud",
            "styles": [
                style_insar_disp_ud,
                style_insar_disp_ew,
                style_insar_stddev_c_ud,
                style_insar_stddev_c_ew,
            ],
        },
    },
    {
        "title": "RADARSAT2 Velocity",
        "abstract": """
        Velocity (linear displacement rate) of ground movement derived from combination
         of ascending and descending line-of-sight InSAR data from two Radarsat-2 data
         stacks in the Sydney Basin area. Original data points were interpolated to 50
         m pixel spacing. The velocity is calculated for the period 2015-07-15 to
         2019-05-31.
        """,
        "name": "radarsat2_velocity",
        # The ODC product name for the associated data product
        "product_name": "cemp_insar_radarsat2_velocity",
        "bands": insar_vel_bands,
        "resource_limits": reslim_wms_min_zoom_15_cache_rules,
        "native_crs": "EPSG:32756",
        "native_resolution": [50, -50],
        "image_processing": {
            "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        },
        "styling": {
            "default_style": "insar_velocity_ud",
            "styles": [
                style_insar_velocity_ud,
                style_insar_velocity_ew,
                style_insar_stddev_cv_ud,
                style_insar_stddev_cv_ew,
            ],
        },
    },
]

insar_layers = []
insar_layers.extend(alos_layers)
insar_layers.extend(envisat_layers)
insar_layers.extend(rs2_layers)

layers = {
    # NOTE: This layer is a folder - it is NOT "named layer" that can be selected in GetMap requests
    # Every layer must have a human-readable title
    "title": "Camden Environmental Monitoring Project InSAR",
    # Top level layers must have a human-readable abstract. The abstract is optional for child-layers - defaulting
    # to that of the parent layer.
    "abstract": """
            These InSAR-derived datasets were produced by Geoscience Australia under the Camden Environmental Monitoring Project.
            Products are given for three separately processed satellite radar datasets: ALOS, Envisat and Radarsat-2.
            Products are derived in up-down and east-west direction from combination of different viewing geometries of the same satellite sensor. The slanted InSAR line-of-sight viewing geometry is insensitive to the north-south direction.
            Negative signals indicate either downward (in up-down products) or westward (in east-west products) surface movements.
            Uncertainties of each product result from error propagation of initial line-of-sight data uncertainties during the data combination step.
            The InSAR processing method used to create these products only uses high-quality pixels with very little signal noise. The resulting products are sparse in some areas (particularly highly vegetated areas) but have a high accuracy as demonstrated by validation with GPS data described in the GA Record. Different InSAR processing methods could be used to retrieve a denser coverage of displacement and velocity observations, but with reduced accuracy.
            ALOS products generally have denser spatial coverage than Envisat and Radarsat-2 products. This is because ALOS uses a longer radar wavelength (~24 cm) than Envisat and Radarsat-2 (~6 cm) which enables the radar to better penetrate vegetation.
            A full description of the project and methods used to derive these InSAR products is given in the associated GA Record.
            """,
    # NOTE: Folder-layers do not have a layer "name".
    # Keywords are optional, but can be added at any folder level and are cumulative.
    # A layer combines its own keywords, the keywords of it's parent (and grandparent, etc) layers,
    # and any keywords defined in the global section above.
    #
    "keywords": [
        "alos-palsar",
        "radarsat-2",
        "sentinel-1",
        "envisat",
        "insar",
    ],
    # Attribution.  This entire section is optional.  If provided, it overrides any
    #               attribution defined in the wms section above or any higher layers, and
    #               applies to this layer and all child layers under this layer unless itself
    #               overridden.
    "attribution": {
        # Attribution must contain at least one of ("title", "url" and "logo")
        # A human readable title for the attribution - e.g. the name of the attributed organisation
        "title": "Digital Earth Australia",
        # The associated - e.g. URL for the attributed organisation
        "url": "http://www.ga.gov.au/dea",
        # Logo image - e.g. for the attributed organisation
        "logo": {
            # Image width in pixels (optional)
            "width": 370,
            # Image height in pixels (optional)
            "height": 73,
            # URL for the logo image. (required if logo specified)
            "url": "https://www.ga.gov.au/__data/assets/image/0011/61589/GA-DEA-Logo-Inline-370x73.png",
            # Image MIME type for the logo - should match type referenced in the logo url (required if logo specified.)
            "format": "image/png",
        },
    },
    # Folder-type layers include a list of sub-layers
    "layers": insar_layers,
}
