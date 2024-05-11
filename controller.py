import tkinter as tk
from tkinter import ttk
import graphmd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

SRC = pd.read_csv("ultimate_sud.csv").astype(str)


def creating_label(frame, txt, r, c):
    label = ttk.Label(frame, text=txt)
    label.grid(row=r, column=c, padx=10, pady=10, sticky=tk.W)
    return label


def create_combobox(frame, var, val, r, c):
    scrollbar = ttk.Combobox(frame, textvariable=var)
    scrollbar['values'] = val
    scrollbar['state'] = 'readonly'
    scrollbar.grid(row=r, column=c, sticky=tk.W)


def create_input(frame, r, c):
    input_txt = tk.Entry(frame, width=20)
    input_txt.grid(row=r, column=c)
    return input_txt


def create_text(frame, text, r, c):
    txt = tk.Text(frame)
    txt.grid(row=r, column=c)
    txt.insert(tk.END, text)


def draw_graph(frame, data, x, y, graph):
    global canvas
    if graph == "pie":
        canvas = FigureCanvasTkAgg(graphmd.pie_graph(data[x]), frame)
    elif graph == "bar":
        canvas = FigureCanvasTkAgg(graphmd.bar_graph(data[x], data[y], x, y), frame)
    elif graph == "line":
        canvas = FigureCanvasTkAgg(graphmd.line_graph(data[x], data[y], x, y), frame)
    elif graph == "distribution":
        canvas = FigureCanvasTkAgg(graphmd.dist_graph(data[x]), frame)
    elif graph == "scatter":
        canvas = FigureCanvasTkAgg(graphmd.scatter_plot(data[x], data[y], x, y), frame)
    canvas.get_tk_widget().grid(row=2, column=0, columnspan=3, rowspan=9)
    canvas.draw()
