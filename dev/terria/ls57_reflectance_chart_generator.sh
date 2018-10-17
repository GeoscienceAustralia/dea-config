#!/bin/bash
#
# This script generates a TerriaJS init file when executed.
# It does this so that we can edit the feature info template with newlines,
# and it is then condensed to a single line.
#

tr -d '\n' > ls57_reflectance-chart.json <<EOF
"template": "
<table>
  <tr><td><b>Time</b></td><td>{{time}}</td></tr>
  <tr><td><b>blue</b></td><td>{{bands.blue}}</td></tr>
  <tr><td><b>green</b></td><td>{{bands.green}}</td></tr>
  <tr><td><b>red</b></td><td>{{bands.red}}</td></tr>
  <tr><td><b>nir</b></td><td>{{bands.nir}}</td></tr>
  <tr><td><b>swir1</b></td><td>{{bands.swir1}}</td></tr>
  <tr><td><b>swir2</b></td><td>{{bands.swir2}}</td></tr>
  <tr><td><b>NDVI (derived)</b></td><td>{{band_derived.ndvi}}</td></tr>
  <tr><td><b>NDWI (derived)</b></td><td>{{band_derived.ndwi}}</td></tr>
</table>

<p>
<chart id='{{lat}}{{lon}}{{time}}'
 title='NBART at {{lat}},{{lon}}'
 column-units='Wavelength (nm), Reflectance x 10k'
 preview-x-label='NBART Reflectance'
>nm,NBART Reflectance\n
478,{{bands.blue}}\n
560,{{bands.green}}\n
662,{{bands.red}}\n
835,{{bands.nir}}\n
1648,{{bands.swir1}}\n
2205,{{bands.swir2}}
</chart>
</p>

<p>
<b>Imagery available for dates:</b>
{{#data_available_for_dates}}
<br/>{{.}}
{{/data_available_for_dates}}
</p>"
EOF
