# GISExtractTool
Tool to extract GIS stuff

Working with the command 

 "C:\path\ogr2ogr" -f "KML" "M:\path\KMLextractfile.kml" "S:\path\INPUTFILE.TAB" -sql "select RouteNumber AS name from INPUTFILE where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)" 

Branch Andrew_dev now has the ability to input the input/export file locatoins and names
