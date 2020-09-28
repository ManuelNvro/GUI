from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image



window = Tk()

window.geometry('700x700')

window.title("NYPA Trasformation")

RPILogo = ImageTk.PhotoImage(Image.open("figures/rpilogo.png").resize((50,50)))
lbll0 = Label(image=RPILogo)
lbll0.grid(column = 100, row = 0)

NYPALogo = ImageTk.PhotoImage(Image.open("figures/nypalogo.jpeg").resize((50,35)))
lbll0 = Label(image=NYPALogo)
lbll0.grid(column = 101, row = 0)

lbl0 = Label(window, text= "NYPA Transformation and Modelica Mass Simulation Tool", font=("Arial Bold", 35))
lbl0.grid(column = 0, row = 0)
lbl0 = Label(window, text= "Created by: ALSET Laboratory, 2019-2020", font=("Arial Bold", 10))
lbl0.grid(column = 0, row = 1)

lbl = Label(window, text= "1) Please select the modeling tool:",font=("Arial", 30))
lbl.grid(column = 0, row = 15)
lbl1 = Label(window, text= "2) Please select the test to be performed:", font=("Arial", 30))
lbl1.grid(column = 0, row = 30)


lbl2 = Label(window, text= "3) Please select the models to simulate:", font=("Arial", 30))
lbl2.grid(column = 0, row = 45)




btn = Button(window, text="Simulate!", font  =("Arial Bold", 10))
btn.grid(column=0, row=50)
btn.config( height = 5, width = 20 )






window.mainloop()