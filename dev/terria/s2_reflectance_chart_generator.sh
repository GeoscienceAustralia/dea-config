#!/bin/bash
#
# This script generates a TerriaJS init file when executed.
# It does this so that we can edit the feature info template with newlines,
# and it is then condensed to a single line.
#

tr -d '\n' > s2_reflectance-chart.json <<EOF
"template": "
<table>
  <tr><td><b>Time</b></td><td>{{time}}</td></tr>
  <tr><td><b>Narrow Blue - 440</b></td><td>{{bands.nbart_coastal_aerosol}}</td></tr>
  <tr><td><b>Blue - 490</b></td><td>{{bands.nbart_blue}}</td></tr>
  <tr><td><b>Green - 560</b></td><td>{{bands.nbart_green}}</td></tr>
  <tr><td><b>Red - 670</b></td><td>{{bands.nbart_red}}</td></tr>
  <tr><td><b>Vegetation Red Edge - 710</b></td><td>{{bands.nbart_red_edge_1}}</td></tr>
  <tr><td><b>Vegetation Red Edge - 740</b></td><td>{{bands.nbart_red_edge_2}}</td></tr>
  <tr><td><b>Vegetation Red Edge - 780</b></td><td>{{bands.nbart_red_edge_3}}</td></tr>
  <tr><td><b>Near Infrared (NIR) - 840</b></td><td>{{bands.nbart_nir_1}}</td></tr>
  <tr><td><b>Narrow Near Infrared - 870</b></td><td>{{bands.nbart_nir_2}}</td></tr>
  <tr><td><b>Shortwave Infrared (SWIR) - 1610</b></td><td>{{bands.nbart_swir_2}}</td></tr>
  <tr><td><b>Shortwave Infrared (SWIR) - 2190</b></td><td>{{bands.nbart_swir_3}}</td></tr>
  <tr><td><b>NDVI - Red, NIR</b></td><td>{{band_derived.ndvi}}</td></tr>
  <tr><td><b>NDWI - Green, NIR</b></td><td>{{band_derived.ndwi}}</td></tr>
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
670,{{bands.nbart_red}}\n
710,{{bands.nbart_red_edge_1}}\n
740,{{bands.nbart_red_edge_2}}\n
780,{{bands.nbart_red_edge_3}}\n
840,{{bands.nbart_nir_1}}\n
870,{{bands.nbart_nir_2}}\n
1610,{{bands.nbart_swir_2}}\n
2190,{{bands.nbart_swir_3}}
</chart>
</p>

<p>
<b>Imagery available for dates:</b>
{{#data_available_for_dates}}
<br/>{{.}}
{{/data_available_for_dates}}
</p>"
EOF
