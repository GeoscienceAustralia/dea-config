layers = {
    "title": "DEA Fractional Cover",
    "abstract": """Geoscience Australia Landsat Fractional Cover

Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region.
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 30m x 30m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see https://knowledge.dea.ga.gov.au/data/product/dea-fractional-cover-landsat/

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.

For service status information, see https://status.dea.ga.gov.au""",
    "layers": [
        {
            "include": "ows_refactored.land_and_vegetation.fc.ows_c3_fc_cfg.layer",
            "type": "python",
        },
        {
            "include": "ows_refactored.land_and_vegetation.fc.ows_c3_fcp_cfg.layer",
            "type": "python",
        },
    ]
}
