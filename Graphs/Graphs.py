import plotly

def generateHistogram_fine(apps, appstore_name):
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

    import plotly.plotly as py
    import plotly.graph_objs as go

    x_s = list(num_of_leaks_dict.keys())  # aantal leaks
    y_s = list(num_of_leaks_dict.values())  # aantal values

    data = [go.Bar(
        x=x_s,
        y=y_s
    )]

    layout = go.Layout(
        title=go.layout.Title(
            text='Histogram van aantal leaks: ' + appstore_name + "\n" + "in totaal 372 apps geanalyseerd",

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