#temporary instructions
#on the command line, go to the location of ogr2ogr
#run the command on the line below
#    py "z:\path-to-python-program\gis_extract_tool_v1.py"
#where z is the disk where the python program is

import os
print ("program start") #for debug purposes

<<<<<<< HEAD
#path_to_ogr2ogr = input("Where is ogr2ogr on your computer?" + '\n' + "On a windows computer this needs to be in an equivalent format to this: C:\path\ogr2ogr" + '\n' + "> ")

#path_to_input_file = input("Where is INPUTFILE.TAB on your computer? ")

# for windows uncomment this, comment the linux line
#os.system('"C:\path\ogr2ogr" -f "KML" "M:\path\KMLextractfile.kml" "S:\path\INPUTFILE.TAB" -sql "select RouteNumber AS name from INPUTFILE where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)' )

#os.system('ogr2ogr --formats')

# for linux uncomment this, comment the windows line 
#os.system('path_to_ogr2ogr -f "KML" "~/Desktop/KMLextractfile.kml" path_to_input_file -sql "select RouteNumber AS name from INPUTFILE where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)')

#os.system('ogr2ogr -f "KML" "~/Desktop/KMLextractfile.kml" "~/Documents/python/GISExtractTool/TrialData/TrialData.tab" -sql "select RouteNumber AS name from INPUTFILE where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)"')

os.system('ogr2ogr -f "KML" "/home/andrew/Desktop/KMLextractfileNov11th.kml" "/home/andrew/Documents/python/GISExtractTool/TrialData/TrialData.tab" -sql "select RouteNumber AS name from TrialData where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)"')


=======
UsrAnsr_InputfileLoc = input("Please provide the location of CycleRoutes.TAB in speech marks starting C: and up to and including .TAB ")
UsrAnsr_ExportfileLoc = input("Please provide the location and name you'd like for the export file, in speech marks starting C: and up to and including .kml ")

# os.system('C:') #this fails
# os.system('cd "C:\Program Files\QGIS Wien\bin\ogr2ogr.exe"') #this fails

cmd="ogr2ogr -f \"KML\" " + UsrAnsr_ExportfileLoc + " " + UsrAnsr_InputfileLoc + " -sql \"select RouteNumber AS name from CycleRoutes where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)\"" #necessary to use a variable for this in order to use variables as part of the input to os.system and notice that the speech marks are escaped with a backslash
>>>>>>> d0acca46396ba62a30eabcea06d527d8b998d1f1

os.system(cmd)# in filepaths backslash characters need to be escaped with a second backslash so that the interpreter (I think) is OK with them, or it works to use a single forward slash

print("program end") #for debug purposes


