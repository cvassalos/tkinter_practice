from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Working with Trace Routes")
root.geometry("600x200")

var = StringVar()

entry = ttk.Button(root, textvariable=var)
entry.grid()

label=ttk.Label(root, text="TEST LABEL")
label.grid()

def update_label(*args):
    label.config(text=var.get())


root.mainloop()
