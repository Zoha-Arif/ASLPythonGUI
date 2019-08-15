import tkinter 
from tkinter import *
import os
from PIL import ImageTk, Image

def login_success():
    Label(screen2, text = "Login Success", fg="green", font=("Calibri", 11)).pack()
    global screen3 
    screen3 = Toplevel(screen)
    screen3.title("We Sign Together Muse")
    screen3.geometry("750x490")

def password_not_recognized():
    Label(screen2, text = "Password does not match username.", fg="red", font=("Calibri", 11)).pack()
    
def user_not_found():
    Label(screen2, text = "Username not found.", fg="red", font=("Calibri", 11)).pack()    

def register_user():
    username_info = username.get()
    password_info = password.get()

    file_name = r"C:\\Users\\ZOHA\\Documents\\GitHub\\ASLPythonGUI\\UsersReachingSigns\\" + username_info
    file = open(file_name, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Success", fg="green", font=("Calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    file_name1 = r"C:\\Users\\ZOHA\\Documents\\GitHub\\ASLPythonGUI\\UsersReachingSigns\\"
    list_of_files = os.listdir(file_name1)
    if username1 in list_of_files: 
        file_name2 = r"C:\\Users\\ZOHA\\Documents\\GitHub\\ASLPythonGUI\\UsersReachingSigns\\" + username1
        file1 = open(file_name2, "r")
        verify = file1.read().splitlines()
        if password1 in verify: 
            login_success()
        else: 
            password_not_recognized()
    else: 
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register: We Sign Together Muse")
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
    username_entry = Entry(screen1, textvariable= username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width= 10, height = 1, command=register_user).pack()

def login():
    global screen2 
    screen2 = Toplevel(screen)
    screen2.title("Login: We Sign Together Muse")
    screen2.geometry("300x250")

    Label(screen2, text = "Please enter details below to login.").pack()
    Label(screen2, text = "").pack()

    global username_verify 
    global password_verify 

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()    
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()    
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
    

def main_screen():
    FILENAME = "loginHome.png"
    home_img = ImageTk.PhotoImage(file = FILENAME)

    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Home: We Sign Together Muse")

    Label(screen, image=home_img).pack()

    Label (text="We Sign Together Muse", bg="grey",width="300", height="2", font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()

main_screen()



