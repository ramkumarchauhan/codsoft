from tkinter import *
from tkinter import messagebox


def add_task():
    task_string = task_field.get()

    if len(task_string) == 0:

        messagebox.showinfo('Error', 'No task found')
    else:

        tasks.append(task_string)
        list_update()
        task_field.delete(0, 'end')


def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)


def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
    except:
        messagebox.showinfo('Error', 'Select task to delete.')


def clear_list():
    task_listbox.delete(0, 'end')


def close():
    print(tasks)
    guiWindow.destroy()


if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("My ToDo List")
    guiWindow.geometry("600x400+550+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#B5E5CF")

    tasks = []

    functions_frame = Frame(guiWindow, bg="black")
    functions_frame.pack(side="top", expand=True, fill="both")

    task_field = Entry(
        functions_frame,
        font=("Arial", "14"),
        width=48,
        foreground="black",
        background="white",
    )

    task_field.insert(0, "Enter any Text")
    task_field.place(x=30, y=30)

    add_button = Button(
        functions_frame,
        text="Add Task",
        width=15,
        bg='#80b918', font=("arial", "14", "bold"),
        command=add_task,

    )
    del_button = Button(
        functions_frame,
        text="Delete Task",
        width=15,
        bg='#D4AC0D', font=("arial", "14", "bold"),
        command=delete_task,
    )

    exit_button = Button(
        functions_frame,
        text="Close",
        width=44,
        bg='#e63946', font=("arial", "14", "bold"),
        command=close
    )

    add_button.place(x=30, y=80, )
    del_button.place(x=375, y=80)
    exit_button.place(x=30, y=330)

    task_listbox = Listbox(
        functions_frame,
        width=48,
        height=7,
        font="bold",
        selectmode='SINGLE',
        background="WHITE",
        foreground="BLACK",
        selectbackground="#D4AC0D",
        selectforeground="BLACK"
    )
    task_listbox.place(x=30, y=140)

    list_update()
    guiWindow.mainloop()
