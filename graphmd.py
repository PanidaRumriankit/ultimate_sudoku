import matplotlib.pyplot as plt


def pie_graph(labels, sizes):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)


def bar_graph(x, y):
    plt.bar(x, y)
    plt.show()


def line_graph(x, y):
    plt.plot(x, y)
    plt.show()


def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.show()
