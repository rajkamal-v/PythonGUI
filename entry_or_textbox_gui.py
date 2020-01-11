from tkinter import *

root = Tk()

my_textbox = Entry(root, width=20, fg="WHITE", bg="blue", border=5)
my_textbox.grid(row=0, column=0)
my_textbox.insert(0, "Enter ur name")


def my_click():
    greetings = "Hi, "+my_textbox.get()+"!"
    my_label_1 = Label(root, text=greetings, fg="red")
    my_label_1.grid(row=1, column=0)


# padx and pady - used to pad across X and Y
my_button_1 = Button(root, text="Click Me!", padx=50, pady=20, command=my_click, fg="#000000", bg="WHITE")
my_button_1.grid(row=0, column=1)

root.mainloop()
