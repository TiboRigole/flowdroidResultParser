# haalt alle apks door flowdroid en zet de outputfile in de overeenkomstige outputs map
# terminal commandos uitvoeren
import subprocess
import sys
# alle files in directory kunnen overlopen
import os

# xml files behandelen (deprecated?)
import xml.etree.ElementTree as ET



# commando's opstellen
# locations
jar = "/home/tibo/flowdroid/soot-infoflow-cmd-jar-with-dependencies.jar"
platforms = "/home/tibo/Android/Sdk/platforms"
sourcesandsinks = "/home/tibo/flowdroid/sourcesandsinks.txt"

# dit is de folder die alle apks bevat
# directory = "/home/tibo/Documents/appsFromGetJar"
# directory = "/home/tibo/Documents/appsFromSlideMe"
# directory = "/home/tibo/Documents/appsFromNothing"
directory = "/home/tibo/Documents/appsFromFDroid"

# if you want to keep the console printing
# sys.stdout = open(directory+'/logging','w')


# verhinder dat filenamen spaties bevatten!
# verhinder dat filenamen '(' en ')' bevatten!
for filename in os.listdir(directory):
    if filename.find(" ") != -1:
        new_filename = filename.replace(" ", "_")
        new_filename = filename.replace("(", "_")
        new_filename = filename.replace(")", "_")
        print("renamed "+filename +" to "+new_filename)
        totalOldPath = directory+"/"+filename
        totalNewPath = directory+"/"+new_filename
        os.rename(totalOldPath, totalNewPath)

print(" ")

# map maken die 'outputs' heet, indien nog niet gemaakt
outputsPath = directory+"/outputs"
if( not os.path.exists(outputsPath) ):
    os.mkdir(outputsPath)
# bijhouden hoeveel apps we geanalyseerd hebben
num_analysed_apps = 0

# elke file overlopen, behalve de outputs map natuurlijk
for filename in os.listdir(directory):
    print("")
    print("")
    print("new file started: "+filename)
    # pad naar app, outputfile setten
    app_path = directory + "/" + filename
    outputXml_path = outputsPath + "/" + filename +"_output.xml"


    # commandos opstellen
    cmdmakeOutputFile = "touch "+outputXml_path
    cmdChangePermissionsOutputFile = "chmod a+rw " + outputXml_path
    cmdAnalyseApp = "java -jar "+jar+" -a "+app_path+" -p "+platforms+ " -s "+sourcesandsinks+" -o "+outputXml_path

    commandoList = [cmdmakeOutputFile, cmdChangePermissionsOutputFile, cmdAnalyseApp]


    #outputs map moeten we skippen => alle mappen gewoon skippen
    path = os.path.join(directory, filename)
    if( not os.path.isdir(path) ):
        for commando in commandoList:
            print ("trying to execute " + commando)
            p = subprocess.Popen(commando, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()

            print("executed " + commando)
            print("")

        num_analysed_apps += 1

print("done")
print("analysed", num_analysed_apps , "apps!")

# todo: fix iets dat de logger ook opslaat ,zodat ik kan nagaan wat er gebeurt!