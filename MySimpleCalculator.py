import time
from tkinter import *

root = Tk()
root.title("Basic Calculator")

my_textbox = Entry(root, width=40, border=5)
my_textbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

num1 = num2 = op_symbol = ""


def num_click(number):
    global num1
    global op_symbol
    global num2
    if len(op_symbol) == 0:
        if len(num1) == 0:
            my_textbox.insert(0, str(number))
        else:
            my_textbox.delete(0, END)
            my_textbox.insert(0, num1+str(number))
        num1 = my_textbox.get()
    else:
        my_textbox.delete(0, END)
        if len(num2) == 0:
            my_textbox.insert(0, str(number))
        else:
            my_textbox.insert(0, num2 + str(number))
        num2 = my_textbox.get()


def clear():
    global num1, num2, op_symbol
    my_textbox.delete(0, END)
    num1 = num2 = op_symbol = ""


def backspace():
    global num1
    num1 = int(my_textbox.get()) // 10
    num1 = str(num1)
    my_textbox.delete(0, END)
    my_textbox.insert(0, num1)


def sym_click(symbol):
    global num1, num2, op_symbol
    op_symbol = symbol
    if num2 != "":
        do_operation()
        my_textbox.delete(0, END)
        my_textbox.insert(0, str(num1))


def click():
    if num1 != "" and num2 != "":
        do_operation()
        my_textbox.delete(0, END)
        my_textbox.insert(0, num1)


def do_operation():
    global num1, num2, op_symbol
    if op_symbol == "+":
        num1 = int(num1) + int(num2)
    elif op_symbol == "-":
        num1 = int(num1) - int(num2)
    elif op_symbol == "*":
        num1 = int(num1) * int(num2)
    elif op_symbol == "/":
        if int(num2) != 0:
            num1 = int(num1) // int(num2)
    num1 = str(num1)
    num2 = op_symbol = ""


# Define Buttons
btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: num_click(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: num_click(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: num_click(3))
btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: num_click(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: num_click(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: num_click(6))
btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: num_click(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: num_click(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: num_click(9))
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: num_click(0))

btn_clear = Button(root, text="Clear", padx=29, pady=20, command=clear)
btn_bkspace = Button(root, text="<--", padx=33, pady=20, command=backspace)
btn_plus = Button(root, text="+", padx=40, pady=20, command=lambda: sym_click("+"))
btn_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: sym_click("-"))
btn_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: sym_click("*"))
btn_division = Button(root, text="/", padx=40, pady=20, command=lambda: sym_click("/"))
btn_result = Button(root, text="=", padx=87, pady=20, command=click)

# put buttons in the grid
btn_1.grid(column=0, row=3)
btn_2.grid(column=1, row=3)
btn_3.grid(column=2, row=3)

btn_4.grid(column=0, row=2)
btn_5.grid(column=1, row=2)
btn_6.grid(column=2, row=2)

btn_7.grid(column=0, row=1)
btn_8.grid(column=1, row=1)
btn_9.grid(column=2, row=1)

btn_division.grid(column=0, row=4)
btn_0.grid(column=1, row=4)
btn_clear.grid(column=2, row=4)

btn_subtract.grid(column=0, row=5)
btn_multiply.grid(column=1, row=5)
btn_bkspace.grid(column=2, row=5)

btn_plus.grid(column=0, row=6)
btn_result.grid(column=1, row=6, columnspan=2)

root.mainloop()
