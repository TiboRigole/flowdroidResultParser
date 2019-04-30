import os

from Objects.App import App
from Utilities.ReadClassificationFiles import setupFromTxt
from Graphs.Graphs import barchart_fine

# path to dir we want to analyze
# analyse_results_dir = "C:\\Users\\tibo\\Documents\\school\\Masterproef\\results\\Huawei"
analyse_results_dir = "C:\\Users\\tibo\\Documents\\school\\Masterproef\\results\\FDroid"
# analyse_results_dir = "C:\\Users\\tibo\\Documents\\school\\Masterproef\\results\\ApkPure"


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

# graph generating
amount_leaks_in_apps = []

for app in apps:
    amount_leaks_in_apps.append(app.get_num_of_leaks())
# met num_of_leaks kan je nu al een histogram maken

num_of_leaks_dict = dict()


for amount_leaks in amount_leaks_in_apps:

    if(amount_leaks not in list(num_of_leaks_dict.keys())):
        num_of_leaks_dict[amount_leaks] = 1

    else:
        num_of_leaks_dict[amount_leaks] += 1

keys_list =list(num_of_leaks_dict.keys())

min_value = min(keys_list)
max_value = max(keys_list)

for i in range(min_value, max_value):

    if(i not in keys_list):
        num_of_leaks_dict[i] = 0


import plotly.plotly as py
import plotly.graph_objs as go
import plotly as yeet
yeet.tools.set_credentials_file(username='tibo.rigole', api_key='QdtkPaCzTA4KaOu8Ouif')

x_s = list(num_of_leaks_dict.keys())   # aantal leaks
y_s = list(num_of_leaks_dict.values())  # aantal values


data = [go.Bar(
    x = x_s,
    y = y_s
)]

py.plot(data, filename='basic-bar')