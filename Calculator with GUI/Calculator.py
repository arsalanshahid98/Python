from tkinter import *

root = Tk()

root.title("Calculator")
root.configure(bg="#000000", padx=10, pady=10)

x = Entry(root, width=50)
x.grid(row=0, column=0, columnspan=3, padx=12, pady=12)


def b_click(number):
    current = x.get()
    x.delete(0, END)
    x.insert(0, str(current) + str(number))


def b_clear():
    x.delete(0, END)


def b_add():
    first_number = x.get()
    global y
    global math
    math = "addition"
    y = int(first_number)
    x.delete(0, END)


def b_equal():
    second_number = x.get()
    x.delete(0, END)

    if math == "addition":
        x.insert(0, y + int(second_number))
    if math == "subtraction":
        x.insert(0, y - int(second_number))
    if math == "multiplication":
        x.insert(0, y * int(second_number))
    if math == "division":
        x.insert(0, y / int(second_number))


def b_subtract():
    first_number = x.get()
    global y
    global math
    math = "subtraction"
    y = int(first_number)
    x.delete(0, END)


def b_multiply():
    first_number = x.get()
    global y
    global math
    math = "multiplication"
    y = int(first_number)
    x.delete(0, END)


def b_divide():
    first_number = x.get()
    global y
    global math
    math = "division"
    y = int(first_number)
    x.delete(0, END)


b_1 = Button(root, text="1", padx=40, pady=20, command=lambda: b_click(1), bg="#0C0C0C", fg="#ffffff", border=0)
b_2 = Button(root, text="2", padx=40, pady=20, command=lambda: b_click(2), bg="#0C0C0C", fg="#ffffff", border=0)
b_3 = Button(root, text="3", padx=40, pady=20, command=lambda: b_click(3), bg="#0C0C0C", fg="#ffffff", border=0)
b_4 = Button(root, text="4", padx=40, pady=20, command=lambda: b_click(4), bg="#0C0C0C", fg="#ffffff", border=0)
b_5 = Button(root, text="5", padx=40, pady=20, command=lambda: b_click(5), bg="#0C0C0C", fg="#ffffff", border=0)
b_6 = Button(root, text="6", padx=40, pady=20, command=lambda: b_click(6), bg="#0C0C0C", fg="#ffffff", border=0)
b_7 = Button(root, text="7", padx=40, pady=20, command=lambda: b_click(7), bg="#0C0C0C", fg="#ffffff", border=0)
b_8 = Button(root, text="8", padx=40, pady=20, command=lambda: b_click(8), bg="#0C0C0C", fg="#ffffff", border=0)
b_9 = Button(root, text="9", padx=40, pady=20, command=lambda: b_click(9), bg="#0C0C0C", fg="#ffffff", border=0)
b_0 = Button(root, text="0", padx=40, pady=20, command=lambda: b_click(0), bg="#0C0C0C", fg="#ffffff", border=0)

b_add = Button(root, text="+", padx=38, pady=38, command=b_add, bg="#FF7400", fg="#ffffff", border=0)
b_equal = Button(root, text="=", padx=88, pady=38, command=b_equal, bg="#0061FF", fg="#ffffff", border=0)
b_clear = Button(root, text="clear", padx=78, pady=20, command=b_clear, bg="#FF2020", fg="#ffffff", border=0)
b_subtract = Button(root, text="-", padx=40, pady=38, command=b_subtract, bg="#FF7400", fg="#ffffff", border=0)
b_multiply = Button(root, text="x", padx=38, pady=38, command=b_multiply, bg="#FF7400", fg="#ffffff", border=0)
b_divide = Button(root, text="/", padx=38, pady=38, command=b_divide, bg="#FF7400", fg="#ffffff", border=0)

b_1.grid(row=3, column=0, padx=8, pady=8)
b_2.grid(row=3, column=1, padx=8, pady=8)
b_3.grid(row=3, column=2, padx=8, pady=8)
b_4.grid(row=2, column=0, padx=8, pady=8)
b_5.grid(row=2, column=1, padx=8, pady=8)
b_6.grid(row=2, column=2, padx=8, pady=8)
b_7.grid(row=1, column=0, padx=8, pady=8)
b_8.grid(row=1, column=1, padx=8, pady=8)
b_9.grid(row=1, column=2, padx=8, pady=8)
b_0.grid(row=4, column=0, padx=8, pady=8)

b_clear.grid(row=5, column=1, columnspan=2, padx=8, pady=8)
b_add.grid(row=5, column=0, padx=8, pady=8)
b_equal.grid(row=6, column=1, columnspan=2, padx=8, pady=8)
b_subtract.grid(row=6, column=0, padx=8, pady=8)
b_multiply.grid(row=4, column=1, padx=8, pady=8)
b_divide.grid(row=4, column=2, padx=8, pady=8)

root.mainloop()
