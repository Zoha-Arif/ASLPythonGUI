import tkinter as tk
from tkinter import *
import os
from PIL import ImageTk, Image

def login_success():
    Label(screen2, text = "Login Success!", fg="green", font='Arial 11 bold').pack()
    global screen3 
    screen3 = Toplevel(screen)
    screen3.title("Reaching Signs Together")
    screen3.geometry("750x490")

def password_not_recognized():
    Label(screen2, text = "Password does not match username.", fg="red", font='Arial 11 bold').pack()
    
def user_not_found():
    Label(screen2, text = "Username not found.", fg="red", font='Arial 11 bold').pack()    

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

    Label(screen1, text = "Registration Success. You may now login.", fg="green", font='Arial 11 bold').pack()

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
    FILENAME2 = "gestureRegister.png"

    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register: Reaching Signs Together")
    canvas2 = tk.Canvas(screen1, width=400, height=350)
    canvas2.pack()
    
    tk_img2 = ImageTk.PhotoImage(Image.open(FILENAME2).resize((400, 350)))
    canvas2.create_image(0, 0, image=tk_img2, anchor='nw')

    global username 
    global password 

    username = StringVar()
    password = StringVar()

    global username_entry 
    global password_entry 

    username_title1 = Label(screen1, text = "Enter username for new account.", font='Arial 8 bold')
    username_window1 = canvas2.create_window(114, 165, anchor='nw', window=username_title1)

    username_entry = Entry(screen1, textvariable=username)
    username_entry_window = canvas2.create_window(114, 190, anchor='nw', window=username_entry)

    password_title1 = Label(screen1, text = "Set password for your new account.", font='Arial 8 bold')
    password_window1 = canvas2.create_window(114, 220, anchor='nw', window=password_title1)

    password_entry = Entry(screen1, textvariable=password)
    password_entry_window = canvas2.create_window(114, 245, anchor='nw', window=password_entry)
    
    register_button1 = tk.Button(screen1, highlightthickness=0, text = "R E G I S T E R", command=register_user, anchor = 'w',
                    width = 10, activebackground = "#16A9FF", bd=0, bg="#16A9FF",fg="#FFFFFF", font='Arial 8 bold')
                                               #second number is up and down
    register_button_window = canvas2.create_window(160, 290, anchor='nw', window=register_button1)

    screen1.mainloop()

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

    #directions = Label(screen2, text = "Please enter details below to login.", font='Arial 8 bold')
    #directions_window = canvas1.create_window(44, 160, anchor='nw', window=directions)

    global username_verify 
    global password_verify 

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    username_title = Label(screen2, text = "Username", font='Arial 8 bold')
    username_window = canvas1.create_window(114, 165, anchor='nw', window=username_title)

    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1_window = canvas1.create_window(114, 190, anchor='nw', window=username_entry1)

    password_title = Label(screen2, text = "Password", font='Arial 8 bold')
    password_window = canvas1.create_window(114, 220, anchor='nw', window=password_title)

    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1_window = canvas1.create_window(114, 245, anchor='nw', window=password_entry1)
   
    login_button1 = tk.Button(screen2, highlightthickness=0, text = "L O G I N", command=login_verify, anchor = 'w',
                    width = 10, activebackground = "#16A9FF", bd=0, bg="#16A9FF",fg="#FFFFFF", font='Arial 8 bold')
                                               #second number is up and down
    login_button_window = canvas1.create_window(165, 295, anchor='nw', window=login_button1)

    screen2.mainloop()
    

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



