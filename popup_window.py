import tkinter as tk
from tkinter.messagebox import showinfo

# Create a root window (not displayed)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Show an info messagebox
showinfo("Information", "Your process has completed successfully!")

# Run the main loop (optional in this case)
root.mainloop()
