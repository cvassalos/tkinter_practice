from tkinter import *
from tkinter import ttk
import re

root = Tk()
root.geometry('500x400')
root.title('Entry Box')

username = StringVar()
pw = StringVar()
num = StringVar()
name = ttk.Entry(root, textvariable=username)
name.grid()
# Turn entry into password entry box
password = ttk.Entry(root, textvariable=pw, show="@")
password.grid()

# Start entry box with text in it
name.insert(0, 'Please Enter your Name Here') # Starts the entry box with this text in it

# Printing string b/c trace indicates entry value has changed
def callback(*args):
    print("Value changed")

# Function prints the entered name and adds a trace to the username entry object
def print_value(event=None):
    # username.trace_add("write", callback)
    # print(username.trace_info())
    username.trace_add("write", lambda *args: updateLabel(name.get()))
    print('Entered Name: %s' % name.get())
    deleteText()

# Deletes text in the entry box
def deleteText(event=None):
    name.delete(0, 'end') # Deletes the value in the entry box after hitting enter

# Supposed to change the text of the label to what has been entered ----- WORK IN PROGRESS
def updateLabel(name):
    name_label.config(text=name)

# Function that validates a string is no longer than 5 characters and only numbers 0 through 9
def check_num(newval):
    return re.match('^[0-9]*$', newval) is not None and len(newval) <= 5
check_num_wrapper = (root.register(check_num), '%P')

# Validated entry
e = ttk.Entry(root, textvariable=num, validate='key', validatecommand=check_num_wrapper)
e.grid()

# Create button object with Print Value as its text and calls print_value function when clicked
button = ttk.Button(root, text='Print Value', command=print_value)
button.grid()
# Create a label
name_label = ttk.Label(root, text="")
name_label.grid()

name.bind('<ButtonPress-1>', deleteText) # Delete the text in the entry box upon clicking
name.bind('<Return>', print_value) # Binds return key to entry box


root.mainloop()
