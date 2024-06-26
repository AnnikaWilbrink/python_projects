from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.resizable(False, False)
window.config(padx=60, pady=30)

#Entry
entry = Entry(width=10)
entry.grid(column=1,row=0)

#Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2,row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0,row=1)

label_num = Label(text="0")
label_num.grid(column=1,row=1)

label_km = Label(text="Km")
label_km.grid(column=2,row=1)

#Buttons
def calculate():
    miles = float(entry.get())
    km = round(miles*1.609, 1)
    label_num.config(text=f"{km}")

#calls action() when pressed
button = Button(text="Calculate", command=calculate)
button.grid(column=1,row=2)

window.mainloop()