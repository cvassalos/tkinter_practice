from tkinter import *
from tkinter import ttk

root = Tk()

# Create listbox
l = Listbox(root, height=10)

# Creating options for the listbox
choices = ["apple", "orange", "banana"]
choicesvar = StringVar(value=choices)
l = Listbox(root, listvariable=choicesvar)
l.grid()

# Add to the Listbox
choices.append("peach")
choicesvar.set(choices)
root.mainloop()
