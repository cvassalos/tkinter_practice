import tkinter as tk

window = tk.Tk()

window.title('Hello Python')
greeting = tk.Label(text="Hello, Tkinter")
window.geometry("300x200+10+20")
window.mainloop()