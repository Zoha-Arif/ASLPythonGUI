import tkinter as tk
from PIL import ImageTk, Image
import requests
import random 

#Arranging the HomePage
FILENAME = 'home.png'
root = tk.Tk()
canvas = tk.Canvas(root, width=750, height=490)
canvas.pack()
tk_img = ImageTk.PhotoImage(file = FILENAME)
#canvas.create_image(125, 125, image=tk_img)
#canvas.create_image(200, 400, image=tk_img, anchor='nw')
canvas.create_image(0, 0, image=tk_img, anchor='nw')


#Translate Button
translate_button = tk.Button(root, highlightthickness=0, text = "    T R A N S L A T E", command = root.quit, anchor = 'w',
                    width = 16, activebackground = "#16A9FF", bd=0, bg="#16A9FF",fg="#FFFFFF", font='Arial 9 bold')
translate_button_window = canvas.create_window(33, 43, anchor='nw', window=translate_button)    

#Sad Face/Help Button
image = Image.open("helpb.png")
image = image.resize((44, 44), Image.ANTIALIAS) ## The (250, 250) is (height, width)
#pw.pic = ImageTk.PhotoImage(image)
helpb = tk.Button(root, width=5, height=0, command = root.quit)
#image1 = ImageTk.PhotoImage(file="helpb.png")
image1 = ImageTk.PhotoImage(image)
# Color Code = #FFD966
helpb.config(image=image1, highlightthickness=0,  activebackground = "#FFD966", bd=0, bg="#FFD966", width=50, height=50)#These set the height and width of box of the picture.
helpb.image = image1
helpb_window = canvas.create_window(200, 30, anchor='nw', window=helpb) #These numbers move the picture. 

#Heart/Information Button
image = Image.open("heartb.png")
image = image.resize((38, 38), Image.ANTIALIAS) ## The (250, 250) is (height, width)
heartb = tk.Button(root, width=5, height=0, command = root.quit)
#image1 = ImageTk.PhotoImage(file="helpb.png")
image2 = ImageTk.PhotoImage(image)
# Color Code = #FFD966
heartb.config(image=image2, highlightthickness=0,  activebackground = "#FFD966", bd=0, bg="#FFD966", width=50, height=50) #These set the height and width of box of the picture.
heartb.image = image2
heartb_window = canvas.create_window(680, 30, anchor='nw', window=heartb) #These numbers move the picture. 


root.mainloop()