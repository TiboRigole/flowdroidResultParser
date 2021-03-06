import plotly.plotly as py
import plotly.graph_objs as go

def countSources(apps, sourcesDict):

    # sourcesDict contains key -> value as source -> category
    # here we only will count sources, so we need to extract these
    sourcesCounts = dict()

    for key in sourcesDict:
        sourcesCounts[key] = 0

    for app in apps:

        for leak in app.getLeaks():

            sources = leak.getSources()

            for source in sources:
                sourcesCounts[key] += 1

    sources = []
    counts = []

    # map them as lists
    for key in sourcesCounts:
        sources.append(str(key))
        counts.append(sourcesCounts[key])

    print(sources)
    print(counts)
    print("total number of apps checked: ", 0) #todo: fill in this!

    # setting graph labels,...

    layout = go.Layout(
        title='hoeveelheid sources in vergelijking met elkaar'
    )
    trace = go.Pie(labels= sources, values=counts)
    py.plot([trace], filename='basic_pie_chart')


def countSinks(apps, sinksDict):
    # sourcesDict contains key -> value as source -> category
    # here we only will count sources, so we need to extract these
    sinkCounts = dict()

    for key in sinksDict:
        sinkCounts[key] = 0

    print("hey")
    for app in apps:

        print(app.name)
        for leak in app.getLeaks():

            sink_from_app = leak.getSink()

            for key in sinkCounts:
                if(sink_from_app.equals(key)):
                    sinkCounts[key] += 1






    sinks = []
    counts = []

    # map them as lists
    for key in sinkCounts:
        sinks.append(str(key))
        counts.append(sinkCounts[key])

    for key in sinkCounts:
        print(str(key) +": "+ str(sinkCounts[key]))

    print(sinks)
    print(counts)
    print("total number of apps checked: ", len(apps))  # todo: fill in this!

    # setting graph labels,...

    layout = go.Layout(
        title='hoeveelheid sinks in vergelijking met elkaar'
    )
    trace = go.Pie(labels=sinks, values=counts)
    py.plot([trace], filename='basic_pie_chart')