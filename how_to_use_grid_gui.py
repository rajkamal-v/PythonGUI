from tkinter import *

root = Tk()

my_label_1 = Label(root, text="My name is Rajkamal")
my_label_2 = Label(root, text="And we are learning GUI Programming with Python Tkinter")
# Frame is divided into rows and columns, we can say where the widget should land in the grid by passing the row and column no
# say label1 in row 0 and col 1 and label2 in row 1 and col 0
my_label_1.grid(row=0, column=0)
my_label_2.grid(row=1, column=0)
# the rows and columns are relative,
# if we skip and give column or row as 5 without giving any widget in column/rpw 1,2,3 and 4, then it will appear same
# as in the column 1 or row 1
# e.g. my_label_2.grid(row=5, column=0) it will appear the same as above.

# if we give two widgets in the same position, the latest one overrides the first one.

root.mainloop()
