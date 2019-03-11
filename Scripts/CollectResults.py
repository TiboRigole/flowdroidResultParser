
# alle files in directory kunnen overlopen
import os

# categorisation setup
from Objects.App import App
from Util.ReadClassificationFiles import setupFromTxt
from Graphs.NumOfLeaks import pieNumOfLeaks, histogramNumOfLeaks
from Graphs.NumAccToCategory import pieCategoriesSinks, pieCategoriesSources

# paths to categorisation of sources and sinks files
sinksCatFile   = "/home/tibo/PycharmProjects/FlowDroidVerwerking/ClassificationFiles/sinksCategorized.txt"
sourcesCatFile = "/home/tibo/PycharmProjects/FlowDroidVerwerking/ClassificationFiles/sourcesCategorized.txt"

# path to directory where the analysed xml's are located
# xmlDirectory = directory = "/home/tibo/Documents/appsFromNothing/outputs/"
xmlDirectory = directory = "/home/tibo/Documents/appsFromGetJar/outputs/"
# xmlDirectory = directory = "/home/tibo/Documents/appsFromFDroid/outputs/"


# read the files and put them in dictonary : sink -> category and source -> category
sinks_Cat_Dict = setupFromTxt(sinksCatFile, "SINKS")
sources_Cat_Dict = setupFromTxt(sourcesCatFile, "SOURCES")

# initialize 1 dimensional array that whill contain all analysed apps
apps = []

# read the output_xml from every app - analyse it
for filename in os.listdir(directory):

    FDOutput = xmlDirectory + filename
    deze_app = App(FDOutput)
    deze_app.setCategories(sinks_Cat_Dict, sources_Cat_Dict)

    # once the app is categorised
    apps.append(deze_app)

# once every app is in the list- we can start making graphs
# pieNumOfLeaks(apps)
# histogramNumOfLeaks(apps)
# pieCategoriesSinks(apps)
pieCategoriesSources(apps)

print("donezo")
