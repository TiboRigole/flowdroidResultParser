import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
def pieNumOfLeaks(appsList):

    # this methode will check all apps in the list and count the number of leaks
    # wil visualise the number of leaks in a pie chart

    aantal_0 = 0
    aantal_1_5 = 0
    aantal_6_15 = 0
    aantal_16_30 = 0
    aantal_31_meer = 0

    for app in appsList:
        numOfLeaks = app.getNumOfLeaks()

        if (numOfLeaks == 0):
            aantal_0 += 1

        elif (numOfLeaks >= 1 and numOfLeaks <= 5):
            aantal_1_5 += 1

        elif (numOfLeaks >= 6 and numOfLeaks <= 15):
            aantal_6_15 += 1

        elif (numOfLeaks >= 16 and numOfLeaks <= 30):
            aantal_16_30 += 1

        elif (numOfLeaks >= 31):
            aantal_31_meer += 1

    # probleem : niet zeker als dit wel 'wetenschappelijk genoeg is'
    labels = ['0 leaks', '1 - 5 leaks', '6 - 15 leaks', '16 - 30 leaks', '31 - ... leaks']
    values = [ aantal_0, aantal_1_5, aantal_6_15, aantal_16_30, aantal_31_meer]

    trace = go.Pie(labels=labels, values=values)
    py.plot([trace], filename='basic_pie_chart')

def histogramNumOfLeaks(appList):

    # setting graph labels,...
    layout = go.Layout(
        title='histogram analyse',
        xaxis=dict(
            title='number of leaks found in app',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='#apps found',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )

    values = []

    for app in appList:
        values.append(app.getNumOfLeaks())

    data = [go.Histogram(x=values)]
    print(values)
    fig = go.Figure(data = data, layout = layout)
    py.plot(fig, filename='basic histogram')

