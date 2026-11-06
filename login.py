from tkinter import *
from tkinter import ttk
import tkinter

root = Tk()
root.title("Scout TF2")

frame_pricipal = ttk.Frame(root, padding=(3, 3, 12, 12))
frame_pricipal.grid(column=0, row=0, sticky=(N, W, E, S))

email = StringVar()
email_entrada = ttk.Entry(frame_pricipal, width=7, textvariable=email, background="red")
email_entrada.grid(column=1, row=1)


root.mainloop()