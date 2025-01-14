from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Radiobutton')
root.geometry('200x200')

phone = StringVar()
home = ttk.Radiobutton(root, text='Home', variable=phone, value='home').grid()
office = ttk.Radiobutton(root, text='Office', variable=phone, value='office').grid()
cell = ttk.Radiobutton(root, text='Cell', variable=phone, value='cell').grid()

root.mainloop()
