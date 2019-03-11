# denk dat het best is om de apps zonder leaks hier uit te laten
# eigenlijk dus kijken voor elke leak?
# een leak heeft 1 source en meerdere sinks (minstens 1)

import plotly.plotly as py
import plotly.graph_objs as go

def pieCategoriesSinks(apps):

    # important!!!
    # one app can only add 1 towards the amount of leaks from that category
    # so if one app has 3 leaks with the same sink, it still only counts as 1 for that category
    # job no. 1 is to extract all unique sinks (and their categories)
    # app has leaks, leaks have sink, source, sinkcat, sourcecats, so no categorisation has te be found out
    # -> dit moet ook zeker in het verslag
    #setup for counting

    # now categories has key = category and value 0
    categoriesCount = dict()

    for app in apps:

        thisAppsSet = set()

        # get all unique sinks and their categories out of this app
        for leak in app.getLeaks():
            sink = leak.getSink()

            if sink not in thisAppsSet:
                thisAppsSet.add(sink)

                category = leak.getSinkCat()

                # if category already has an amount
                if(category in categoriesCount):
                    categoriesCount[category] += 1

                # if new category
                else:
                    categoriesCount[category] = 1

    # after every app is analysed
    labels = []
    values = []

    for key, value in categoriesCount.items():
        labels.append(str(key))
        values.append(value)

    print(labels)
    print(values)

    trace = go.Pie(labels=labels, values=values)
    py.plot([trace], filename='basic_pie_chart')


def pieCategoriesSources(apps):

    categoriesCount = dict()

    for app in apps:

        thisAppSet = set()

        # get all unique sources and their categories out of this app
        for leak in app.getLeaks():
            sourcesCatDict = leak.getSourcesCatDict()

            for source in sourcesCatDict:
                if source not in thisAppSet:
                    thisAppSet.add(source)

                    category = sourcesCatDict[source]

                    # if category already has an amount
                    if(category in categoriesCount):
                        categoriesCount[category] += 1

                    # if new category
                    else:
                        categoriesCount[category] = 1

    # after every app is analysed
    labels = []
    values = []

    for key, value in categoriesCount.items():
        labels.append(str(key))
        values.append(value)

    print(labels)
    print(values)

    trace = go.Pie(labels=labels, values=values)
    py.plot([trace], filename='basic_pie_chart')


def histoCategoriesSources(apps):
    pass

def histoCategoriesSinks(apss):
    pass

