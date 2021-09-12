from ows_refactored.others.aster.abstract_aster_cfg import (
    abstract_aster_aloh_group_composition, abstract_aster_aloh_group_content,
    abstract_aster_false_colour, abstract_aster_feoh_group_content,
    abstract_aster_ferric_oxide_composition,
    abstract_aster_ferric_oxide_content,
    abstract_aster_ferrous_iron_content_in_mgoh,
    abstract_aster_ferrous_iron_index, abstract_aster_green_vegetation,
    abstract_aster_gypsum_index, abstract_aster_kaolin_group_index,
    abstract_aster_mgoh_group_composition, abstract_aster_mgoh_group_content,
    abstract_aster_opaque_index, abstract_aster_quartz_index,
    abstract_aster_regolith_ratios, abstract_aster_silica_index)
from ows_refactored.others.aster.band_aster_cfg import (
    bands_aster, bands_aster_single_band)
from ows_refactored.others.aster.style_aster_cfg import (
    style_aster_aloh_comp_ramp, style_aster_aloh_cont_ramp,
    style_aster_b2_gray, style_aster_false_colour, style_aster_feoh_cont_ramp,
    style_aster_ferrous_idx_ramp, style_aster_ferrous_mgoh_ramp,
    style_aster_ferrox_comp_ramp, style_aster_ferrox_cont_ramp,
    style_aster_green_veg_ramp, style_aster_gypsum_idx_ramp,
    style_aster_kaolin_idx_ramp, style_aster_mgoh_comp_ramp,
    style_aster_mgoh_cont_ramp, style_aster_opaque_idx_ramp,
    style_aster_quartz_idx_ramp, style_aster_silica_idx_ramp,
    style_aster_simple_rgb)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_10

layers = {
    "title": "ASTER Geoscience Map of Australia",
    "abstract": """
The National ASTER Map of Australia is the parent datafile of a dataset that comprises a set of 14+ geoscience products made up of mosaiced ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) scenes across Australia.

The individual geoscience products are a combination of bands and band ratios to highlight different mineral groups and parameters including:
- False Colour Mosaic
- CSIRO Landsat TM
- Regolith Ratios
- AlOH Group Composition
- AlOH Group Content
- FeOH Group Content
- Ferric Oxide Composition
- Ferric Oxide Content
- Ferrous Iron Content in MgOH/Carbonate
- Ferrous Iron Index
- Green Vegetation Content
- Gypsum Index
- Kaolin Group Index
- MgOH Group Composition
- MgOH Group Content
- Opaque Index
- TIR Silica index
- TIR Quartz Index
- Surface mineral group distribution (relative abundance and composition)

For parent datafile information, see the dataset record: http://pid.geoscience.gov.au/dataset/ga/74347
""",
    "layers": [
        {
            "title": "ASTER Geoscience Map of Australia (False Colour Mosaic)",
            "name": "aster_false_colour",
            "abstract": abstract_aster_false_colour,
            "product_name": "aster_false_colour",
            "bands": bands_aster,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1", "Band_2", "Band_3"],
            },
            "styling": {
                "default_style": "false_colour",
                "styles": [
                    style_aster_false_colour,
                    style_aster_b2_gray,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Regolith Ratios)",
            "name": "aster_regolith_ratios",
            "abstract": abstract_aster_regolith_ratios,
            "product_name": "aster_regolith_ratios",
            "bands": bands_aster,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1", "Band_2", "Band_3"],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": [
                    style_aster_simple_rgb,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (AlOH Group Composition)",
            "name": "aster_aloh_group_composition",
            "abstract": abstract_aster_aloh_group_composition,
            "product_name": "aster_aloh_group_composition",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_aloh_comp_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (AlOH Group Content)",
            "name": "aster_aloh_group_content",
            "abstract": abstract_aster_aloh_group_content,
            "product_name": "aster_aloh_group_content",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_aloh_cont_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (FeOH Group Content)",
            "name": "aster_feoh_group_content",
            "abstract": abstract_aster_feoh_group_content,
            "product_name": "aster_feoh_group_content",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_feoh_cont_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Ferric Oxide Composition)",
            "name": "aster_ferric_oxide_composition",
            "abstract": abstract_aster_ferric_oxide_composition,
            "product_name": "aster_ferric_oxide_composition",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_ferrox_comp_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Ferric Oxide Content)",
            "name": "aster_ferric_oxide_content",
            "abstract": abstract_aster_ferric_oxide_content,
            "product_name": "aster_ferric_oxide_content",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_ferrox_cont_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Ferrous Iron Content in MgOH/Carbonate)",
            "name": "aster_ferrous_iron_content_in_mgoh",
            "abstract": abstract_aster_ferrous_iron_content_in_mgoh,
            "product_name": "aster_ferrous_iron_content_in_mgoh",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_ferrous_mgoh_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Ferrous Iron Index)",
            "name": "aster_ferrous_iron_index",
            "abstract": abstract_aster_ferrous_iron_index,
            "product_name": "aster_ferrous_iron_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_ferrous_idx_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Green Vegetation Content)",
            "name": "aster_green_vegetation",
            "abstract": abstract_aster_green_vegetation,
            "product_name": "aster_green_vegetation",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_green_veg_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Gypsum Index)",
            "name": "aster_gypsum_index",
            "abstract": abstract_aster_gypsum_index,
            "product_name": "aster_gypsum_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_gypsum_idx_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Kaolin Group Index)",
            "name": "aster_kaolin_group_index",
            "abstract": abstract_aster_kaolin_group_index,
            "product_name": "aster_kaolin_group_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_kaolin_idx_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (MgOH Group Composition)",
            "name": "aster_mgoh_group_composition",
            "abstract": abstract_aster_mgoh_group_composition,
            "product_name": "aster_mgoh_group_composition",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_mgoh_comp_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (MgOH Group Content)",
            "name": "aster_mgoh_group_content",
            "abstract": abstract_aster_mgoh_group_content,
            "product_name": "aster_mgoh_group_content",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_mgoh_cont_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (Opaque Index)",
            "name": "aster_opaque_index",
            "abstract": abstract_aster_opaque_index,
            "product_name": "aster_opaque_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_opaque_idx_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (TIR Silica index)",
            "name": "aster_silica_index",
            "abstract": abstract_aster_silica_index,
            "product_name": "aster_silica_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_silica_idx_ramp,
                ],
            },
        },
        {
            "title": "ASTER Geoscience Map of Australia (TIR Quartz Index)",
            "name": "aster_quartz_index",
            "abstract": abstract_aster_quartz_index,
            "product_name": "aster_quartz_index",
            "bands": bands_aster_single_band,
            "resource_limits": reslim_wms_min_zoom_10,
            "native_crs": "EPSG:3577",
            "native_resolution": [15.0, 15.0],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "default_bands": ["Band_1"],
            },
            "styling": {
                "default_style": "ramp",
                "styles": [
                    style_aster_quartz_idx_ramp,
                ],
            },
        },
    ],
}
