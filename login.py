import tkinter
from tkinter import messagebox
import sqlite3 


window = tkinter.Tk()
window.title("Gestion de stock")
window.geometry('500x500')
window.configure(bg='#333333')

# Database

def login():
    conn = sqlite3.connect("login.db")

    cursor = conn.cursor()

    user= 'SELECT * FROM login WHERE username = ? and password = ? '
    cursor.execute(user, [(username_entry.get()),(password_entry.get())])
    result= cursor.fetchall()


    if result:
        messagebox.showinfo("Login Success", message="You successfully logged in.")
        window.destroy()
        import Form
    else:
        messagebox.showerror("Error", message="Invalid login.")
        



frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()



window.mainloop()
