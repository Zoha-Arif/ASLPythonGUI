import tkinter 
from tkinter import *

def register():
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("200x250")
    
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below.").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    Entry(screen1, textvariable= username)
    Label(screen1, text = "Password * ").pack()
    Entry(screen1, textvariable = password)
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width= 10, height = 1).pack()

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



