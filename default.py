import tkinter as tk
from tkinter import ttk

import pandas as pd

import controller


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
    def __init__(self, parent, controll):
        tk.Frame.__init__(self, parent)

        self.data = controller.SRC

        button_page = ttk.Button(self, text="Table", command=lambda: controll.show_frame(TablePage))
        button_page.grid(row=0, column=0, padx=5, pady=5)

        controller.creating_label(self, "x: ", 1, 0)
        var1 = tk.StringVar()
        controller.create_combobox(self, var1, ('difficulty', 'uniqueness', 'clues', 'time', 'branching'), 1, 1)

        controller.creating_label(self, "y: ", 1, 2)
        var2 = tk.StringVar()
        controller.create_combobox(self, var2, ('difficulty', 'uniqueness', 'clues', 'time', 'branching'), 1, 3)

        controller.creating_label(self, "graph: ", 1, 4)

        var3 = tk.StringVar()
        controller.create_combobox(self, var3, ('bar', 'line', 'pie', 'scatter'), 1, 5)

        def on_button_click():
            v1 = var1.get()
            v2 = var2.get()
            v3 = var3.get()
            controller.draw_graph(self, self.data, v1, v2, v3)

        button_graph = tk.Button(self, text="Draw", bg="lightgray", cursor="hand2", width=15, padx=10, pady=5,
                                 command=on_button_click)
        button_graph.grid(row=1, column=6, padx=20, pady=20)

        controller.creating_label(self, "filter: ", 2, 3)

        controller.creating_label(self, "x ", 2, 4)
        var4 = tk.StringVar()
        controller.create_combobox(self, var4, ('equal to', 'greater than', 'less than'), 2, 5)
        x_f = controller.create_input(self, 2, 6)

        controller.creating_label(self, "y ", 3, 4)
        var5 = tk.StringVar()
        controller.create_combobox(self, var5, ('equal to', 'greater than', 'less than'), 3, 5)
        y_f = controller.create_input(self, 3, 6)

        def filter_click():
            filtered_x = self.filt(self.data, var4.get(), var1.get(), x_f.get())
            filtered_y = self.filt(filtered_x, var5.get(), var2.get(), y_f.get())
            self.data = filtered_y
            on_button_click()

        button_filter = tk.Button(self, text="Filter", bg="lightgray", cursor="hand2", width=15, padx=10, pady=5,
                                  command=filter_click)
        button_filter.grid(row=4, column=6, padx=20, pady=20)

        controller.creating_label(self, "adding data", 5, 3)

        controller.creating_label(self, "difficulty: ", 6, 3)
        diff_new = controller.create_input(self, 6, 4)

        controller.creating_label(self, "uniqueness: ", 7, 3)
        uniq_new = controller.create_input(self, 7, 4)

        controller.creating_label(self, "clues: ", 8, 3)
        clues_new = controller.create_input(self, 8, 4)

        controller.creating_label(self, "time: ", 9, 3)
        time_new = controller.create_input(self, 9, 4)

        controller.creating_label(self, "branching: ", 10, 3)
        br_new = controller.create_input(self, 10, 4)

        def adding_data_click():
            new_data = {'difficulty': diff_new.get(),
                        'uniqueness': uniq_new.get(),
                        'clues': clues_new.get(),
                        'time': time_new.get(),
                        'branching': br_new.get()}
            self.data.loc[len(self.data)] = new_data
            on_button_click()

        button_filter = tk.Button(self, text="Add", bg="lightgray", cursor="hand2", width=15, padx=10, pady=5,
                                  command=adding_data_click)
        button_filter.grid(row=7, column=6, padx=20, pady=20)

        def reset():
            self.data = pd.read_csv('ultimate_sud.csv').astype(str)
            on_button_click()

        button_reset = tk.Button(self, text="Reset", bg="lightgray", cursor="hand2", width=15, padx=10, pady=5,
                                  command=reset)
        button_reset.grid(row=0, column=7, padx=20, pady=20)

    @staticmethod
    def filt(data, sign, v, f):
        if sign == "equal to":
            result = data[data[v] == f]
        elif sign == "greater than":
            result = data[data[v] > f]
        else:
            result = data[data[v] < f]
        return result


class TablePage(tk.Frame):
    def __init__(self, parent, controll):
        tk.Frame.__init__(self, parent)
        button_page = ttk.Button(self, text="Graph", command=lambda: controll.show_frame(GraphPage))
        button_page.grid(row=0, column=0, padx=5, pady=5)

        self.data = pd.read_csv('ultimate_sud.csv')
        self.labels = []
        self.data_num = self.data.drop(['difficulty', 'puzzle'], axis=1)

        controller.creating_label(self, "count", 1, 2)
        controller.creating_label(self, "mean", 1, 3)
        controller.creating_label(self, "SD", 1, 4)
        controller.creating_label(self, "min", 1, 5)
        controller.creating_label(self, "25%", 1, 6)
        controller.creating_label(self, "50%", 1, 7)
        controller.creating_label(self, "75%", 1, 8)
        controller.creating_label(self, "max", 1, 9)

        controller.creating_label(self, "uniqueness", 2, 1)
        controller.creating_label(self, "clues", 3, 1)
        controller.creating_label(self, "time", 4, 1)
        controller.creating_label(self, "branching", 5, 1)

        names = ['uniqueness', 'clues', 'time', 'branching']

        for name in names:
            self.data[name] = self.data[name].astype(float)

        for i in range(4):
            for j in range(8):
                self.labels.append(controller.creating_label(self, self.data[names[i]].describe()[j], i + 2, j + 2))

        self.datas = controller.creating_label(self, self.data_num.corr(), 13, 1)

        def destroy_tb():
            for label in self.labels:
                label.destroy()

        def reset_table():
            destroy_tb()
            self.data = pd.read_csv('ultimate_sud.csv')
            self.datas.destroy()
            self.data_num = self.data.drop(['difficulty', 'puzzle'], axis=1)
            self.datas = controller.creating_label(self, self.data_num.corr(), 13, 1)
            self.labels = []
            for i in range(4):
                for j in range(8):
                    self.labels.append(controller.creating_label(self, self.data[names[i]].describe()[j], i + 2, j + 2))

        button_reset = tk.Button(self, text="Reset", bg="lightgray", cursor="hand2", width=15, padx=10, pady=5,
                                  command=reset_table)
        button_reset.grid(row=0, column=7, padx=20, pady=20)

        controller.creating_label(self, "adding data", 7, 1)

        controller.creating_label(self, "difficulty: ", 8, 1)
        diff_new = controller.create_input(self, 8, 2)

        controller.creating_label(self, "uniqueness: ", 9, 1)
        uniq_new = controller.create_input(self, 9, 2)

        controller.creating_label(self, "clues: ", 10, 1)
        clues_new = controller.create_input(self, 10, 2)

        controller.creating_label(self, "time: ", 11, 1)
        time_new = controller.create_input(self, 11, 2)

        controller.creating_label(self, "branching: ", 12, 1)
        br_new = controller.create_input(self, 12, 2)

        def adding_data_click():
            new_data = {'difficulty': diff_new.get(),
                        'uniqueness': float(uniq_new.get()),
                        'clues': float(clues_new.get()),
                        'time': float(time_new.get()),
                        'branching': float(br_new.get())}
            self.data.loc[len(self.data)] = new_data
            destroy_tb()
            self.datas.destroy()
            self.data_num = self.data.drop(['difficulty', 'puzzle'], axis=1)
            self.datas = controller.creating_label(self, self.data_num.corr(), 13, 1)
            for i in range(4):
                for j in range(8):
                    self.labels.append(controller.creating_label(self, self.data[names[i]].describe()[j], i + 2, j + 2))

        button_add = tk.Button(self, text="Add", bg="lightgray", cursor="hand2", width=15, padx=10, pady=5,
                                  command=adding_data_click)
        button_add.grid(row=12, column=3, padx=20, pady=20)

        controller.creating_label(self, self.data_num.corr(), 13, 1)

# Check this file
# app = DefaultPage()
# app.mainloop()
