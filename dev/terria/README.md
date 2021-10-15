## DEA Maps and Terria Cube configs

TerriaJS config files for DEA Maps and Terria Cube are located here:

* Terria Cube: https://github.com/GeoscienceAustralia/dea-config/blob/master/dev/terria/terria-cube-v8.json
* DEA Maps: https://github.com/GeoscienceAustralia/dea-config/blob/master/dev/terria/dea-maps-v8.json

### Terria config change testing

Please test changes on Terria Cube first before implementing them on DEA Maps.

The Terria Cube catalogue (`terria-cube-v8.json`) contains two sections: "DEA Development" (for dev/non-prod OWS and Geoserver endpoints) and "DEA Production" (for production OWS and Geoserver endpoints). 
Once changes have been tested on Terria Cube, they can be implemented in the DEA Maps catalogue by editing `dea-maps-v8.json`.

When making a change to `terria-cube-v8.json` or `dea-maps-v8.json`, test the changed file using a clean Terria instance:

1. Terria Cube: https://terria-cube.terria.io/#clean
2. DEA Maps: https://maps.dea.ga.gov.au/#clean

#### Procedural Way
2. Click on `Explore map data` button
3. Go to `My Data` tab on the pop up
4. Click on `Add Local Data`
5. On the next page, under `Step 2: Select file` Click on `Browse...` Button
6. Select the file from the new pop up `file explorer window`
7. Click open

#### Quick and easy way
2. Drag the file from folder and drop into the web page

### Catalog Json files standard

Use four spaces for indentation matching conventions used in Python and shell scripts.

#### Apply prettify using Visual Studio Code (VSCODE) IDE
1. Install Prettier - Code formatter extension
2. select the code changes in the file
3. Press `Ctrl + Shift + P` to open up a popup tool
4. Type in `Format Selection`
