from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="hello world").grid(column=0, row=0)
ttk.Button(frm, text="Quit",width=200, padding=20, command=root.destroy).grid(column=0, row=3)

root.mainloop()