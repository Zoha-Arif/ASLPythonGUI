import tkinter as tk
import requests
import random 

root = tk.Tk()
#widthxheight
root.geometry("750x490")
frame = tk.Frame(root, bg="#FFFFFF")
frame.pack()

#home page image
home = tk.PhotoImage(file="home.png", height=500)
home1 = tk.Label(frame, image=home,bg="#FFFFFF")
home1.pack()
#home1.place(relx=0.2,rely=0, relwidth=0.6, relheight=0.6)

translateButton = tk.Button(root, text="T R A N S L A T E", bg="#16a9ff", font=("oemfixed", 10, "bold"), bd=2, height=1, width=20, padx=0, pady=0)
#translateButton = tk.Button(root, text="", bd=2, height=1, width=20, padx=0, pady=0)
translateButton.pack()


root.mainloop()