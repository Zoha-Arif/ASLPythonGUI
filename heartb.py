import tkinter 
from tkinter import *

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info+".txt", "w")
    file.write(username_info)
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(text = "Registration Success")


def register():
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("200x250")
    
    global username 
    global password 
    username = StringVar()
    password = StringVar()

    global username_entry 
    global password_entry 
    
    Label(screen1, text = "Please enter details below.").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable= username).pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password).pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width= 10, height = 1, command=register_user).pack()

def login():
    print("Login session started")

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("We Sign Together Muse")
    Label (text="We Sign Together Muse", bg="grey",width="300", height="2", font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()

main_screen()



