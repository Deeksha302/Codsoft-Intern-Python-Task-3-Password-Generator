import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 1:
            messagebox.showerror("Invalid Input", "Password length should be at least 1.")
        else:
            password = generate_password(length)
            result_var.set(password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
tk.Label(root, text="Enter password length:").grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate", command=on_generate)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_Var=tk.StringVar()
result_label=tk.label(root,textvariable=result_var,fg="blue",front=("Helvetica",12))

#Starting the main event loop
root.mainloop()
