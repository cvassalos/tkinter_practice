from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x350')
root.title('Combobox!')

# A combobox widget combines an entry with a list of choices. This lets users either choose from
# a set of values you've provided (eg typical settings), but also puts in their own value (eg for less
# common cases)

def on_country_selected(event):
    # Get the selected value from the combobox
    print(f"Event widget: {event.widget}")
    print(f"Event type: {event.type}")
    selected_country = countryvar.get()
    print(f"Selected country: {selected_country}")

countryvar = StringVar()
country = ttk.Combobox(root, textvariable=countryvar)
country['values'] = ("USA", "Canada", "Greece")
country.grid()

# Bind teh <<Comboboxselected>> event to the handler
country.bind("<<ComboboxSelected>>", on_country_selected)

root.mainloop()
