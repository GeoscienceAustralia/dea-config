---
name: OWS layer request
about: Used for requesting ows layers
title: OWS layer request - [product]
labels: ows layer request
assignees: ''

---

## Input for ows ##

|  ows config fieldname |  request                             |
| -------------------------| -----------------------------|
| Title:                |   Fractional Cover Landsat 8 |
| Product name: | ls8_fc_albers  |
| ows layer name:  | ls8_fc_albers  |
| data description: |  Fractional Cover version 2.2.1, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577). Data is only visible at higher resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 25m x 25m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information please see data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena.

This product contains Fractional Cover dervied from the Landsat 8 satellite

For service status information, see https://status.dea.ga.gov.au |

## OWS layer style*s* for the requested layer, duplicate if more than 1 or point a reusable existing style ##

| field | value |
|----- | ----|
| title  | Fractional Cover  |
| abstract | Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red |  

### color ramp - provide values ###
| field | value |
| ----- | ----- |
| required band | band_1, band_2 |

**color ramp**
```
  "color_ramp": [
        {
            "value": 0.0,
            "color": "#8F3F20",
            "alpha": 0.0,
        },
        {"value": 1, "color": "#000000"},
        {"value": 10, "color": "#2d002b"},
        {"value": 25, "color": "#550071"},
        {"value": 60, "color": "#0400ff"},
        {"value": 90, "color": "#0098ff"},
        {"value": 110, "color": "#00ffff"},
        {"value": 130, "color": "#00ff94"},
        {"value": 150, "color": "#00ff2a"},
        {"value": 170, "color": "#3fff00"},
        {"value": 210, "color": "#ffee00"},
        {"value": 230, "color": "#ff8300"},
        {
            "value": 255.0,
            "color": "#ff0000",
        },
    ],
```

**legend**
```
     "legend": {
        "begin": "0.0",
        "end": "255.0",
        # note that legend value does not match the derived band value returned by GetFeatureInfo
        "tick_labels": {
            "0.0": {"label": "0.6"},
            "255.0": {"label": "1.4"},
        },
        "units": "Blue-cyan is magnesite-dolomite, amphibole, \nRed is calcite, epidote, amphibole",
    }, 
```
## Input for terria catalog (this is for release, last step, easy task)## 

| field | value |
|----- | ----|
| Level 1	| Fractional Cover |
| Level 2	| Fractional Cover Daily Observations |
| Level 3	|  |
| Layer name | Fractional Cover Landsat 8 |
