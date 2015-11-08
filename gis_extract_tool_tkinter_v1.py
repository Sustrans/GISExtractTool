#print ("hello Nicole, Robert and Andrew")
import os
from Tkinter import *

master = Tk()

#whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
#msg = Message(master, text = whatever_you_do)

#ogr2ogr_results = os.system('ogr2ogr --version')
ogr2ogr_results = os.uname()

#whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = ogr2ogr_results)

msg.config(bg='lightgreen', font=('times', 24, 'italic')) # , borderwidth=30
msg.pack( )
mainloop( )

#path_to_ogr2ogr = input("Where is ogr2ogr on your computer?" + '\n' + "On a windows computer this needs to be in an equivalent format to this: C:\path\ogr2ogr" + '\n' + "> ")

#path_to_input_file = input("Where is INPUTFILE.TAB on your computer? ")

# for windows uncomment this, comment the linux line
#os.system('"C:\path\ogr2ogr" -f "KML" "M:\path\KMLextractfile.kml" "S:\path\INPUTFILE.TAB" -sql "select RouteNumber AS name from INPUTFILE where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)' )



# for linux uncomment this, comment the windows line 
#os.system('path_to_ogr2ogr -f "KML" "~/Desktop/KMLextractfile.kml" path_to_input_file -sql "select RouteNumber AS name from INPUTFILE where ((RouteType = 1 or RouteType = 2) and OpenStatus >= 3)')





