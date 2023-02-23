## DEA Maps TerriaJS config

This directory contains the `dea-maps-v8.json` TerriaJS config file for the production DEA Maps map (maps.dea.ga.gov.au).

> **Note:** Please test changes in Terria Cube first before implementing them on DEA Maps [by editing the config here](https://github.com/GeoscienceAustralia/dea-config/blob/master/dev/terria/terria-cube-v8.json).

### Testing Terria config changes using the Terria preview bot

1. Make edits to the `dea-maps-v8.json`
2. Create a draft pull request
3. Once the pull request has been created, the Terria preview bot will post a comment containing links to a preview the draft config on DEA Maps:

![](../../_static/terria_preview.jpg)

4. Test the layer on the preview on DEA Maps, and update the pull request to fix any issues.
5. When ready, mark the pull request as "Ready for review".

### Testing Terria config changes manually

1. Download the `dea-maps-v8.json` file to your PC
2. Launch a clean instance of DEA Maps by appending `#clean` to the URL: https://maps.dea.ga.gov.au/#clean
2. Drag the `dea-maps-v8.json` file from your PC into DEA Maps

### Catalog Json files standard

Use four spaces for indentation matching conventions used in Python and shell scripts.

#### Apply prettify using Visual Studio Code (VSCODE) IDE
1. Install Prettier - Code formatter extension
2. select the code changes in the file
3. Press `Ctrl + Shift + P` to open up a popup tool
4. Type in `Format Selection`
