from tkinter import *
from tkinter import ttk

root = Tk()

# Using BooleanVar to store state
button_state = BooleanVar(value=False)

# Create a Checkbutton bound to the BooleanVar
check_button = ttk.Checkbutton(root, text="Click me", variable=button_state)
check_button.grid()

# Use button_state.get() to get the current state of the button
def print_state():
    print(button_state.get())  # Prints True or False

button = ttk.Button(root, text="Print State", command=print_state)
button.grid()

root.mainloop()