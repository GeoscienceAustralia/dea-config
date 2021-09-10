category_layers = {
    "title": "Baseline satellite data",
    "abstract": "",
    "layers": [
        {
            "include": "ows_refactored.baseline_satellite_data.surface_reflectance.ows_geomedian_cfg.layers",
            "type": "python",
        },
        {
            "title": "Near Real-Time",
            "abstract": """
This is a 90-day rolling archive of daily Near Real-Time data.
The Near Real-Time capability provides analysis-ready data that is processed on receipt using
the best-available ancillary information at the time to provide atmospheric corrections.
For more information see http://pid.geoscience.gov.au/dataset/ga/122229
""",
            "layers": [
                {
                    "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_cfg.multi_layers",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_cfg.s2b_layer",
                    "type": "python",
                },
                {
                    "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_cfg.s2a_layer",
                    "type": "python",
                },
            ],
        },
        {
            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_ard_cfg.layers",
            "type": "python",
        },
        {
            "include": "ows_refactored.baseline_satellite_data.tmad.ows_tmad_cfg.layers",
            "type": "python",
        },
        {
            "title": "Geoscience Australia Collection 3",
            "abstract": "Geoscience Australia Collection 3 represents the third reprocessing of Landsat and Sentinel-2 baseline and derivative products",
            "layers": [
                {
                    "include": "ows_refactored.baseline_satellite_data.c3.ows_c3_cfg.layers",
                    "type": "python",
                },
                {
                    "title": "Geoscience Australia Sentinel-2 Collection 3",
                    "abstract": """Collection 3 represents a consistent processing and upgrade to the Geoscience Australia's Sentinel-2 Multispectral Imager baseline and derivate product datasets.

For service status information, see https://status.dea.ga.gov.au""",
                    "layers": [
                        {
                            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_provisional_cfg.multi_layers",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_provisional_cfg.s2b_layer",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.baseline_satellite_data.sentinel2.ows_nrt_provisional_cfg.s2a_layer",
                            "type": "python",
                        },
                    ],
                },
            ],
        },
    ]
}