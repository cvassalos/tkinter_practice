import tkinter as tk

def validate_input(action, index, proposed_value, current_value, input_text, validation_type, widget_name):
    print(f"Action: {action}")           # Type of action (1=insert, 0=delete, -1=focus change)
    print(f"Index: {index}")             # Index of the change
    print(f"Proposed: {proposed_value}") # Proposed new value of the Entry
    print(f"Current: {current_value}")   # Current value of the Entry
    print(f"Input: {input_text}")        # Text that is being inserted or deleted
    print(f"Type: {validation_type}")    # Type of validation (key, focusin, focusout)
    print(f"Widget: {widget_name}")      # Name of the widget
    print('\n')

    # Example validation: Allow only numeric input
    if proposed_value.isdigit() or proposed_value == "":
        return True
    return False

root = tk.Tk()
root.geometry("300x100")

vcmd = (root.register(validate_input), '%d', '%i', '%P', '%s', '%S', '%v', '%W')

entry = tk.Entry(root, validate="key", validatecommand=vcmd)
entry.pack(pady=20)

root.mainloop()
