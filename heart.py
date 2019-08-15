import tkinter as tk
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
    FILENAME1 = "gestureLogin.png"
    
    global screen2 
    screen2 = Toplevel(screen)
    screen2.title("Login: Reaching Signs Together")
    canvas1 = tk.Canvas(screen2, width=400, height=350)
    canvas1.pack()
                                                        #width, height
    tk_img1 = ImageTk.PhotoImage(Image.open(FILENAME1).resize((400, 350)))
    canvas1.create_image(0, 0, image=tk_img1, anchor='nw')

    Label(screen2, text = "Please enter details below to login.").pack()
    Label(screen2, text = "").pack()


    #global username_verify 
    #global password_verify 

    #username_verify = StringVar()
    #password_verify = StringVar()

    #global username_entry1
    #global password_entry1

    #Label(screen2, text = "Username * ").pack()
    #username_entry1 = Entry(screen2, textvariable=username_verify)
    #username_entry1.pack()
    #Label(screen2, text = "").pack()    
    #Label(screen2, text = "Password * ").pack()
    #password_entry1 = Entry(screen2, textvariable=password_verify)
    #password_entry1.pack()
    #Label(screen2, text = "").pack()    
    #Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
    

def main_screen():
    FILENAME = "gestureHome.png"
  
    global screen
    screen = Tk()
    screen.title("Home: Reaching Signs Together")
    canvas = tk.Canvas(screen, width=400, height=350)
    canvas.pack()
                                                         #width, height
    tk_img = ImageTk.PhotoImage(Image.open(FILENAME).resize((400, 350)))
    canvas.create_image(0, 0, image=tk_img, anchor='nw')

    #Login Button 
    login_button = tk.Button(screen, highlightthickness=0, text = "    L O G I N", command=login, anchor = 'w',
                    width = 16, activebackground = "#16A9FF", bd=0, bg="#16A9FF",fg="#FFFFFF", font='Arial 13 bold')
                                               #second number is up and down
    login_button_window = canvas.create_window(125, 184, anchor='nw', window=login_button)

    #Register Button 
    register_button = tk.Button(screen, highlightthickness=0, text = "  R E G I S T E R", command=register, anchor = 'w',
                    width = 16, activebackground = "#16A9FF", bd=0, bg="#16A9FF",fg="#FFFFFF", font='Arial 13 bold')
                                               #second number is up and down
    register_button_window = canvas.create_window(120, 255, anchor='nw', window=register_button)

    screen.mainloop()

main_screen()



