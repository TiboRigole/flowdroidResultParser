import os

from Objects.App import App
from Utilities.ReadClassificationFiles import setupFromTxt
from Graphs.Graphs import generateHistogram_fine, generateHistogram_percentages, generateSourceCategorisation_coarse, generateSinkCategorisation_coarse

# path to dir we want to analyze
analyse_results_dir = "C:\\Users\\tibo\\Desktop\\outputs\\FDroid"
appstore_name = "FDroid app store"

# analyse_results_dir = "C:\\Users\\tibo\\Desktop\\outputs\\Huawei"
# appstore_name = "Huawei app store"

# analyse_results_dir = "C:\\Users\\tibo\\Desktop\\outputs\\ApkPure"
# appstore_name = "ApkPure app store"

#analyse_results_dir = "C:\\Users\\tibo\\Desktop\\outputs\\Tencent"
#appstore_name = "Tencent app store"


# path to sources and sinks categorisation files
sinks_cat_path = 'C:\\Users\\tibo\Documents\\school\\Masterproef\\flowdroidResultParser\\ClassificationFiles\\sinksCategorized.txt'
sources_cat_path = 'C:\\Users\\tibo\\Documents\\school\\Masterproef\\flowdroidResultParser\\ClassificationFiles\\sourcesCategorized.txt'

# setup dictionarys for categorizing the apps
sinks_cat_dict = setupFromTxt(sinks_cat_path, "SINKS")
sources_cat_dict = setupFromTxt(sources_cat_path, "SOURCES")

# list of analyzed apps
apps = []

for filename in os.listdir(analyse_results_dir):

    #print()
    #print(filename)

    absolute_path_to_file = analyse_results_dir + "\\" + filename

    this_app = App(filename, absolute_path_to_file)
    this_app.set_categories(sinks_cat_dict, sources_cat_dict)

    apps.append(this_app)


# histogram maken, elke hoeveelheid leaks wordt geplot
# generateHistogram_fine(apps, appstore_name)
# generateHistogram_percentages(apps, appstore_name)


# piechart van de sources maken, om te zien welke data de meeste leaks proberen te lekken
# hier kunnen we weer fine grained gaan en coarse grained gaan
# categorien zijn opgedeeld in hoofdcategoriën en subcategoriën
#generateSourceCategorisation_coarse(apps, appstore_name, sources_cat_dict)
generateSinkCategorisation_coarse(apps, appstore_name, sinks_cat_dict)