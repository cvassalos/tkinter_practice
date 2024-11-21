from tkinter import *
from tkinter import ttk

def buttonText(event):
    if button_state.get():
        big_button.configure(text="YOU UNCLICKED THE BUTTON")
    else:
        big_button.configure(text="YOU CLICKED THE BUTTON")

    button_state.set(not button_state.get())

root = Tk()
root.title("BUTTONS")
root.geometry("400x300")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

button_state = BooleanVar(value=False)

big_button = ttk.Button(root, text="HELLO WORLD", padding=(20, 10))
big_button.place(relx=0.5, rely=0.5, anchor="center")

big_button.bind('<ButtonPress-1>', buttonText)


root.mainloop()