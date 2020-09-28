from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('NYPA Model Transformation Modelica Routines')


Img = ImageTk.PhotoImage(Image.open("figures/rpilogo.png"))
label = Label(image=Img)
label.pack()




root.mainloop()