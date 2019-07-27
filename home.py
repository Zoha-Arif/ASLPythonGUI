import tkinter as tk
import requests
import random 

root = tk.Tk()

HEIGHT = 700 
WIDTH = 800 

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#b5d6b2")
canvas.pack()

frame = tk.Frame(root, bg="#b5d6b2")
frame.place(relwidth=1, relheight=1)



root.mainloop()