from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
root.title("TESTING LABELS")

# Creating two styles
s = ttk.Style()
# Style1
s.configure('Style1.Label', background='black',
            foreground='white',
            font=('Helvetica', 24, 'bold'))
# Style2, both created using the same Style() object (s)
s.configure('Style2.Label', background='lightblue',
            foreground='darkblue',
            font=('Arial', 14, 'bold'))
# Style for a frame
s.configure('StyleF.TFrame', background='green', borderwidth=6, relief='raised')

# Create a frame to mess with geometry
frame1 = ttk.Frame(root, style='StyleF.TFrame').grid()

# Create two labels and put them in the grid
main_label = ttk.Label(root, text='MAIN LABEL', style='Style1.Label').grid()
secondary_label = ttk.Label(frame1, 
                            text='SECONDARY LABEL\nTWO LINES',
                            style='Style2.Label',
                            justify='center').grid()

# Save image to variable
image = PhotoImage(file='AEK_Athletic_Club.png')

# Create Label to be an image
image_label = ttk.Label(frame1, 
                        text='AEK Athletic Club Logo',
                        image=image,
                        compound='top',  # Options: 'top', 'bottom', 'left', 'right', 'center', or 'none'
                        font=('Helvetica', 12, 'bold'))
image_label.grid()

root.mainloop()
