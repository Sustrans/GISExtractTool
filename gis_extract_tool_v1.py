#temporary instructions
#on the command line, go to the location of ogr2ogr
#run the command on the line below
#    py "z:\path-to-python-program\gis_extract_tool_v1.py"
#where z is the disk where the python program is
#This means that ogr2ogr will be available whereas if the current
#directory is on the z drive I can't access it. 

import os
print ("program start") #for debug purposes
#orgr2ogr = input("where is ogr2ogr on your computer? ")

# works for windows

# os.system('C:') this fails

os.system('ogr2ogr -f "KML" "C:/Users/Robert Limited/Documents/Temporary Items/KMLextractfile.kml" "C:/Users/Robert Limited/Documents/Temporary Items/TempCycleroutes/CycleRoutes.TAB" -sql "select RouteNumber AS name from CycleRoutes where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)' )# in file paths backslash characters need to be escaped with a second backslash so that the interpreter (I think) is OK with them, or it works to use a single forward slash

print("program end") #for debug purposes


