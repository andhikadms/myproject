#Andhika Dimas Pornomo
#01123956151-36

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("2000x2000")
root.title("Growth Curve")

Label(root, text="WHO Growth Curve\n Input Weight, Length, and Gender from your baby").grid(row=0, column=3, columnspan=3, sticky=W)
Label(root, text=None).grid(row=1,column=3, columnspan=3) # space between inputs and outputs

gender = IntVar()
Label(root, text="Gender").grid(row=27, column=1, sticky=W)
Radiobutton(root, text="Men", variable=gender, value=1).grid(row=28, column=1, sticky=W) 
Radiobutton(root, text="Women", variable=gender, value=2).grid(row=28, column=2, sticky=W)

Label(root, text="1 Weight").grid(row=2, column=1, sticky=W)
Label(root, text="2 Weight").grid(row=3, column=1, sticky=W)
Label(root, text="3 Weight").grid(row=4, column=1, sticky=W)
Label(root, text="4 Weight").grid(row=5, column=1, sticky=W)
Label(root, text="5 Weight").grid(row=6, column=1, sticky=W)
Label(root, text="6 Weight").grid(row=7, column=1, sticky=W)
Label(root, text="7 Weight").grid(row=8, column=1, sticky=W)
Label(root, text="8 Weight").grid(row=9, column=1, sticky=W)
Label(root, text="9 Weight").grid(row=10, column=1, sticky=W)
Label(root, text="10 Weight").grid(row=11, column=1, sticky=W)
Label(root, text="11 Weight").grid(row=12, column=1, sticky=W)
Label(root, text="12 Weight").grid(row=13, column=1, sticky=W)
Label(root, text="13 Weight").grid(row=14, column=1, sticky=W)
Label(root, text="14 Weight").grid(row=15, column=1, sticky=W)
Label(root, text="15 Weight").grid(row=16, column=1, sticky=W)
Label(root, text="16 Weight").grid(row=17, column=1, sticky=W)
Label(root, text="17 Weight").grid(row=18, column=1, sticky=W)
Label(root, text="18 Weight").grid(row=19, column=1, sticky=W)
Label(root, text="19 Weight").grid(row=20, column=1, sticky=W)
Label(root, text="20 Weight").grid(row=21, column=1, sticky=W)
Label(root, text="21 Weight").grid(row=22, column=1, sticky=W)
Label(root, text="22 Weight").grid(row=23, column=1, sticky=W)
Label(root, text="23 Weight").grid(row=24, column=1, sticky=W)
Label(root, text="24 Weight").grid(row=25, column=1, sticky=W)


Label(root, text="  1 Length").grid(row=2, column=3, sticky=W)
Label(root, text="  2 Length").grid(row=3, column=3, sticky=W)
Label(root, text="  3 Length").grid(row=4, column=3, sticky=W)
Label(root, text="  4 Length").grid(row=5, column=3, sticky=W)
Label(root, text="  5 Length").grid(row=6, column=3, sticky=W)
Label(root, text="  6 Length").grid(row=7, column=3, sticky=W)
Label(root, text="  7 Length").grid(row=8, column=3, sticky=W)
Label(root, text="  8 Length").grid(row=9, column=3, sticky=W)
Label(root, text="  9 Length").grid(row=10, column=3, sticky=W)
Label(root, text="  10 Length").grid(row=11, column=3, sticky=W)
Label(root, text="  11 Length").grid(row=12, column=3, sticky=W)
Label(root, text="  12 Length").grid(row=13, column=3, sticky=W)
Label(root, text="  13 Length").grid(row=14, column=3, sticky=W)
Label(root, text="  14 Length").grid(row=15, column=3, sticky=W)
Label(root, text="  15 Length").grid(row=16, column=3, sticky=W)
Label(root, text="  16 Length").grid(row=17, column=3, sticky=W)
Label(root, text="  17 Length").grid(row=18, column=3, sticky=W)
Label(root, text="  18 Length").grid(row=19, column=3, sticky=W)
Label(root, text="  19 Length").grid(row=20, column=3, sticky=W)
Label(root, text="  20 Length").grid(row=21, column=3, sticky=W)
Label(root, text="  21 Length").grid(row=22, column=3, sticky=W)
Label(root, text="  22 Length").grid(row=23, column=3, sticky=W)
Label(root, text="  23 Length").grid(row=24, column=3, sticky=W)
Label(root, text="  24 Length").grid(row=25, column=3, sticky=W)






# variables to store inputs


weight_1 = IntVar()
weight_2 = IntVar()
weight_3 = IntVar()
weight_4 = IntVar()
weight_5 = IntVar()
weight_6 = IntVar()
weight_7 = IntVar()
weight_8 = IntVar()
weight_9 = IntVar()
weight_10 = IntVar()
weight_11 = IntVar()
weight_12 = IntVar()
weight_13 = IntVar()
weight_14 = IntVar()
weight_15 = IntVar()
weight_16 = IntVar()
weight_17 = IntVar()
weight_18 = IntVar()
weight_19 = IntVar()
weight_20 = IntVar()
weight_21 = IntVar()
weight_22 = IntVar()
weight_23 = IntVar()
weight_24 = IntVar()

length_1 = IntVar()
length_2 = IntVar()
length_3 = IntVar()
length_4 = IntVar()
length_5 = IntVar()
length_6 = IntVar()
length_7 = IntVar()
length_8 = IntVar()
length_9 = IntVar()
length_10 = IntVar()
length_11 = IntVar()
length_12 = IntVar()
length_13 = IntVar()
length_14 = IntVar()
length_15 = IntVar()
length_16 = IntVar()
length_17 = IntVar()
length_18 = IntVar()
length_19 = IntVar()
length_20 = IntVar()
length_21 = IntVar()
length_22 = IntVar()
length_23 = IntVar()
length_24 = IntVar()


Entry(root, textvariable = weight_1, 
    justify=RIGHT).grid(row=2,column=2)
Entry(root, textvariable = weight_2, 
    justify=RIGHT).grid(row=3,column=2)
Entry(root, textvariable = weight_3, 
    justify=RIGHT).grid(row=4,column=2)    
Entry(root, textvariable = weight_4, 
    justify=RIGHT).grid(row=5,column=2)
Entry(root, textvariable = weight_5, 
    justify=RIGHT).grid(row=6,column=2)
Entry(root, textvariable = weight_6, 
    justify=RIGHT).grid(row=7,column=2) 
Entry(root, textvariable = weight_7, 
    justify=RIGHT).grid(row=8,column=2)
Entry(root, textvariable = weight_8, 
    justify=RIGHT).grid(row=9,column=2)
Entry(root, textvariable = weight_9, 
    justify=RIGHT).grid(row=10,column=2)   
Entry(root, textvariable = weight_10, 
    justify=RIGHT).grid(row=11,column=2)  
Entry(root, textvariable = weight_11, 
    justify=RIGHT).grid(row=12,column=2)    
Entry(root, textvariable = weight_12, 
    justify=RIGHT).grid(row=13,column=2) 
Entry(root, textvariable = weight_13, 
    justify=RIGHT).grid(row=14,column=2)
Entry(root, textvariable = weight_14, 
    justify=RIGHT).grid(row=15,column=2)
Entry(root, textvariable = weight_15, 
    justify=RIGHT).grid(row=16,column=2) 
Entry(root, textvariable = weight_16, 
    justify=RIGHT).grid(row=17,column=2) 
Entry(root, textvariable = weight_17, 
    justify=RIGHT).grid(row=18,column=2)
Entry(root, textvariable = weight_18, 
    justify=RIGHT).grid(row=19,column=2) 
Entry(root, textvariable = weight_19, 
    justify=RIGHT).grid(row=20,column=2)
Entry(root, textvariable = weight_20, 
    justify=RIGHT).grid(row=21,column=2)
Entry(root, textvariable = weight_21, 
    justify=RIGHT).grid(row=22,column=2)
Entry(root, textvariable = weight_22, 
    justify=RIGHT).grid(row=23,column=2) 
Entry(root, textvariable = weight_23, 
    justify=RIGHT).grid(row=24,column=2) 
Entry(root, textvariable = weight_24, 
    justify=RIGHT).grid(row=25,column=2)                


Entry(root, textvariable = length_1, 
    justify=RIGHT).grid(row=2,column=4)
Entry(root, textvariable = length_2, 
    justify=RIGHT).grid(row=3,column=4)
Entry(root, textvariable = length_3, 
    justify=RIGHT).grid(row=4,column=4)
Entry(root, textvariable = length_4, 
    justify=RIGHT).grid(row=5,column=4)
Entry(root, textvariable = length_5, 
    justify=RIGHT).grid(row=6,column=4)
Entry(root, textvariable = length_6, 
    justify=RIGHT).grid(row=7,column=4)
Entry(root, textvariable = length_7, 
    justify=RIGHT).grid(row=8,column=4)
Entry(root, textvariable = length_8, 
    justify=RIGHT).grid(row=9,column=4)
Entry(root, textvariable = length_9, 
    justify=RIGHT).grid(row=10,column=4)
Entry(root, textvariable = length_10, 
    justify=RIGHT).grid(row=11,column=4)
Entry(root, textvariable = length_11, 
    justify=RIGHT).grid(row=12,column=4)
Entry(root, textvariable = length_12, 
    justify=RIGHT).grid(row=13,column=4)
Entry(root, textvariable = length_13, 
    justify=RIGHT).grid(row=14,column=4)
Entry(root, textvariable = length_14, 
    justify=RIGHT).grid(row=15,column=4)
Entry(root, textvariable = length_15, 
    justify=RIGHT).grid(row=16,column=4)
Entry(root, textvariable = length_16, 
    justify=RIGHT).grid(row=17,column=4)
Entry(root, textvariable = length_17, 
    justify=RIGHT).grid(row=18,column=4)
Entry(root, textvariable = length_18, 
    justify=RIGHT).grid(row=19,column=4)
Entry(root, textvariable = length_19, 
    justify=RIGHT).grid(row=20,column=4)
Entry(root, textvariable = length_20, 
    justify=RIGHT).grid(row=21,column=4)
Entry(root, textvariable = length_21, 
    justify=RIGHT).grid(row=22,column=4)
Entry(root, textvariable = length_22, 
    justify=RIGHT).grid(row=23,column=4)
Entry(root, textvariable = length_23, 
    justify=RIGHT).grid(row=24,column=4)
Entry(root, textvariable = length_24, 
    justify=RIGHT).grid(row=25,column=4)


def plot1():
  
    # the figure that will contain the plot
    fig1 = Figure(figsize = (3, 3),
                 dpi = 100)
  
    x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    y = [length_1.get(), length_2.get(), length_3.get(), length_4.get(), length_5.get(), length_6.get(),
        length_7.get(), length_8.get(), length_9.get(),
        length_10.get(), length_11.get(), length_12.get(), length_13.get(), length_14.get(), 
        length_15.get(), length_16.get(), length_17.get(), length_18.get(),
        length_19.get(), length_20.get(), length_21.get(), 
        length_22.get(), length_23.get(), length_24.get()]
        
    # adding the subplot
    plot1 = fig1.add_subplot(111)

    # plotting the graph
    plot1.scatter(x,y)
    plot1.set_title("Year vs Length")

    # containing the Matplotlib figure
    canvas1 = FigureCanvasTkAgg(fig1, master = root)  
    canvas1.draw()
  
    # placing the canvas on the Tkinter window
    canvas1.get_tk_widget().grid(row = 2, column = 8, rowspan=20)

    # creating the Matplotlib toolbar
    toolbar1 = NavigationToolbar2Tk(canvas1, root)
    toolbar1.update()
  
def plot2():
  
    # the figure that will contain the plot
    fig2 = Figure(figsize = (3, 3),
                 dpi = 100)
  
    x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    z = [weight_1.get(), weight_2.get(), weight_3.get(), weight_4.get(), weight_5.get(), weight_6.get(),
        weight_7.get(), weight_8.get(), weight_9.get(),
        weight_10.get(), weight_11.get(), weight_12.get(), weight_13.get(), weight_14.get(), 
        weight_15.get(), weight_16.get(), weight_17.get(), weight_18.get(),
        weight_19.get(), weight_20.get(), weight_21.get(), 
        weight_22.get(), weight_23.get(), weight_24.get() ]
    
    # adding the subplot
    plot2 = fig2.add_subplot(111)

    # plotting the graph
    plot2.scatter(x,z)
    plot2.set_title("Year vs Weight")

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas2 = FigureCanvasTkAgg(fig2, master = root)  
    canvas2.draw()
  
    # placing the canvas on the Tkinter window
    canvas2.get_tk_widget().grid(row = 2, column = 16, rowspan=20)

    # creating the Matplotlib toolbar
    toolbar2 = NavigationToolbar2Tk(canvas2, root)
    toolbar2.update()

plot_button1 = Button(master = root, 
                     command = plot1,
                     text = "Plot-Length")
plot_button1.grid(row = 1, column = 8, columnspan=3)

plot_button2 = Button(master = root, 
                     command = plot2,
                     text = "Plot-Weight")
plot_button2.grid(row = 1, column = 12, columnspan=3)

def criteria_length():
    if gender.get() == 1:
        if length_24.get() >= 97:
            myLabel1 = Label(root, text = "berperawakan tubuh tinggi")
            myLabel1.grid(row = 26, column = 8, columnspan=3)
        elif length_24.get() <= 82 and length_24.get()>= 79:
            myLabel1 = Label(root, text = "berperawakan pendek")
            myLabel1.grid(row = 26, column = 8, columnspan=3)
        elif length_24.get() <79:
            myLabel1 = Label(root, text = "berperawakan kerdil")
            myLabel1.grid(row = 26, column = 8, columnspan=3)
        else:
            myLabel1 = Label(root, text = "normal")
            myLabel1.grid(row = 26, column = 8, columnspan=3)
    
    if gender.get() == 2:
        if length_24.get() >= 96:
            myLabel1 = Label(root, text = "berperawakan tubuh tinggi")
            myLabel1.grid(row = 26, column = 8, columnspan=3)
        elif length_24.get() <= 80 and length_24.get()>= 77:
            myLabel1 = Label(root, text = "berperawakan pendek")
            myLabel1.grid(row = 26, column = 8, columnspan=3)
        elif length_24.get() <77:
            myLabel1 = Label(root, text = "berperawakan kerdil")
            myLabel1.grid(row = 26, column = 8, columnspan=3)
        else:
            myLabel1 = Label(root, text = "normal")
            myLabel1.grid(row = 26, column = 8, columnspan=3)
    
def criteria_weight():
    if gender.get() == 1:
        if weight_24.get() >= 13:
            myLabel2 = Label(root, text = "Kemungkinan Terdapat Masalah Berat Badan")
            myLabel2.grid(row = 26, column = 12, columnspan=3)
        elif weight_24.get() <= 10:
            myLabel2 = Label(root, text = "Gizi Kurang")
            myLabel2.grid(row = 26, column = 12, columnspan=3)
        elif length_24.get() <=9:
            myLabel2 = Label(root, text = "Gizi Buruk")
            myLabel2.grid(row = 26, column = 12, columnspan=3)
        else:
            myLabel2 = Label(root, text = "normal")
            myLabel2.grid(row = 26, column = 12, columnspan=3)
    
    if gender.get() == 2:
        if length_24.get() >= 12:
            myLabel2 = Label(root, text = "Kemungkinan Terdapat Masalah Berat Badan")
            myLabel2.grid(row = 26, column = 12, columnspan=3)
        elif length_24.get() <= 9:
            myLabel2 = Label(root, text = "Gizi Kurang")
            myLabel2.grid(row = 26, column = 12, columnspan=3)
        elif length_24.get() <= 8:
            myLabel2 = Label(root, text = "Gizi Buruk")
            myLabel2.grid(row = 26, column = 12, columnspan=3)
        else:
            myLabel2 = Label(root, text = "normal")
            myLabel2.grid(row = 26, column = 12, columnspan=3)

criteria_button1 = Button(master = root, 
                     command = criteria_length,
                     text = "Length-Criteria")
criteria_button1.grid(row = 25, column = 8, columnspan=3)  

criteria_button2 = Button(master = root, 
                     command = criteria_weight,
                     text = "Weight-Criteria")
criteria_button2.grid(row = 25, column = 12, columnspan=3) 


root.mainloop()