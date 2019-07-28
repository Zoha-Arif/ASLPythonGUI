import tkinter as tk
import PIL
#import Pillow
from PIL import ImageTk, Image

class CanvasButton:
    def __init__(self, canvas):
        self.canvas = canvas
        self.number = tk.IntVar()
        self.button = tk.Button(canvas, textvariable=self.number,
                                command=self.buttonclicked)
        self.id = canvas.create_window(50, 100, width=25, height=25,
                                       window=self.button)
    def buttonclicked(self):
        self.number.set(self.number.get()+1)  # auto updates Button

root = tk.Tk()
root.resizable(width=False, height=False)
root.wm_attributes("-topmost", 1)

imgpath = 'home.png'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

#canvas = tk.Canvas(root, bd=0, highlightthickness=0, height=500, width=500)
#canvas = tk.Canvas(root, height=500, width=500)
canvas = tk.Canvas(root, bd=0, highlightthickness=0)
canvas.pack()
#create_image(x, y, anchor = NW, image = can.tab[nb]['image'])
canvas.create_image(1000, 10000, image=photo)

CanvasButton(canvas)  # create a clickable button on the canvas

root.mainloop()