import default
import storytelling
import tkinter as tk


root = tk.Tk()
root.title("Ultimate sudoku")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

page_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Page", menu=page_menu)
page_menu.add_command(label="default", command=default.DefaultPage)
page_menu.add_command(label="Storytelling", command=storytelling.StorytellingPage)

exit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Exit", menu=exit_menu)
exit_menu.add_command(label="Quit", command=root.quit)

root.config(menu=menu_bar)
root.mainloop()
