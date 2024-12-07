from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Messing with BooleanVar")
root.geometry("300x300")

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

def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)

print_hierarchy(root)

root.mainloop()
