#temporary instructions
#on the command line, go to the location of ogr2ogr
#run the command on the line below
#    py "z:\path-to-python-program\gis_extract_tool_v1.py"
#where z is the disk where the python program is

import os
print ("program start") #for debug purposes

UsrAnsr_InputfileLoc = input("Please provide the location of CycleRoutes.TAB in speech marks starting C: and up to and including .TAB ")
UsrAnsr_ExportfileLoc = input("Please provide the location and name you'd like for the export file, in speech marks starting C: and up to and including .kml ")

# os.system('C:') #this fails
# os.system('cd "C:\Program Files\QGIS Wien\bin\ogr2ogr.exe"') #this fails

<<<<<<< HEAD
cmd="ogr2ogr -f \"KML\" " + UsrAnsr_ExportfileLoc + " " + UsrAnsr_InputfileLoc + " -sql \"select RouteNumber AS name from CycleRoutes where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)\"" #necessary to use a variable for this in order to use variables as part of the input to os.system and notice that the speech marks are escaped with a backslash

os.system(cmd)# in filepaths backslash characters need to be escaped with a second backslash so that the interpreter (I think) is OK with them, or it works to use a single forward slash
=======
os.system('ogr2ogr -f "KML" "C:/Users/path-to-file/KMLextractfile.kml" "C:/Users/path-to-file/CycleRoutes.TAB" -sql "select RouteNumber AS name from CycleRoutes where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)' )# in filepaths backslash characters need to be escaped with a second backslash so that the interpreter (I think) is OK with them, or it works to use a single forward slash
>>>>>>> andrew_dev

print("program end") #for debug purposes


