import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username.isalpha():
        messagebox.showwarning("Peringatan", "Username harus berupa teks!")
        return

    if not password.isdigit():
        messagebox.showwarning("Peringatan", "Password harus berupa angka!")
        return

    valid_username = "danny"
    valid_password = "12345678"

    if username == valid_username and password == valid_password:
        messagebox.showinfo("Sukses", "Login berhasil!")
    else:
        messagebox.showerror("Gagal", "Username atau password salah!")

root = tk.Tk()
root.title("instagram")
root.geometry("300x150")  


tk.Label(root, text="Username:").grid(row=0, column=0, padx=25, pady=10, sticky="we")
entry_username = tk.Entry(root, width=25)
entry_username.grid(row=0, column=1, padx=10, pady=10)


tk.Label(root, text="Password:", bg="lightgray").grid(row=1, column=0, padx=25, pady=10, sticky="we")
entry_password = tk.Entry(root, show="*", width =25)
entry_password.grid(row=1, column=1, padx=10, pady=10)


tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()