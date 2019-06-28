#!/bin/bash
#
# This script generates a TerriaJS init file when executed.
# It does this so that we can edit the feature info template with newlines,
# and it is then condensed to a single line.
#

tr -d '\n' > reflectance-chart.json <<EOF
{
  "catalog": [
    {
      "name": "Near Real-Time Surface Reflectance (Sentinel 2A)",
      "layers": "s2a_nrt_granule_nbar_t",
      "url": "https://ows.prod.dea.ga.gov.au",
      "type": "wms",
      "ignoreUnknownTileErrors": true,
      "opacity": 1,
      "isEnabled": true,
      "featureInfoTemplate": {
        "formats": {
          "lat": {"maximumFractionDigits": 5},
          "lon": {"maximumFractionDigits": 5}
        },
        "template": "
<table>
  <tr><td><b>Time</b></td><td>{{time}}</td></tr>
  <tr><td><b>nbart_coastal_aerosol</b></td><td>{{bands.nbart_coastal_aerosol}}</td></tr>
  <tr><td><b>nbart_blue</b></td><td>{{bands.nbart_blue}}</td></tr>
  <tr><td><b>nbart_green</b></td><td>{{bands.nbart_green}}</td></tr>
  <tr><td><b>nbart_red</b></td><td>{{bands.nbart_red}}</td></tr>
  <tr><td><b>nbart_red_edge_1</b></td><td>{{bands.nbart_red_edge_1}}</td></tr>
  <tr><td><b>nbart_red_edge_2</b></td><td>{{bands.nbart_red_edge_2}}</td></tr>
  <tr><td><b>nbart_red_edge_3</b></td><td>{{bands.nbart_red_edge_3}}</td></tr>
  <tr><td><b>nbart_nir_1</b></td><td>{{bands.nbart_nir_1}}</td></tr>
  <tr><td><b>nbart_nir_2</b></td><td>{{bands.nbart_nir_2}}</td></tr>
  <tr><td><b>nbart_swir_2</b></td><td>{{bands.nbart_swir_2}}</td></tr>
  <tr><td><b>nbart_swir_3</b></td><td>{{bands.nbart_swir_3}}</td></tr>
  <tr><td><b>NDVI (derived)</b></td><td>{{band_derived.ndvi}}</td></tr>
  <tr><td><b>NDWI (derived)</b></td><td>{{band_derived.ndwi}}</td></tr>
</table>

<p>
<chart id='{{lat}}{{lon}}{{time}}'
 title='NBART at {{lat}},{{lon}}'
 column-units='Wavelength (nm), Reflectance x 10k'
 preview-x-label='NBART Reflectance'
>nm,NBART Reflectance\n
440,{{bands.nbart_coastal_aerosol}}\n
490,{{bands.nbart_blue}}\n
560,{{bands.nbart_green}}\n
665,{{bands.nbart_red}}\n
704,{{bands.nbart_red_edge_1}}\n
740,{{bands.nbart_red_edge_2}}\n
780,{{bands.nbart_red_edge_3}}\n
830,{{bands.nbart_nir_1}}\n
860,{{bands.nbart_nir_2}}\n
1600,{{bands.nbart_swir_2}}\n
2200,{{bands.nbart_swir_3}}
</chart>
</p>

<p>
<b>Imagery available for dates:</b>
{{#data_available_for_dates}}
<br/>{{.}}
{{/data_available_for_dates}}
</p>"
      }
    }
  ]
}
EOF
