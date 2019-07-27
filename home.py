import tkinter as tk
import requests
import random 

root = tk.Tk()

HEIGHT = 700 
WIDTH = 800 

#canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#FFFFFF")
#canvas.pack()
#widthxheight
root.geometry("750x490")
frame = tk.Frame(root, bg="#FFFFFF")
#frame.place(relwidth=1, relheight=1)
frame.pack()

home = tk.PhotoImage(file="home.png", height=500)
home1 = tk.Label(frame, image=home,bg="#FFFFFF")
home1.pack()
#home1.place(relx=0.2,rely=0, relwidth=0.6, relheight=0.6)



root.mainloop()