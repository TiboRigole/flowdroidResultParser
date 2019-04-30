import os

from Objects.App import App
from Utilities.ReadClassificationFiles import setupFromTxt

# path to dir we want to analyze
analyse_results_dir = "C:\\Users\\tibo\\Documents\\school\\Masterproef\\results\\Huawei"

# path to sources and sinks categorisation files
sinks_cat_path = 'C:\\Users\\tibo\Documents\\school\\Masterproef\\flowdroidResultParser\\ClassificationFiles\\sinksCategorized.txt'
sources_cat_path = 'C:\\Users\\tibo\\Documents\\school\\Masterproef\\flowdroidResultParser\\ClassificationFiles\\sourcesCategorized.txt'

# setup dictionarys for categorizing the apps
sinks_cat_dict = setupFromTxt(sinks_cat_path, "SINKS")
sources_cat_dict = setupFromTxt(sources_cat_path, "SOURCES")

# list of analyzed apps
apps = []

for filename in os.listdir(analyse_results_dir):

    print()
    print(filename)

    absolute_path_to_file = analyse_results_dir + "\\" + filename

    this_app = App(filename, absolute_path_to_file)
    this_app.set_categories(sinks_cat_dict, sources_cat_dict)

    apps.append(this_app)