import plotly.plotly as py
import plotly.graph_objs as go

def generateHistogram_fine(apps, appstore_name):
    # graph generating
    amount_leaks_in_apps = []

    for app in apps:
        amount_leaks_in_apps.append(app.get_num_of_leaks())
    # met num_of_leaks kan je nu al een histogram maken

    aantal_apps = str(len(apps))


    num_of_leaks_dict = dict()

    for amount_leaks in amount_leaks_in_apps:

        if (amount_leaks not in list(num_of_leaks_dict.keys())):
            num_of_leaks_dict[amount_leaks] = 1

        else:
            num_of_leaks_dict[amount_leaks] += 1

    keys_list = list(num_of_leaks_dict.keys())

    min_value = min(keys_list)
    max_value = max(keys_list)

    for i in range(min_value, max_value):

        if (i not in keys_list):
            num_of_leaks_dict[i] = 0


    x_s = list(num_of_leaks_dict.keys())  # aantal leaks
    y_s = list(num_of_leaks_dict.values())  # aantal values

    data = [go.Bar(
        x=x_s,
        y=y_s
    )]

    layout = go.Layout(
        title=go.layout.Title(
            text='Histogram van aantal leaks: ' + appstore_name + "\n" + "in totaal "+aantal_apps+" apps geanalyseerd",

        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text='Aantal leaks gevonden',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text='Aantal apps',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        )
    )

    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, filename='histogram')

def generateHistogram_percentages(apps, appstore_name):
    # graph generating
    amount_leaks_in_apps = []

    for app in apps:
        amount_leaks_in_apps.append(app.get_num_of_leaks())
    # met num_of_leaks kan je nu al een histogram maken

    num_of_leaks_dict = dict()

    for amount_leaks in amount_leaks_in_apps:

        if (amount_leaks not in list(num_of_leaks_dict.keys())):
            num_of_leaks_dict[amount_leaks] = 1

        else:
            num_of_leaks_dict[amount_leaks] += 1

    keys_list = list(num_of_leaks_dict.keys())

    min_value = min(keys_list)
    max_value = max(keys_list)

    for i in range(min_value, max_value):

        if (i not in keys_list):
            num_of_leaks_dict[i] = 0



    # parse aantal naar percentages
    aantal_apps = len(apps)

    percentages = []

    for value in list(num_of_leaks_dict.values()):
        percentages.append((value / aantal_apps) *100)

    x_s = list(num_of_leaks_dict.keys())  # aantal leaks
    y_s = percentages  # aantal values

    data = [go.Bar(
        x=x_s,
        y=y_s
    )]

    layout = go.Layout(
        title=go.layout.Title(
            text='Histogram van aantal leaks in percentages: ' + appstore_name + "\n" + "in totaal "+str(aantal_apps)+" apps geanalyseerd",

        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text='Aantal leaks gevonden',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text='Percentage van alle apps',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        )
    )

    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, filename='histogrampercentages')






def generateSourceCategorisation_coarse(apps, appstore_name, sources_cat_dict):
    all_leaks = []

    aantal_apps = str(len(apps))

    for app in apps:
        leaks_for_this_app = app.get_leaks()

        for leak in leaks_for_this_app:
            all_leaks.append(leak)

    # every leak is now in the leaks array

    sources_maincategories_dict = dict()

    for leak in all_leaks:
        sources_categories = leak.sources_categories

        for source_cat in sources_categories:

            #parsinge
            main_cat = source_cat.get_main_cat()

            if main_cat in sources_maincategories_dict:
                sources_maincategories_dict[main_cat] += 1

            else:
                sources_maincategories_dict[main_cat] = 1


    for key,value in sources_maincategories_dict.items():
        print(key, ": ",value)


    labels = list(sources_maincategories_dict.keys())
    values = list(sources_maincategories_dict.values())

    data = [go.Pie(
        labels = labels,
        values = values
    )]

    layout = go.Layout(
        title=go.layout.Title(
            text='Taartdiagram ivm frequentie van voorkomen van sources: ' + appstore_name + "\n" + "in totaal " + str(
                aantal_apps) + " apps geanalyseerd",
        ),
    )

    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, filename='sourcescategorisationhoofdniveau')




def generateSinkCategorisation_coarse(apps, appstore_name, sinks_cat_dict):

    all_leaks = []

    aantal_apps = str(len(apps))

    for app in apps:
        leaks_for_this_app = app.get_leaks()

        for leak in leaks_for_this_app:
            all_leaks.append(leak)

    sinks_maincategories_dict = dict()

    for leak in all_leaks:
        sink_category = leak.sink_category

        # parsinge
        main_cat = sink_category.get_main_cat()

        if main_cat in sinks_maincategories_dict:
            sinks_maincategories_dict[main_cat] += 1

        else:
            sinks_maincategories_dict[main_cat] = 1

    for key,value in sinks_maincategories_dict.items():
        print(key, ": ",value)


    labels = list(sinks_maincategories_dict.keys())
    values = list(sinks_maincategories_dict.values())

    data = [go.Pie(
        labels = labels,
        values = values
    )]

    layout = go.Layout(
        title=go.layout.Title(
            text='Taartdiagram ivm frequentie van voorkomen van sinks: ' + appstore_name + "\n" + "in totaal " + str(
                aantal_apps) + " apps geanalyseerd",
        ),
    )

    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, filename='sinkscategorisationhoofdniveau')
