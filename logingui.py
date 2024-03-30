import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

root = tk.Tk()
root.geometry("500x500")
root.resizable(False,False)
root.title('Sign In')

name = tk.StringVar()
password = tk.StringVar()

def login_clicked():
    
    entered_username = name.get()
    entered_password = password.get()
    
    stored_username = "lancemirano01@gmail.com"
    stored_password = "lance123"

    if entered_username == stored_username and entered_password == stored_password:
        msg = 'Welcome on board'
        showinfo(
            title='Information',
            message=msg
        )
    else:
        showerror(
            title='Error',
            message='You entered wrong credentials'
        )


name_label = ttk.Label(root, text="Email Address:").place(x=100,y=100)
name_entry = ttk.Entry(root, textvariable=name).place(x=100,y=120)
name_label = ttk.Label(root, text="Password:").place(x=100,y=160)
name_entry = ttk.Entry(root, textvariable=password).place(x=100,y=180)

login_button = ttk.Button(root, text="Login", command=login_clicked).place(x=150,y=210)

root.mainloop()