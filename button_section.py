from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("250x400")
root.title("BUTTONS")

action = ttk.Button(root, text="Action")
root.bind('<Return>', lambda e: action.invoke())

action.state(['disabled']) # set the disabled flag
action.state(['!disabled']) # clear the disabled flag
action.instate(['disabled']) # true if disabled, else false
action.instate(['!disabled']) # true if not disabled, else false
action.instate(['!disabled'], cmd) # execute 'cmd' if not disabled
action.grid()

root.mainloop()
