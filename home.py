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

comb = tk.PhotoImage(file="comb.png", height=400)
comb1 = tk.Label(frame, image=comb,bg="#b5d6b2")
comb1.place(relx=0.2,rely=0, relwidth=0.6, relheight=0.6)

text = tk.PhotoImage(file="text.png")
text1 = tk.Label(frame, image=text,bg="#b5d6b2", height=100, width=500)
text1.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.4)



root.mainloop()