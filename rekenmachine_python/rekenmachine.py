import tkinter as tk

def btn_click(item):
    """
    Adds something to the global variable expression
    depending on which button is clicked.
    """
    global expression
    expression = expression + str(item)
    input_var.set(expression)

def equals():
    """
    Shows the result of the input if the equal button
    is clicked.
    """
    global expression
    result = str(eval(expression))
    input_var.set(result)
    expression = ""

def clear():
    """
    Clears the input on display.
    """
    global expression 
    expression = "" 
    input_var.set("")
    
# Create a window
window = tk.Tk()
window.geometry("325x340")
window.resizable(0, 0)
window.title("Calculator")

# Input
input_var = tk.StringVar()
expression = ""

# Frame with all content
content = tk.Frame(master=window).grid(column=0, row=0)

# Display of the input
display = tk.Frame(content, width=325, height=60).grid(column=0, row=0, columnspan=4)
entry_display = tk.Entry(display, font=('arial', 18, 'bold'), textvariable=input_var, width=24, bg="#eee", bd=0, justify="right").grid(column=0, row=0, columnspan=4)

# All the calculator buttons
btn_clear = tk.Button(master=content, text="C", height=3, command=lambda: clear()).grid(row=1, column=0, columnspan=3, sticky='nesw')
btn_divide = tk.Button(master=content, text="/", height=3, command=lambda: btn_click("/")).grid(row=1, column=3, sticky='nesw')
btn_multiply = tk.Button(master=content, text="*", height=3, command=lambda: btn_click("*")).grid(row=2, column=3, sticky='nesw')
btn_minus = tk.Button(master=content, text="-", height=3, command=lambda: btn_click("-")).grid(row=3, column=3, sticky='nesw')
btn_plus = tk.Button(master=content, text="+", height=3, command=lambda: btn_click("+")).grid(row=4, column=3, sticky='nesw')
btn_equals = tk.Button(master=content, text="=", height=3, command=lambda: equals()).grid(row=5, column=3, sticky='nesw')
btn_decimal = tk.Button(master=content, text=".", height=3, command=lambda: btn_click(".")).grid(row=5, column=2, sticky='nesw')

btn_1 = tk.Button(master=content, text="1", height=3, command=lambda: btn_click(1)).grid(row=4, column=0, sticky='nesw')
btn_2 = tk.Button(master=content, text="2", height=3, command=lambda: btn_click(2)).grid(row=4, column=1, sticky='nesw')
btn_3 = tk.Button(master=content, text="3", height=3, command=lambda: btn_click(3)).grid(row=4, column=2, sticky='nesw')
btn_4 = tk.Button(master=content, text="4", height=3, command=lambda: btn_click(4)).grid(row=3, column=0, sticky='nesw')
btn_5 = tk.Button(master=content, text="5", height=3, command=lambda: btn_click(5)).grid(row=3, column=1, sticky='nesw')
btn_6 = tk.Button(master=content, text="6", height=3, command=lambda: btn_click(6)).grid(row=3, column=2, sticky='nesw')
btn_7 = tk.Button(master=content, text="7", height=3, command=lambda: btn_click(7)).grid(row=2, column=0, sticky='nesw')
btn_8 = tk.Button(master=content, text="8", height=3, command=lambda: btn_click(8)).grid(row=2, column=1, sticky='nesw')
btn_9 = tk.Button(master=content, text="9", height=3, command=lambda: btn_click(9)).grid(row=2, column=2, sticky='nesw')
btn_0 = tk.Button(master=content, text="0", height=3, command=lambda: btn_click(0)).grid(row=5, column=0, columnspan=2, sticky='nesw')

window.mainloop()

