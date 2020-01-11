from tkinter import *

root = Tk()

def my_click():
    my_label_1 = Label(root, text="You just clicked me!!!", fg="red")
    my_label_1.grid(row=1, column=0)

#padx and pady - used to pad across X and Y
my_button_1 = Button(root, text="Click Me!", padx=50, pady=20, command=my_click, fg="#000000", bg="WHITE")
my_button_1.grid(row=0, column=0)

root.mainloop()
