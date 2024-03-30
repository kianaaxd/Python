import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Discount Calculator")
root.geometry("500x500")
root.resizable(False,False)

price = tk.StringVar()
discount_var = tk.IntVar()


def calculate_discount():
    
    entered_price = float(price.get())
    discount = discount_var.get()
    if discount == 1:
        discounted_price = entered_price * 0.9
    elif discount == 2:
        discounted_price = entered_price * 0.75
    elif discount == 3:
        discounted_price = entered_price * 0.5
    messagebox.showinfo("Discount", f"The discounted price is: {discounted_price}")



name_label = ttk.Label(root, text="Enter Price:").place(x=180,y=0)
name_entry = ttk.Entry(root, textvariable=price).place(x=180,y=20)


tk.Label(root, text="Select Discount:").place(x=0, y=10)

tk.Radiobutton(root, text="10% Discount", variable=discount_var, value=1).place(x=10, y=40)
tk.Radiobutton(root, text="25% Discount", variable=discount_var, value=2).place(x=10, y=60)
tk.Radiobutton(root, text="50% Discount", variable=discount_var, value=3).place(x=10, y=80)



tk.Button(root, text="Calculate Discount", command=calculate_discount).place(x=190, y=160)

root.mainloop()