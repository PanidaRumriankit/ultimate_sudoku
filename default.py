import tkinter as tk
from tkinter import ttk
import graphmd
import pandas as pd


class DefaultPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (GraphPage, TablePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(GraphPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        self.src = pd.read_csv('ulsudoku.csv')
        tk.Frame.__init__(self, parent)

        v1 = 0
        v2 = 0
        v3 = 0

        button_page = ttk.Button(self, text="Table", command=lambda: controller.show_frame(TablePage))
        button_page.grid(row=0, column=0, padx=5, pady=5)

        labelx = ttk.Label(self, text="x: ")
        labelx.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        var1 = tk.StringVar()
        scrollbar_x = ttk.Combobox(self, textvariable=var1)
        scrollbar_x['values'] = ('difficulty', 'uniqueness', 'clues', 'time', 'branching')
        scrollbar_x['state'] = 'readonly'
        scrollbar_x.grid(row=1, column=1, sticky=tk.W)

        # def one():
        #     v1 = var1.get()
        #
        # scrollbar_x.bind("<<ComboboxSelected>>", one)


        labely = ttk.Label(self, text="y: ")
        labely.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)

        var2 = tk.StringVar()
        scrollbar_y = ttk.Combobox(self, textvariable=var2)
        scrollbar_y['values'] = ('difficulty', 'uniqueness', 'clues', 'time', 'branching')
        scrollbar_y['state'] = 'readonly'
        scrollbar_y.grid(row=1, column=3, sticky=tk.W)

        # def two():
        #     v2 = var2.get()
        #
        # scrollbar_y.bind("<<ComboboxSelected>>", two)

        lb_graph = ttk.Label(self, text="graph: ")
        lb_graph.grid(row=1, column=4, padx=10, pady=10, sticky=tk.W)

        var3 = tk.StringVar()
        scrollbar_g = ttk.Combobox(self, textvariable=var3)
        scrollbar_g['values'] = ('bar', 'pie', 'line', 'scatter')
        scrollbar_g['state'] = 'readonly'
        scrollbar_g.grid(row=1, column=5, sticky=tk.W)

        # def three():
        #     v3 = var3.get()
        #
        # scrollbar_y.bind("<<ComboboxSelected>>", three)

        # label = ttk.Label(self, text=var3.get())
        # label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        # print(var3.get())

        # def compute(event):
        #     button_graph = tk.Button(self, text="Draw", bg="lightgray", cursor="hand2", width=15, padx=10, pady=5,
        #                              command=self.draw_graph(v1, v2, v3))
        #     button_graph.grid(row=1, column=6, padx=20, pady=20)
        #
        # scrollbar_g.bind("<<ComboboxSelected>>", compute)


    # def draw_graph(self, x, y, graph):
    #     if graph == "pie":
    #         graphmd.pie_graph([x, y], x)
    #     elif graph == "bar":
    #         label = ttk.Label(self, text="XDXDXDXDXD")
    #         label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    #         graphmd.bar_graph(self.src[x], self.src[y])
    #     elif graph == "line":
    #         graphmd.line_graph(self.src[x], self.src[y])
    #     elif graph == "scatter":
    #         graphmd.scatter_plot(self.src[x], self.src[y])








class TablePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button_page = ttk.Button(self, text="Graph", command=lambda: controller.show_frame(GraphPage))
        button_page.grid(row=0, column=0, padx=5, pady=5)
