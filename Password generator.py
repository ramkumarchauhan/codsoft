from tkinter import *
import random

win = Tk()
win.title("Password Generator")
win.geometry("500x500")
win.configure(bg="#adb5bd")

Label(win, text='PASSWORD GENERATOR', font='ariel 15 bold', bg="#adb5bd").pack(pady=10)

user_name = StringVar()
pass_len = IntVar()
pass_len.set(0)

Label(win, text='User Name', font='ariel 10 bold', bg="#adb5bd").pack(pady=10)
Entry(win, textvariable=user_name, width=30).pack()
Label(win, text='PASSWORD LENGTH', font='ariel 10 bold', bg="#adb5bd").pack(pady=10)
Entry(win, textvariable=pass_len, width=30).pack()


passwrd = StringVar()


def generate():  # Function to generate the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for x in range(pass_len.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)


Button(win, text="Generate", command=generate).pack(pady=40)
Entry(win, textvariable=passwrd,width=30,).pack(pady=3)

win.update()
win.mainloop()
