from tkinter import *


# def button_clicked():
#     new_text = inpu.get()
#     my_label.config(text=new_text)


# window = Tk()
# window.title("GUI Program")
# window.minsize(500, 300)
# # makes space around the labels / buttons all together
# window.config(padx= 30, pady= 40)
#
# # pack, place and grid used to position. grid and pack not compatible with each other.
# my_label = Label(text="Vanakkam Nanba", font=("Verdana", 20, "bold"))
# my_label.grid(row=0, column=0)
# # make space arond the label
# my_label.config(pady= 34, padx= 41)
#
# inpu = Entry(width=10)
# inpu.grid(row=8, column=8)
#
# button2 = Button(text="Button 2", command=button_clicked)
# button2.grid(row=0, column=4)
#
# button = Button(text="click here", command=button_clicked)
# button.grid(row=2, column=2)

windows = Tk()
windows.title("Mile to Km converter")
windows.minsize(width=250, height=150)
windows.config(padx=40, pady=20)


def convert_to_km():
    mil = miles_input.get()
    kilometer = float(mil)*1.609
    km.config(text=kilometer)


miles = Label(text="Mile", font=("Verdana", 20, "bold"))
miles.grid(row=0, column=0)
miles.config(pady=24, padx=24)

miles_input = Entry(width=14)
miles_input.grid(row=0, column=2)

km = Label(text="Kilometer", font=("Verdana", 20, "bold"))
km.grid(row=1, column=0)
km.config(pady=24, padx=24)

km = Label(text="0", font=("Verdana", 20, "bold"))
km.grid(row=1, column=2)
km.config(pady=24, padx=24)

calc = Button(text="Convert", command=convert_to_km)
calc.grid(row=2, column=1)



windows.mainloop()
