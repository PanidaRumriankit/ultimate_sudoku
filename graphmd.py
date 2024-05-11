import matplotlib.pyplot as plt


def pie_graph(x):
    fig, ax = plt.subplots(figsize=(5, 5))
    size = x.value_counts(normalize=True) * 100
    sizes = size.tolist()
    labels = list(x.unique())
    ax.pie(sizes, labels=labels)
    ax.grid(True)
    return fig


def bar_graph(x, y, name_x, name_y):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.bar(x, y, color="skyblue")
    ax.set_xlabel(name_x)
    ax.set_ylabel(name_y)
    ax.grid(True)
    return fig


def dist_graph(x):
    fig, ax = plt.subplots()
    ax.hist(x)
    ax.set_xlabel('clues')
    ax.set_ylabel('Frequency')
    return fig


def line_graph(x, y, name_x, name_y):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(x, y, color="b")
    ax.set_xlabel(name_x)
    ax.set_ylabel(name_y)
    ax.grid(True)
    return fig


def scatter_plot(x, y, name_x, name_y):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.scatter(x, y, color="b")
    ax.set_xlabel(name_x)
    ax.set_ylabel(name_y)
    ax.grid(True)
    return fig
