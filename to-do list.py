from tkinter import *
from tkinter import messagebox

def create_Tsk():
    task = entry.get()
    if task:
        to_Do.insert(END, task)
        entry.delete(0,END)
    else:
        messagebox.showwarning("Alert!", "Please add a task.")

def del_Tsk():
    try:
        index = to_Do.curselection()[0]
        to_Do.delete(index)
    except IndexError:
        messagebox.showwarning("Alert!", "Please select at Least one task.")

def up_Tsk():
    try:
        index = to_Do.curselection()[0]
        updated_task = entry.get()
        to_Do.delete(index)
        to_Do.insert(index, updated_task)
        entry.delete(0,END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select at Least one task.")
global entry, to_Do
win = Tk()
win.title("To-Do List")
win.configure(bg="lightblue")
win.geometry("1368x700")
entry = Entry(win, font=("Times", 18),width=80,fg = "black",borderwidth=8,bg = "lightpink",relief = RAISED)
entry.pack(pady=10)
to_Do = Listbox(win,borderwidth=12,font=("Times",14),width = 120,height=22, fg = "blacK",bg = "white",relief = RAISED)
to_Do.pack(pady=10)

#buttons
button_frame = Frame(win,bg="lightblue")
button_frame.pack(pady=10)

Create = Button(button_frame, text="Create Task", command=create_Tsk,borderwidth=12,font=("Times",14),width = 16, fg = "white",bg = "red", padx=10,pady=10,relief = RAISED)
Create.grid(row=0, column=0,padx=20)

Update = Button(button_frame, text="Update", command=up_Tsk,borderwidth=12,font=("Times",14),width = 16, fg = "white",bg = "purple", padx=10,pady=10,relief = RAISED)
Update.grid(row=0, column=1,padx=20)

Delete = Button(button_frame, text="Delete", command=del_Tsk,borderwidth=12,font=("Times",14),width = 16, fg = "white",bg = "black", padx=10,pady=10,relief = RAISED)
Delete.grid(row=0, column=2,padx=20)
win.mainloop()
