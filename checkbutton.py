from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x300")
root.title("Checkbutton")

measureSystem = StringVar()
check = ttk.Checkbutton(root, text='Use Metric',
                        variable=measureSystem,
                        onvalue='metric', offvalue='imperial').grid()

check.instate(['alternate'])


root.mainloop()
