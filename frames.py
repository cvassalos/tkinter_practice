from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
root.title("Frames on Frames")

s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')


frame1 = ttk.Frame(root, width=200, height=200, padding=5, style='Danger.TFrame')
frame1['padding'] = 5
frame1['borderwidth'] = 5
frame1['relief'] = 'sunken'
frame1.grid()

frame2 = ttk.Frame(root, width=500, height=500, padding=5, style='Danger.TFrame')
frame2['padding'] = 5
frame2['borderwidth'] = 5
frame2['relief'] = 'sunken'
frame2.grid()

label1 = ttk.Label(frame1, text="Label One").grid()
label2 = ttk.Label(frame2, text="Label Two").grid()



root.mainloop()
