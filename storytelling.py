import tkinter as tk
from tkinter import ttk
import pandas as pd
import controller


class StorytellingPage(tk.Tk):
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
    def __init__(self, parent, controll):
        tk.Frame.__init__(self, parent)

        self.data = pd.read_csv('ultimate_sud.csv')

        button_page = ttk.Button(self, text="Table", command=lambda: controll.show_frame(TablePage))
        button_page.grid(row=0, column=0, padx=5, pady=5)

        controller.creating_label(self, "x: ", 1, 0)
        var1 = tk.StringVar()
        controller.create_combobox(self, var1, ('difficulty', 'clues'), 1, 1)

        controller.creating_label(self, "y: ", 1, 2)
        var2 = tk.StringVar()
        controller.create_combobox(self, var2, ('', 'clues'), 1, 3)

        controller.creating_label(self, "graph: ", 1, 4)
        var3 = tk.StringVar()
        controller.create_combobox(self, var3, ('pie', 'bar', 'distribution'), 1, 5)

        def on_button_click():
            v1 = var1.get()
            v2 = var2.get()
            v3 = var3.get()
            controller.draw_graph(self, self.data, v1, v2, v3)

        button_graph = tk.Button(self, text="Draw", bg="lightgray", cursor="hand2", width=15, padx=10, pady=5,
                                 command=on_button_click)
        button_graph.grid(row=1, column=6, padx=20, pady=20)


class TablePage(tk.Frame):
    def __init__(self, parent, controll):
        tk.Frame.__init__(self, parent)
        button_page = ttk.Button(self, text="Graph", command=lambda: controll.show_frame(GraphPage))
        button_page.grid(row=0, column=0, padx=5, pady=5)

        self.data = pd.read_csv('ultimate_sud.csv')
        self.labels = []

        controller.creating_label(self, "count", 1, 2)
        controller.creating_label(self, "mean", 1, 3)
        controller.creating_label(self, "SD", 1, 4)
        controller.creating_label(self, "min", 1, 5)
        controller.creating_label(self, "25%", 1, 6)
        controller.creating_label(self, "50%", 1, 7)
        controller.creating_label(self, "75%", 1, 8)
        controller.creating_label(self, "max", 1, 9)

        controller.creating_label(self, "time", 2, 1)

        self.data['time'] = self.data['time'].astype(float)

        for j in range(8):
            self.labels.append(controller.creating_label(self, self.data['time'].describe()[j], 2, j + 2))

        data = self.data.drop(['difficulty', 'puzzle'], axis=1)
        controller.creating_label(self, data.corr(), 13, 1)

# Check this file
# app = StorytellingPage()
# app.mainloop()
