#print ("hello Nicole, Robert and Andrew")
import os

#orgr2ogr = input("where is ogr2ogr on your computer? ")

# works for windows

os.system('"C:\path\ogr2ogr" -f "KML" "M:\path\KMLextractfile.kml" "S:\path\INPUTFILE.TAB" -sql "select RouteNumber AS name from INPUTFILE where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)' )




