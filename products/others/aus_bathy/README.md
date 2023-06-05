
# Geoscience Australia Australian Bathymetry and Topography Grid, June 2009



## About the Data

This data product was produced and published by Geoscience Australia in 2009, with complete
information provided via http://dx.doi.org/10.4225/25/53D99B6581B9A 


## Process

1. Download the ESRI Grid zip file.
2. Convert to a Cloud Optimised GeoTIFF

    gdalwarp /vsizip/ESRI_Grid.zip/ESRI_Grid/ausbath_09_v4 ausbath_09_v4.tiff -of COG -co NUM_THREADS=ALL_CPUS -co PREDICTOR=YES

3. Use [rio-stac](https://github.com/developmentseed/rio-stac) to smash out a STAC Item document.

    rio stac ausbath_09_v4.tiff | jq > ga_multi_ausbath_0.stac-item.json

4. Manually add some metadata to the STAC JSON, and manually create an ODC Product Definition YAML.
