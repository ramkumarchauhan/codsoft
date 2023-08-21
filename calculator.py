from tkinter import *

calc = Tk()
calc.title("My Calculator")
calc.configure(background="yellow")


inbox = Entry(calc, borderwidth=3, relief=RIDGE)
inbox.grid(padx=15, pady=10, row=0,sticky="w")


def delete():
    get_input = inbox.get()
    inbox.delete(first=len(get_input) - 1, last="end")


def result():
    if inbox.get() == "":
        pass
    elif inbox.get()[0] == "0":
        inbox.delete(0, "end")
    else:
        c_res = inbox.get()
        c_res = eval(c_res)
        clear()
        inbox.insert("end", c_res)


def clear():
    inbox.delete(0, "end")


clean = Button(calc, text="Cr", width=2, command=clear, fg="black", relief=RIDGE)
clean.grid(row=0, sticky="w", padx=125)

seven = Button(text="7", width=2, command=lambda: inbox.insert("end", "7"), borderwidth=2, relief=RIDGE)
seven.grid(row=1, sticky="w", padx=15)

eight = Button(text="8", width=2, command=lambda: inbox.insert("end", "8"), borderwidth=2, relief=RIDGE)
eight.grid(row=1, sticky="w", padx=45)

nine = Button(calc, text="9", width=2, command=lambda: inbox.insert("end", "9"), borderwidth=2, relief=RIDGE)
nine.grid(row=1, sticky="w", padx=75)

Char_plus = Button(calc, text="+", width=2, command=lambda: inbox.insert("end", "+"), borderwidth=2, relief=RIDGE)
Char_plus.grid(row=1, sticky="e", padx=125)

four = Button(text="4", width=2, command=lambda: inbox.insert("end", "4"), borderwidth=2, relief=RIDGE)
four.grid(row=2, sticky="w", padx=15, pady=5)

Char_five = Button(text="5", width=2, command=lambda: inbox.insert("end", "5"), borderwidth=2, relief=RIDGE)
Char_five.grid(row=2, sticky="w", padx=45, pady=5)

six = Button(calc, text="6", width=2, command=lambda: inbox.insert("end", "6"), borderwidth=2, relief=RIDGE)
six.grid(row=2, sticky="w", padx=75, pady=5)

minus = Button(calc, text="-", width=2, command=lambda: inbox.insert("end", "-"), borderwidth=2, relief=RIDGE)
minus.grid(row=2, sticky="e", padx=125, pady=5)

one = Button(text="1", width=2, command=lambda: inbox.insert("end", "1"), borderwidth=2, relief=RIDGE)
one.grid(row=3, sticky="w", padx=15, pady=5)

two = Button(text="2", width=2, command=lambda: inbox.insert("end", "2"), borderwidth=2, relief=RIDGE)
two.grid(row=3, sticky="w", padx=45, pady=5)

three = Button(calc, text="3", width=2, command=lambda: inbox.insert("end", "3"), borderwidth=2, relief=RIDGE)
three.grid(row=3, sticky="w", padx=75, pady=5)

mul = Button(calc, text="*", width=2, command=lambda: inbox.insert("end", "*"), borderwidth=2, relief=RIDGE)
mul.grid(row=3, sticky="e", padx=125, pady=5)

zero = Button(text="0", width=2, command=lambda: inbox.insert("end", "0"), borderwidth=2, relief=RIDGE)
zero.grid(row=4, sticky="w", padx=15, pady=5)

dot = Button(text=".", width=2, command=lambda: inbox.insert("end", "."), borderwidth=2, relief=RIDGE)
dot.grid(row=4, sticky="w", padx=45, pady=5)

delete = Button(calc, text="del", width=2, command=delete, borderwidth=2, relief=RIDGE)
delete.grid(row=4, sticky="w", padx=75, pady=5)

divide = Button(calc, text="/", width=2, command=lambda: inbox.insert("end", "/"), borderwidth=2, relief=RIDGE)
divide.grid(row=4, sticky="e", padx=125, pady=5)

result = Button(calc, text="=", width=10, command=result, borderwidth=2, relief=RIDGE)
result.grid(row=5, sticky="w", padx=15, pady=5)

modulus = Button(calc, text="%", width=2, command=lambda: inbox.insert("end", "%"), borderwidth=2, relief=RIDGE)
modulus.grid(row=5, sticky="e", padx=125, pady=5)

calc.update()
calc.mainloop()
