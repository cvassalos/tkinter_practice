from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x400')
root.title('Entry Box')

username = StringVar()
name = ttk.Entry(root, textvariable=username)
name.grid()

name.insert(0, 'Please Enter your Name Here') # Starts the entry box with this text in it

def print_value(event=None):
    print('Entered Name: %s' % name.get())
    deleteText()

def deleteText(event=None):
    name.delete(0, '5') # Deletes the value in the entry box after hitting enter

button = ttk.Button(root, text='Print Value', command=print_value)
button.grid()

name.bind('<ButtonPress-1>', deleteText) # Delete the text in the entry box upon clicking
name.bind('<Return>', print_value) # Binds return key to entry box


root.mainloop()
