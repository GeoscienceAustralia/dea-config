from ows_refactored.baseline_satellite_data.landsat_annual.band_ls_cfg import \
    bands_ls
from ows_refactored.baseline_satellite_data.landsat_annual.style_ls_cfg import \
    styles_tide_list
from ows_refactored.ows_reslim_cfg import reslim_standard

layers = {
    "title": "High and Low Tide Composites (HLTC)",
    "abstract": """High and Low Tide Composites (HLTC)

The High and Low Tide Composites product is composed of two surface reflectance composite mosaics
of Landsat TM and ETM+ (Landsat 5 and Landsat 7 respectively) and OLI (Landsat 8)
surface reflectance data (Li et al., 2012). These products have been produced using
Digital Earth Australia (DEA). The two mosaics allow cloud free and noise reduced visualisation
of the shallow water and inter-tidal coastal regions of Australia, as observed at
high and low tide respectively.The composites are generated utilising the geomedian approach of
Roberts et al (2017) to ensure a valid surface reflectance spectra suitable for uses such as
habitat mapping. The time range used for composite generation in each polygon of the mosaic is
tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud
free composite to be generated. The concepts of the Observed Tidal Range (OTR),
and Highest and Lowest Observed Tide (HOT, LOT) are discussed and described fully in Sagar et al.
(2017) and the product description for the ITEM v 1.0 product (Geoscience Australia, 2016).

https://knowledge.dea.ga.gov.au/data/product/dea-high-and-low-tide-imagery-landsat/

For service status information, see https://status.dea.ga.gov.au
    """,
    "layers": [
        {
            "title": "High Tide Composite (HLTC)",
            "name": "high_tide_composite",
            "abstract": """High Tide and Low Tide Composites 2.0.0 (Landsat, High Tide)

The High and Low Tide Composites product is composed of two surface reflectance composite mosaics of Landsat TM and ETM+ (Landsat 5 and Landsat 7 respectively) and OLI (Landsat 8) surface reflectance data (Li et al., 2012). These products have been produced using Digital Earth Australia (DEA).
The two mosaics allow cloud free and noise reduced visualisation of the shallow water and inter-tidal coastal regions of Australia, as observed at high and low tide respectively (Sagar et al. 2018).

The composites are generated utilising the geomedian approach of Roberts et al (2017) to ensure a valid surface reflectance spectra suitable for uses such as habitat mapping.
The time range used for composite generation in each polygon of the mosaic is tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud free composite to be generated. The concepts of the Observed Tidal Range (OTR), and Highest and Lowest Observed Tide (HOT, LOT) are discussed and described fully in Sagar et al. (2017) and the product description for the ITEM v 1.0 product (Geoscience Australia, 2016).

*Overview*

Inter-tidal zones are difficult regions to characterise due to the dynamic nature of the tide. They are highly changeable environments, subject to forcings from the land, sea and atmosphere and yet they form critical habitats for a wide range of organisms from birds to fish and sea grass.
By harnessing the long archive of satellite imagery over Australia's coastal zones in the DEA and pairing the images with regional tidal modelling, the archive can be sorted by tide height rather than date, enabling the inter-tidal zone to be viewed at any stage of the tide regime.

The High Low Tide Composites (HLTC_25) product is composed of two mosaics, distinguished by tide height, representing a composite image of the synthetic geomedian surface reflectance from Landsats 5 TM, Landsat 7 ETM+ and Landsat 8 OLI NBAR data (Li et al., 2012; Roberts et al., 2017). Oregon State Tidal Prediction (OTPS) software (Egbert and Erofeeva, 2002, 2010) was used to generate tide heights, relative to mean sea level, for the Australian continental coastline, split into 306 distinct tidal regions.
These time and date stamped tidal values were then attributed to all coastal tile observations for their time of acquisition, creating a range of observed tide heights for the Australian coastline. The two mosaics in HLTC_25 are composited from the highest and lowest 20 % of observed tide in the ensemble and are termed HOT and LOT respectively.
A geomedian composite for each Landsat band is calculated from the tiles in each ensemble subset to produce the respective HOT and LOT composites. Note that Landsat 7 ETM+ observations are excluded after May 2003 due to a large number of data artifacts.

The time range used for composite generation in each of the 306 polygons of the mosaics are tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud free composite to be generated.
The maximum epoch for which the products are calculated is between 1995-2017, although this varies due to data resolution and observation quality. The product also includes a count of clear observations per pixel for both mosaics and attribute summaries per polygon that include the date range, the highest and lowest modeled astronomical tide as well as the highest and lowest observed tide for that time range, the total observation count and the maximum count of observations for any one pixel in the polygon, the polygon ID number (from 1 to 306), the polygon centroid in longitude and latitude and the count of tide stages attributed to every observation used in that polygon of the mosaic. For the count of tidal stage observations, e = ebbing tide, f = flowing tide, ph = peak high tide and pl = peak low tide.
The tide stages were calculated bycomparison to the modeled tide data for 15 minutes either side of the observation to determine the ebb, flow or peak movement of the tide.

Observations are filtered to remove poor quality observations including cloud, cloud shadow and band saturation (of any band).

https://knowledge.dea.ga.gov.au/data/product/dea-high-and-low-tide-imagery-landsat/

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "high_tide_comp_20p",
            "bands": bands_ls,
            "time_resolution": "summary",
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
                "styles": styles_tide_list,
            },
        },
        {
            "title": "Low Tide Composite (HLTC)",
            "name": "low_tide_composite",
            "abstract": """High Tide and Low Tide Composites 2.0.0 (Landsat, Low Tide)

The High and Low Tide Composites product is composed of two surface reflectance composite mosaics of Landsat TM and ETM+ (Landsat 5 and Landsat 7 respectively) and OLI (Landsat 8) surface reflectance data (Li et al., 2012). These products have been produced using Digital Earth Australia (DEA).
The two mosaics allow cloud free and noise reduced visualisation of the shallow water and inter-tidal coastal regions of Australia, as observed at high and low tide respectively (Sagar et al. 2018).

The composites are generated utilising the geomedian approach of Roberts et al (2017) to ensure a valid surface reflectance spectra suitable for uses such as habitat mapping.
The time range used for composite generation in each polygon of the mosaic is tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud free composite to be generated. The concepts of the Observed Tidal Range (OTR), and Highest and Lowest Observed Tide (HOT, LOT) are discussed and described fully in Sagar et al. (2017) and the product description for the ITEM v 1.0 product (Geoscience Australia, 2016).

*Overview*

Inter-tidal zones are difficult regions to characterise due to the dynamic nature of the tide. They are highly changeable environments, subject to forcings from the land, sea and atmosphere and yet they form critical habitats for a wide range of organisms from birds to fish and sea grass.
By harnessing the long archive of satellite imagery over Australia's coastal zones in the DEA and pairing the images with regional tidal modelling, the archive can be sorted by tide height rather than date, enabling the inter-tidal zone to be viewed at any stage of the tide regime.

The High Low Tide Composites (HLTC_25) product is composed of two mosaics, distinguished by tide height, representing a composite image of the synthetic geomedian surface reflectance from Landsats 5 TM, Landsat 7 ETM+ and Landsat 8 OLI NBAR data (Li et al., 2012; Roberts et al., 2017). Oregon State Tidal Prediction (OTPS) software (Egbert and Erofeeva, 2002, 2010) was used to generate tide heights, relative to mean sea level, for the Australian continental coastline, split into 306 distinct tidal regions.
These time and date stamped tidal values were then attributed to all coastal tile observations for their time of acquisition, creating a range of observed tide heights for the Australian coastline. The two mosaics in HLTC_25 are composited from the highest and lowest 20 % of observed tide in the ensemble and are termed HOT and LOT respectively.
A geomedian composite for each Landsat band is calculated from the tiles in each ensemble subset to produce the respective HOT and LOT composites. Note that Landsat 7 ETM+ observations are excluded after May 2003 due to a large number of data artifacts.

The time range used for composite generation in each of the 306 polygons of the mosaics are tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud free composite to be generated.
The maximum epoch for which the products are calculated is between 1995-2017, although this varies due to data resolution and observation quality. The product also includes a count of clear observations per pixel for both mosaics and attribute summaries per polygon that include the date range, the highest and lowest modeled astronomical tide as well as the highest and lowest observed tide for that time range, the total observation count and the maximum count of observations for any one pixel in the polygon, the polygon ID number (from 1 to 306), the polygon centroid in longitude and latitude and the count of tide stages attributed to every observation used in that polygon of the mosaic. For the count of tidal stage observations, e = ebbing tide, f = flowing tide, ph = peak high tide and pl = peak low tide.
The tide stages were calculated bycomparison to the modeled tide data for 15 minutes either side of the observation to determine the ebb, flow or peak movement of the tide.

Observations are filtered to remove poor quality observations including cloud, cloud shadow and band saturation (of any band).

https://knowledge.dea.ga.gov.au/data/product/dea-high-and-low-tide-imagery-landsat/

For service status information, see https://status.dea.ga.gov.au""",
            "product_name": "low_tide_comp_20p",
            "time_resolution": "summary",
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
                "styles": styles_tide_list,
            },
        },
    ],
}
